#!/usr/bin/env python3
"""
Jira → Obsidian KB pipeline:
1. Search closed bugs with root cause/solution/fix keywords
2. Distill into structured template notes
3. Build MOC index

Usage:
    python3 distill_jira_kb.py                  # full refresh
    python3 distill_jira_kb.py --days 7          # last 7 days only
    python3 distill_jira_kb.py --days 7 --quiet  # silent mode (for cron)
"""
import json, os, re, sys, argparse, urllib.request, ssl, base64, time
from datetime import date

# ── Config ──────────────────────────────────────────────────────────────
OUTPUT_DIR = "/Users/aukaiyan/Claude-Project/Knowledge Base EPM/03-Resources/troubleshooting"
AUTH_STR = os.environ.get("JIRA_AUTH", "email:api_token")
AUTH_B64 = base64.b64encode(AUTH_STR.encode()).decode()
BASE = "https://ctil.atlassian.net/rest/api/3"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Category keywords for component inference
COMPONENT_KEYWORDS = {
    "Authentication & Login": ["password", "login", "login", "reset password", "activation", "account", "permission", "access"],
    "Email & Notification": ["email", "notification", "reminder", "cc ", "notification"],
    "E-Form & Workflow": ["e-form", "eform", "approval", "submission", "draft", "validation", "workflow"],
    "Reporting & Export": ["report", "export", "generation", "excel", "print", "pdf"],
    "Supplier Management": ["supplier", "registration", "vendor", "company", "info change"],
    "Tender & RFQ": ["tender", "rfq", "quotation", "award", "bid", "offer", "submission"],
    "User Management": ["user", "role", "delegation", "sysadmin", "buyer", "admin"],
    "Integration": ["fms", "api", "interface", "integration", "po "],
    "UI/UX": ["display", "show", "misalignment", "label", "ui", "button", "page"],
    "Payment & Fee": ["fee", "payment", "price", "cost", "currency", "financial"],
}

def jira_post(path, payload):
    req = urllib.request.Request(
        f"{BASE}{path}",
        data=json.dumps(payload).encode(),
        headers={"Authorization": f"Basic {AUTH_B64}", "Content-Type": "application/json", "Accept": "application/json"}
    )
    return json.loads(urllib.request.urlopen(req, context=ctx).read())

def jira_get(path):
    req = urllib.request.Request(
        f"{BASE}{path}",
        headers={"Authorization": f"Basic {AUTH_B64}", "Accept": "application/json"}
    )
    return json.loads(urllib.request.urlopen(req, context=ctx).read())

def extract_text(node):
    """Extract plain text from Atlassian Document Format JSON."""
    parts = []
    if isinstance(node, str):
        return [node]
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
            inner = extract_text(node.get('content',[]))
            parts.append(f"`{''.join(inner)}`")
        elif t == 'codeBlock':
            lang = node.get('attrs',{}).get('language','')
            inner = extract_text(node.get('content',[]))
            parts.append(f"\n```{lang}\n{''.join(inner)}\n```\n")
        elif t == 'mediaSingle':
            parts.append('[Image]\n')
        elif t == 'media':
            parts.append('[Media]')
        elif t == 'emoji':
            parts.append(node.get('attrs',{}).get('shortName',''))
        elif t == 'rule':
            parts.append('\n---\n')
        elif t == 'paragraph':
            inner = extract_text(node.get('content',[]))
            parts.append(''.join(inner) + '\n')
        elif t == 'heading':
            lvl = node.get('attrs',{}).get('level',1)
            inner = extract_text(node.get('content',[]))
            parts.append(f"\n{'#'*lvl} {''.join(inner)}\n")
        elif t in ('orderedList', 'bulletList'):
            for j, item in enumerate(node.get('content',[]), 1):
                prefix = f'{j}. ' if t == 'orderedList' else '- '
                inner = extract_text(item)
                parts.append(f"{prefix}{''.join(inner)}")
            parts.append('\n')
        elif t == 'listItem':
            inner = extract_text(node.get('content',[]))
            parts.append(''.join(inner))
        elif t == 'table':
            parts.append('\n[Table]\n')
        elif t == 'blockquote':
            inner = extract_text(node.get('content',[]))
            parts.append(f"\n> {''.join(inner)}\n")
        elif t == 'panel':
            parts.extend(extract_text(node.get('content',[])))
        else:
            if 'content' in node:
                parts.extend(extract_text(node['content']))
    elif isinstance(node, list):
        for item in node:
            parts.extend(extract_text(item))
    return parts

