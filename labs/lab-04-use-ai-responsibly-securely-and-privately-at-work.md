# Lab 4 — Use AI Responsibly, Securely and Privately at Work

**Topic 01:** Getting Started with Claude for Microsoft 365  |  **Day 1**  |  **Approx. 35 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Scenario

Lumina Living is a small home-and-lifestyle retailer. The quarter has just closed and your manager needs the Q3 business-review pack — a short written report, the numbers behind it, a slide deck for the management meeting, and the emails that send it out — by the end of the day. You have a rough brief, a sales workbook and a handful of facts to work from. Across this course you use Claude alongside Microsoft 365 to turn that raw material into a finished, checked pack. Use this scenario only if you cannot use real, non-confidential work of your own; your own material is always preferred.

## Goal

Decide what is safe to share with AI, and write a personal safe-use checklist you apply to the review pack.

## What you'll build

A personal safe-use checklist, and one prompt you have rewritten to remove sensitive data before sending.

**Tools and techniques:** Data privacy, redaction, verification, safe-use checklist

## Prerequisites

- Labs 1–3 complete — your Q3 Project (or prepared chat) and your saved Lab 3 prompt are ready.
- The 'Lumina Living — Q3 Sales.xlsx' workbook open in Excel, so you can verify a figure at source.
- Claude open at claude.ai or in the desktop app.

## Steps

### Step 1

List the kinds of data that should not go into an AI prompt without approval: passwords and keys, customer names and contact details, staff personal data, unreleased financials, and anything under NDA.

### Step 2

Practise redacting: take a sentence that names a real customer and rewrite it to make the same request safely.

Prompt to give Claude (paste into the chat):

```text
Rewrite this so it asks the same question without naming anyone: 'Summarise why customer Tan Wei Ming from 12 Orchard Road cancelled his order.'
```

### Step 3

Ask Claude for good practice, then sanity-check its advice against your own organisation's policy.

Prompt to give Claude (paste into the chat):

```text
What should I avoid putting into an AI prompt when working with real company data, and how can I get the same help safely?
```

### Step 4

Confirm the verification rule with a quick test: ask Claude for a specific figure from the workbook, then check it in Excel — never accept a number you cannot tie back to the source.

Prompt to give Claude (paste into the chat):

```text
What was the single best-selling product in the Q3 workbook, and what was its total sales value? Tell me which cells you used.
```

### Step 5

Note who is accountable: Claude drafts, but you are responsible for what you send. Decide where you will record that AI helped (for example a note in the document's properties).

### Step 6

Draft your safe-use checklist — keep confidential data out of prompts; redact before sharing; verify every figure, name and claim; keep a human decision on anything that goes out; record where AI was used.

### Step 7

Apply the checklist to your Lab 3 prompt: check it contains nothing sensitive, and adjust it if it does.

## Test it

You have a written safe-use checklist, a prompt you rewrote to remove a real name, and a figure from the workbook that you verified in Excel before trusting it.

## Troubleshooting

- **Claude's redacted rewrite still hints at who the customer is.** Generalise further — replace the name and address with a role or category ('a customer who cancelled a large order') rather than a lightly disguised version. The safe test: could a reader identify the person from what remains? If yes, keep cutting.
- **The figure Claude gives doesn't match Excel.** Trust Excel, not the chat. Ask Claude which cells it used, then check those exact cells; a mismatch usually means it read the wrong column or included a subtotal row. This is exactly why the verify-at-source rule exists.
- **You're unsure whether a detail counts as sensitive.** When in doubt, leave it out and ask your manager or your organisation's policy — Claude's general advice in Step 3 is a starting point, not your company's rule. Redact first, confirm later.

## Challenge

Write a one-line 'AI used' note and add it to the document properties of your Q3 brief or workbook (File > Info > Properties in the Microsoft 365 app). This gives your connected Lumina Living Q3 pack a simple, honest record of where AI helped — ready for the final review.

## Reflection

LO4 — Decide what is safe to share with AI, and write a personal safe-use checklist you apply to the review pack. In your own words, how will you use this in your own work, and how will you check Claude got it right?

## Deliverable

Save your work — this safe-use checklist and verified figure become the trust layer for the connected **Lumina Living Q3 review pack**, the single deliverable you complete and send in Lab 8.

---

*Claude Microsoft 365 Masterclass (C197) · C197 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
