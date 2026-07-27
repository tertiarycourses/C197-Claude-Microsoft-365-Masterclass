# Lab 3 — Write Effective Prompts for Everyday Work Tasks

**Topic 01:** Getting Started with Claude for Microsoft 365  |  **Day 1**  |  **Approx. 40 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Scenario

Lumina Living is a small home-and-lifestyle retailer. The quarter has just closed and your manager needs the Q3 business-review pack — a short written report, the numbers behind it, a slide deck for the management meeting, and the emails that send it out — by the end of the day. You have a rough brief, a sales workbook and a handful of facts to work from. Across this course you use Claude alongside Microsoft 365 to turn that raw material into a finished, checked pack. Use this scenario only if you cannot use real, non-confidential work of your own; your own material is always preferred.

## Goal

Compare a vague prompt with a specific one and capture a reusable four-part prompt pattern for work tasks.

## What you'll build

A written four-part prompt pattern (Role · Context · Task · Output) and one strong, tested prompt saved for reuse.

**Tools and techniques:** Prompt design, role/context/task/output, refinement

## Prerequisites

- Labs 1 and 2 complete — your 'Lumina Living — Q3 Review' Project (or prepared chat) holds the brief and the workbook.
- Claude open at claude.ai or in the desktop app.
- A notes doc (Word, or a note pinned in the Project) to save your pattern in.

## Steps

### Step 1

Run a deliberately vague prompt in the Project and note how generic the answer is.

Prompt to give Claude (paste into the chat):

```text
Write something about our sales.
```

### Step 2

Now run a specific prompt for the same intent and compare the result.

Prompt to give Claude (paste into the chat):

```text
You are my business analyst. Context: this is Lumina Living's Q3 sales workbook. Task: write three short paragraphs summarising how the quarter went for a management audience. Output: plain paragraphs, no jargon, with the key figure named in each.
```

### Step 3

Write down the four parts that made the second prompt work: the Role, the Context, the Task, and the Output format.

### Step 4

Capture your reusable pattern where you can find it — a notes doc, or pinned in the Project.

Pattern:

```text
ROLE: who Claude should act as | CONTEXT: which file/task | TASK: what to produce | OUTPUT: format, length, tone, and what to include
```

### Step 5

Add the conditions that keep results trustworthy: name the file, ask Claude to show where figures come from, and state the length and tone you need.

### Step 6

Rewrite one request of your own about the Q3 pack using the pattern, and run it.

### Step 7

Refine once: change the Output part (for example 'make it half as long', or 'more formal') and re-run to see the result change. Keep the better version.

### Step 8

Save your best prompt in the Project — you will reuse this pattern in every remaining lab.

## Test it

You can show two answers for the same intent (vague vs specific), a written four-part prompt pattern, and one refined prompt that produced the output you specified in the format you asked for.

## Troubleshooting

- **The specific prompt and the vague one give oddly similar answers.** Check the file is actually attached to this chat or present in the Project — without the workbook, Claude has no real numbers to work from and falls back on generic text. Re-attach it, or move into the Project chat, then re-run.
- **Claude gives figures but won't say where they came from.** Add the source requirement explicitly to the Output part: 'name the cell or column each figure comes from'. If it still cannot, the data it needs may not be in the attached file — check you uploaded the right sheet.
- **The refined version is worse than the original.** Refinement is not always an improvement. Because you kept the earlier answer in the chat, scroll back, copy the better version, and save that one — you are the editor deciding which draft to keep.

## Challenge

Take your best Q3 prompt and write a second version aimed at a different audience — for example the wider team rather than management — changing only the Role and Output parts. Save both in the Project so your connected Lumina Living Q3 pack has ready-made prompts for each audience you will write for later.

## Reflection

LO3 — Compare a vague prompt with a specific one and capture a reusable four-part prompt pattern for work tasks. In your own words, how will you use this in your own work, and how will you check Claude got it right?

## Deliverable

Save your work — this four-part pattern and your tested prompt become reusable tools for the connected **Lumina Living Q3 review pack**, the single deliverable you complete and send in Lab 8.

---

*Claude Microsoft 365 Masterclass (C197) · C197 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
