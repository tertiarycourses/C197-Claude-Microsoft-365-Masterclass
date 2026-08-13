# Lab 2 — Analyse Staff Data and Decide What Claude May Read

**Topic 01:** Getting Claude Ready for HR Work  |  **Day 1**  |  **Approx. 20 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update.

Claude summarises the staff list by team, builds a chart, and you check its formulas. Then you decide what access Claude actually needed, having just seen what read-only access can do.

## Goal

Use Claude to summarise and chart real staff data, then decide what access it needed to do that.

## What you'll build

A summary table and chart built by Claude in your own workbook, plus a completed access table.

**Tools and techniques:** Claude for Word, Claude Skills

## Company use case

- **Department:** Human Resources
- **Sponsor:** Head of HR
- **Business challenge:** Ask for a section the handbook says nothing about, and check it refuses to invent one.
- **Decision:** Does the saved standard hold without being restated?
- **Evidence:** The second half of the staff handbook
- **Measures:** Sections drafted from one line; Standard held; Nothing invented
- **Controls:** No invented entitlements; No legal conclusions; A person approves before release

## Files in this lab folder

- `Lumina-Living-Lab-02-HR-Brief.docx`
- `Lumina-Living-Lab-02-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-02-Staff-Information.xlsx`
- `Lumina-Living-Lab-02-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Lab 1 completed.
- Excel installed, with the Claude panel available from the ribbon.
- Lumina-Living-Lab-02-Staff-Information.xlsx from this folder. No work account and no connector are needed.

## Process map

New section → One short line → Same standard applied → Check it held → Repeat at will

## Steps

### Step 1

Open Lumina-Living-Lab-02-Staff-Information.xlsx from this lab folder and click the Staff_List tab. It shows 12 roles across four teams, with headcount, salary, leavers and how long each role takes to fill. Open the Claude panel in Excel: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac.

### Step 2

Ask Claude to summarise the staff data by team. Watch the new table appear on the sheet.

**Prompt to give Claude:**

```text
Look at the Staff_List sheet in this open workbook.

Work out, for each team:
- total headcount
- total monthly salary cost
- how many people left in the last 12 months
- the leaver rate as a percentage of headcount

Put the results in a new table on the Staff_List sheet, starting two rows below the data.
Use Excel formulas that point at the rows above, not typed-in numbers.
Then tell me which team has the biggest staffing problem and why.
```

### Step 3

Ask Claude to chart it. A bar chart appears on the sheet.

**Prompt to give Claude:**

```text
On the Staff_List sheet, add a bar chart showing the leaver rate for each team, using the summary table you just built.

Give the chart a title that says what it shows.
Sort the bars from highest leaver rate to lowest.
Place the chart to the right of the summary table so it does not cover any data.
```

### Step 4

Check the numbers yourself. Click one cell in the summary table and read the formula bar: it should point at the rows above, not be a number someone typed. Then press Cmd+S or Ctrl+S to save.

### Step 5

Now click the Where_Info_Is_Kept tab. It lists the four places HR keeps staff information, including the payroll data behind the salary column you just used. Fill in the What_Claude_May_Do tab: for each place type 'Read only' or 'Read and change', name who owns it, and say what you would do if it were unavailable. Then ask Claude to check your two tabs against each other.

**Prompt to give Claude:**

```text
Compare the What_Claude_May_Do sheet with the Where_Info_Is_Kept sheet in this workbook. Tell me any place that has no owner, no read-or-change decision, or where the two sheets disagree. Say which row you mean. Do not change the workbook.
```

## Test it

The summary table uses formulas that point at the staff rows, the chart shows leaver rate by team, the file is saved, and all four places have a read-or-change decision with an owner.

## Troubleshooting

- **Claude ignores the skill.** Name it: 'Apply my hr-draft skill.' If it is missing, check the plus menu, Skills.
- **The result differs from Lab 1.** A rule was not captured when you saved. Go back, correct it and save the skill again.
- **A section invents an entitlement.** That is a finding. Correct it, and add the rule to the skill so it cannot recur.

## Challenge

Design a read-only pilot group and a separate, smaller write-enabled group for the company rollout.

## Reflection

What did you not have to say this time that you said in the last lab?

## Deliverable

A summary table and chart built by Claude in your own workbook, plus a completed access table.

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
