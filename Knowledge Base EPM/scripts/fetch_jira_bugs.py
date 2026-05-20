#!/usr/bin/env python3
"""Fetch Jira bug issues and create knowledge base markdown files."""
import json, os, sys, re, urllib.request, urllib.error

OUTPUT_DIR = "/Users/aukaiyan/Claude-Project/Knowledge Base EPM/03-Resources/jira-knowledge"
AUTH = "Basic YW5kcmV3X2F1QGN0aWwuY29tOkFUQVRUM3hGZkdGME1yTzMwbVM5VzVBdEtlQlVKQjF6TUNUVk5KX1lhU0s4U05XNW15M0t1blhZRnNCNDA5RXZrVEgtdmV4azl2a1lNSVhmS3FmcVk1U1BmYnIwQzFuaTBSQXpZUTJub2F2Vi1weExDV3k5RlJHLUo2a2VLbm1MQnc5M0k5dXVSV3NaSHVTTzlRdkl3RnVXMTF0aW1OX1JlOVRNb082d1BrTHlLbnk0Mk5HMm1PMD0yNjI3MUI1MA=="
BASE = "https://ctil.atlassian.net/rest/api/3"

def jira(path):
    req = urllib.request.Request(f"{BASE}{path}", headers={"Authorization": AUTH, "Accept": "application/json"})
    return json.loads(urllib.request.urlopen(req).read())

def extract_text(node):
    """Extract plain text from Atlassian Document Format JSON."""
    parts = []
    if isinstance(node, dict):
        t = node.get('type', '')
        if t == 'text':
            parts.append(node.get('text', ''))
        elif t == 'inlineCard':
            parts.append(f"[Link:{node.get('attrs',{}).get('url','?')}]")
        elif t == 'hardBreak':
            parts.append('\n')
        elif t == 'mention':
            parts.append(f"@{node.get('attrs',{}).get('id','?')}")
        elif t == 'code':
            parts.append(f"`{''.join(extract_text(c) for c in node.get('content',[]))}`")
        elif t == 'codeBlock':
            lang = node.get('attrs',{}).get('language','')
            code = ''.join(extract_text(c) for c in node.get('content',[]))
            parts.append(f"\n```{lang}\n{code}\n```\n")
        elif t == 'mediaSingle':
            parts.append('[Image]')
        elif t == 'media':
            parts.append('[Media]')
        elif t == 'rule':
            parts.append('\n---\n')
        elif t == 'paragraph':
            parts.append(''.join(extract_text(c) for c in node.get('content',[])) + '\n')
        elif t in ('heading',):
            lvl = '#' * node.get('attrs',{}).get('level',1)
            parts.append(f"\n{lvl} {''.join(extract_text(c) for c in node.get('content',[]))}\n")
        elif t in ('orderedList', 'bulletList'):
            for item in node.get('content',[]):
                prefix = '1. ' if t == 'orderedList' else '- '
                item_text = ''.join(extract_text(c) for c in item.get('content',[]))
                parts.append(f"{prefix}{item_text}")
            parts.append('\n')
        elif t == 'listItem':
            parts.append(''.join(extract_text(c) for c in node.get('content',[])))
        elif t == 'table':
            parts.append('\n[Table]\n')
        else:
            for v in node.values():
                if isinstance(v, (dict, list)):
                    parts.append(''.join(extract_text(v)))
    elif isinstance(node, list):
        for item in node:
            parts.append(''.join(extract_text(item)))
    return parts

def get_description(issue):
    desc = issue['fields'].get('description')
    if not desc:
        return ''
    if isinstance(desc, str):
        return desc
    if isinstance(desc, dict):
        return ''.join(extract_text(desc))
    return str(desc)

def get_comments(key):
    try:
        data = jira(f"/issue/{key}/comment")
        texts = []
        for c in data.get('comments', []):
            author = c.get('author', {}).get('displayName', '?')
            body = c.get('body', '')
            if isinstance(body, dict):
                body = ''.join(extract_text(body))
            if body and 'Issue has been created since' not in body:
                texts.append(f"**{author}**: {body[:1000]}")
        return '\n\n'.join(texts)
    except:
        return ''

def sanitize_filename(text):
    text = re.sub(r'[<>:"/\\|?*]', '', text)
    text = re.sub(r'\s+', '-', text)
    return text[:80]

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Search for all matching issues
    jql = 'project = EPMTDCPROT AND issuetype in ("Bug PRD", "Bug QA", "Bug DEV", "Bug-UAT") AND status = Release'
    encoded = urllib.parse.quote(jql)
    results = jira(f"/search/jql?jql={encoded}&maxResults=100&fields=summary,description,issuetype,priority,created,resolutiondate,labels")

    issues = results.get('issues', [])
    print(f"Processing {len(issues)} issues...")

    for i, issue in enumerate(issues):
        key = issue['key']
        fields = issue['fields']
        summary = fields.get('summary', 'N/A')
        issue_type = fields.get('issuetype', {}).get('name', '')
        priority = fields.get('priority', {}).get('name', '') if fields.get('priority') else ''
        created = fields.get('created', '')[:10]
        resolved = fields.get('resolutiondate', '')[:10] if fields.get('resolutiondate') else ''
        labels = fields.get('labels', [])

        description = get_description(issue)
        comments = get_comments(key)

        # Build frontmatter
        ticket_url = f"https://ctil.atlassian.net/browse/{key}"
        tags = ['jira', 'bug', 'release']
        if 'TDC-CR' in labels:
            tags.append('tdc-cr')
        if 'Production' in summary:
            tags.append('production')

        frontmatter = f"""---
tags: [{', '.join(tags)}]
related-ticket: {key}
jira-url: {ticket_url}
issue-type: {issue_type}
priority: {priority}
created: {created}
resolved: {resolved}
---

# {key}: {summary}

**Jira URL**: [{key}]({ticket_url})
**Type**: {issue_type}
**Priority**: {priority}
**Status**: Release
**Created**: {created}

## Problem

"""
        # Extract problem from description (first paragraph or heading)
        desc_lines = description.strip().split('\n')
        problem_found = False
        for line in desc_lines:
            line = line.strip()
            if not line or line.startswith('---'):
                continue
            if 'root cause' in line.lower() or 'revised fix' in line.lower() or 'expected fixing' in line.lower() or 'suggested' in line.lower():
                break
            frontmatter += line + '\n'
            problem_found = True

        if not problem_found or len(frontmatter.split('\n')[-2].strip() if len(frontmatter.split('\n')) > 1 else '') < 10:
            frontmatter += description[:500] + ('...' if len(description) > 500 else '')

        # Add full description
        frontmatter += "\n## Full Description\n\n"
        frontmatter += description if description else "_No description provided._"

        # Add comments
        if comments:
            frontmatter += "\n\n## Comments / Resolution Notes\n\n"
            frontmatter += comments

        # Add code snippet placeholder
        code_block_pattern = r'```[\s\S]*?```'
        code_snippets = re.findall(code_block_pattern, description + '\n' + comments)
        if code_snippets:
            frontmatter += "\n\n## Code Snippets\n\n"
            for snippet in code_snippets:
                frontmatter += snippet + '\n'

        # Write file
        filename = f"{key}-solution.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, 'w') as f:
            f.write(frontmatter)

        print(f"  [{i+1}/{len(issues)}] {key}: {summary[:60]}... -> {filename}")

    print(f"\nDone! Created {len(issues)} files in {OUTPUT_DIR}")

import urllib.parse
if __name__ == '__main__':
    main()
