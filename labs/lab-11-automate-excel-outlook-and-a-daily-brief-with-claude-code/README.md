# Lab 11 — Automate Excel, Outlook and a Daily Brief with Claude Code

**Topic 04:** Agentic Coordination with Outlook, Cowork and Claude Code  |  **Day 1**  |  **Approx. 30 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore omnichannel home-and-lifestyle company with retail, e-commerce and marketplace operations. Learners join its Business Transformation Office to prepare an integrated FY2027 planning and management pack.

Build a safe, repeatable work process that refreshes a local Excel control workbook, searches approved planning mail and generates a source-linked daily brief without embedding secrets or auto-sending messages.

## Goal

Use Claude Code and approved connectors to update Excel, search Outlook and produce a daily management brief.

## What you'll build

A reviewed automation plan, local workbook-update script, connector-assisted Outlook search and generated daily brief with run log.

**Tools and techniques:** Claude Code, MCP, Microsoft 365 connector, Python, openpyxl, python-docx, run log, approval gates

## Company use case

- **Department:** Business Performance
- **Sponsor:** Chief Operating Officer
- **Business challenge:** Prepare a reliable daily management brief from the latest control workbook and approved Outlook planning messages.
- **Decision:** Which KPI exception, decision request or overdue action needs management attention today?
- **Evidence:** Daily control workbook; Approved Outlook planning mail; Brief template; Automation configuration
- **Measures:** Workbook updated; Messages cited; Exceptions identified; Run status; Reviewer approval
- **Controls:** No secrets in source; Explicit MCP approval; No auto-send; Idempotent update and backup

## Files in this lab folder

- `Lumina-Living-Lab-11-Company-Brief.docx`
- `Lumina-Living-Lab-11-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-11-Working-Workbook.xlsx`
- `Lumina-Living-Lab-11-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`
- `automation/update_daily_control.py`
- `automation/generate_daily_brief.py`
- `inputs/daily-input.csv`
- `inputs/outlook-findings.json`

## Prerequisites

- Labs 1–10 completed.
- Claude Code installed and authenticated with the approved Claude.ai account.
- Python 3 with openpyxl and python-docx available; the lab provides an offline-ready starter.

## Process map

Plan and inspect → Verify MCP and files → Update Excel locally → Search approved Outlook context → Generate and review daily brief

## Steps

### Step 1

Open a terminal in the Lab 11 folder and inspect every supplied file before starting Claude Code.

**Command or in-app command:**

```bash
pwd
find . -maxdepth 2 -type f -print | sort
```

### Step 2

Create and activate a local virtual environment, then install only the two required document libraries if they are not already present.

**Command or in-app command:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install openpyxl python-docx
```

### Step 3

Start Claude Code and verify its version and MCP status. The approved Microsoft 365 connector configured in Claude.ai should appear when the same subscription authentication is active.

**Command or in-app command:**

```bash
claude --version
claude mcp list
```

### Step 4

Inside Claude Code, open /mcp, authenticate the approved Microsoft 365 connector if prompted and inspect the available read/write tools. Do not approve a write tool for this exercise.

**Command or in-app command:**

```bash
/mcp
```

### Step 5

Ask Claude Code to inspect the workbook, brief template and starter script, then propose a plan before editing.

**Prompt to give Claude:**

```text
Inspect this lab folder. Explain the workbook sheets, formulas and control cells; the daily-brief template; the starter Python script; and the run-log contract. Propose the smallest safe implementation. Do not edit or run anything until I approve the plan.
```

### Step 6

Approve the local-file phase. Ask Claude Code to complete or review the workbook updater so it writes today's approved inputs, preserves formulas and formats, creates a timestamped backup and appends a run-log row.

**Prompt to give Claude:**

```text
Implement the local workbook update only. Preserve formulas, named tables, charts and formats; create a timestamped backup; make the update idempotent; validate expected sheets and columns; and append date, input file, rows changed, status and reviewer placeholder to Run_Log. Do not access Outlook yet.
```

### Step 7

Run the updater on the fictional input file and inspect the workbook output.

**Command or in-app command:**

```bash
python automation/update_daily_control.py --input inputs/daily-input.csv --workbook Lumina-Living-Daily-Control.xlsx --output outputs/Lumina-Living-Daily-Control-Updated.xlsx
```

### Step 8

Ask Claude Code to use the approved Microsoft 365 connector to search only the fictional planning messages for the last business day. Require source citations and no draft/send action.

**Prompt to give Claude:**

```text
Search the approved Lumina Living planning mailbox context for the last business day. Return only decisions requested, overdue actions, material risks and changed deadlines. Cite each message. Do not create, update, draft or send anything in Microsoft 365.
```

### Step 9

Provide the cited mail findings to the local brief generator and require workbook cell citations for KPI exceptions.

**Prompt to give Claude:**

```text
Generate today's management brief from outputs/Lumina-Living-Daily-Control-Updated.xlsx and the cited Outlook findings. Use the supplied Word template. Include KPI exceptions with cell citations, decisions requested with message citations, overdue actions, risks, and a reviewer checklist. Do not invent missing information or send the brief.
```

### Step 10

Run the local brief generator and open the DOCX for review.

**Command or in-app command:**

```bash
python automation/generate_daily_brief.py --workbook outputs/Lumina-Living-Daily-Control-Updated.xlsx --mail inputs/outlook-findings.json --template templates/Daily-Brief-Template.docx --output outputs/Lumina-Living-Daily-Brief.docx
```

### Step 11

Verify backup creation, formula integrity, cited messages, cited cells, no embedded secrets and a completed run log. Record the human approval without sending the file.

## Test it

The reviewed scripts run successfully, the updated workbook preserves formulas and charts, the daily brief cites Excel and Outlook evidence, the run log is complete and no email was sent or secret stored.

## Troubleshooting

- **The M365 connector is absent in Claude Code.** Run /status to confirm Claude.ai subscription authentication, configure the connector in Claude.ai, then use /mcp; do not hardcode tokens or unreviewed endpoints.
- **The workbook loses formulas or formatting.** Write only designated input cells, load without data_only, preserve styles and validate formulas before saving.
- **The updater duplicates rows.** Use a stable business key and make the update idempotent before rerunning.
- **Mail search returns too much.** Narrow the date, mailbox context, subject prefix and allowed output fields; require citations.

## Challenge

Add a dry-run flag that reports proposed cell changes and mail-query scope without writing any output.

## Reflection

Which automation step needs the strongest approval boundary, and how would you monitor it in production?

## Deliverable

A reviewed automation plan, local workbook-update script, connector-assisted Outlook search and generated daily brief with run log.

## Current product references

- [Claude for Microsoft 365 overview](https://claude.com/claude-for-microsoft-365)
- [Set up the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector)
- [Use Claude for Microsoft 365 with third-party platforms](https://claude.com/docs/office-agents/third-party-platforms)
- [Get started in Claude Cowork in three steps](https://claude.com/resources/tutorials/get-started-in-claude-cowork-in-three-steps)
- [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)
- [Copilot Cowork overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/)
- [Microsoft 365 Copilot with Anthropic models](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-anthropic-apps)
- [Syracuse University: Claude Microsoft 365 connector](https://its.syr.edu/your-work-apps-meet-your-ai-assistant-using-claudes-microsoft-365-connector/)
- [Claude for Microsoft 365 setup and use cases](https://justinmckelvey.com/blog/claude-for-microsoft-365)

---

*Claude Microsoft 365 Masterclass (C197) · C197 · Version v2.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
