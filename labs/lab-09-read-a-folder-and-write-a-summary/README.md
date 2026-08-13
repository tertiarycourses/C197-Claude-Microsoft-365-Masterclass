# Lab 9 — Read a Whole Folder and Write the Summary

**Topic 04:** Staff Questions, Repeatable Work and Advanced Claude  |  **Day 1**  |  **Approx. 20 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update.

A quarter's worth of HR reports sits in one folder as PDFs, with a CSV of the numbers. No single file answers the question. Claude reads them all and writes one summary, naming the file behind every claim.

## Goal

Have Claude read across a folder of HR files and write one summary, reporting what the files disagree on rather than resolving it.

## What you'll build

A two-page people summary built only from the folder, naming the file behind every claim, with disagreements reported rather than settled.

**Tools and techniques:** Claude Cowork, work folder, Projects, plugins, Microsoft 365 connector, multi-step execution, approvals

## Company use case

- **Department:** Human Resources
- **Sponsor:** Head of HR
- **Business challenge:** Add a file of your own to the folder that contradicts one of the others, and see whether Claude notices.
- **Decision:** What does the HR head need to know this week?
- **Evidence:** HR files in this folder
- **Measures:** Files read; Claims with a named file; Disagreements reported
- **Controls:** Only files in this folder; Every claim names its file; Disagreements reported, not resolved

## Files in this lab folder

- `Lumina-Living-Lab-09-HR-Brief.docx`
- `Lumina-Living-Lab-09-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-09-Staff-Questions.xlsx`
- `Lumina-Living-Lab-09-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Lab 0 completed, so Claude Desktop is installed and signed in.
- The hr-quarter-files folder from this lab folder: three PDF reports and a CSV.
- No work account or connector is needed. Everything is read from your own computer.

## Process map

Scope the folder → Connect approved context → Plan the task → Watch and steer → Review files in Microsoft 365

## Steps

### Step 1

Open the hr-quarter-files folder inside this lab folder. It holds what an HR team actually receives in a quarter: three reports as PDFs — headcount, exit interview themes and the hiring pipeline — plus a CSV of team numbers. Skim them. No single file answers the question 'how are our people doing?', and you cannot edit a PDF to find out.

### Step 2

Open the Claude Desktop app. Select the plus button, then Add files or photos, and give it access to this lab folder. The Office panel can only see one open file; Desktop can read the whole folder at once, which is what this job needs.

### Step 3

Ask Claude to read across the folder first, before writing anything. Read what it found, and pay attention to the last part of the answer.

**Prompt to give Claude:**

```text
Read every file in the hr-quarter-files folder here. There are three PDF reports and a CSV.

For each file tell me: its name, what it covers, and which question about our people it helps answer.

Then tell me anything the files disagree on, or any point one file raises that the others miss. Name the file behind every point. Do not change any file.
```

### Step 4

The files do not fully agree. The headcount report says total headcount is 88; add up the CSV and see what you get. The exit interview note also warns that flexible working will not fix the warehouse problem, which the headcount report does not mention. Claude should have surfaced both. If it did not, ask it directly what the numbers add up to.

### Step 5

Now ask for the summary. Check two figures against the CSV yourself, then write at the end of the summary which claims you verified and which still need the Head of HR to confirm.

**Prompt to give Claude:**

```text
Using only the files in the hr-quarter-files folder, write a two-page people summary for the Head of HR.

Cover: where headcount stands against plan, why people are leaving, and what the hiring pipeline looks like.

Take numbers from the CSV and the headcount report, and wording from the notes. Name the file and section behind every claim.

Where two files disagree, say so and give both figures — do not pick one. Where the files say nothing, write 'need to check'.

Save it as Lumina-Living-People-Summary.docx in this folder.
```

## Test it

The summary covers headcount against plan, why people are leaving and the hiring pipeline; every claim names its file; the disagreement between the headcount report and the CSV is reported with both figures; two figures were checked by hand; and the closing note says what still needs the Head of HR to confirm.

## Troubleshooting

- **Claude cannot see the files.** Give it access to this lab folder, not to a single file. Use the plus button, then Add files or photos.
- **Claude picked one figure and moved on.** That is the finding. Ask it directly: 'what does the CSV add up to, and does that match the headcount report?'
- **The summary cites a file that does not exist.** Ask it to list the exact file names it used, and compare them with the folder.
- **Claude resolved a contradiction on its own.** The prompt requires it to report both figures. Re-run it and say so again — an AI that quietly picks a number is the risk this lab is about.

## Challenge

Turn the approved hand-off workflow into a reusable Cowork skill outline with explicit inputs, checks and approval points.

## Reflection

Which mattered more here: what the files said, or what they disagreed about?

## Deliverable

A two-page people summary built only from the folder, naming the file behind every claim, with disagreements reported rather than settled.

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
