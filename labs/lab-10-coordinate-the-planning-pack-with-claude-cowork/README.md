# Lab 10 — Coordinate the Planning Pack with Claude Cowork

**Topic 04:** Agentic Coordination with Outlook, Cowork and Claude Code  |  **Day 1**  |  **Approx. 35 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore omnichannel home-and-lifestyle company with retail, e-commerce and marketplace operations. Learners join its Business Transformation Office to prepare an integrated FY2027 planning and management pack.

Set up a scoped Cowork project, bring in approved Microsoft 365 evidence, create a multi-step plan and deliver reviewed Office files back to the company workflow.

## Goal

Use Claude Cowork and Microsoft 365 context to coordinate a bounded multi-file company task.

## What you'll build

A Cowork project folder, execution plan, consolidated management brief, discrepancy log and reviewed Office hand-off.

**Tools and techniques:** Claude Cowork, work folder, Projects, plugins, Microsoft 365 connector, multi-step execution, approvals

## Company use case

- **Department:** Business Transformation Office
- **Sponsor:** Chief Operating Officer
- **Business challenge:** Consolidate the approved FY2027 plan into a consistent management brief and hand-off pack.
- **Decision:** Can the planning pack proceed to Executive Committee review without unresolved evidence or version conflicts?
- **Evidence:** Approved lab outputs; Microsoft 365 planning messages; Decision log; Source register
- **Measures:** Files reconciled; Discrepancies found; Approvals complete; Turnaround time
- **Controls:** Scoped folder; Read-first connector; Checkpoint approvals; Native Office review

## Files in this lab folder

- `Lumina-Living-Lab-10-Company-Brief.docx`
- `Lumina-Living-Lab-10-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-10-Working-Workbook.xlsx`
- `Lumina-Living-Lab-10-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Labs 1–9 completed.
- Claude desktop with Cowork access.
- The Microsoft 365 connector is approved or the supplied local source pack is used as fallback.

## Process map

Scope the folder → Connect approved context → Plan the task → Watch and steer → Review files in Microsoft 365

## Steps

### Step 1

Create a clean work folder inside the Lab 10 folder and copy only the reviewed Word, Excel and PowerPoint outputs from earlier labs.

### Step 2

Open Claude desktop, select Cowork and run the guided setup if required. Choose only the Lab 10 work folder.

**Command or in-app command:**

```bash
/setup-cowork
```

### Step 3

Inspect the active plugins, connectors and folder boundary. Record unavailable capabilities rather than requesting broad access.

### Step 4

Give Cowork a result-oriented task and require a plan before file changes.

**Prompt to give Claude:**

```text
Using only this work folder and the approved Microsoft 365 planning context, prepare a consolidated FY2027 Executive Committee hand-off. First show a plan with inputs, reconciliation checks, output files and approval checkpoints. Do not modify or create files until I approve the plan.
```

### Step 5

Review the plan. Confirm source priority: verified Excel for figures, approved Word documents for narrative, Outlook for decisions and the source register for ownership.

### Step 6

Approve the analysis phase only. Ask Cowork to create a discrepancy log covering figures, dates, owners, versions, commitments and missing approvals.

**Prompt to give Claude:**

```text
Create a discrepancy log before drafting the brief. Compare the approved files and planning messages for figures, dates, owners, version names, commitments and approvals. Cite every source and do not resolve conflicts by guessing.
```

### Step 7

Resolve high-impact discrepancies in the source files with the named owner. Replace the work-folder copy with the reviewed version.

### Step 8

Ask Cowork to create a two-page management brief and updated hand-off index in the folder.

**Prompt to give Claude:**

```text
Create a two-page management brief and hand-off index from the reconciled sources. Include decision required, strategic choices, marketing priorities, financial outlook, sustainability/people commitments, Q1 milestones, risks and approvals. Cite the source file or message for each section.
```

### Step 9

Open the generated Word, Excel and PowerPoint files in their native apps. Use Claude for Microsoft 365 to make only selected, tracked corrections.

### Step 10

Record final approvals and keep the Cowork task, discrepancy log and source files together as the audit trail.

## Test it

Cowork worked only inside the scoped project, produced a visible plan and discrepancy log, and every generated Office artifact was reviewed in its native app before the hand-off was approved.

## Troubleshooting

- **Cowork cannot access Microsoft 365.** Use the local approved source pack and record the connector limitation; do not widen permissions merely to complete the lab.
- **Cowork writes too early.** Require a plan-first approval and give staged approval for analysis, drafting and final file creation.
- **Files disagree.** Resolve the conflict in the authoritative source with its owner, then rerun only the affected output.

## Challenge

Turn the approved hand-off workflow into a reusable Cowork skill outline with explicit inputs, checks and approval points.

## Reflection

Which checkpoint gave you the most control over a multi-step agentic task?

## Deliverable

A Cowork project folder, execution plan, consolidated management brief, discrepancy log and reviewed Office hand-off.

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
