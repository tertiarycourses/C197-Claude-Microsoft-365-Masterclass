# Lab 7 — Build a Leadership Deck Two Ways

**Topic 03:** People Numbers and Reporting to Leadership  |  **Day 1**  |  **Approx. 30 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update.

Start from a blank deck. Build it with the Office panel, pasting the chart yourself so it stays linked to Excel. Then have Claude Desktop build the whole thing unaided, and compare what each produced.

## Goal

Build the same deck twice — once with the PowerPoint panel and a pasted Excel chart, once with Claude Desktop reading both files — and judge which suits the job.

## What you'll build

Two versions of the same six-slide update: one built in the panel with a linked Excel chart, one built end to end by Claude Desktop.

**Tools and techniques:** Claude for PowerPoint, Claude for Excel, Claude Desktop, linked native charts

## Company use case

- **Department:** Human Resources
- **Sponsor:** Head of HR
- **Business challenge:** Change a leaver number in the workbook and see which of the two decks updates.
- **Decision:** What do we want leadership to decide after this update?
- **Evidence:** HR brief; People numbers workbook; Company template
- **Measures:** Slides; Conclusions stated; Figures with a source
- **Controls:** Company template unchanged; Every figure has a source note; Untraceable figures flagged

## Files in this lab folder

- `Lumina-Living-Lab-07-HR-Brief.docx`
- `Lumina-Living-Lab-07-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-07-People-Numbers.xlsx`
- `Lumina-Living-Lab-07-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Lab 6 completed, so you have seen this analysis built.
- Excel and PowerPoint installed, with the Claude panel available in both.
- Lumina-Living-Lab-07-People-Numbers.xlsx (with charts on the Analysis tab), Lumina-Living-Lab-07-Blank-Deck.pptx and Lumina-Living-Lab-07-HR-Brief.docx from this folder.

## Process map

Get the headline in Excel → Plan the six slides → Panel builds, you paste the chart → Desktop builds the whole deck → Compare and refine

## Steps

### Step 1

Open Lumina-Living-Lab-07-People-Numbers.xlsx from this lab folder and click the Analysis tab. It already holds a summary table and two charts built from the Staff_List data. Open the Claude panel in Excel: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac. Get your headline before you build any slide.

**Prompt to give Claude:**

```text
On the Analysis sheet of this open workbook there are already two charts and a summary table.

Check the summary table first: click a cell in the Leaver rate column and confirm it is a formula pointing at Staff_List, not a typed-in number.

Then tell me the one sentence a leadership team should take away from the leaver-rate chart, and say which team I should talk about first.
```

### Step 2

Method one, the Office panel. Click the leaver-rate chart, press Cmd+C or Ctrl+C to copy it, and leave Excel open. Open Lumina-Living-Lab-07-Blank-Deck.pptx from this lab folder — a title slide and nothing else. Open the Claude panel in PowerPoint and ask it to plan the six slides before building anything.

**Prompt to give Claude:**

```text
I am building a six-slide people update for the Lumina Living leadership team, starting from a blank deck.

Using Lumina-Living-Lab-07-HR-Brief.docx and the charts in Lumina-Living-Lab-07-People-Numbers.xlsx, both in this folder, propose the six slides.

For each slide give:
- a title that states the conclusion, not the topic
- the single message of the slide
- what it is based on, naming the file
- whether it needs a chart, a table, or just words

Show me the outline. Do not build any slides yet.
```

### Step 3

Ask Claude to build the slides. It leaves a labelled placeholder where the chart belongs, because the panel works on one file at a time and cannot reach into Excel. Go to that slide, click the placeholder and press Cmd+V or Ctrl+V. Choose Keep Source Formatting so the chart stays linked to your workbook — change a number in Excel and the slide follows.

**Prompt to give Claude:**

```text
Build those six slides into this open presentation.

Keep the title slide as it is and add the six after it.
One message per slide. Use the title you proposed, not a topic word.
Where a slide needs the leaver-rate chart, leave a clearly labelled placeholder box saying which chart goes there — I will paste it from Excel myself.
Put a source note in small text at the bottom of any slide showing a figure, naming the file.
Write three short speaker notes lines per slide.
```

### Step 4

Method two, Claude Desktop. Open the Claude Desktop app and give it access to this lab folder. Ask it to build the whole deck itself, including the chart. It can read both files at once, so it does not need you to copy anything.

**Prompt to give Claude:**

```text
Read Lumina-Living-Lab-07-People-Numbers.xlsx and Lumina-Living-Lab-07-HR-Brief.docx in this folder.

Build a six-slide people update for the Lumina Living leadership team as a new PowerPoint file called Lumina-Living-Q1-Update-Desktop.pptx in this folder.

Every slide title must state the conclusion, not name a topic. Include the leaver-rate chart from the Analysis sheet on the slide about turnover. Put a source note naming the file under every figure. Add three short speaker notes lines per slide.
```

### Step 5

Open both decks side by side and compare. Check three things in the Desktop version: is the chart a real chart or a picture, does it still update when you change a number in the workbook, and did every title state a conclusion? Then keep refining whichever deck you prefer with plain prompts until it is right. Save your chosen deck into this lab folder.

**Prompt to give Claude:**

```text
Slide 3 is too crowded. Split it into two slides, keeping one message on each, and renumber the rest. Keep every source note.
```

## Test it

Both decks exist: one built in the panel with the Excel chart pasted in and linked, one named Lumina-Living-Q1-Update-Desktop.pptx built by Claude Desktop. Every title states a conclusion, every figure has a source note, you have written which version keeps the chart linked to the workbook, and at least one refinement prompt was used after the first build.

## Troubleshooting

- **The chart will not paste.** Copy it in Excel first, then click into the slide before pasting. Choose Keep Source Formatting to keep the link.
- **Claude built slides without the placeholder.** Ask again and say explicitly: 'leave a labelled placeholder box where the chart goes; do not draw the chart yourself.'
- **Claude Desktop produced a picture, not a chart.** That is the finding. Record it — a picture cannot update when the numbers change, which is why the panel method still matters.
- **Claude Desktop cannot see the files.** Confirm you gave it access to this lab folder, not to a single file.
- **A title names a topic.** Ask: 'rewrite the title of slide N so it states what we concluded.'

## Challenge

Create an appendix slide that reconciles every deck KPI to its Excel source cell and owner.

## Reflection

Which method would you use for a deck you must rebuild every quarter, and why?

## Deliverable

Two versions of the same six-slide update: one built in the panel with a linked Excel chart, one built end to end by Claude Desktop.

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
