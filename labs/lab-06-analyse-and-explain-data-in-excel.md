# Lab 6 — Analyse and Explain Data in Excel

**Topic 02:** Boosting Productivity Across Microsoft 365 with Claude  |  **Day 1**  |  **Approx. 50 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Scenario

Lumina Living is a small home-and-lifestyle retailer. The quarter has just closed and your manager needs the Q3 business-review pack — a short written report, the numbers behind it, a slide deck for the management meeting, and the emails that send it out — by the end of the day. You have a rough brief, a sales workbook and a handful of facts to work from. Across this course you use Claude alongside Microsoft 365 to turn that raw material into a finished, checked pack. Use this scenario only if you cannot use real, non-confidential work of your own; your own material is always preferred.

## Goal

Use Claude to analyse a dataset, build the formulas you need, and explain a formula — verifying every figure in Excel.

## What you'll build

A verified Q3 analysis in Microsoft Excel — key figures computed by formulas you checked, and one formula you can explain.

**Tools and techniques:** Microsoft Excel, Claude (analysis / formula generation / formula explanation), SUM, SUMIF, AVERAGE

## Prerequisites

- Labs 1–4 completed: Claude is set up, the Q3 sales workbook is connected in your Project, and you have your safe-use checklist.
- Lab 5 completed: the Q3 review report exists — this lab produces the verified numbers behind it.
- Microsoft Excel installed and open, with the 'Lumina Living — Q3 Sales.xlsx' workbook loaded.
- Remember: Claude is a separate assistant, not a ribbon inside Excel. Claude suggests formulas; you paste them into Excel and confirm the result yourself.

## Steps

### Step 1

Ask Claude to analyse the workbook and surface the figures the report needs.

Prompt to give Claude (paste into the chat):

```text
From the Q3 sales workbook, give me: total sales for the quarter, the best- and worst-selling product by value, the top region, and the month-by-month trend. Show the figure for each and say which columns you used.
```

### Step 2

Ask Claude for the exact Excel formula for the headline figure so you can reproduce it.

Prompt to give Claude (paste into the chat):

```text
Give me the Excel formula to compute total Q3 sales from the Total column, assuming the data is in rows 2 to 500.
```

### Step 3

In Excel, put that formula in an empty cell and confirm it matches the figure Claude reported.

Excel formula:

```text
=SUM(F2:F500)
```

### Step 4

Ask for a conditional formula and verify it too — for example sales for the top region.

Prompt to give Claude (paste into the chat):

```text
Give me an Excel formula that totals the Total column only for rows where the Region column equals "North".
```

### Step 5

Paste it into Excel and cross-check by filtering the sheet to that region and reading the status-bar Sum.

Excel formula:

```text
=SUMIF(D2:D500,"North",F2:F500)
```

### Step 6

Learn from a formula: paste an unfamiliar one and ask Claude to explain it step by step.

Prompt to give Claude (paste into the chat):

```text
Explain, step by step, what this Excel formula does: =IF(F2>500,"Large","Standard")
```

### Step 7

Set the rule and record the checked figures: never accept a number you cannot tie back to a formula in the sheet. Note the verified headline figures where the report can reuse them.

## Test it

Your key Q3 figures each match an Excel formula you ran yourself, one conditional total agrees with a filtered status-bar Sum, and you can explain in one sentence what the =IF formula does.

## Troubleshooting

- **A formula returns 0, a wrong total or #REF!.** The row range does not match your data. Check where your rows actually start and end — headers usually sit in row 1, so data begins at row 2 — and adjust the range (for example F2:F500) so it covers every data row and no blank trailing rows. A #REF! means a referenced column was deleted or shifted; re-point the formula at the correct column letter.
- **Claude's reported total differs from what Excel computes.** Trust Excel — it is reading the live cells; Claude is estimating from what it saw. Re-ask Claude to name the exact column, then rely on the figure your own =SUM gives. Record the Excel number in the report, not Claude's.
- **=SUMIF returns 0 because the region name does not match.** The text in the Region column must match your criterion exactly. Watch for a trailing space, different casing or 'North Region' versus 'North'. Click a real cell in column D to copy the exact spelling, or filter the column to see the true category names, then correct the criterion in the formula.

## Challenge

Ask Claude for an =AVERAGE or =SUMIF formula that gives the mean order value for your top region, paste it into Excel, and verify it against a filtered status-bar reading before adding the figure to the Lumina Living Q3 pack.

## Reflection

LO6 — Use Claude to analyse a dataset, build the formulas you need, and explain a formula — verifying every figure in Excel. In your own words, how will you use this in your own work, and how will you check Claude got it right?

## Deliverable

Your verified Q3 figures in Excel — the checked numbers that feed the report and the deck, joining the connected **Lumina Living Q3 review pack**.

---

*Claude Microsoft 365 Masterclass (C197) · C197 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
