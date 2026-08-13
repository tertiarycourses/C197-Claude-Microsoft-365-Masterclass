# Lab 11 — Build a Daily HR Routine with Cowork

**Topic 04:** Staff Questions, Repeatable Work and Advanced Claude  |  **Day 1**  |  **Approx. 20 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update.

Ten things landed on the HR desk this week. Cowork finds what actually repeats, writes a daily routine, applies it back to the week, and produces the Monday brief. No terminal, no scripts.

## Goal

Turn a week of scattered HR work into a repeatable daily routine, and let Cowork run it across your files.

## What you'll build

A written daily routine covering inbox, reporting and chasing; this week's work assigned an owner and a deadline; and today's daily HR report.

**Tools and techniques:** Claude Cowork, Claude Desktop, Excel, Word

## Company use case

- **Department:** Human Resources
- **Sponsor:** Head of HR
- **Business challenge:** Add one more item to This_Week that the routine does not cover, and see whether Cowork spots the gap.
- **Decision:** What should the HR daily routine be, and who owns each step?
- **Evidence:** This week's HR inbox; The empty routine sheet
- **Measures:** Repeating work identified; Routine written; Every item owned; Monday brief produced
- **Controls:** No invented owners or deadlines; Gaps recorded rather than filled; Head of HR reads the brief before it is acted on

## Files in this lab folder

- `Lumina-Living-Lab-11-HR-Brief.docx`
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

- Lab 0 completed, so Claude Desktop is installed and signed in.
- Cowork available in Claude Desktop. It is on paid plans; if you do not have it, watch the trainer and follow along in the workbook.
- Lumina-Living-Lab-11-This-Week.xlsx from this folder. Everything is local; no terminal and no scripts.

## Process map

A week of scattered work → Find what repeats → Write the routine → Apply it to the week → Run it: today's report

## Steps

### Step 1

Open Lumina-Living-Lab-11-This-Week.xlsx from this lab folder and look at the This_Week sheet. Ten things landed on the HR desk this week — new starters, leavers, leave requests, probation reviews and questions. Three columns are empty. Doing this by hand every week is the problem this lab solves.

### Step 2

Open Claude Desktop and switch to Cowork. Give it access to this lab folder so it can work across the files. Ask it to look at the week and find the work that actually repeats.

**Prompt to give Claude:**

```text
Read Lumina-Living-Lab-11-This-Week.xlsx in this folder and look at the This_Week sheet.

It lists everything that landed on the HR desk this week: new starters, leavers, leave requests, probation reviews and questions.

Group them by what kind of work they are, and tell me which ones happen every single week no matter what. Those are the ones worth turning into a routine. Do not change the sheet yet.
```

### Step 3

Ask Cowork to design the daily routine and write it into the workbook. Notice the three things it must include: checking the inbox, producing the daily report, and chasing what is overdue. Those are the jobs that happen every day whatever else lands.

**Prompt to give Claude:**

```text
Now design the daily HR routine from that list.

Write it into the Daily_Routine sheet of the same workbook, one row per step.

It must include these three things, because they happen every day whatever else does:
- checking the HR inbox and sorting what came in
- the daily report to the Head of HR
- chasing anything that has passed its deadline

For each row give: when it happens, what to do in one plain sentence, where the information is (name the sheet or file), and who checks it before anything goes out.

Keep it to work that genuinely repeats. Anything that happened only once this week is not a routine.
```

### Step 4

Now ask it to apply that routine back to this week's list. Every row should get an action, an owner and a deadline — or be marked as not covered yet, which tells you the routine has a gap.

**Prompt to give Claude:**

```text
Using the routine you just wrote, fill in the three empty columns on the This_Week sheet for every row: what must happen, who owns it, and by when.

Base the owner and the deadline on the routine, not on guesswork. Where the routine does not cover something, write 'not in the routine yet' rather than inventing an owner.
```

### Step 5

Finally, ask Cowork to run the routine and produce today's report. Open it, check two items against the workbook, and decide whether you would send it to the Head of HR as it stands. This is the routine working: the same report, the same way, every morning.

**Prompt to give Claude:**

```text
Using the routine, produce today's daily HR report as a new Word document called Lumina-Living-Daily-HR-Report.docx in this folder.

Three short sections:
- What came in today, from the This_Week sheet
- What is due or overdue, with the owner named
- What needs a decision from the Head of HR

Name the row behind every item. Where something has no owner, say so plainly rather than filling the gap. Keep it to one page — it is read standing up.
```

## Test it

The Daily_Routine sheet covers checking the inbox, the daily report and chasing overdue items, each with when, what, where and who. Every row of This_Week has an action, an owner and a deadline, or is marked as not covered. Lumina-Living-Daily-HR-Report.docx exists, fits one page, and names the row behind every item.

## Troubleshooting

- **Cowork is not in Claude Desktop.** It is available on paid plans. If it is missing, do the same steps in a normal Claude Desktop conversation with folder access — the routine is the point, not the mode.
- **Cowork cannot see the workbook.** Give it access to this lab folder, not to a single file.
- **It invented an owner.** Ask again and say 'write not in the routine yet where the routine does not cover something'. An invented owner is worse than an admitted gap.
- **The routine includes one-off work.** Ask it to remove anything that happened only once this week. A routine is what repeats.

## Challenge

Add a dry-run flag that reports proposed cell changes and mail-query scope without writing any output.

## Reflection

Which part of your own week would still work if you were away tomorrow?

## Deliverable

A written daily routine covering inbox, reporting and chasing; this week's work assigned an owner and a deadline; and today's daily HR report.

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
