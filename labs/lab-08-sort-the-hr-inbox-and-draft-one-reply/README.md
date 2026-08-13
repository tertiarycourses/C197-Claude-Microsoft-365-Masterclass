# Lab 8 — Sort the HR Inbox and Draft One Reply

**Topic 04:** Staff Questions, Repeatable Work and Advanced Claude  |  **Day 1**  |  **Approx. 20 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update.

Work through a set of fictional staff messages held in a local workbook. Claude sorts them by what each one needs and drafts one reply. Then the Microsoft 365 connector turns that reply into a real Outlook draft — which you review and send yourself.

## Goal

Sort a set of staff messages by what each one needs, and draft one reply for approval.

## What you'll build

Every message sorted, one reply drafted, the person who would approve it named, and the reply created as an Outlook draft ready for review.

**Tools and techniques:** Claude for Outlook beta, Outlook categories, thread citations, reply templates, calendar, approval queue

## Company use case

- **Department:** Human Resources
- **Sponsor:** Head of HR
- **Business challenge:** Keep on top of staff questions without letting anything go out unchecked.
- **Decision:** Which messages need a reply from HR, and which need someone else to decide?
- **Evidence:** Staff messages sheet
- **Measures:** Messages sorted; Reply drafted; Approver named
- **Controls:** Nothing is sent; No invented dates or entitlements; A named person approves the reply

## Files in this lab folder

- `Lumina-Living-Lab-08-HR-Brief.docx`
- `Lumina-Living-Lab-08-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-08-Working-Workbook.xlsx`
- `Lumina-Living-Lab-08-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Excel installed, with the Claude panel available from the ribbon.
- Lumina-Living-Lab-08-Staff-Questions.xlsx from this folder.
- No mailbox, no Outlook and no work account are required. Nothing in this lab is sent.

## Process map

Classify → Summarise with citations → Select approved template → Draft in native form → Review recipients and send

## Steps

### Step 1

Open Lumina-Living-Lab-08-Staff-Questions.xlsx from this lab folder and click the Staff_Messages tab. These are fictional messages from Lumina Living staff. Everything here is local; you will not open Outlook and nothing is ever sent.

### Step 2

Open the Claude panel in Excel and ask Claude to sort the messages. Read the answer on screen.

**Prompt to give Claude:**

```text
Read the messages on the Staff_Messages sheet in this open workbook. Sort them into four groups: needs a reply from HR today, needs a decision from someone else, is just information, and needs nothing. Give your reason and say which Message_ID you mean for each one. Do not change the sheet.
```

### Step 3

In the Action column of the Staff_Messages tab, write the group you agree with for each message.

### Step 4

Pick one message that needs a reply and ask Claude to draft it. Read the draft on screen.

**Prompt to give Claude:**

```text
Draft a short reply to the message I have selected on the Staff_Messages sheet. Use only what that message and this workbook actually say. Keep it under 120 words, say clearly what happens next and who is doing it, and write 'need to check' rather than inventing any date, amount or entitlement. Show me the draft. Do not send anything and do not change the workbook.
```

### Step 5

Now put the reply into Outlook. Open Claude Desktop, where you connected Microsoft 365 in Lab 0, and ask it to create the draft. It creates a draft only — nothing is sent, and you are still the one who presses Send. If your connector is not available, record it and read the draft you wrote in Excel instead; the approval lesson is the same.

**Prompt to give Claude:**

```text
Using the Microsoft 365 connector, create a draft reply in Outlook to the message I chose on the Staff_Messages sheet.

Use the reply I wrote in the Draft_Reply column, exactly as it stands. Do not reword it.
Address it to the sender of that message only. Use the original subject with 'Re:' in front.

Create it as a draft. Do not send it. Tell me where to find it when you are done.
```

## Test it

Every message has an answer in the Action column, one reply under 120 words is written in the Draft_Reply column, its approver is named, and the reply exists as an unsent draft in Outlook or the connector state is recorded. Nothing was sent.

## Troubleshooting

- **You expected to open Outlook to read the messages.** The messages are in the workbook so the lab runs on any computer. Outlook is used only at the end, to create the draft.
- **The connector is not available.** Record it and stop at the Excel draft. Every earlier step works without Outlook.
- **Claude reworded my reply.** Ask again and say 'use the text exactly as it stands, do not reword'. The point is that you approve the words, not Claude.
- **Claude sent the message.** It should not. The prompt says create a draft and do not send. If it sent, report it and check the recipient immediately.
- **Claude invents a figure or a date.** Re-run the prompt; it instructs Claude to write 'need to check' instead of inventing.

## Challenge

Create an escalation rule for messages that contain a financial commitment, legal interpretation or personal data.

## Reflection

Which part of email handling should remain human even if drafting becomes nearly automatic?

## Deliverable

Every message sorted, one reply drafted, the person who would approve it named, and the reply created as an Outlook draft ready for review.

## Current product references

- [Claude for Microsoft 365 overview](https://claude.com/claude-for-microsoft-365)
- [Claude for Microsoft 365 add-ins overview](https://claude.com/docs/office-agents/overview)
- [Set up the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector)
- [Connect to Microsoft 365](https://support.claude.com/en/articles/15183774-connect-to-microsoft-365)
- [Use Claude for Microsoft 365 with third-party platforms](https://claude.com/docs/office-agents/third-party-platforms)
- [Get started in Claude Cowork in three steps](https://claude.com/resources/tutorials/get-started-in-claude-cowork-in-three-steps)
- [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)
- [Copilot Cowork overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/)
- [Microsoft 365 Copilot with Anthropic models](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-anthropic-apps)
- [Syracuse University: Claude Microsoft 365 connector](https://its.syr.edu/your-work-apps-meet-your-ai-assistant-using-claudes-microsoft-365-connector/)
- [Claude for Microsoft 365 setup and use cases](https://justinmckelvey.com/blog/claude-for-microsoft-365)

---

*Claude Microsoft 365 Masterclass (C197) · C197 · Version v3.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
