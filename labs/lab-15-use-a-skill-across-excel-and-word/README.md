# Lab 15 — Use the Skill from Word Without Opening Excel

**Topic 04:** Staff Questions, Repeatable Work and Advanced Claude  |  **Day 1**  |  **Approx. 15 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update.

The quarterly update is due and the figures are in a workbook. One short line, and the skill reads the workbook, works the numbers out your way, and writes them into the update.

## Goal

Invoke a saved skill from Word so it reads the Excel workbook and writes the figures into the document.

## What you'll build

A completed quarterly update with figures drawn from the workbook, saved as a final copy.

**Tools and techniques:** Claude Skills, Claude Desktop, Word, Excel

## Company use case

- **Department:** Human Resources
- **Sponsor:** Head of HR
- **Business challenge:** Run the same line on a second quarter's workbook and see whether anything breaks.
- **Decision:** Which team should leadership act on first this quarter?
- **Evidence:** The Q1 staff workbook; The Q1 update document
- **Measures:** Figures drawn from the workbook; Two figures checked by hand; Final copy saved
- **Controls:** No figure without a source; A person checks before it goes to leadership; Nothing sent automatically

## Files in this lab folder

- `Lumina-Living-Lab-15-HR-Brief.docx`
- `Lumina-Living-Lab-15-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-15-Working-Workbook.xlsx`
- `Lumina-Living-Lab-15-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Lab 3 completed, with the staff-numbers skill saved.
- The Claude Desktop app installed, and Word available.
- Both Lab 04 files in this folder. Everything is local; no work account is needed.

## Process map

Figures in one file, words in another → Desktop can see both → One short line → Check the figures → Save the final copy

## Steps

### Step 1

Open Lumina-Living-Lab-15-Q1-Update.docx from this lab folder. It is the quarterly people update for the leadership team, with the figures still missing. The staff data is in Lumina-Living-Lab-15-Q1-Staff.xlsx in this same folder — do not open it.

### Step 2

Open Claude Desktop and give it access to this lab folder. The Word panel can only see the document you have open; reading a second file needs Desktop. This is the same difference you have seen all course.

### Step 3

Ask for the update in one short line. Do not explain the totals, the leaver rate, the formulas or the finding — say none of it. Your skill already knows.

**Prompt to give Claude:**

```text
Check the staff workbook in this folder and add the figures to the Q1 update document.
```

### Step 4

Read what it produced. Every rule from Lab 3 should be there: totals by team, the leaver rate to one decimal place, the worst team named and explained. Check two figures against the workbook yourself.

### Step 5

Notice what Desktop did with the document: it produced a copy for you to download rather than editing the file you had open. Save it into this folder as Lumina-Living-Q1-Update-Final.docx. Write one sentence at the end saying which team leadership should act on first.

## Test it

The update contains totals by team and the leaver rate to one decimal place, the worst team is named and explained, two figures were checked against the workbook by hand, and a file named Lumina-Living-Q1-Update-Final.docx exists in the folder.

## Troubleshooting

- **Claude cannot see the workbook.** Confirm you gave Claude Desktop access to this lab folder, not to a single file.
- **The figures do not match the workbook.** That is a finding. Ask which cells it used, and check them yourself before trusting the update.
- **Claude ignores the skill.** Name it: 'Apply my staff-numbers skill.' If it is missing, check the plus menu, Skills.
- **Desktop edits nothing.** That is expected. Desktop produces a copy to download; save it into this folder yourself.

## Challenge

Add a stop/go decision rule for the weakest hiring after four weeks of evidence.

## Reflection

What did you not have to explain this time that you spelled out in the last lab?

## Deliverable

A completed quarterly update with figures drawn from the workbook, saved as a final copy.

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
