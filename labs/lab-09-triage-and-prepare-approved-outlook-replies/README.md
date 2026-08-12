# Lab 9 — Triage and Prepare Approved Outlook Replies

**Topic 04:** Agentic Coordination with Outlook, Cowork and Claude Code  |  **Day 1**  |  **Approx. 30 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore omnichannel home-and-lifestyle company with retail, e-commerce and marketplace operations. Learners join its Business Transformation Office to prepare an integrated FY2027 planning and management pack.

Use Claude for Outlook and approved Microsoft 365 context to classify planning mail, summarise threads, prepare draft replies and coordinate meetings without silently sending anything.

## Goal

Triage Outlook messages and prepare consistent replies with a human send gate.

## What you'll build

A triage queue, cited thread summary, approved reply templates, draft responses and an unsent meeting invitation.

**Tools and techniques:** Claude for Outlook beta, Outlook categories, thread citations, reply templates, calendar, approval queue

## Company use case

- **Department:** Executive Office
- **Sponsor:** Chief of Staff
- **Business challenge:** Handle the FY2027 planning inbox quickly without losing decisions, deadlines or approval control.
- **Decision:** Which messages need escalation, a standard draft, a tailored reply or no action?
- **Evidence:** Planning inbox sample; Reply policy; Executive tone guide; Meeting calendar
- **Measures:** Messages triaged; Draft turnaround; Citation completeness; Escalations; Send defects
- **Controls:** No silent send; Recipient verification; Attachment/version check; Escalation rules

## Files in this lab folder

- `Lumina-Living-Lab-09-Company-Brief.docx`
- `Lumina-Living-Lab-09-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-09-Working-Workbook.xlsx`
- `Lumina-Living-Lab-09-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Labs 1–8 completed.
- Open the supplied fictional Outlook thread export and Reply Policy.
- Claude for Outlook may require tenant deployment and Graph consent for inbox-wide features.

## Process map

Classify → Summarise with citations → Select approved template → Draft in native form → Review recipients and send

## Steps

### Step 1

Review the Reply Policy and configure four categories in the Triage Queue: Executive decision, Draft eligible, Information only and Escalate.

### Step 2

Open the supplied planning thread in Outlook or use the trainer-prepared mailbox. Activate Claude in the message ribbon.

### Step 3

Ask for a cited thread summary before drafting.

**Prompt to give Claude:**

```text
Summarise this planning thread into decisions made, unresolved questions, owner, deadline and required reply. Cite the source email for every item and flag any contradictory date, amount or attachment version. Do not draft or send yet.
```

### Step 4

Compare the summary with the Word and Excel source files. Resolve any figure or version mismatch in the source artifact.

### Step 5

If inbox-wide access is approved, ask Claude to classify only the fictional planning messages against the four categories.

**Prompt to give Claude:**

```text
Classify the approved FY2027 planning messages into Executive decision, Draft eligible, Information only or Escalate. For each, state reason, priority, SLA and source citation. Do not move, archive, delete, reply or send.
```

### Step 6

Select a Draft eligible message and choose the matching approved reply template.

### Step 7

Ask Claude to prepare the response in the native compose form and leave it unsent.

**Prompt to give Claude:**

```text
Draft a reply using the approved Executive Office template and tone guide. Confirm the decision, list the agreed actions with owners, cite the correct attached file versions and request comments by the stated deadline. Keep it under 160 words. Place it in Outlook as a draft and do not send.
```

### Step 8

Review To, Cc, Bcc, subject, names, dates, amounts, commitments, attachments, sensitivity and tone. Record the reviewer in the queue.

### Step 9

Ask Claude to find a 30-minute review slot and prepare an invitation with purpose, agenda, pre-read and decision required. Leave it unsent.

**Prompt to give Claude:**

```text
Find a 30-minute review time for the people on this thread. Prepare an Outlook invitation with purpose, three-item agenda, named pre-read files and the decision required. Leave the invitation unsent for review.
```

### Step 10

The authorised user may send only after trainer approval in the classroom simulation; otherwise retain or discard the draft.

## Test it

The triage queue is complete, the thread summary cites every decision, each draft uses an approved template and the reviewer has checked recipients, content, attachments and deadline before any send action.

## Troubleshooting

- **Outlook requests admin approval.** Treat the visible state as real and use the supplied thread export for the exercise; the authorised administrator must grant the required access.
- **Claude is ready to draft but not send.** This is the expected Claude for Outlook control. Review in the native compose form and retain the human send gate.
- **The summary misses context.** Open the full conversation, ask for per-message citations and compare the source thread manually.

## Challenge

Create an escalation rule for messages that contain a financial commitment, legal interpretation or personal data.

## Reflection

Which part of email handling should remain human even if drafting becomes nearly automatic?

## Deliverable

A triage queue, cited thread summary, approved reply templates, draft responses and an unsent meeting invitation.

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
