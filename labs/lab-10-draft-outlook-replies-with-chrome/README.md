# Lab 10 — Draft an Outlook Reply with Claude in Chrome

**Topic 04:** Staff Questions, Repeatable Work and Advanced Claude  |  **Day 1**  |  **Approx. 20 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update.

Claude in Chrome works on the page in front of you. Open a staff message in Outlook web, have Claude draft the reply into the real compose box, check it, and decide whether it goes.

## Goal

Use Claude for Chrome to draft a reply inside Outlook on the web, review it, and send it yourself.

## What you'll build

A reviewed reply drafted in Outlook on the web, sent only after you approved it or deliberately left in Drafts.

**Tools and techniques:** Claude for Chrome, Outlook on the web, per-action approval

## Company use case

- **Department:** Human Resources
- **Sponsor:** Head of HR
- **Business challenge:** Ask Claude to draft a reply to a question the handbook does not answer, and check it refuses to invent one.
- **Decision:** Is this reply accurate enough to send, and who approves it?
- **Evidence:** The open staff message; The Lumina Living handbook
- **Measures:** Draft produced in Outlook; Recipient checked; Facts traced; Send decision recorded
- **Controls:** Manual approval mode only; No invented dates or entitlements; A person presses Send

## Files in this lab folder

- `Lumina-Living-Lab-10-HR-Brief.docx`
- `Lumina-Living-Lab-10-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-10-Working-Workbook.xlsx`
- `Lumina-Living-Lab-10-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Lab 0 completed, with Claude for Chrome installed, pinned and set to Manually approve.
- Google Chrome. Claude for Chrome does not work in other browsers.
- Outlook on the web, signed in with your training account.
- If Chrome or the extension is unavailable, follow the trainer demonstration and record it; Lab 8 covers the same reply work locally.

## Process map

Open Outlook in Chrome → Open the message → Claude drafts into the reply box → Check it in Outlook → You press Send

## Steps

### Step 1

Open Google Chrome and sign in to Outlook on the web with your training account. Open the Claude for Chrome side panel — you installed and pinned it in Lab 0. Check the permission mode says Manually approve, never Skip all approvals.

### Step 2

Open one staff message that needs a reply. Use a message from your own training mailbox, or the trainer will point you at one. Claude in Chrome reads the page you are looking at, so the message must be open on screen before you ask for anything.

### Step 3

Type the request into the Claude panel on the right of your browser window — the Claude for Chrome side panel, not the Outlook message box. When Chrome asks whether Claude may act on this page, choose Allow for this action only. Watch the draft appear in the Outlook compose window: not in the panel, but in the real reply box.

**Prompt to give Claude:**

```text
Draft a reply to the message that is open in Outlook.

Use only what that message and the Lumina Living handbook actually say. Keep it under 120 words, plain English.

Say clearly what happens next and who is doing it. Where you do not have a fact — a date, an amount, an entitlement — write 'need to check' rather than inventing one.

Leave the draft open in Outlook. Do not send it.
```

### Step 4

Read the draft in Outlook itself, not in the chat. Check the recipient, the subject, and every fact. Then ask Claude to check its own work before you commit to anything.

**Prompt to give Claude:**

```text
Before I send this, check it for me.

Tell me: is the recipient right, does anything in the reply state a rule the handbook does not contain, and is there any figure or date you cannot trace?

Do not change the draft. Just tell me what you find.
```

### Step 5

You decide what happens next. If the reply is right and the trainer approves it, press Send yourself. If anything is wrong, correct it in Outlook or leave it in Drafts. Claude drafted it; you are the one who sends it, and that has been true in every lab on this course.

## Test it

A reply was drafted into the Outlook compose box, the recipient and every fact were checked, anything unsupported is marked 'need to check', and the message was either sent after approval or deliberately left in Drafts. Permission mode stayed on Manually approve throughout.

## Troubleshooting

- **Claude cannot see the message.** Refresh the Outlook tab and make sure the message is open on screen. Claude in Chrome reads the visible page.
- **Chrome did not ask for approval.** Check the permission mode in the side panel. It must be Manually approve; never use Skip all approvals on a real mailbox.
- **The draft appeared only in the chat.** Ask again and say 'draft it into the Outlook reply box, not here'.
- **Claude invented an entitlement.** That is the finding. Correct it, and note that the same rule applies here as in every other lab: no fact without a source.
- **The extension will not install.** It needs Chrome and a paid plan. Record it and watch the trainer; Lab 8 teaches the same review discipline without a browser.

## Challenge

Name one HR question you could only answer if Claude could see the whole team's files, not just yours.

## Reflection

What would have to be true before you let a reply go out without reading it?

## Deliverable

A reviewed reply drafted in Outlook on the web, sent only after you approved it or deliberately left in Drafts.

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
