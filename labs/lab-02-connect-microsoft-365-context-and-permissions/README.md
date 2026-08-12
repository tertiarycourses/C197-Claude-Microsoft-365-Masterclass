# Lab 2 — Connect Microsoft 365 Context and Map Permissions

**Topic 01:** Governed Foundations for Claude and Microsoft 365  |  **Day 1**  |  **Approx. 25 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore omnichannel home-and-lifestyle company with retail, e-commerce and marketplace operations. Learners join its Business Transformation Office to prepare an integrated FY2027 planning and management pack.

Build a source-and-permission register for Lumina Living's SharePoint, OneDrive, Outlook and Teams planning evidence.

## Goal

Connect approved Microsoft 365 context and map what Claude may read or write.

## What you'll build

A least-privilege source register with access status, evidence owner, retention note and approved use.

**Tools and techniques:** Microsoft 365 connector, Microsoft Entra, delegated permissions, SharePoint, OneDrive, Outlook, Teams

## Company use case

- **Department:** Information Governance
- **Sponsor:** Head of IT and Data Protection Officer
- **Business challenge:** Connect only the FY2027 planning evidence required by the project team.
- **Decision:** Which sources and tools should be enabled for each role?
- **Evidence:** SharePoint Strategy site; OneDrive project folder; Outlook planning mailbox; Teams leadership chat
- **Measures:** Sources approved; Owners confirmed; Read tools tested; Write tools disabled or approved
- **Controls:** Least privilege; Business Entra tenant; Per-user access boundary; No Teams write claim

## Files in this lab folder

- `Lumina-Living-Lab-02-Company-Brief.docx`
- `Lumina-Living-Lab-02-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-02-Working-Workbook.xlsx`
- `Lumina-Living-Lab-02-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Lab 1 completed.
- The trainer has confirmed whether Entra administrator consent is already present.
- Use only the fictional Lumina Living sources supplied in this folder.

## Process map

Inventory sources → Assign owners → Grant tenant consent → Connect individually → Test read before write

## Steps

### Step 1

Review the Source Register workbook and identify the business owner, sensitivity, retention need and intended Claude use for every source.

### Step 2

In Claude, navigate to Customize > Connectors > Microsoft 365. Connect only if the organisation and tenant consent are already approved.

### Step 3

Record the connector's visible tools and whether they are read or write. Do not assume write access from a successful sign-in.

### Step 4

Ask Claude to search only the approved FY2027 planning context and return a source inventory rather than a narrative.

**Prompt to give Claude:**

```text
Search the approved Microsoft 365 planning sources for Lumina Living FY2027. Return a table with item title, service, owner if stated, last modified date and direct source citation. Do not infer missing owners and do not create or update anything.
```

### Step 5

Compare the results with the supplied register. Mark missing, duplicate, stale or inaccessible sources.

### Step 6

Test an Outlook read query for planning messages and require per-message citations.

**Prompt to give Claude:**

```text
Find the fictional FY2027 planning messages approved for this exercise. List sender, date, subject, decision and unresolved action with a citation to each message. Do not draft or send email.
```

### Step 7

If write tools are not approved, record the limitation and retain read-only operation. If approved, perform only the trainer-authorised low-risk draft-to-self test.

**Prompt to give Claude:**

```text
Draft an email to my own training account summarising the connector test. Leave it as a draft and do not send it.
```

### Step 8

Update the Permission Map with the user group, source, tool, scope, owner, review date and fallback.

### Step 9

Ask Claude to identify excessive or missing permissions, then resolve each finding with the source owner.

**Prompt to give Claude:**

```text
Review this permission map for least-privilege issues. Flag any source or write capability that is not necessary for the stated business outcome. Cite the row and propose a narrower alternative.
```

## Test it

The source register reconciles to the connector results, every source has an owner and approved use, and write tools are either explicitly authorised or documented as unavailable.

## Troubleshooting

- **Admin approval is required.** Stop the connection attempt and escalate to the authorised Entra Global Administrator.
- **A source is missing.** Check the signed-in user's existing Microsoft 365 permission and the source location; do not request broad tenant access as a shortcut.
- **A Teams action is requested.** The Claude Microsoft 365 connector can read supported Teams context but does not provide tools to post Teams messages or change Teams settings.

## Challenge

Design a read-only pilot group and a separate, smaller write-enabled group for the company rollout.

## Reflection

Which permission would create the largest consequence if misused, and who should approve it?

## Deliverable

A least-privilege source register with access status, evidence owner, retention note and approved use.

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
