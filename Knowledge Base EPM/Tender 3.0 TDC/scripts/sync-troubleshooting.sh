#!/bin/bash
# Daily sync: run Jira KB distill, then copy troubleshooting files into Tender 3.0 TDC vault

VAULT_DIR="/Users/aukaiyan/Claude-Project/Knowledge Base EPM"
TENDER_DIR="${VAULT_DIR}/Tender 3.0 TDC"

# Step 1: Run the Jira KB sync
cd "$VAULT_DIR"
python3 scripts/distill_jira_kb.py --days 7 --quiet 2>&1 | logger -t jira-kb-sync

# Step 2: Copy updated troubleshooting files into Tender 3.0 TDC vault
cp -u "${VAULT_DIR}/03-Resources/troubleshooting/"*.md "${TENDER_DIR}/03-Resources/troubleshooting/" 2>&1 | logger -t tender-sync

# Log completion
echo "[$(date)] Tender 3.0 TDC sync complete" | logger -t tender-sync