def get_description(issue):
    desc = issue['fields'].get('description')
    if not desc:
        return ''
    if isinstance(desc, str):
        return desc
    if isinstance(desc, dict):
        return ''.join(extract_text(desc)).strip()
    return str(desc)

def get_comments(key):
    try:
        data = jira_get(f"/issue/{key}/comment")
        texts = []
        for c in data.get('comments', []):
            author = c.get('author', {}).get('displayName', '?')
            body = c.get('body', '')
            if isinstance(body, dict):
                body = ''.join(extract_text(body)).strip()
            if body and 'Issue has been created since' not in body:
                texts.append({"author": author, "body": body[:3000]})
        return texts
    except Exception as e:
        print(f"    [WARN] Comments failed for {key}: {e}")
        return []

def get_code_snippets(description, comments_text):
    """Extract code blocks from description and comments."""
    code_blocks = re.findall(r'```[\s\S]*?```', description + '\n' + comments_text)
    return code_blocks

def infer_component(summary, description, labels):
    """Try to infer the component from text keywords."""
    combined = (summary + ' ' + description).lower()
    scores = {}
    for comp, keywords in COMPONENT_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw.lower() in combined)
        if score > 0:
            scores[comp] = score
    if scores:
        return max(scores, key=scores.get)
    return "General"

def extract_symptom(description):
    """Extract a concise symptom from the first few lines."""
    lines = [l.strip() for l in description.split('\n') if l.strip() and not l.startswith('[') and not l.startswith('![')]
    for line in lines:
        if len(line) > 20 and len(line) < 200:
            return line[:150]
    if lines:
        return lines[0][:150]
    return ""

def extract_root_cause(text):
    """Look for root cause mentions."""
    # Look for "root cause" sections
    rc_patterns = [
        r'(?:root\s*cause|RC)[\s:]*\n(.*?)(?:\n#|\n---|\Z)',
        r'(?:root\s*cause|RC)[\s:]+(.*?)(?:\n|$)',
    ]
    for pat in rc_patterns:
        m = re.search(pat, text, re.IGNORECASE | re.DOTALL)
        if m:
            rc = m.group(1).strip()
            if len(rc) > 10:
                return rc[:500]
    return ""

def extract_solution_text(text):
    """Extract solution/fix description."""
    sol_patterns = [
        r'(?:solution|fix|revised\s*fix|expected\s*fixing|suggested\s*fix)[\s:]*\n(.*?)(?:\n#|\n---|\Z)',
        r'(?:solution|fix|revised\s*fix)[\s:]+(.*?)(?:\n|$)',
    ]
    for pat in sol_patterns:
        m = re.search(pat, text, re.IGNORECASE | re.DOTALL)
        if m:
            sol = m.group(1).strip()
            if len(sol) > 10:
                return sol[:1000]
    return ""

def extract_diagnosis(comments, description):
    """Extract diagnosis steps from comments and description."""
    combined = description + '\n'
    for c in comments:
        combined += '\n' + c['body']

    # Look for investigation-related text
    diag_lines = []
    in_diag = False
    for line in combined.split('\n'):
        ll = line.lower().strip()
        if any(kw in ll for kw in ['investigate', 'check', 'found that', 'identified', 'analysis', 'testing', 'debug', 'confirmed', 'verified', 'test result', 'traced', 'reproduce']):
            in_diag = True
            diag_lines.append(line)
        elif in_diag and len(line.strip()) > 10 and not line.strip().startswith('#'):
            diag_lines.append(line)
        elif in_diag and line.strip().startswith('#'):
            break
    
    if diag_lines:
        return '\n'.join(diag_lines[:15])
    return ""

