# Lab 3 — Ask Claude Clearly

**Topic 01:** Getting Claude Ready for HR Work  |  **Day 1**  |  **Approx. 15 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update.

Run a vague request and a clear one against the same HR brief, and see the difference for yourself.

## Goal

Write a request that says what you want, what to use, what not to change, and when to stop.

## What you'll build

A new section written into the brief by Claude, a second copy produced by the Desktop app, and a completed request checklist.

**Tools and techniques:** Claude for Excel, Claude Skills, natural-language skill creation

## Company use case

- **Department:** Human Resources
- **Sponsor:** Head of HR
- **Business challenge:** Add one rule to the skill that your own organisation would need.
- **Decision:** How do we make the same analysis come out the same way every quarter?
- **Evidence:** This quarter's staff data
- **Measures:** Summary produced; Method corrected; Skill saved
- **Controls:** Formulas point at source rows; No typed-in totals; A person checks the finding

## Files in this lab folder

- `Lumina-Living-Lab-03-HR-Brief.docx`
- `Lumina-Living-Lab-03-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-03-Working-Workbook.xlsx`
- `Lumina-Living-Lab-03-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Labs 1 and 2 completed.
- Word installed, with the Claude panel available from the ribbon.
- The Claude Desktop app installed.
- Lumina-Living-Lab-03-HR-Brief.docx from this folder.

## Process map

Ask for it your way → Correct until right → Save it in one sentence → Check it is listed → Ready to reuse

## Steps

### Step 1

Open Lumina-Living-Lab-03-HR-Brief.docx from this lab folder and read the six headings. Open the Claude panel in Word: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac.

### Step 2

Type this vague request. Claude answers in the panel but cannot do much with it: it does not know which plan you mean, what to change, or where to put anything. Read what comes back, then move on.

**Prompt to give Claude:**

```text
Improve our plan.
```

### Step 3

Now type the clear request below. This time watch the document itself: a new section appears after '3. Required management outputs'. When it finishes, read it — every fact should name the heading it came from, and anything the brief does not say should be marked 'need to check'. Delete anything you cannot trace back, then press Cmd+S or Ctrl+S to save.

**Prompt to give Claude:**

```text
Using the open Lumina-Living-Lab-03-HR-Brief.docx, add a new section called 'What we will do', straight after the section '3. Required management outputs'.

Write it into the document using the same heading style as the other sections.

For each action give:
- the reason we are doing it
- who owns it
- how we will know it worked
- the date it is due

Use only what this brief actually says. After each fact, name the heading you took it from. Where the brief says nothing, write 'need to check' instead of making something up.
```

### Step 4

Now open the Claude Desktop app, give it access to this lab folder, and type exactly the same clear request again. It cannot write into the document you have open. Instead it produces a new Word file and offers a Download button. Select Download and open, then File > Save As into this folder as Lumina-Living-Lab-03-HR-Brief-Desktop.docx.

**Prompt to give Claude:**

```text
Using the open Lumina-Living-Lab-03-HR-Brief.docx, add a new section called 'What we will do', straight after the section '3. Required management outputs'.

Write it into the document using the same heading style as the other sections.

For each action give:
- the reason we are doing it
- who owns it
- how we will know it worked
- the date it is due

Use only what this brief actually says. After each fact, name the heading you took it from. Where the brief says nothing, write 'need to check' instead of making something up.
```

### Step 5

Put the two documents side by side. Your original keeps the brief's own heading styles because Claude wrote straight into it; the downloaded copy is a new document, so its headings were rebuilt and may not match. Open templates/Prompt-and-Review-Template.docx and write down two things: the five parts that made the clear request work, and which of the two documents you would send to the HR head.

## Test it

The new section sits after '3. Required management outputs' with every fact naming its heading, the file is saved, a second file named Lumina-Living-Lab-03-HR-Brief-Desktop.docx exists, and the checklist says which document you would send on and why.

## Troubleshooting

- **Claude does not save the skill.** Say it plainly: 'Save that as a skill called staff-numbers.' If nothing happens, try /skillify instead.
- **The table has typed-in numbers.** Correct it before you save. Whatever you save is what you get every future time.
- **The leaver rate looks wrong.** Check it divides leavers by headcount for that team, not by total headcount.

## Challenge

Create a prompt rubric that a colleague can use without knowing how the prompt was written.

## Reflection

Which correction would have cost you most if you had saved without making it?

## Deliverable

A new section written into the brief by Claude, a second copy produced by the Desktop app, and a completed request checklist.

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
