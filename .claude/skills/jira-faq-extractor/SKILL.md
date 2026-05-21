---
name: jira-faq-extractor
description: Extract FAQ-worthy issues from Jira projects and generate structured Obsidian knowledge base files. Use when the user wants to convert Jira issues into FAQ documentation, extract troubleshooting knowledge from Jira, or build an Obsidian vault from Jira data. Triggers: "Jira FAQ", "extract issues to Obsidian", "Jira knowledge base", "convert Jira to FAQ", "download Jira issues as markdown".
---

# Jira FAQ Extractor

Extracts FAQ-worthy issues from Jira projects and generates structured Obsidian markdown knowledge base files organized by project and component category.

## Workflow

### Step 1: Discovery

Get the Atlassian cloud ID via `mcp__atlassian__getAccessibleAtlassianResources`, then use `mcp__atlassian__getVisibleJiraProjects` to identify the target projects by key.

Confirm project keys and scope with the user before proceeding.

### Step 2: Full-Text Candidate Search

For each target project, search for Done issues containing FAQ-relevant keywords:

```
project = {KEY} AND statusCategory = Done AND (
  text ~ "root cause" OR text ~ "solution" OR text ~ "fix"
  OR text ~ "workaround" OR text ~ "原因" OR text ~ "解决" OR text ~ "修复"
) ORDER BY updated DESC
```

**CRITICAL**: Paginate through ALL results using `nextPageToken`. Never stop at the first page — process every page until `isLast: true`.

Capture for each result: key, summary, status, resolution date.

### Step 3: Parallel Classification

Launch parallel Explore agents to read candidate issues in batches (20-30 per agent). For each issue, fetch the full description via `mcp__atlassian__getJiraIssue`.

**FAQ-worthy criteria (INCLUDE):**
- Has documented root cause AND solution
- Configuration / setup / deployment issues
- Recurring problems (affects multiple stores/users, mentioned multiple times)
- API/integration errors with identifiable patterns
- Performance issues with identified bottlenecks
- Common error messages with troubleshooting steps

**NOT FAQ-worthy (EXCLUDE):**
- Typo fixes, text/translation corrections
- One-time data fixes in specific environments
- Already-fixed version-specific bugs unlikely to recur
- Empty descriptions, no technical detail
- SOW/project-task items, test cases
- Pure UI tweaks (color, spacing, layout)
- Trivial tasks (update config, add logging)
- Duplicate issues (keep the most detailed one)

### Step 4: Content Extraction

For each confirmed FAQ-worthy issue, extract:
- **symptom**: One-sentence problem description (from summary + description)
- **root-cause**: The underlying cause (from description comments or resolution)
- **solution**: How it was fixed (from resolution comments)
- **fix-version**: Version where the fix was applied
- **component**: The affected module/area
- **resolved**: Resolution date (ISO format)

### Step 5: Organize by Category

Classify each FAQ into a two-level hierarchy:

```
FAQ_test/
├── index.md                    ← Master index
├── {PROJECT}/
│   ├── index.md                ← Project index
│   └── {Category}/
│       └── {KEY}-{slug}.md     ← Individual FAQ note
```

Categories are determined dynamically based on the actual issue content. Common categories include:
- **FE**: 交易流程, DayEnd-结算, 会员-API, 折扣-优惠券, 列印, 系统服务, 其他
- **MP**: 安装部署, 交易流程, 会员, 系统兼容
- **BE**: Polling, Data Interface, BEAPI/CRM, eName
- **WEB**: eName, Member-API, ePromo

### Step 6: Generate Obsidian Files

Use this exact template for each FAQ note:

```markdown
---
tags: [faq, {project}, {category_tag}]
component: "{component}"
symptom: "{one-line symptom}"
root-cause: "{one-line root cause}"
solution: "{one-line solution}"
jira: {ISSUE-KEY}
resolved: {YYYY-MM-DD}
fix-version: "{version or empty}"
---

# {ISSUE-KEY}: {Title}

## 問題

{symptom description}

## 根因

{root cause analysis}

## 解法

{solution steps}

## 相關資訊

- Jira: [{ISSUE-KEY}](https://ctil.atlassian.net/browse/{ISSUE-KEY})
- Fix Version: {fix version or 未記錄}
- 解決日期: {resolved date}
```

### Step 7: Generate Index Files

Create `index.md` for each directory level:
- **Root index**: Table with project → FAQ count → description
- **Project index**: Table grouped by category with ticket links
- Include metadata: `tags: [moc, faq, {project}, index]`, `updated: {date}`

## Batch Processing Strategy

Given the scale (hundreds to thousands of issues across projects), use this efficient approach:

1. **Phase 1** — Launch one Explore agent per project in parallel for candidate search (Step 2)
2. **Phase 2** — Launch multiple Explore agents in parallel for classification (Step 3), each handling 20-30 issues
3. **Phase 3** — Use a Python script to generate all `.md` files from the classified results (Steps 5-7)

This keeps the main conversation context clean while maximizing throughput.

## Jira API Notes

- Cloud ID is derived from the Atlassian site URL (e.g., `ctil.atlassian.net`)
- `maxResults` is capped at 100 per page; always check `isLast` for pagination
- `mcp__atlassian__searchJiraIssuesUsingJql` returns summaries; use `mcp__atlassian__getJiraIssue` for full details
- Use `mcp__atlassian__fetch` for ARI-based lookups if needed

## Output Verification

After generation, verify:
1. Count files per category matches expected FAQ count
2. Spot-check 3-5 files for content quality
3. Ensure all wikilinks in index files resolve to existing notes
4. Run `npx quartz build -d .` to verify site builds cleanly