def extract_preventive_measures(comments, description):
    """Look for preventive measures mentioned."""
    combined = description + '\n'
    for c in comments:
        combined += '\n' + c['body']

    prev_lines = []
    for line in combined.split('\n'):
        ll = line.lower().strip()
        if any(kw in ll for kw in ['prevent', 'avoid', 'ensure', 'should not', 'recommend', 'going forward', 'improvement', 'enhance']):
            prev_lines.append(line)
    if prev_lines:
        return '\n'.join(prev_lines[:5])
    return ""

def extract_related_issues(description, comments_text, key):
    """Extract related EPRO and EPMTDCPROT references."""
    combined = description + ' ' + comments_text
    # EPRO links
    epros = re.findall(r'EPRO-(\d+)', combined)
    epros = sorted(set(epros), key=lambda x: int(x))
    # Other EPMTDCPROT references (exclude self)
    keys = re.findall(r'EPMTDCPROT-(\d+)', combined)
    keys = sorted(set(keys), key=lambda x: int(x))
    keys = [k for k in keys if f'EPMTDCPROT-{k}' != key]
    
    related = []
    for e in epros:
        related.append(f"- [[EPRO-{e}]]")
    for k in keys:
        related.append(f"- [[EPMTDCPROT-{k}-solution|EPMTDCPROT-{k}]]")
    return '\n'.join(related) if related else ""

def build_tags(summary, labels):
    """Build tag list."""
    tags = ['bug', 'jira']
    # Labels
    for l in labels:
        tag = l.lower().replace(' ', '-')
        if tag not in tags:
            tags.append(tag)
    # Environment
    if 'production' in summary.lower() or 'prd' in summary.lower():
        tags.append('production')
    if 'uat' in summary.lower():
        tags.append('uat')
    if 'pre-prd' in summary.lower() or 'preprd' in summary.lower():
        tags.append('pre-production')
    if 'phase 2' in summary.lower() or 'phase2' in summary.lower():
        tags.append('phase-2')
    if 'hot fix' in summary.lower() or 'hotfix' in summary.lower():
        tags.append('hotfix')
    if 'cr' in summary.lower() or 'change request' in summary.lower():
        tags.append('change-request')
    return tags

def generate_note(issue, comments):
    """Generate a simplified troubleshooting note."""
    key = issue['key']
    fields = issue['fields']
    summary = fields.get('summary', 'N/A')
    resolved = fields.get('resolutiondate', '')[:10] if fields.get('resolutiondate') else ''
    labels = fields.get('labels', [])

    description = get_description(issue)
    comments_text = '\n'.join(c['body'] for c in comments)
    combined = description + '\n' + comments_text

    # Extract structured fields
    component = infer_component(summary, description, labels)
    symptom = extract_symptom(description)
    root_cause = extract_root_cause(combined)
    solution_text = extract_solution_text(combined)
    related = extract_related_issues(description, comments_text, key)
    tags = build_tags(summary, labels)
    code_snippets = get_code_snippets(description, comments_text)

    # Format frontmatter fields
    rc_fm = root_cause.replace('"', "'").replace('\n', ' ').strip() if root_cause else ""
    sol_fm = solution_text.replace('"', "'").replace('\n', ' ').strip()[:120] if solution_text else ""
    tags_str = ', '.join(tags)

    note = f"""---
tags: {tags_str}
component: {component}
symptom: "{symptom}"
root-cause: "{rc_fm}"
solution: "{sol_fm}"
jira: {key}
resolved: {resolved}
---

# {key}: {summary}

## 問題

{description if description else '_No description provided._'}

"""
    # 根因 section (use extracted root cause or diagnosis)
    rc_section = root_cause if root_cause else ""
    if not rc_section:
        diag = extract_diagnosis(comments, description)
        if diag:
            rc_section = diag
    if rc_section:
        note += f"""## 根因

{rc_section}

"""

    # 解法 section
    if solution_text:
        note += f"""## 解法

{solution_text}

"""
    elif code_snippets:
        note += "## 解法\n\n"
        for sn in code_snippets:
            note += sn + '\n'
        note += '\n'
    else:
        note += f"""## 解法

_See Jira ticket for resolution details._

"""

    if related:
        note += f"""## 相關問題

{related}

"""
    return note

