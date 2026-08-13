# Lab 6 — Build a Headcount Analysis in Excel

**Topic 03:** People Numbers and Reporting to Leadership  |  **Day 1**  |  **Approx. 25 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update.

Compare actual headcount and staff cost against plan, month by month and team by team, using formulas that point at the source data.

## Goal

Build a headcount and cost analysis in Excel using live formulas, not typed-in numbers.

## What you'll build

An analysis sheet where every result is a formula that points back to the source data.

**Tools and techniques:** Claude for Excel, tables, formulas, pivots, scenarios, chart selection, dashboard, audit log

## Company use case

- **Department:** Human Resources
- **Sponsor:** Head of HR
- **Business challenge:** Explain to leadership why headcount and staff cost differ from plan.
- **Decision:** Where are we above or below plan, and why?
- **Evidence:** Staff list; Headcount plan; Assumptions
- **Measures:** Headcount; Staff cost; Gap against plan; Leavers
- **Controls:** Formulas point at source data; No typed-in totals; Assumptions kept on one sheet

## Files in this lab folder

- `Lumina-Living-Lab-06-HR-Brief.docx`
- `Lumina-Living-Lab-06-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-06-Working-Workbook.xlsx`
- `Lumina-Living-Lab-06-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Labs 1–6 completed.
- Open the supplied Finance Model workbook and Data Dictionary.
- Use only the fictional transaction data supplied in this lab.

## Process map

Understand the model → Validate inputs → Build formulas → Explain drivers → Dashboard and senior review

## Steps

### Step 1

Open Lumina-Living-Lab-06-People-Numbers.xlsx from this lab folder. Click the Staff_List tab to see the people data, then the Assumptions tab. Open the Claude panel in Excel.

### Step 2

Ask Claude to plan the analysis before it changes anything. Read the answer on screen.

**Prompt to give Claude:**

```text
Look at the Staff_List sheet and the Assumptions sheet in this open workbook. Tell me the formulas and checks you would use to compare actual headcount and staff cost against the plan, month by month and team by team. Name the sheets and columns you would use. Do not change the workbook yet.
```

### Step 3

Ask Claude to build the analysis with live formulas, not typed-in numbers.

**Prompt to give Claude:**

```text
On the Analysis sheet of this open workbook, build a comparison of actual headcount and staff cost against plan, by month and by team, using the Staff_List and Plan sheets. Show headcount, staff cost and the gap against plan. Use Excel formulas that point at the source data. Do not type in any total by hand. Keep every assumption on the Assumptions sheet.
```

### Step 4

Click into two of the result cells and read the formula bar. Check each one points at real data and is not a number someone typed.

### Step 5

Change one figure on the Assumptions tab and check the Analysis sheet updates. Write the check on the Checks tab.

## Test it

Two result cells checked in the formula bar show real formulas pointing at the source data, and changing an assumption updates the analysis.

## Troubleshooting

- **A KPI does not recalculate.** Trace precedents and replace any pasted value with a formula tied to the approved table.
- **The variance sign is confusing.** Define favourable/unfavourable logic once and apply it consistently across tables, charts and narrative.
- **The dashboard is crowded.** Keep four KPIs and three decision charts; move details to Analysis and document definitions.

## Challenge

Add a sensitivity table showing which assumption has the largest effect on Operating Contribution.

## Reflection

Which model control gave you the strongest evidence that the dashboard can be trusted?

## Deliverable

An analysis sheet where every result is a formula that points back to the source data.

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
