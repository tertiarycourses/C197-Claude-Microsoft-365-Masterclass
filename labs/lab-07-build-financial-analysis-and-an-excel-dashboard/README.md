# Lab 7 — Build Financial Analysis and an Excel Dashboard

**Topic 03:** Financial Analysis and Executive Storytelling  |  **Day 1**  |  **Approx. 50 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore omnichannel home-and-lifestyle company with retail, e-commerce and marketplace operations. Learners join its Business Transformation Office to prepare an integrated FY2027 planning and management pack.

Move from transaction data and budget assumptions to formula-driven analysis, scenario testing, native charts and a one-screen management dashboard.

## Goal

Build an auditable financial model and management dashboard in Excel with Claude.

## What you'll build

A controlled FY2026 financial workbook with actual-vs-budget analysis, scenarios, three native charts and an executive dashboard.

**Tools and techniques:** Claude for Excel, tables, formulas, pivots, scenarios, chart selection, dashboard, audit log

## Company use case

- **Department:** Finance and Business Performance
- **Sponsor:** Chief Financial Officer
- **Business challenge:** Explain FY2026 performance and test the FY2027 plan before the Executive Committee meeting.
- **Decision:** Which revenue, margin and cost actions should management prioritise?
- **Evidence:** FY2026 transaction ledger; Monthly budget; Product cost table; Scenario assumptions
- **Measures:** Revenue; Gross profit; Gross margin; Operating contribution; Budget variance; Average order value
- **Controls:** Dynamic formulas; No formula errors; Source ranges cited; Independent KPI checks

## Files in this lab folder

- `Lumina-Living-Lab-07-Company-Brief.docx`
- `Lumina-Living-Lab-07-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-07-Working-Workbook.xlsx`
- `Lumina-Living-Lab-07-Executive-Starter.pptx`
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

Inspect the workbook manually: identify input, calculation, output and control sheets before using Claude.

### Step 2

Ask Claude to map the workbook and cite the key ranges without editing.

**Prompt to give Claude:**

```text
Map this workbook before making changes. For each sheet state its purpose, input ranges, formula ranges, outputs, named tables, charts and control checks. Cite cells or table names and flag any ambiguity.
```

### Step 3

Validate the transaction and budget tables for duplicates, blanks, invalid dates, unexpected categories, negative values and inconsistent formula columns.

**Prompt to give Claude:**

```text
Audit tblFinance and tblBudget for duplicates, blanks, invalid dates, unrecognised regions/channels/products, negative amounts and formula inconsistencies. Create a Data_Quality summary with issue count, affected rows and proposed fix. Do not silently delete or overwrite data.
```

### Step 4

Approve only justified fixes and require a change-log entry for each edit.

**Prompt to give Claude:**

```text
Apply only the approved data-quality corrections. Record old value, new value, reason, source and reviewer in Audit_Log. Re-run the checks and stop if any high-impact issue remains.
```

### Step 5

Build formula-driven Actual vs Budget analysis by month, channel and product.

**Prompt to give Claude:**

```text
Using tblFinance and tblBudget, build a formula-driven Actual vs Budget analysis for Revenue, Gross Profit, Gross Margin and Operating Contribution by month and channel. Use formulas or pivots, cite source ranges, keep assumptions on the Assumptions sheet and do not hardcode totals. List the formulas and checks before editing.
```

### Step 6

Trace and explain the Gross Margin and Operating Contribution formulas. Check for range, sign, timing and allocation errors.

**Prompt to give Claude:**

```text
Explain the Gross Margin and Operating Contribution formulas, trace their precedents and test whether each range includes all twelve months. Audit for hardcoded totals, inconsistent signs, omitted rows, circular references and #REF!, #VALUE!, #N/A or #DIV/0! errors.
```

### Step 7

Create Base, Upside and Downside scenarios using explicit growth, discount and cost assumptions. Keep the assumptions separate from actuals.

**Prompt to give Claude:**

```text
Create Base, Upside and Downside scenarios for FY2027. Inputs: unit growth, average discount, unit-cost inflation and marketing spend. Keep scenario inputs on Assumptions, calculate Revenue, Gross Profit, Gross Margin and Operating Contribution dynamically, and show the change versus Base.
```

### Step 8

Ask Claude to recommend charts by decision question, then approve a monthly trend, actual-vs-budget variance and contribution by channel visual.

**Prompt to give Claude:**

```text
Recommend three management charts. For each state the decision question, source range, chart type, scale, unit and risk of misinterpretation. Prioritise monthly performance, budget variance and contribution by channel.
```

### Step 9

Create native editable charts and a one-screen Dashboard with four KPI cards, three charts, definitions, scenario selector note and last-refreshed timestamp.

**Prompt to give Claude:**

```text
Build a one-screen Executive Dashboard using the verified Analysis outputs. Include Revenue, Gross Profit, Gross Margin and Operating Contribution KPI cards; the three approved native charts; definitions; selected scenario; and last-refreshed note. Use restrained company colours and no 3D effects.
```

### Step 10

Run a sceptical CFO review.

**Prompt to give Claude:**

```text
Act as a sceptical CFO. Review the model for weak assumptions, hardcodes, timing or allocation errors, misleading scales, unsupported causal claims and decision-relevant sensitivities. Rank findings by financial impact and cite the cell, range or chart source.
```

### Step 11

Resolve material findings, recalculate the workbook, independently reproduce two KPIs and complete the Audit Log.

## Test it

The model has no formula errors, all four KPIs reconcile, scenarios change through named assumptions, three native charts answer management questions and the audit log records independent checks.

## Troubleshooting

- **A KPI does not recalculate.** Trace precedents and replace any pasted value with a formula tied to the approved table.
- **The variance sign is confusing.** Define favourable/unfavourable logic once and apply it consistently across tables, charts and narrative.
- **The dashboard is crowded.** Keep four KPIs and three decision charts; move details to Analysis and document definitions.

## Challenge

Add a sensitivity table showing which assumption has the largest effect on Operating Contribution.

## Reflection

Which model control gave you the strongest evidence that the dashboard can be trusted?

## Deliverable

A controlled FY2026 financial workbook with actual-vs-budget analysis, scenarios, three native charts and an executive dashboard.

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
