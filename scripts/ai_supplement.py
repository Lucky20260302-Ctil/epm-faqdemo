#!/usr/bin/env python3
"""
AI FAQ Supplement Script
=========================
Reads FAQ files with quality=partial, uses LLM to extract structured
symptom/root_cause/solution from raw Jira content, and rewrites files.

Usage:
  python scripts/ai_supplement.py --dry-run          # Preview changes
  python scripts/ai_supplement.py --batch 10         # Process 10 files
  python scripts/ai_supplement.py --all              # Process all partial files
  python scripts/ai_supplement.py --file <path>      # Process single file

Environment:
  ANTHROPIC_API_KEY - required for API calls
"""

import os
import re
import sys
import json
import yaml
import time
import argparse
from pathlib import Path
from typing import Optional

FAQ_DIR = Path("FAQ_test")

SYSTEM_PROMPT = """You are a technical FAQ editor for an ERP retail system (EPM/FEPOS/ChainStorePlus).

Given a raw Jira ticket transcription, extract and structure the content into three sections:

1. SYMPTOM (症狀): What the user saw - error messages, unexpected behavior, business impact. 2-3 sentences.
2. ROOT CAUSE (根因): Technical reason why it happened. 1-3 sentences. If unknown, write "待確認".
3. SOLUTION (解法): How to fix it - code changes, config changes, workaround steps. 1-3 sentences. If unknown, write "待確認".

Also extract metadata:
- severity: low | medium | high | critical
- components: list of affected system components

Output ONLY valid JSON with this exact structure:
{
  "symptom": "...",
  "root_cause": "...",
  "solution": "...",
  "severity": "medium",
  "components": ["Component1", "Component2"],
  "quality": "complete"
}

If content is just raw chat logs without technical substance, set quality to "partial" and provide whatever can be extracted. If content is completely meaningless, set quality to "stub" and use empty strings.

IMPORTANT: Output ONLY the JSON. No markdown fences, no explanation."""


def parse_frontmatter_and_body(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter and body from markdown content."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return {}, content
    try:
        fm = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        fm = {}
    body = content[match.end():]
    return fm or {}, body


def call_llm(body_text: str, issue_key: str) -> Optional[dict]:
    """Call Anthropic API to extract structured FAQ content."""
    import anthropic

    client = anthropic.Anthropic()

    user_message = f"""Jira Issue: {issue_key}

Raw content:
{body_text[:4000]}"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_message}],
        )
        response_text = message.content[0].text.strip()
        # Remove markdown fences if present
        response_text = re.sub(r"^```(?:json)?\s*", "", response_text)
        response_text = re.sub(r"\s*```$", "", response_text)
        return json.loads(response_text)
    except Exception as e:
        print(f"  API error: {e}", file=sys.stderr)
        return None


def supplement_file(file_path: Path, dry_run: bool = True) -> dict:
    """Process a single FAQ file with AI supplement."""
    result = {"path": str(file_path), "action": "skipped", "quality_before": "partial", "quality_after": "partial"}

    content = file_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter_and_body(content)

    if fm.get("quality") != "partial":
        result["action"] = "skipped"
        result["quality_before"] = fm.get("quality")
        return result

    result["quality_before"] = "partial"
    issue_key = fm.get("issue_key", file_path.stem.split("-")[0:2])
    if isinstance(issue_key, list):
        issue_key = "-".join(issue_key)

    print(f"  Processing {issue_key}...")

    extracted = call_llm(body, str(issue_key))
    if not extracted:
        result["action"] = "api_error"
        return result

    # Update frontmatter
    fm["symptom"] = extracted.get("symptom", "")
    fm["root_cause"] = extracted.get("root_cause", "")
    fm["solution"] = extracted.get("solution", "")
    fm["quality"] = extracted.get("quality", "partial")
    if extracted.get("severity"):
        fm["severity"] = extracted["severity"]
    if extracted.get("components"):
        fm["components"] = extracted["components"]

    # Rebuild file content with structured sections
    title = fm.get("title", f"{issue_key}")

    new_body = f"# {title}\n\n"
    new_body += f"## 症狀\n\n{extracted.get('symptom', '')}\n\n"
    new_body += f"## 根因\n\n{extracted.get('root_cause', '')}\n\n"
    new_body += f"## 解法\n\n{extracted.get('solution', '')}\n\n"
    new_body += "## 相關資訊\n\n"
    new_body += f"- **Jira:** [{issue_key}]({fm.get('jira_url', '')})\n"

    new_fm_yaml = yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200).strip()
    new_content = f"---\n{new_fm_yaml}\n---\n\n{new_body}"

    if dry_run:
        result["action"] = "would_update"
        result["quality_after"] = extracted.get("quality", "partial")
        result["preview"] = {
            "symptom": extracted.get("symptom", "")[:100],
            "root_cause": extracted.get("root_cause", "")[:100],
            "solution": extracted.get("solution", "")[:100],
        }
    else:
        file_path.write_text(new_content, encoding="utf-8")
        result["action"] = "updated"
        result["quality_after"] = extracted.get("quality", "partial")

    return result


def main():
    parser = argparse.ArgumentParser(description="AI FAQ Supplement")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Preview changes only")
    parser.add_argument("--apply", action="store_true", help="Actually write changes")
    parser.add_argument("--batch", type=int, default=0, help="Process N files")
    parser.add_argument("--all", action="store_true", help="Process all partial files")
    parser.add_argument("--file", type=str, help="Process a single file")
    args = parser.parse_args()

    dry_run = not args.apply

    if dry_run:
        print("[DRY RUN] Preview mode — use --apply to write changes\n")
    else:
        print("[APPLY] Writing changes to files\n")

    # Collect files to process
    targets = []
    if args.file:
        targets = [Path(args.file)]
    else:
        for md_file in sorted(FAQ_DIR.rglob("*.md")):
            if md_file.name.startswith(".") or md_file.name == "index.md":
                continue
            targets.append(md_file)

        # Filter to partial only
        partial_targets = []
        for t in targets:
            content = t.read_text(encoding="utf-8")
            if "quality: partial" in content[:500]:
                partial_targets.append(t)
        targets = partial_targets

        if args.batch > 0:
            targets = targets[:args.batch]
        elif not args.all:
            print(f"Found {len(targets)} partial files. Use --batch N or --all to process.")
            print("Example: python scripts/ai_supplement.py --apply --batch 10")
            return

    print(f"Processing {len(targets)} files...\n")

    results = []
    for i, file_path in enumerate(targets):
        print(f"[{i+1}/{len(targets)}]", end=" ")
        result = supplement_file(file_path, dry_run=dry_run)
        results.append(result)

    # Summary
    updated = [r for r in results if r["action"] in ("updated", "would_update")]
    completed = [r for r in updated if r["quality_after"] == "complete"]
    errors = [r for r in results if r["action"] == "api_error"]

    print(f"\n{'='*50}")
    print(f"SUMMARY")
    print(f"{'='*50}")
    print(f"Total: {len(results)}")
    print(f"  Supplemented: {len(updated)} ({len(completed)} -> complete)")
    print(f"  Errors: {len(errors)}")

    if dry_run and updated:
        print(f"\n--- Preview (first 5) ---")
        for r in updated[:5]:
            p = r.get("preview", {})
            print(f"\n  {r['path']}")
            print(f"    Quality: {r['quality_before']} -> {r['quality_after']}")
            print(f"    Symptom: {p.get('symptom', '')[:80]}...")
            print(f"    Root Cause: {p.get('root_cause', '')[:80]}...")


if __name__ == "__main__":
    main()
