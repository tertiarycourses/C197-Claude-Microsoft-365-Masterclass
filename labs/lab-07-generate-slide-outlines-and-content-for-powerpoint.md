# Lab 7 — Generate Slide Outlines and Content for PowerPoint

**Topic 02:** Boosting Productivity Across Microsoft 365 with Claude  |  **Day 1**  |  **Approx. 50 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Scenario

Lumina Living is a small home-and-lifestyle retailer. The quarter has just closed and your manager needs the Q3 business-review pack — a short written report, the numbers behind it, a slide deck for the management meeting, and the emails that send it out — by the end of the day. You have a rough brief, a sales workbook and a handful of facts to work from. Across this course you use Claude alongside Microsoft 365 to turn that raw material into a finished, checked pack. Use this scenario only if you cannot use real, non-confidential work of your own; your own material is always preferred.

## Goal

Use Claude to turn the report and analysis into a slide-by-slide outline with titles, bullets and speaker notes.

## What you'll build

A Q3 review slide deck in Microsoft PowerPoint, built from a Claude-generated outline you refined and checked.

**Tools and techniques:** Microsoft PowerPoint, Claude (slide outline / speaker notes), Outline view, copy-paste

## Prerequisites

- Labs 1–4 completed: Claude is set up and your Q3 files are connected in your Project.
- Lab 5 completed: the Q3 review report — this deck presents its content.
- Lab 6 completed: the verified Q3 figures — the deck must reuse these exact numbers, not fresh ones.
- Microsoft PowerPoint installed and open.
- Remember: Claude is a separate assistant, not a ribbon inside PowerPoint. Claude writes the outline; you build the slides in PowerPoint using View > Outline.

## Steps

### Step 1

Ask Claude to convert your report and verified figures into a slide outline.

Prompt to give Claude (paste into the chat):

```text
Turn the Q3 review report and the verified figures into a 6-slide deck for a 10-minute management meeting. For each slide give a title, no more than three short bullets, and two lines of speaker notes. Keep every figure consistent with the report.
```

### Step 2

Read the outline and check the figures on each slide against your verified numbers from Lab 6. Fix any that drift.

### Step 3

Refine the flow with a follow-up.

Prompt to give Claude (paste into the chat):

```text
Reorder so the recommended actions are the final slide, and make the opening slide a single headline that states how the quarter went.
```

### Step 4

Tighten wording so no bullet runs over one line.

Prompt to give Claude (paste into the chat):

```text
Shorten every bullet to at most eight words, keeping the meaning.
```

### Step 5

Build the slides: open PowerPoint, use View > Outline, and paste the titles and bullets so each slide is created from the outline (Tab to demote a line to a bullet).

### Step 6

Add the speaker notes: for each slide, paste Claude's two lines into the Notes pane (View > Notes).

### Step 7

Do the final human check: click through the deck, confirm every figure matches the report and workbook, then save it as 'Lumina Living — Q3 Review.pptx'.

## Test it

You have a saved 6-slide PowerPoint deck with a headline opener and an actions closer, one-line bullets, and speaker notes — with every figure consistent with your Word report and Excel analysis.

## Troubleshooting

- **Bullets overflow onto a second line on the slide.** The text is too long for the placeholder. Ask Claude to shorten each bullet to a hard word count ('at most eight words') rather than 'make it shorter', and cut filler words. If one still wraps, split the idea across two bullets or move the detail into the speaker notes.
- **A figure on a slide does not match the report.** Trust the report and the verified Lab 6 workbook, not the deck. Claude may have rounded or restated a number when it reformatted for slides. Correct the slide to the verified figure, and re-check every other slide for the same drift before you present.
- **Pasting the outline creates a single slide instead of many.** You are not in Outline view, or the lines are not structured as titles and bullets. Switch to View > Outline, put each slide title flush left (this starts a new slide), and press Tab to demote a line into a bullet under it. Paste as plain text so PowerPoint reads the indent levels, not the source formatting.

## Challenge

Ask Claude to draft a single closing slide that lists the three recommended actions with an owner placeholder for each, add it after your actions slide, and confirm the actions match your Word report word for word before the deck goes into the Lumina Living Q3 pack.

## Reflection

LO7 — Use Claude to turn the report and analysis into a slide-by-slide outline with titles, bullets and speaker notes. In your own words, how will you use this in your own work, and how will you check Claude got it right?

## Deliverable

Your saved 'Lumina Living — Q3 Review.pptx' — the management deck that joins the connected **Lumina Living Q3 review pack**.

---

*Claude Microsoft 365 Masterclass (C197) · C197 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
