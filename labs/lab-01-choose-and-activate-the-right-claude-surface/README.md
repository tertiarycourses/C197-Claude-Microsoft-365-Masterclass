# Lab 1 — Choose and Activate the Right Claude Surface

**Topic 01:** Governed Foundations for Claude and Microsoft 365  |  **Day 1**  |  **Approx. 20 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore omnichannel home-and-lifestyle company with retail, e-commerce and marketplace operations. Learners join its Business Transformation Office to prepare an integrated FY2027 planning and management pack.

Compare the Office add-ins, Microsoft 365 connector, Claude Cowork and Claude-powered Microsoft 365 Copilot experiences before touching company data.

## Goal

Select and activate the Claude surface that fits a governed Lumina Living task.

## What you'll build

A completed operating-surface decision matrix and environment-readiness record.

**Tools and techniques:** Claude for Microsoft 365, Claude connector, Claude Cowork, Microsoft 365 Copilot, admin deployment

## Company use case

- **Department:** Business Transformation Office
- **Sponsor:** Chief Operating Officer
- **Business challenge:** Choose a safe operating surface for the FY2027 planning pack before granting or requesting access.
- **Decision:** Which Claude surface should each planning, analysis and communication task use?
- **Evidence:** IT acceptable-use note; Microsoft 365 tenant capability register; FY2027 planning brief
- **Measures:** Users ready; Add-ins available; Connector consent status; Fallback tested
- **Controls:** No shared password in learner files; No permission bypass; Named system owner approval

## Files in this lab folder

- `Lumina-Living-Lab-01-Company-Brief.docx`
- `Lumina-Living-Lab-01-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-01-Working-Workbook.xlsx`
- `Lumina-Living-Lab-01-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- The trainer has privately assigned a classroom account; credentials are not written in this lab or repository.
- Word, Excel, PowerPoint and Outlook are installed or available on the web.
- Claude desktop and Claude Code are installed for later labs, where available.

## Process map

Define the task → Compare surfaces → Check licence and tenant → Activate the approved route → Record the fallback

## Steps

### Step 1

Open the lab folder and inspect the company brief, readiness workbook and executive starter deck before signing in anywhere.

### Step 2

Classify four example tasks—edit a strategy section, analyse finance, search recent Outlook decisions and coordinate a multi-file pack—against the four operating surfaces.

### Step 3

Open Word, Excel and PowerPoint, locate the Claude add-in and sign in with the trainer-issued classroom account. Record the visible state in the Readiness workbook.

### Step 4

Open Outlook and check whether Claude for Outlook is present. If the tenant shows an approval requirement, record it as an environment constraint; do not attempt a workaround.

### Step 5

In Claude, open Customize > Connectors and inspect Microsoft 365. Record whether organisation enablement, Entra administrator consent and write tools are available.

### Step 6

Open Claude desktop and confirm whether Cowork appears in the mode picker. Do not grant folder access yet.

### Step 7

Open Microsoft 365 Copilot only if your tenant provides it. Record it as a distinct Microsoft surface, not as the Anthropic Office add-in.

### Step 8

Complete the decision matrix: task, preferred surface, required permission, human approval, fallback and owner.

### Step 9

Use Claude to challenge your matrix without asking it to change the file.

**Prompt to give Claude:**

```text
Act as an enterprise AI adoption lead. Review this operating-surface matrix for mismatched tasks, excessive permissions, missing approval owners and unrealistic fallbacks. Cite the row for every finding. Do not edit the workbook.
```

### Step 10

Correct the matrix yourself and save the approved copy in the lab folder.

## Test it

Every example task has one preferred surface, one governed fallback, a permission owner and a human approval point; no credential is stored in any learner-facing file.

## Troubleshooting

- **An add-in is missing.** Treat the visible state as real. Record it, use the approved upload fallback for class and ask the authorised administrator about deployment.
- **Connector authentication fails.** Confirm a business Entra account and tenant admin consent; personal Outlook.com accounts cannot use this connector.
- **Two products are both labelled Cowork.** Distinguish Anthropic Claude Cowork from Microsoft 365 Copilot Cowork by host, licensing, data boundary and approval model.

## Challenge

Add one recurring task from your role and justify the lowest-privilege surface that can complete it.

## Reflection

What evidence would convince your system owner that the selected surface is appropriate?

## Deliverable

A completed operating-surface decision matrix and environment-readiness record.

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