def main():
    parser = argparse.ArgumentParser(description="Sync Jira closed bugs to Obsidian KB")
    parser.add_argument("--days", type=int, default=0, help="Only process tickets updated in last N days")
    parser.add_argument("--quiet", action="store_true", help="Suppress detailed output")
    args = parser.parse_args()
    verbose = not args.quiet

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Build JQL
    jql = 'project = EPMTDCPROT AND status = Closed AND resolution IS NOT NULL AND (text ~ "root cause" OR text ~ "solution" OR text ~ "fix")'
    if args.days > 0:
        jql += f' AND updated >= -{args.days}d'

    if verbose:
        print("=" * 60)
        print(f"Step 1: Searching Jira {'(last {args.days}d)'.format(args=args) if args.days else '(full)'}")
        print(f"  JQL: {jql}")
        print("=" * 60)

    all_issues = []
    page_token = None
    page = 0
    while True:
        payload = {
            "jql": jql, "maxResults": 100,
            "fields": ["summary", "issuetype", "priority", "created", "resolutiondate", "labels", "description"]
        }
        if page_token:
            payload["nextPageToken"] = page_token
        data = jira_post("/search/jql", payload)
        issues = data.get('issues', [])
        all_issues.extend(issues)
        page += 1
        if verbose:
            print(f"  Page {page}: {len(issues)} issues (total: {len(all_issues)})")
        if data.get('isLast', True):
            break
        page_token = data.get('nextPageToken')
        time.sleep(0.3)

    if verbose:
        print(f"\nTotal matching from Jira text search: {len(all_issues)}")

    # Filter locally: only tickets where parsed description contains keywords
    filtered = []
    for issue in all_issues:
        desc_text = get_description(issue).lower()
        summary = issue['fields'].get('summary', '').lower()
        combined = desc_text + ' ' + summary
        if any(kw in combined for kw in ['root cause', 'solution', 'fix']):
            filtered.append(issue)

    if verbose:
        print(f"After ADF parsing filter (root cause/solution/fix in description): {len(filtered)}")
    issues = filtered

    if not issues:
        if verbose:
            print("No matching issues found. Exiting.")
        return

    # ── Process each issue ─────────────────────────────────────────
    if verbose:
        print("\n" + "=" * 60)
        print("Step 2: Distilling Jira tickets into structured notes")
        print("=" * 60)

    notes_data = []  # For MOC index

    for idx, issue in enumerate(issues):
        key = issue['key']
        fields = issue['fields']
        summary = fields.get('summary', 'N/A')

        if verbose:
            print(f"  [{idx+1}/{len(issues)}] {key}: {summary[:60]}...")

        # Fetch comments
        comments = get_comments(key)

        # Generate note
        note = generate_note(issue, comments)

        # Write file
        filename = f"{key}-troubleshooting.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(note)

        # Collect for MOC
        component = infer_component(summary, get_description(issue), fields.get('labels', []))
        symptom = extract_symptom(get_description(issue))
        notes_data.append({
            "key": key,
            "summary": summary,
            "component": component,
            "symptom": symptom[:80] if symptom else summary[:80],
            "resolved": fields.get('resolutiondate', '')[:10] if fields.get('resolutiondate') else '',
            "type": fields.get('issuetype', {}).get('name', ''),
        })

        # Rate limit
        if (idx + 1) % 20 == 0:
            time.sleep(1)

    # ── Step 3: Build MOC index ────────────────────────────────────
    if verbose:
        print("\n" + "=" * 60)
        print("Step 3: Building MOC index")
        print("=" * 60)

    # Group by component
    by_component = {}
    for n in notes_data:
        comp = n["component"]
        if comp not in by_component:
            by_component[comp] = []
        by_component[comp].append(n)

    # Group by symptom keyword
    symptom_groups = {
        "Error / Exception": [],
        "Missing Data / Display": [],
        "Email / Notification": [],
        "Workflow / Approval": [],
        "Integration / API": [],
        "Permission / Access": [],
        "UI / UX": [],
        "Performance": [],
        "Other": [],
    }

    err_kw = ['error', 'exception', 'fail', 'bug', 'incorrect', 'wrong']
    missing_kw = ['missing', 'no show', 'disappear', 'not display', 'blank', 'empty']
    email_kw = ['email', 'notification', 'reminder', 'mail']
    workflow_kw = ['approval', 'submission', 'workflow', 'validation', 'draft', 'discard', 'return']
    integration_kw = ['fms', 'api', 'interface', 'po ', 'integration']
    permission_kw = ['permission', 'access', 'role', 'delegation', 'login', 'user']
    ui_kw = ['display', 'show', 'ui', 'label', 'button', 'page', 'misalignment']
    perf_kw = ['performance', 'slow', 'unresponsive', 'timeout', 'crash']

    def classify_symptom(text):
        tl = text.lower()
        if any(kw in tl for kw in err_kw): return "Error / Exception"
        if any(kw in tl for kw in missing_kw): return "Missing Data / Display"
        if any(kw in tl for kw in email_kw): return "Email / Notification"
        if any(kw in tl for kw in workflow_kw): return "Workflow / Approval"
        if any(kw in tl for kw in integration_kw): return "Integration / API"
        if any(kw in tl for kw in permission_kw): return "Permission / Access"
        if any(kw in tl for kw in ui_kw): return "UI / UX"
        if any(kw in tl for kw in perf_kw): return "Performance"
        return "Other"

    for n in notes_data:
        cat = classify_symptom(n["symptom"] + " " + n["summary"])
        symptom_groups[cat].append(n)

    today = date.today().isoformat()
    
    moc = """---
tags: moc, troubleshooting, index
created: {today}
---

# 解決手冊

> 共 {total} 條記錄 · 更新於 {today}

## 依症狀

""".format(today=today, total=len(notes_data))

    for cat in ["Error / Exception", "Missing Data / Display", "Email / Notification",
                 "Workflow / Approval", "Integration / API", "Permission / Access",
                 "UI / UX", "Performance", "Other"]:
        items = symptom_groups.get(cat, [])
        if items:
            moc += f"### {cat}（{len(items)}）\n\n"
            for n in items:
                moc += f"- [[{n['key']}-troubleshooting|{n['key']}]] — {n['symptom'][:60]}\n"
            moc += "\n"

    moc += "## 依元件\n\n"
    for comp in sorted(by_component.keys()):
        items = by_component[comp]
        moc += f"### {comp}（{len(items)}）\n\n"
        for n in items:
            moc += f"- [[{n['key']}-troubleshooting|{n['key']}]] — {n['symptom'][:60]}\n"
        moc += "\n"

    moc += "## 完整列表\n\n| Ticket | Summary | Component | Resolved |\n|--------|---------|-----------|----------|\n"
    for n in sorted(notes_data, key=lambda x: x['key']):
        summary_safe = n['summary'].replace('|', '\\|')[:70]
        moc += f"| [[{n['key']}-troubleshooting|{n['key']}]] | {summary_safe} | {n['component']} | {n['resolved']} |\n"

    index_path = os.path.join(OUTPUT_DIR, "index.md")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(moc)

    if verbose:
        print(f"\n{'='*60}")
        print(f"Done!")
        print(f"  Notes created: {len(notes_data)} → {OUTPUT_DIR}/")
        print(f"  MOC index: {index_path}")
        print(f"{'='*60}")

if __name__ == '__main__':
    main()
