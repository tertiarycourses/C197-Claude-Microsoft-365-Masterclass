# Lab 3 — Build an Auditable Prompt and Review Contract

**Topic 01:** Governed Foundations for Claude and Microsoft 365  |  **Day 1**  |  **Approx. 20 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore omnichannel home-and-lifestyle company with retail, e-commerce and marketplace operations. Learners join its Business Transformation Office to prepare an integrated FY2027 planning and management pack.

Turn vague requests into professional prompt contracts for Word, Excel and PowerPoint, then log evidence and review outcomes.

## Goal

Write reusable prompts that ground evidence, constrain edits and define human approval.

## What you'll build

A reusable cross-app prompt library, prompt test log and acceptance checklist.

**Tools and techniques:** Prompt architecture, evidence clauses, stop rules, output contracts, review log

## Company use case

- **Department:** Business Transformation Office
- **Sponsor:** Director, Strategy
- **Business challenge:** Create a prompt standard that works across the full Lumina Living planning pack.
- **Decision:** Which prompt elements are mandatory for a company-standard AI workflow?
- **Evidence:** FY2027 planning brief; Company style guide; Data dictionary; Approval matrix
- **Measures:** Prompt pass rate; Citations present; Unsupported claims; Review time
- **Controls:** No unstated assumptions; No fabricated citations; Smallest useful edit; Human approval

## Files in this lab folder

- `Lumina-Living-Lab-03-Company-Brief.docx`
- `Lumina-Living-Lab-03-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-03-Working-Workbook.xlsx`
- `Lumina-Living-Lab-03-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Labs 1–2 completed.
- Word, Excel and PowerPoint sample files open.
- The approved source register is available.

## Process map

Business outcome → Named evidence → Constraints → Output contract → Verification and approval

## Steps

### Step 1

Open the Prompt Library document and the Prompt Test Log workbook.

### Step 2

Run the vague request 'Improve our plan' against the supplied Word brief and record why the result is difficult to verify.

**Prompt to give Claude:**

```text
Improve our plan.
```

### Step 3

Rewrite it with the five-part structure: business outcome, evidence, constraints, output contract and approval gate.

**Prompt to give Claude:**

```text
Using the open FY2027 brief, draft only the Executive summary for the Lumina Living leadership team. Preserve the current heading styles and keep it under 180 words. Use only stated facts, cite the source heading for each material claim and list missing evidence separately. Show proposed text before editing the document.
```

### Step 4

Create an Excel prompt that requires formula-first analysis, cell citations and a review plan before edits.

**Prompt to give Claude:**

```text
Using tblFinance in the open workbook, propose a formula-driven Actual vs Budget analysis for Revenue, Gross Profit, Gross Margin and Operating Contribution. Cite source ranges, keep assumptions on the Assumptions sheet and do not hardcode totals. List the formulas and validation checks before applying changes.
```

### Step 5

Create a PowerPoint prompt that preserves the company template and demands native charts, conclusion-led titles and source notes.

**Prompt to give Claude:**

```text
Using the open company template, approved strategy document and verified Excel summary ranges, propose an eight-slide Executive Committee story. Preserve the slide master, use one conclusion-led message per slide, native editable charts and concise speaker notes. Add a source note to every data slide and flag unreconciled figures before building.
```

### Step 6

Test each prompt once. Log the input sources, output quality, citation accuracy, time to review and corrections required.

### Step 7

Add a stop rule to any prompt that encouraged guessing.

**Prompt to give Claude:**

```text
If the approved sources do not contain a required fact, stop that part of the task, name the missing evidence and ask one precise question. Do not invent a value, owner, date or citation.
```

### Step 8

Ask Claude to critique the three prompts against the company standard.

**Prompt to give Claude:**

```text
Audit these Word, Excel and PowerPoint prompts. For each, score outcome clarity, grounding, constraints, output contract, verification and approval from 1 to 5. Cite the exact missing phrase and propose the smallest correction.
```

### Step 9

Save the approved prompts as company templates for Labs 4, 7 and 8.

## Test it

The Word, Excel and PowerPoint prompts each name a business result, approved evidence, constraints, output format, verification method, stop rule and human approval gate.

## Troubleshooting

- **Claude still guesses.** Add an explicit missing-evidence stop rule and require the source location for every material claim.
- **The prompt is too long.** Separate stable company instructions from the task-specific prompt and remove repeated context.
- **The edit is too broad.** Name the exact selected section, sheet, range, slide or object to change.

## Challenge

Create a prompt rubric that a colleague can use without knowing how the prompt was written.

## Reflection

Which prompt clause most reduced your review effort, and why?

## Deliverable

A reusable cross-app prompt library, prompt test log and acceptance checklist.

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
