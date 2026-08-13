# Claude Microsoft 365 Masterclass (C197) — Learner Guide

**Course Code:** C197  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v3.0 · 13 August 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Prompt Best Practices for Word, Excel and PowerPoint](#prompt-best-practices-for-word-excel-and-powerpoint)
  - [Group A — Type these into the Claude panel INSIDE Word, Excel or PowerPoint](#group-a--type-these-into-the-claude-panel-inside-word-excel-or-powerpoint)
  - [Group B — Type these into the Claude Desktop app instead](#group-b--type-these-into-the-claude-desktop-app-instead)
- [Topic 01 — Getting Claude Ready for HR Work  (24%)](#topic-01--getting-claude-ready-for-hr-work--24)
  - [Lab 0 — Set Up Claude for Microsoft 365](#lab-0--set-up-claude-for-microsoft-365)
  - [Lab 1 — Shortlist Candidates with AI Experience](#lab-1--shortlist-candidates-with-ai-experience)
  - [Lab 2 — Analyse Staff Data and Decide What Claude May Read](#lab-2--analyse-staff-data-and-decide-what-claude-may-read)
  - [Lab 3 — Ask Claude Clearly](#lab-3--ask-claude-clearly)
- [Topic 02 — Hiring Plans, Policies and Staff Documents  (28%)](#topic-02--hiring-plans-policies-and-staff-documents--28)
  - [Lab 4 — Write a Hiring Plan in Word](#lab-4--write-a-hiring-plan-in-word)
  - [Lab 5 — Build an HR Policy Skill from Your Real Policies](#lab-5--build-an-hr-policy-skill-from-your-real-policies)
- [Topic 03 — People Numbers and Reporting to Leadership  (25%)](#topic-03--people-numbers-and-reporting-to-leadership--25)
  - [Lab 6 — Build a Headcount Analysis in Excel](#lab-6--build-a-headcount-analysis-in-excel)
  - [Lab 7 — Build a Leadership Deck Two Ways](#lab-7--build-a-leadership-deck-two-ways)
- [Topic 04 — Staff Questions, Repeatable Work and Advanced Claude  (23%)](#topic-04--staff-questions-repeatable-work-and-advanced-claude--23)
  - [Lab 15 — Use the Skill from Word Without Opening Excel](#lab-15--use-the-skill-from-word-without-opening-excel)
  - [Lab 8 — Sort the HR Inbox and Draft One Reply](#lab-8--sort-the-hr-inbox-and-draft-one-reply)
  - [Lab 9 — Read a Whole Folder and Write the Summary](#lab-9--read-a-whole-folder-and-write-the-summary)
  - [Lab 11 — Build a Daily HR Routine with Cowork](#lab-11--build-a-daily-hr-routine-with-cowork)
  - [Lab 12 — Automate an HR Pipeline with a Project](#lab-12--automate-an-hr-pipeline-with-a-project)
  - [Lab 10 — Draft an Outlook Reply with Claude in Chrome](#lab-10--draft-an-outlook-reply-with-claude-in-chrome)
  - [Lab 13 — Add Skills and Connectors to the Project](#lab-13--add-skills-and-connectors-to-the-project)
  - [Lab 14 — Upload a Shared Skill for Slides](#lab-14--upload-a-shared-skill-for-slides)
- [Wrap-Up — One Governed Company Workflow](#wrap-up--one-governed-company-workflow)
- [Next Steps](#next-steps)
- [Glossary](#glossary)
- [References and Further Learning](#references-and-further-learning)


## Introduction

This Learner Guide accompanies C197 and contains the complete procedures for eleven connected company activities. It is the operational companion to the concept-led slide deck.

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update. Every activity uses the same evidence chain so the hiring plan, people plan, policies, financial dashboard, presentation, Outlook hand-off, Cowork task and Claude Code daily brief remain consistent.


## Course Learning Outcomes

- LO1: Choose the right place to use Claude for an HR task.
- LO2: Decide what staff information Claude may read, and what it must never change.
- LO3: Write a request that says what you want, what to use, what to leave alone and when to stop.
- LO4: Write a hiring plan in Word using only what the brief actually says.
- LO5: Draft leave and flexible-work policy wording that flags every point needing legal review.
- LO6: Build a headcount and turnover analysis in Excel using live formulas.
- LO7: Build a leadership update deck where every slide title states a conclusion.
- LO8: Sort the HR inbox and draft one reply ready for approval.
- LO9: Have Claude read one folder and write a people summary that says where each fact came from.
- LO10: Automate a weekly people update on your own computer.
- LO11: Save a working method as a Skill so the whole team applies the same standard.
- LO12: Use the Microsoft 365 connector to find HR files stored in SharePoint.
- LO13: Add a plugin, and judge when a task needs one and when it does not.


## Before You Start — Preparation

**What you need**

- A current Windows or Mac laptop with Google Chrome, Microsoft 365 Word, Excel, PowerPoint and Outlook on the web.
- A paid Claude plan for the Office add-ins and Claude in Chrome. Lab 01 also distinguishes the Microsoft 365 connector in Claude Desktop and uses Claude in Chrome when the Outlook add-in is unavailable.
- Claude desktop with Cowork access for Lab 10 and Claude Code installed for Lab 11.
- An organisational Microsoft 365 account in an Entra tenant. The Microsoft 365 connector requires administrator consent; personal Outlook.com accounts are not supported.
- The self-contained Office files and templates inside each labs/lab-NN-*/ folder.

**Verify your setup**

Confirm the visible availability of every required surface before class. Missing add-ins, connector consent or Cowork access are real environment states and require the authorised administrator or the documented fallback.

```text
open Word / Excel / PowerPoint add-ins  ·  open Claude Desktop > Customize > Connectors  ·  verify Claude in Chrome is pinned and set to Manual approval
```

**Conventions used in every lab**

- All Lumina Living information is fictional and safe for training; do not replace it with confidential or personal data without approval.
- Shaded blocks are copy-ready prompts or commands. Replace angle-bracket placeholders before use.
- Every material figure must trace to a workbook cell, table or approved source note.
- Draft, save, write and send actions remain subject to the named human approval gate.

**Supplied sample files**

- Each lab folder contains a realistic company brief (.docx), working workbook (.xlsx), executive starter deck (.pptx) and reusable review templates.
- Lab 7 contains the headcount and staff-cost analysis; Lab 8 contains the leadership update deck that uses its checked figures.
- Lab 11 also contains a safe local automation starter for Excel updates and daily-brief generation; Microsoft 365 search uses the approved connector visible in Claude Code.


## Prompt Best Practices for Word, Excel and PowerPoint

A professional prompt is a compact work contract. It defines the result, evidence, constraints, output and approval boundary before Claude edits the work product.

**Five practices**

- Name the business result — State the decision, audience and artifact—not merely the app you are using.
- Ground the work — Name the open file, table, sheet, section or approved message set Claude may use.
- Constrain the edit — Define scope, length, style, formula method, layout and anything Claude must not change.
- Demand evidence — Require cell, range, heading or email citations and ask Claude to flag missing information.
- Set the approval gate — Ask for proposed changes first; verify them before accepting, saving, sending or publishing.

READ THIS FIRST. The prompts below are worked examples that show what a good prompt looks like. They are NOT lab steps. Every lab has its own numbered steps in its own section later in this guide. Every example below uses ONE folder only, so you never have to jump between labs: labs/lab-03-ask-claude-clearly/. Open the labs folder that came with your course materials, then open the lab-03-build-an-auditable-prompt-and-review-contract folder inside it. The Word, Excel and PowerPoint files named below are all sitting in that one folder. Double-click the named file to open it before you type anything. Each prompt deliberately stops at proposed changes: reading the proposal and choosing NOT to accept it is the correct result, because that is the human approval gate this course teaches.


### Group A — Type these into the Claude panel INSIDE Word, Excel or PowerPoint

1. Double-click the file named above the prompt so it opens in Word, Excel or PowerPoint.
2. Open the Claude panel from that app's ribbon. On Windows select Home, then Add-ins, then Claude. On Mac select Tools, then Add-ins, then Claude.
3. The Claude panel opens as a narrow column on the RIGHT-HAND side of your document.
4. Type the prompt into the box at the bottom of that panel. Do NOT type it into the document itself.
5. Read what Claude proposes, then stop. Do not accept the change.

> **Note:** In Group A, Claude can only see and change the one file you have open in front of you.

**Word example — Draft a decision-ready strategy section**

**Open this file first: labs/lab-03-ask-claude-clearly/Lumina-Living-Lab-03-HR-Brief.docx**

```text
Using the open Lumina-Living-Lab-03-HR-Brief.docx, write a new 'What we will do' section for the HR leadership team, placed after '3. Required management outputs'. Preserve the existing Heading 1 styles. For each action give the reason, who owns it, how we will know it worked, and the date. Use only facts stated in the brief; cite the source heading and flag missing evidence. Show proposed text before editing the document.
```

**Excel example — Build an auditable management view**

**Open this file first: labs/lab-03-ask-claude-clearly/Lumina-Living-Lab-03-Working-Workbook.xlsx**

```text
Using the table on the Management_Control sheet of the open Lumina-Living-Lab-03-Working-Workbook.xlsx, build a formula-driven summary of control status by owner on the Summary sheet. Use native formulas, cite the source rows you counted, and do not paste hardcoded totals. Before editing, list the formulas and checks you will apply.
```

**PowerPoint example — Create an executive planning story**

**Open this file first: labs/lab-03-ask-claude-clearly/Lumina-Living-Lab-03-Executive-Starter.pptx**

```text
Using the open Lumina-Living-Lab-03-Executive-Starter.pptx, together with Lumina-Living-Lab-03-HR-Brief.docx and Lumina-Living-Lab-03-Working-Workbook.xlsx from the same lab-03 folder, suggest a six-slide update for the HR leadership team. Use conclusion-led titles, one message per slide and concise speaker notes. Preserve the slide master and brand rules. Add a source note to each data slide and flag any figure that does not reconcile. Show the proposed outline before changing any slide.
```


### Group B — Type these into the Claude Desktop app instead

1. Do NOT open any Office file. This group does not use one.
2. Open the Claude Desktop application on your computer.
3. Select Customize, then Connectors, and check that Microsoft 365 shows as connected. If it does not, stop and record Admin approval required.
4. Type the prompt into the main chat box in the middle of the Claude Desktop window.
5. Read what Claude returns and check that every item carries a source citation.

> **Note:** This is the difference that matters: Group A changes the one file you have open, while Group B searches across your authorised Microsoft 365 files without opening any of them.

**Claude Desktop example — Find an authorised source before you draft**

**Before you type this: Do not open any Office file. Confirm the Microsoft 365 connector is connected in Claude Desktop at Customize > Connectors.**

```text
Find the latest fictional Lumina Living FY2027 planning item available to this training account. Return only its title, Microsoft 365 service and source citation. Do not draft, create, update, send or delete anything.
```

**Claude Desktop example — Compare evidence across Microsoft 365**

**Before you type this: Do not open any Office file. Confirm the Microsoft 365 connector is connected in Claude Desktop at Customize > Connectors.**

```text
Search my authorised Microsoft 365 content for Lumina Living FY2027 planning material. List each item with its title, service, owner and last modified date, and cite the source for every row. Report only what you can cite and state clearly what you could not find. Do not create, edit, send or delete anything.
```


## Topic 01 — Getting Claude Ready for HR Work  (24%)

Where to use Claude · what it may read · asking for what you want

**Key concepts**

- Three places to use Claude — inside Word, Excel and PowerPoint; in the Claude Desktop app; and in the browser. Each one sees different things.
- The panel inside Office works on the file you already have open, and keeps your headings, formulas and slide layouts.
- The Claude Desktop app can read a whole folder at once, so use it when the answer spans several files.
- HR files hold information about real people. Decide what Claude may read, and what it must never change, before you start.
- Ask Claude to say where each fact came from — which file, which sheet, which line — so you can check it before it reaches a staff member.
- You decide, not Claude. Nothing is sent, published or approved until a named person says yes.


### Lab 0 — Set Up Claude for Microsoft 365

Learning outcome: Install and check every way you will use Claude on this course, and record what your own account allows..

Goal: Install the Claude add-in in Word, Excel and PowerPoint, sign in to Claude Desktop, connect the Microsoft 365 connector, and add Claude for Chrome. Record what works on your machine before the labs begin.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: Which of the four routes is ready, and who do we ask about the rest?
- Evidence: Your own laptop; Your Claude account; Your Microsoft 365 account
- Controls: Do not bypass an administrator block; Record what you see; No staff data used during setup

**What you'll build**

A completed setup checklist showing which of the four routes are ready, and what to do about any that are not.   (Tools: Claude for Microsoft 365 add-in, Claude Desktop, Microsoft 365 connector, Claude for Chrome.)

**Prerequisites**

- A Claude account. The Office add-in, Skills and Claude for Chrome need a paid plan.
- Word, Excel and PowerPoint installed on your own computer.
- Google Chrome, if you want the browser route. It is not supported in other browsers.
- A Microsoft 365 work account for the connector. A personal Outlook.com account will not work.

**Process map**

Office add-in → Claude Desktop → Microsoft 365 connector → Claude for Chrome → Record what works

**Step-by-step**

1. Open Lumina-Living-Lab-00-Setup-Checklist.xlsx from this lab folder and click the Setup tab. You will record the result of every step below in the Result column: Ready, Not available, or Needs IT approval.
2. Install the Office add-in. In Word, select Home > Add-ins on Windows, or Tools > Add-ins on Mac, search for Claude, and add it. Sign in when prompted. Open Excel and PowerPoint and confirm Claude now appears there too — one install covers all the Office apps. Record the result for each app.
3. Open the Claude Desktop app and sign in with the same account. Give it access to one folder on your computer so you can see how folder access works: select the plus button, then Add files or photos, and choose this lab folder. Record whether Desktop is signed in and can see the folder.
4. Connect Microsoft 365. In Claude Desktop select Customize > Connectors, find Microsoft 365 and select Connect. Read the permission screen before you accept it — it lists exactly what Claude will be allowed to see. Sign in with your work account. If your organisation has not approved the connector, stop and record Needs IT approval; do not try to work around it.
5. Install Claude for Chrome. Open https://claude.com/claude-for-chrome, select Add to Chrome, and confirm the publisher is Anthropic. Pin it from the Extensions menu. In the side panel, set the permission mode to Manually approve. Record the result, then check every row of your checklist is filled in.

**Test it**

Every row of the Setup tab has a result. The Claude panel opens in Word, Excel and PowerPoint. Claude Desktop is signed in. The Microsoft 365 connector is either connected or recorded as Needs IT approval. Claude for Chrome is installed and set to Manually approve, or recorded as unavailable.

**Troubleshooting**

- The add-in is missing from Office — Open Home > Add-ins on Windows or Tools > Add-ins on Mac. If self-service installation is blocked by policy, record Needs IT approval — the labs work with the Desktop app instead.
- The Microsoft 365 connector is not listed — It needs a paid plan and, for work accounts, administrator approval. Record Not available. Every lab on this course also has a local route.
- Sign-in to the connector is blocked — A Microsoft 365 administrator must approve the connector for your organisation. Record Needs IT approval and continue; nothing on this course depends on it.
- Claude for Chrome will not install — It is Chrome only, and needs a paid plan. Record Not available; the browser route is used in one optional step.
- You are unsure which account to use — Ask your trainer before signing in. Do not connect a personal Microsoft account to a work machine during the class.

**Challenge**

Open the same file in the Office panel and in Claude Desktop, and note one thing each can do that the other cannot.

**Reflection**

Which of the four routes will you use most in your own work, and what would you need approved to use the others?

> **Note:** The matching detailed lab folder is in labs/lab-00-set-up-claude-for-microsoft-365/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 1 — Shortlist Candidates with AI Experience

Learning outcome: Use Claude to shortlist job applicants, and see the difference between the Excel panel and the Claude Desktop app..

Goal: Twenty-four people applied for HR roles. Claude fills in the shortlist directly in your Excel sheet, you check its decisions, then you run the same request in the Claude Desktop app and see that it hands you a downloaded copy instead of editing your file.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: What are our rules for HR wording, and can we make them stick?
- Evidence: The staff handbook in this folder
- Controls: No invented dates or entitlements; No legal conclusions; Legal review before release

**What you'll build**

A saved shortlist in your own workbook, a second copy saved from the Desktop app, and one sentence on which way suits work that must stay in one file.   (Tools: Claude for Word, Claude Skills, natural-language skill creation.)

**Prerequisites**

- Excel installed, with the Claude panel available from the ribbon.
- The Claude Desktop app installed on your own computer.
- Lumina-Living-Lab-01-Candidates.xlsx from this folder. No work account is needed and nothing is stored in the cloud.

**Files you will use, and what the steps call them**

Every file for this lab is in one folder: labs/lab-01-screen-candidates-in-excel/ . The steps below name these items in plain English; use this table to find the exact file to open and the exact sheet tab to click at the bottom of the Excel window.

| The steps call it | App | Open this file | Then click |
|---|---|---|---|
| The list of job applicants you work on | Excel | Lumina-Living-Lab-01-Candidates.xlsx | opens on the first tab |
| How this workbook is organised — read this tab first | Excel | Lumina-Living-Lab-01-Candidates.xlsx | the "Read_Me" tab |
| The 24 applicants and the two columns you fill in | Excel | Lumina-Living-Lab-01-Candidates.xlsx | the "Candidates" tab |

**Process map**

Ask for it your way → Correct until right → Save it in one sentence → Check it is listed → Stop repeating yourself

**Step-by-step**

1. Open Lumina-Living-Lab-01-Candidates.xlsx from this lab folder and click the Candidates tab. It lists 24 people who applied for HR roles at Lumina Living. Read a few of the Experience notes and see how long it would take you to find the right people by hand. The last two columns, Shortlist and Why, are empty. Claude is about to fill them in.
2. Open the Claude panel in Excel: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac. Type the request below. Watch the two columns fill in on the sheet, then press Cmd+S or Ctrl+S to save. Your own file now holds the shortlist. Prompt to give Claude:

   ```text
   I am shortlisting people for an HR job. Only shortlist someone if they have actually used an AI tool at work.

On the Candidates sheet, fill in two columns for all 24 rows:
- In the Shortlist column, write Yes or No.
- In the Why column, copy the words from the Experience notes that made you decide.

Write Yes only if the notes show they used an AI tool in their job.
Write No if the notes show no AI tool, or if they only studied AI or attended a course.

Do not change any other column.
   ```

3. Check what Claude decided. Row C-011 attended an AI course and row C-013 is studying for a certificate. Neither has used an AI tool at work, so both should be No. Rows C-006, C-012 and C-017 say 'piloted', 'trialled' and 'experimented with' — you decide whether trying something at work counts as using it. Type over any row you disagree with.
4. Now open the Claude Desktop app, give it access to this lab folder, and type exactly the same request again. Watch what happens: it reads your workbook and offers a filled copy to download rather than typing into the sheet you have open. Select Download and open, then File > Save As into this folder as Lumina-Living-Lab-01-Candidates-Desktop.xlsx. Prompt to give Claude:

   ```text
   I am shortlisting people for an HR job. Only shortlist someone if they have actually used an AI tool at work.

On the Candidates sheet, fill in two columns for all 24 rows:
- In the Shortlist column, write Yes or No.
- In the Why column, copy the words from the Experience notes that made you decide.

Write Yes only if the notes show they used an AI tool in their job.
Write No if the notes show no AI tool, or if they only studied AI or attended a course.

Do not change any other column.
   ```

5. Open both files side by side. They hold the same shortlist but they are two separate files, and only the first is the one the hiring manager opens. Write one sentence at the bottom of your original sheet: if the shortlist must stay in one agreed file, which of the two would you use, and why?

**Test it**

All 24 rows have Yes or No with a quoted reason and the file is saved, rows C-011 and C-013 are marked No, a second file named Lumina-Living-Lab-01-Candidates-Desktop.xlsx exists in the folder, and you have written which of the two ways keeps the shortlist in one agreed file.

**Troubleshooting**

- Claude does not save the skill — Say it plainly: 'Save that as a skill called hr-draft.' If nothing happens, try /skillify instead.
- Skills is not in the plus menu — Skills is available on paid Claude plans. Record it and keep the written method to reuse by hand in the next lab.
- Claude states a legal conclusion — Correct it before you save. Whatever you save is what you get every future time.

**Challenge**

Explain in one sentence which route you would choose for work on an open Word document and which route you would choose to search authorised Microsoft 365 content.

**Reflection**

Which of your corrections would have been most costly to leave out?

> **Note:** The matching detailed lab folder is in labs/lab-01-screen-candidates-in-excel/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 2 — Analyse Staff Data and Decide What Claude May Read

Learning outcome: Use Claude to summarise and chart real staff data, then decide what access it needed to do that..

Goal: Claude summarises the staff list by team, builds a chart, and you check its formulas. Then you decide what access Claude actually needed, having just seen what read-only access can do.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: Does the saved standard hold without being restated?
- Evidence: The second half of the staff handbook
- Controls: No invented entitlements; No legal conclusions; A person approves before release

**What you'll build**

A summary table and chart built by Claude in your own workbook, plus a completed access table.   (Tools: Claude for Word, Claude Skills.)

**Prerequisites**

- Lab 1 completed.
- Excel installed, with the Claude panel available from the ribbon.
- Lumina-Living-Lab-02-Staff-Information.xlsx from this folder. No work account and no connector are needed.

**Files you will use, and what the steps call them**

Every file for this lab is in one folder: labs/lab-02-analyse-staff-data-in-excel/ . The steps below name these items in plain English; use this table to find the exact file to open and the exact sheet tab to click at the bottom of the Excel window.

| The steps call it | App | Open this file | Then click |
|---|---|---|---|
| The workbook you complete in this lab | Excel | Lumina-Living-Lab-02-Staff-Information.xlsx | opens on the first tab |
| The summary view | Excel | Lumina-Living-Lab-02-Staff-Information.xlsx | the "Summary" tab |
| How this workbook is organised — read this tab first | Excel | Lumina-Living-Lab-02-Staff-Information.xlsx | the "Read_Me" tab |
| The staff data you analyse | Excel | Lumina-Living-Lab-02-Staff-Information.xlsx | the "Staff_List" tab |
| What Claude may do with each one | Excel | Lumina-Living-Lab-02-Staff-Information.xlsx | the "What_Claude_May_Do" tab |
| Where staff information is kept | Excel | Lumina-Living-Lab-02-Staff-Information.xlsx | the "Where_Info_Is_Kept" tab |
| The review log — where you record who checked the work | Excel | Lumina-Living-Lab-02-Staff-Information.xlsx | the "Review_Log" tab |

**Process map**

New section → One short line → Same standard applied → Check it held → Repeat at will

**Step-by-step**

1. Open Lumina-Living-Lab-02-Staff-Information.xlsx from this lab folder and click the Staff_List tab. It shows 12 roles across four teams, with headcount, salary, leavers and how long each role takes to fill. Open the Claude panel in Excel: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac.
2. Ask Claude to summarise the staff data by team. Watch the new table appear on the sheet. Prompt to give Claude:

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

3. Ask Claude to chart it. A bar chart appears on the sheet. Prompt to give Claude:

   ```text
   On the Staff_List sheet, add a bar chart showing the leaver rate for each team, using the summary table you just built.

Give the chart a title that says what it shows.
Sort the bars from highest leaver rate to lowest.
Place the chart to the right of the summary table so it does not cover any data.
   ```

4. Check the numbers yourself. Click one cell in the summary table and read the formula bar: it should point at the rows above, not be a number someone typed. Then press Cmd+S or Ctrl+S to save.
5. Now click the Where_Info_Is_Kept tab. It lists the four places HR keeps staff information, including the payroll data behind the salary column you just used. Fill in the What_Claude_May_Do tab: for each place type 'Read only' or 'Read and change', name who owns it, and say what you would do if it were unavailable. Then ask Claude to check your two tabs against each other. Prompt to give Claude:

   ```text
   Compare the What_Claude_May_Do sheet with the Where_Info_Is_Kept sheet in this workbook. Tell me any place that has no owner, no read-or-change decision, or where the two sheets disagree. Say which row you mean. Do not change the workbook.
   ```


**Test it**

The summary table uses formulas that point at the staff rows, the chart shows leaver rate by team, the file is saved, and all four places have a read-or-change decision with an owner.

**Troubleshooting**

- Claude ignores the skill — Name it: 'Apply my hr-draft skill.' If it is missing, check the plus menu, Skills.
- The result differs from Lab 1 — A rule was not captured when you saved. Go back, correct it and save the skill again.
- A section invents an entitlement — That is a finding. Correct it, and add the rule to the skill so it cannot recur.

**Challenge**

Design a read-only pilot group and a separate, smaller write-enabled group for the company rollout.

**Reflection**

What did you not have to say this time that you said in the last lab?

> **Note:** The matching detailed lab folder is in labs/lab-02-analyse-staff-data-in-excel/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 3 — Ask Claude Clearly

Learning outcome: Write a request that says what you want, what to use, what not to change, and when to stop..

Goal: Run a vague request and a clear one against the same HR brief, and see the difference for yourself.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: How do we make the same analysis come out the same way every quarter?
- Evidence: This quarter's staff data
- Controls: Formulas point at source rows; No typed-in totals; A person checks the finding

**What you'll build**

A new section written into the brief by Claude, a second copy produced by the Desktop app, and a completed request checklist.   (Tools: Claude for Excel, Claude Skills, natural-language skill creation.)

**Prerequisites**

- Labs 1 and 2 completed.
- Word installed, with the Claude panel available from the ribbon.
- The Claude Desktop app installed.
- Lumina-Living-Lab-03-HR-Brief.docx from this folder.

**Files you will use, and what the steps call them**

Every file for this lab is in one folder: labs/lab-03-ask-claude-clearly-in-word/ . The steps below name these items in plain English; use this table to find the exact file to open and the exact sheet tab to click at the bottom of the Excel window.

| The steps call it | App | Open this file | Then click |
|---|---|---|---|
| The HR brief — the source you read before asking Claude anything | Word | Lumina-Living-Lab-03-HR-Brief.docx | — |
| The blank prompt contract you fill in | Word | templates/Prompt-and-Review-Template.docx | — |

**Process map**

Ask for it your way → Correct until right → Save it in one sentence → Check it is listed → Ready to reuse

**Step-by-step**

1. Open Lumina-Living-Lab-03-HR-Brief.docx from this lab folder and read the six headings. Open the Claude panel in Word: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac.
2. Type this vague request. Claude answers in the panel but cannot do much with it: it does not know which plan you mean, what to change, or where to put anything. Read what comes back, then move on. Prompt to give Claude:

   ```text
   Improve our plan.
   ```

3. Now type the clear request below. This time watch the document itself: a new section appears after '3. Required management outputs'. When it finishes, read it — every fact should name the heading it came from, and anything the brief does not say should be marked 'need to check'. Delete anything you cannot trace back, then press Cmd+S or Ctrl+S to save. Prompt to give Claude:

   ```text
   Using the open Lumina-Living-Lab-03-HR-Brief.docx, add a new section called 'What we will do', straight after the section '3. Required management outputs'.

Write it into the document using the same heading style as the other sections.

For each action give:
- the reason we are doing it
- who owns it
- how we will know it worked
- the date it is due

Use only what this brief actually says. After each fact, name the heading you took it from. Where the brief says nothing, write 'need to check' instead of making something up.
   ```

4. Now open the Claude Desktop app, give it access to this lab folder, and type exactly the same clear request again. It cannot write into the document you have open. Instead it produces a new Word file and offers a Download button. Select Download and open, then File > Save As into this folder as Lumina-Living-Lab-03-HR-Brief-Desktop.docx. Prompt to give Claude:

   ```text
   Using the open Lumina-Living-Lab-03-HR-Brief.docx, add a new section called 'What we will do', straight after the section '3. Required management outputs'.

Write it into the document using the same heading style as the other sections.

For each action give:
- the reason we are doing it
- who owns it
- how we will know it worked
- the date it is due

Use only what this brief actually says. After each fact, name the heading you took it from. Where the brief says nothing, write 'need to check' instead of making something up.
   ```

5. Put the two documents side by side. Your original keeps the brief's own heading styles because Claude wrote straight into it; the downloaded copy is a new document, so its headings were rebuilt and may not match. Open templates/Prompt-and-Review-Template.docx and write down two things: the five parts that made the clear request work, and which of the two documents you would send to the HR head.

**Test it**

The new section sits after '3. Required management outputs' with every fact naming its heading, the file is saved, a second file named Lumina-Living-Lab-03-HR-Brief-Desktop.docx exists, and the checklist says which document you would send on and why.

**Troubleshooting**

- Claude does not save the skill — Say it plainly: 'Save that as a skill called staff-numbers.' If nothing happens, try /skillify instead.
- The table has typed-in numbers — Correct it before you save. Whatever you save is what you get every future time.
- The leaver rate looks wrong — Check it divides leavers by headcount for that team, not by total headcount.

**Challenge**

Create a prompt rubric that a colleague can use without knowing how the prompt was written.

**Reflection**

Which correction would have cost you most if you had saved without making it?

> **Note:** The matching detailed lab folder is in labs/lab-03-ask-claude-clearly-in-word/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


## Topic 02 — Hiring Plans, Policies and Staff Documents  (28%)

Hiring plan · leave and flexible-work policy · handbook wording · who signs off

**Key concepts**

- A hiring plan makes choices: which roles now, which can wait, and what the budget will not cover.
- Every role needs a hiring manager, a start date, a salary range and the reason the role exists.
- Policy wording carries real consequences. Anything about pay, leave, notice or conduct needs proper review before release.
- Keep three things apart: what the policy says, how it works day to day, and what needs legal advice.
- Work inside the company template so the document looks like every other HR document staff receive.
- Say plainly what you do not yet know, rather than filling the gap with a confident guess.


### Lab 4 — Write a Hiring Plan in Word

Learning outcome: Write an FY2027 hiring plan in Word using only what the HR brief actually says..

Goal: Section 2 of the brief lists five roles the teams want and the budget that limits them. Claude works out what fits, writes the plan into your document, then exports it as a standalone document for approval.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: Which roles do we fill now, and which do we hold back?
- Evidence: HR brief; Team headcount list; Salary bands; Budget limit
- Controls: No invented salary figures; Cost stays within budget; Head of HR approves

**What you'll build**

A hiring plan section written into the brief, and a separate Lumina-Living-FY2027-Hiring-Plan.docx ready for the Head of HR.   (Tools: Claude for Word, company templates, evidence checks, human approval.)

**Prerequisites**

- Labs 1 to 3 completed.
- Word installed, with the Claude panel available from the ribbon.
- Lumina-Living-Lab-04-HR-Brief.docx from this folder.

**Files you will use, and what the steps call them**

Every file for this lab is in one folder: labs/lab-04-write-a-hiring-plan-in-word/ . The steps below name these items in plain English; use this table to find the exact file to open and the exact sheet tab to click at the bottom of the Excel window.

| The steps call it | App | Open this file | Then click |
|---|---|---|---|
| The HR brief — the source you read before asking Claude anything | Word | Lumina-Living-Lab-04-HR-Brief.docx | — |

**Process map**

Read the role table → Work out what fits → Write it into the brief → Check every figure → Export for approval

**Step-by-step**

1. Open Lumina-Living-Lab-04-HR-Brief.docx from this lab folder. Go to section 2 and read the table of five roles the teams have asked for, and the budget line underneath it. In Lab 2 you found the warehouse team is losing people fastest; three of these five roles are warehouse and online replacements. Open the Claude panel in Word.
2. Ask Claude to work out what fits. Read the answer and check the arithmetic yourself before you go on. Claude answers in the panel only — your document will not change yet. That happens in the next step. Prompt to give Claude:

   ```text
   Using the open Lumina-Living-Lab-04-HR-Brief.docx, look at the table of roles requested for FY2027 in section 2, and at the budget line under it.\n\nTell me which roles we should fill and which we should hold back, so that we stay inside both the budget and the headcount cap.\n\nFor each role give: the team, how many, the salary band from the table, the cost if we fill it, and the reason.\nAdd up the total and show it against the budget and the cap.\nUse the salary bands exactly as written. Do not invent a figure.\n\nShow me your answer here. Do not change the document yet.
   ```

3. Now ask Claude to write the plan into the document. This is the step that changes the document. Watch the new section appear after section 3, then press Cmd+S or Ctrl+S to save. Prompt to give Claude:

   ```text
   Now write that hiring plan into the open Lumina-Living-Lab-04-HR-Brief.docx, straight after the section '3. Required management outputs'.\n\nUse the same heading style as the other sections. Call it 'FY2027 hiring plan' and include:\n- Roles to fill: team, how many, salary band, cost, hiring manager\n- Roles to hold back, with the reason\n- Total added monthly cost against the $38,000 budget and the 10-role cap\n- Who approves the plan\n\nTake every figure from the table in section 2 and name the section you took it from. Where the brief says nothing, write 'need to check'.
   ```

4. Read the new section. Check every salary against the table in section 2, check the total, and check that anything the brief does not say is marked 'need to check'. Correct anything wrong yourself.
5. Now ask Claude to pull that section out into a document of its own. This is the version that goes to the Head of HR, without the rest of the brief attached. Prompt to give Claude:

   ```text
   Create a new Word document called Lumina-Living-FY2027-Hiring-Plan.docx in this lab folder.\n\nPut only the 'FY2027 hiring plan' section into it — the roles to fill, the roles to hold back, the cost against budget and the approver. Do not include the rest of the brief.\n\nAdd a short heading at the top: 'FY2027 Hiring Plan — for approval by the Head of HR'. Keep the figures exactly as they are in the brief.
   ```


**Test it**

The brief has an 'FY2027 hiring plan' section after section 3 with every salary matching the table in section 2, the total is shown against the $38,000 budget and the 10-role cap, and a separate file named Lumina-Living-FY2027-Hiring-Plan.docx exists in the folder containing only the plan.

**Troubleshooting**

- Claude says every field needs checking — Confirm you are looking at section 2 of the Lab 04 brief. The role table with salary bands must be visible in the open document.
- The total does not match — Ask Claude to show the arithmetic role by role, then check it against the table yourself.
- Claude changed the document at step 2 — That step ends with 'do not change the document yet'. Undo with Ctrl+Z or Cmd+Z and run it again exactly as written.
- The exported plan includes the whole brief — Ask again, naming only the 'FY2027 hiring plan' section.

**Challenge**

Change the budget to $30,000 and ask Claude which role now has to go.

**Reflection**

Which role was hardest to hold back, and what evidence would change your mind?

> **Note:** The matching detailed lab folder is in labs/lab-04-write-a-hiring-plan-in-word/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 5 — Build an HR Policy Skill from Your Real Policies

Learning outcome: Create a skill from your company's existing policy documents, then use it to draft new policy wording that matches them..

Goal: Your house style already exists in the policies you have published and the template you write them into. Hand Claude the examples, the rules and the template, turn that into a skill, then draft two new policies from a real consultation note.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: What can we publish now, and what must go to legal first?
- Evidence: HR brief; Existing staff handbook
- Controls: Policy, practice and legal advice kept separate; No legal conclusions stated; Legal review before release

**What you'll build**

An hr-policy-draft skill built from your real policy library and template, and two new policies on the company letterhead.   (Tools: Claude Skills, Upload a skill, Claude for Word.)

**Prerequisites**

- Labs 1 to 4 completed.
- Word installed, with the Claude panel available from the ribbon.
- A Claude account you can sign in to on claude.ai or in Claude Desktop. Skills is available on paid plans.
- The hr-policy-library folder, how-we-write-hr-policy.md, templates/HR-Policy-Template.docx and Lumina-Living-Lab-05-HR-Consultation-Note.docx from this folder.

**Process map**

Define boundary → Verify metrics → Draft narrative → Separate policy from procedure → Obtain specialist approval

**Step-by-step**

1. Open the hr-policy-library folder inside this lab folder. It holds three approved Lumina Living policies as PDFs: annual leave, notice period and probation. Open one and see how it is written — company letterhead, four numbered sections, every gap marked, approval table at the end. Then open Lumina-Living-Lab-05-HR-Consultation-Note.docx: this is your source, and it separates what the management team has agreed from what is still open.
2. Open Claude Desktop or go to claude.ai and start a new conversation. Attach how-we-write-hr-policy.md, all three PDFs from hr-policy-library, and templates/HR-Policy-Template.docx. Then ask Claude to build the skill. It learns your house style from real examples and the layout from your own template. Prompt to give Claude:

   ```text
   I am attaching four things from our HR folder: how-we-write-hr-policy.md, three approved policies from our policy library, and our blank HR-Policy-Template.docx.

Create a skill called hr-policy-draft that I can use whenever I draft HR policy wording for staff.

Base it on all of them:
- the rules in the markdown file
- the way the three approved policies are actually written: their four-part structure, their tone, and how they cross-reference each other by name in single quotes
- the blank template, which is the layout every new policy must follow, including the letterhead, the version and approver line, and the approval table at the end

The skill must always produce policy wording that drops straight into that template. Keep every rule. Do not simplify them.
   ```

3. Check it saved. Open Settings > Skills and confirm hr-policy-draft is listed with you as the author. Read what Claude wrote: does it capture the four sections, the rule about marking gaps, and the template layout? Add anything it missed — you own the standard, not Claude.
4. Open templates/HR-Policy-Template.docx from this lab folder and immediately save a copy into the lab folder as Flexible-Working-Policy.docx. Close every other Word window, so this copy is the only document open — the Claude panel writes into whichever document is active, so having the brief open as well will confuse it. Now open the Claude panel: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac. Prompt to give Claude:

   ```text
   Apply my hr-policy-draft skill and write the flexible working policy into this open document.

This document is our blank HR policy template. Fill in the policy name, the four numbered sections and the approval table. Keep the letterhead exactly as it is.

Take the source material from sections 2 and 3 of Lumina-Living-Lab-05-HR-Consultation-Note.docx, in this same folder. Section 2 is what has been agreed; section 3 lists what is still open. Every point in section 3 must appear under 'Still to confirm' rather than being decided by you.
   ```

5. Check it: the letterhead is untouched, the four sections are filled, every fact names the heading it came from, gaps are marked 'need to check', no legal conclusion is stated, and the approval table is still there. Put it beside a policy from hr-policy-library — it should look like one of them. Save. Then make a second copy of the template, call it Leave-Carry-Over-Policy.docx, close the first one, and draft again in one line. Prompt to give Claude:

   ```text
   Apply my hr-policy-draft skill and write the leave carry-over policy into this open document, the same way. Keep the letterhead, fill the four sections and the approval table, and take the source material from sections 4 and 5 of Lumina-Living-Lab-05-HR-Consultation-Note.docx in this folder.
   ```


**Test it**

A skill named hr-policy-draft is listed in Settings > Skills, both new policies use the company letterhead and the four numbered sections, every fact traces to the consultation note, every open point from the note appears under 'Still to confirm', no legal conclusion is stated, the approval table is intact, and both files are saved in the lab folder.

**Troubleshooting**

- Claude says it is bound to the wrong document — The Word panel writes into whichever document is active. Close every other Word window, leave only your copy of the template open, and ask again.
- Claude will not attach the PDFs — Attach how-we-write-hr-policy.md on its own and paste one policy's text into the conversation as an example.
- Skills is not in the menu — Skills is available on paid Claude plans. If it is missing, paste the rules from how-we-write-hr-policy.md into your request each time.
- The letterhead disappeared — Undo with Ctrl+Z or Cmd+Z. Ask again and say 'keep the letterhead exactly as it is' — a skill only protects what its rules mention.
- A legal conclusion appears — That breaks the standard. Correct it, and add the rule to the skill so it cannot recur.

**Challenge**

Add a methodology-change disclosure showing how a revised conversion factor affects comparability.

**Reflection**

What did Claude learn from the example policies that the written rules alone did not say?

> **Note:** The matching detailed lab folder is in labs/lab-05-draft-hr-policy-in-word/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


## Topic 03 — People Numbers and Reporting to Leadership  (25%)

Headcount and turnover in Excel · what the numbers say · the leadership update

**Key concepts**

- Keep the staff data, the assumptions and the results on separate sheets so anyone can follow the working.
- Use live formulas that point at the source data. A number typed in by hand cannot be checked or updated.
- Compare actual headcount and cost against plan, month by month and team by team, before you explain the result.
- Pick the chart that answers the question leadership asked. More charts is not more insight.
- Every slide title should say what you concluded, not name a topic.
- Put the source under any figure on a slide, so the room can challenge it.


### Lab 6 — Build a Headcount Analysis in Excel

Learning outcome: Build a headcount and cost analysis in Excel using live formulas, not typed-in numbers..

Goal: Compare actual headcount and staff cost against plan, month by month and team by team, using formulas that point at the source data.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: Where are we above or below plan, and why?
- Evidence: Staff list; Headcount plan; Assumptions
- Controls: Formulas point at source data; No typed-in totals; Assumptions kept on one sheet

**What you'll build**

An analysis sheet where every result is a formula that points back to the source data.   (Tools: Claude for Excel, tables, formulas, pivots, scenarios, chart selection, dashboard, audit log.)

**Prerequisites**

- Labs 1–6 completed.
- Open the supplied Finance Model workbook and Data Dictionary.
- Use only the fictional transaction data supplied in this lab.

**Files you will use, and what the steps call them**

Every file for this lab is in one folder: labs/lab-06-build-a-headcount-analysis-in-excel/ . The steps below name these items in plain English; use this table to find the exact file to open and the exact sheet tab to click at the bottom of the Excel window.

| The steps call it | App | Open this file | Then click |
|---|---|---|---|
| The workbook you complete in this lab | Excel | Lumina-Living-Lab-06-People-Numbers.xlsx | opens on the first tab |
| How this workbook is organised — read this tab first | Excel | Lumina-Living-Lab-06-People-Numbers.xlsx | the "Read_Me" tab |
| The staff data you analyse | Excel | Lumina-Living-Lab-06-People-Numbers.xlsx | the "Staff_List" tab |
| The assumptions used by every formula | Excel | Lumina-Living-Lab-06-People-Numbers.xlsx | the "Assumptions" tab |
| The analysis working area | Excel | Lumina-Living-Lab-06-People-Numbers.xlsx | the "Analysis" tab |

**Process map**

Understand the model → Validate inputs → Build formulas → Explain drivers → Dashboard and senior review

**Step-by-step**

1. Open Lumina-Living-Lab-06-People-Numbers.xlsx from this lab folder. Click the Staff_List tab to see the people data, then the Assumptions tab. Open the Claude panel in Excel.
2. Ask Claude to plan the analysis before it changes anything. Read the answer on screen. Prompt to give Claude:

   ```text
   Look at the Staff_List sheet and the Assumptions sheet in this open workbook. Tell me the formulas and checks you would use to compare actual headcount and staff cost against the plan, month by month and team by team. Name the sheets and columns you would use. Do not change the workbook yet.
   ```

3. Ask Claude to build the analysis with live formulas, not typed-in numbers. Prompt to give Claude:

   ```text
   On the Analysis sheet of this open workbook, build a comparison of actual headcount and staff cost against plan, by month and by team, using the Staff_List and Plan sheets. Show headcount, staff cost and the gap against plan. Use Excel formulas that point at the source data. Do not type in any total by hand. Keep every assumption on the Assumptions sheet.
   ```

4. Click into two of the result cells and read the formula bar. Check each one points at real data and is not a number someone typed.
5. Change one figure on the Assumptions tab and check the Analysis sheet updates. Write the check on the Checks tab.

**Test it**

Two result cells checked in the formula bar show real formulas pointing at the source data, and changing an assumption updates the analysis.

**Troubleshooting**

- A KPI does not recalculate — Trace precedents and replace any pasted value with a formula tied to the approved table.
- The variance sign is confusing — Define favourable/unfavourable logic once and apply it consistently across tables, charts and narrative.
- The dashboard is crowded — Keep four KPIs and three decision charts; move details to Analysis and document definitions.

**Challenge**

Add a sensitivity table showing which assumption has the largest effect on Operating Contribution.

**Reflection**

Which model control gave you the strongest evidence that the dashboard can be trusted?

> **Note:** The matching detailed lab folder is in labs/lab-06-build-a-headcount-analysis-in-excel/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 7 — Build a Leadership Deck Two Ways

Learning outcome: Build the same deck twice — once with the PowerPoint panel and a pasted Excel chart, once with Claude Desktop reading both files — and judge which suits the job..

Goal: Start from a blank deck. Build it with the Office panel, pasting the chart yourself so it stays linked to Excel. Then have Claude Desktop build the whole thing unaided, and compare what each produced.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: What do we want leadership to decide after this update?
- Evidence: HR brief; People numbers workbook; Company template
- Controls: Company template unchanged; Every figure has a source note; Untraceable figures flagged

**What you'll build**

Two versions of the same six-slide update: one built in the panel with a linked Excel chart, one built end to end by Claude Desktop.   (Tools: Claude for PowerPoint, Claude for Excel, Claude Desktop, linked native charts.)

**Prerequisites**

- Lab 6 completed, so you have seen this analysis built.
- Excel and PowerPoint installed, with the Claude panel available in both.
- Lumina-Living-Lab-07-People-Numbers.xlsx (with charts on the Analysis tab), Lumina-Living-Lab-07-Blank-Deck.pptx and Lumina-Living-Lab-07-HR-Brief.docx from this folder.

**Files you will use, and what the steps call them**

Every file for this lab is in one folder: labs/lab-07-build-a-leadership-update-in-powerpoint/ . The steps below name these items in plain English; use this table to find the exact file to open and the exact sheet tab to click at the bottom of the Excel window.

| The steps call it | App | Open this file | Then click |
|---|---|---|---|
| The HR brief — the source you read before asking Claude anything | Word | Lumina-Living-Lab-07-HR-Brief.docx | — |
| The workbook you complete in this lab | Excel | Lumina-Living-Lab-07-People-Numbers.xlsx | opens on the first tab |
| How this workbook is organised — read this tab first | Excel | Lumina-Living-Lab-07-People-Numbers.xlsx | the "Read_Me" tab |
| The staff data you analyse | Excel | Lumina-Living-Lab-07-People-Numbers.xlsx | the "Staff_List" tab |
| The assumptions used by every formula | Excel | Lumina-Living-Lab-07-People-Numbers.xlsx | the "Assumptions" tab |
| The analysis working area | Excel | Lumina-Living-Lab-07-People-Numbers.xlsx | the "Analysis" tab |

**Process map**

Get the headline in Excel → Plan the six slides → Panel builds, you paste the chart → Desktop builds the whole deck → Compare and refine

**Step-by-step**

1. Open Lumina-Living-Lab-07-People-Numbers.xlsx from this lab folder and click the Analysis tab. It already holds a summary table and two charts built from the Staff_List data. Open the Claude panel in Excel: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac. Get your headline before you build any slide. Prompt to give Claude:

   ```text
   On the Analysis sheet of this open workbook there are already two charts and a summary table.

Check the summary table first: click a cell in the Leaver rate column and confirm it is a formula pointing at Staff_List, not a typed-in number.

Then tell me the one sentence a leadership team should take away from the leaver-rate chart, and say which team I should talk about first.
   ```

2. Method one, the Office panel. Click the leaver-rate chart, press Cmd+C or Ctrl+C to copy it, and leave Excel open. Open Lumina-Living-Lab-07-Blank-Deck.pptx from this lab folder — a title slide and nothing else. Open the Claude panel in PowerPoint and ask it to plan the six slides before building anything. Prompt to give Claude:

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

3. Ask Claude to build the slides. It leaves a labelled placeholder where the chart belongs, because the panel works on one file at a time and cannot reach into Excel. Go to that slide, click the placeholder and press Cmd+V or Ctrl+V. Choose Keep Source Formatting so the chart stays linked to your workbook — change a number in Excel and the slide follows. Prompt to give Claude:

   ```text
   Build those six slides into this open presentation.

Keep the title slide as it is and add the six after it.
One message per slide. Use the title you proposed, not a topic word.
Where a slide needs the leaver-rate chart, leave a clearly labelled placeholder box saying which chart goes there — I will paste it from Excel myself.
Put a source note in small text at the bottom of any slide showing a figure, naming the file.
Write three short speaker notes lines per slide.
   ```

4. Method two, Claude Desktop. Open the Claude Desktop app and give it access to this lab folder. Ask it to build the whole deck itself, including the chart. It can read both files at once, so it does not need you to copy anything. Prompt to give Claude:

   ```text
   Read Lumina-Living-Lab-07-People-Numbers.xlsx and Lumina-Living-Lab-07-HR-Brief.docx in this folder.

Build a six-slide people update for the Lumina Living leadership team as a new PowerPoint file called Lumina-Living-Q1-Update-Desktop.pptx in this folder.

Every slide title must state the conclusion, not name a topic. Include the leaver-rate chart from the Analysis sheet on the slide about turnover. Put a source note naming the file under every figure. Add three short speaker notes lines per slide.
   ```

5. Open both decks side by side and compare. Check three things in the Desktop version: is the chart a real chart or a picture, does it still update when you change a number in the workbook, and did every title state a conclusion? Then keep refining whichever deck you prefer with plain prompts until it is right. Save your chosen deck into this lab folder. Prompt to give Claude:

   ```text
   Slide 3 is too crowded. Split it into two slides, keeping one message on each, and renumber the rest. Keep every source note.
   ```


**Test it**

Both decks exist: one built in the panel with the Excel chart pasted in and linked, one named Lumina-Living-Q1-Update-Desktop.pptx built by Claude Desktop. Every title states a conclusion, every figure has a source note, you have written which version keeps the chart linked to the workbook, and at least one refinement prompt was used after the first build.

**Troubleshooting**

- The chart will not paste — Copy it in Excel first, then click into the slide before pasting. Choose Keep Source Formatting to keep the link.
- Claude built slides without the placeholder — Ask again and say explicitly: 'leave a labelled placeholder box where the chart goes; do not draw the chart yourself.'
- Claude Desktop produced a picture, not a chart — That is the finding. Record it — a picture cannot update when the numbers change, which is why the panel method still matters.
- Claude Desktop cannot see the files — Confirm you gave it access to this lab folder, not to a single file.
- A title names a topic — Ask: 'rewrite the title of slide N so it states what we concluded.'

**Challenge**

Create an appendix slide that reconciles every deck KPI to its Excel source cell and owner.

**Reflection**

Which method would you use for a deck you must rebuild every quarter, and why?

> **Note:** The matching detailed lab folder is in labs/lab-07-build-a-leadership-update-in-powerpoint/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


## Topic 04 — Staff Questions, Repeatable Work and Advanced Claude  (23%)

Sorting the HR inbox · one folder, one summary · the weekly update · Skills, connectors and plugins

**Key concepts**

- Sort staff messages by what each one needs: a reply from you, a decision from someone else, or nothing at all.
- Claude drafts the reply; you check the facts, the tone and the recipient, and you are the one who sends it.
- Point Claude Desktop at one folder and it can pull a summary together from everything inside it.
- When two files disagree, that disagreement is the finding. It is not Claude's job to settle it quietly.
- Work you repeat every week is worth automating once, with a backup taken before anything is overwritten.
- An automated update still needs a person to read it before it goes to anyone else.


### Lab 15 — Use the Skill from Word Without Opening Excel

Learning outcome: Invoke a saved skill from Word so it reads the Excel workbook and writes the figures into the document..

Goal: The quarterly update is due and the figures are in a workbook. One short line, and the skill reads the workbook, works the numbers out your way, and writes them into the update.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: Which team should leadership act on first this quarter?
- Evidence: The Q1 staff workbook; The Q1 update document
- Controls: No figure without a source; A person checks before it goes to leadership; Nothing sent automatically

**What you'll build**

A completed quarterly update with figures drawn from the workbook, saved as a final copy.   (Tools: Claude Skills, Claude Desktop, Word, Excel.)

**Prerequisites**

- Lab 3 completed, with the staff-numbers skill saved.
- The Claude Desktop app installed, and Word available.
- Both Lab 04 files in this folder. Everything is local; no work account is needed.

**Process map**

Figures in one file, words in another → Desktop can see both → One short line → Check the figures → Save the final copy

**Step-by-step**

1. Open Lumina-Living-Lab-15-Q1-Update.docx from this lab folder. It is the quarterly people update for the leadership team, with the figures still missing. The staff data is in Lumina-Living-Lab-15-Q1-Staff.xlsx in this same folder — do not open it.
2. Open Claude Desktop and give it access to this lab folder. The Word panel can only see the document you have open; reading a second file needs Desktop. This is the same difference you have seen all course.
3. Ask for the update in one short line. Do not explain the totals, the leaver rate, the formulas or the finding — say none of it. Your skill already knows. Prompt to give Claude:

   ```text
   Check the staff workbook in this folder and add the figures to the Q1 update document.
   ```

4. Read what it produced. Every rule from Lab 3 should be there: totals by team, the leaver rate to one decimal place, the worst team named and explained. Check two figures against the workbook yourself.
5. Notice what Desktop did with the document: it produced a copy for you to download rather than editing the file you had open. Save it into this folder as Lumina-Living-Q1-Update-Final.docx. Write one sentence at the end saying which team leadership should act on first.

**Test it**

The update contains totals by team and the leaver rate to one decimal place, the worst team is named and explained, two figures were checked against the workbook by hand, and a file named Lumina-Living-Q1-Update-Final.docx exists in the folder.

**Troubleshooting**

- Claude cannot see the workbook — Confirm you gave Claude Desktop access to this lab folder, not to a single file.
- The figures do not match the workbook — That is a finding. Ask which cells it used, and check them yourself before trusting the update.
- Claude ignores the skill — Name it: 'Apply my staff-numbers skill.' If it is missing, check the plus menu, Skills.
- Desktop edits nothing — That is expected. Desktop produces a copy to download; save it into this folder yourself.

**Challenge**

Add a stop/go decision rule for the weakest hiring after four weeks of evidence.

**Reflection**

What did you not have to explain this time that you spelled out in the last lab?

> **Note:** The matching detailed lab folder is in labs/lab-15-use-a-skill-across-excel-and-word/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 8 — Sort the HR Inbox and Draft One Reply

Learning outcome: Sort a set of staff messages by what each one needs, and draft one reply for approval..

Goal: Work through a set of fictional staff messages held in a local workbook. Claude sorts them by what each one needs and drafts one reply. Then the Microsoft 365 connector turns that reply into a real Outlook draft — which you review and send yourself.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: Which messages need a reply from HR, and which need someone else to decide?
- Evidence: Staff messages sheet
- Controls: Nothing is sent; No invented dates or entitlements; A named person approves the reply

**What you'll build**

Every message sorted, one reply drafted, the person who would approve it named, and the reply created as an Outlook draft ready for review.   (Tools: Claude for Outlook beta, Outlook categories, thread citations, reply templates, calendar, approval queue.)

**Prerequisites**

- Excel installed, with the Claude panel available from the ribbon.
- Lumina-Living-Lab-08-Staff-Questions.xlsx from this folder.
- No mailbox, no Outlook and no work account are required. Nothing in this lab is sent.

**Files you will use, and what the steps call them**

Every file for this lab is in one folder: labs/lab-08-sort-the-hr-inbox-and-draft-one-reply/ . The steps below name these items in plain English; use this table to find the exact file to open and the exact sheet tab to click at the bottom of the Excel window.

| The steps call it | App | Open this file | Then click |
|---|---|---|---|
| The workbook you complete in this lab | Excel | Lumina-Living-Lab-08-Staff-Questions.xlsx | opens on the first tab |
| The summary view | Excel | Lumina-Living-Lab-08-Staff-Questions.xlsx | the "Summary" tab |
| How this workbook is organised — read this tab first | Excel | Lumina-Living-Lab-08-Staff-Questions.xlsx | the "Read_Me" tab |
| The staff messages you sort | Excel | Lumina-Living-Lab-08-Staff-Questions.xlsx | the "Staff_Messages" tab |
| Where staff information is kept | Excel | Lumina-Living-Lab-08-Staff-Questions.xlsx | the "Where_Info_Is_Kept" tab |
| The review log — where you record who checked the work | Excel | Lumina-Living-Lab-08-Staff-Questions.xlsx | the "Review_Log" tab |

**Process map**

Classify → Summarise with citations → Select approved template → Draft in native form → Review recipients and send

**Step-by-step**

1. Open Lumina-Living-Lab-08-Staff-Questions.xlsx from this lab folder and click the Staff_Messages tab. These are fictional messages from Lumina Living staff. Everything here is local; you will not open Outlook and nothing is ever sent.
2. Open the Claude panel in Excel and ask Claude to sort the messages. Read the answer on screen. Prompt to give Claude:

   ```text
   Read the messages on the Staff_Messages sheet in this open workbook. Sort them into four groups: needs a reply from HR today, needs a decision from someone else, is just information, and needs nothing. Give your reason and say which Message_ID you mean for each one. Do not change the sheet.
   ```

3. In the Action column of the Staff_Messages tab, write the group you agree with for each message.
4. Pick one message that needs a reply and ask Claude to draft it. Read the draft on screen. Prompt to give Claude:

   ```text
   Draft a short reply to the message I have selected on the Staff_Messages sheet. Use only what that message and this workbook actually say. Keep it under 120 words, say clearly what happens next and who is doing it, and write 'need to check' rather than inventing any date, amount or entitlement. Show me the draft. Do not send anything and do not change the workbook.
   ```

5. Now put the reply into Outlook. Open Claude Desktop, where you connected Microsoft 365 in Lab 0, and ask it to create the draft. It creates a draft only — nothing is sent, and you are still the one who presses Send. If your connector is not available, record it and read the draft you wrote in Excel instead; the approval lesson is the same. Prompt to give Claude:

   ```text
   Using the Microsoft 365 connector, create a draft reply in Outlook to the message I chose on the Staff_Messages sheet.

Use the reply I wrote in the Draft_Reply column, exactly as it stands. Do not reword it.
Address it to the sender of that message only. Use the original subject with 'Re:' in front.

Create it as a draft. Do not send it. Tell me where to find it when you are done.
   ```


**Test it**

Every message has an answer in the Action column, one reply under 120 words is written in the Draft_Reply column, its approver is named, and the reply exists as an unsent draft in Outlook or the connector state is recorded. Nothing was sent.

**Troubleshooting**

- You expected to open Outlook to read the messages — The messages are in the workbook so the lab runs on any computer. Outlook is used only at the end, to create the draft.
- The connector is not available — Record it and stop at the Excel draft. Every earlier step works without Outlook.
- Claude reworded my reply — Ask again and say 'use the text exactly as it stands, do not reword'. The point is that you approve the words, not Claude.
- Claude sent the message — It should not. The prompt says create a draft and do not send. If it sent, report it and check the recipient immediately.
- Claude invents a figure or a date — Re-run the prompt; it instructs Claude to write 'need to check' instead of inventing.

**Challenge**

Create an escalation rule for messages that contain a financial commitment, legal interpretation or personal data.

**Reflection**

Which part of email handling should remain human even if drafting becomes nearly automatic?

> **Note:** The matching detailed lab folder is in labs/lab-08-sort-the-hr-inbox-and-draft-one-reply/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 9 — Read a Whole Folder and Write the Summary

Learning outcome: Have Claude read across a folder of HR files and write one summary, reporting what the files disagree on rather than resolving it..

Goal: A quarter's worth of HR reports sits in one folder as PDFs, with a CSV of the numbers. No single file answers the question. Claude reads them all and writes one summary, naming the file behind every claim.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: What does the HR head need to know this week?
- Evidence: HR files in this folder
- Controls: Only files in this folder; Every claim names its file; Disagreements reported, not resolved

**What you'll build**

A two-page people summary built only from the folder, naming the file behind every claim, with disagreements reported rather than settled.   (Tools: Claude Cowork, work folder, Projects, plugins, Microsoft 365 connector, multi-step execution, approvals.)

**Prerequisites**

- Lab 0 completed, so Claude Desktop is installed and signed in.
- The hr-quarter-files folder from this lab folder: three PDF reports and a CSV.
- No work account or connector is needed. Everything is read from your own computer.

**Process map**

Scope the folder → Connect approved context → Plan the task → Watch and steer → Review files in Microsoft 365

**Step-by-step**

1. Open the hr-quarter-files folder inside this lab folder. It holds what an HR team actually receives in a quarter: three reports as PDFs — headcount, exit interview themes and the hiring pipeline — plus a CSV of team numbers. Skim them. No single file answers the question 'how are our people doing?', and you cannot edit a PDF to find out.
2. Open the Claude Desktop app. Select the plus button, then Add files or photos, and give it access to this lab folder. The Office panel can only see one open file; Desktop can read the whole folder at once, which is what this job needs.
3. Ask Claude to read across the folder first, before writing anything. Read what it found, and pay attention to the last part of the answer. Prompt to give Claude:

   ```text
   Read every file in the hr-quarter-files folder here. There are three PDF reports and a CSV.

For each file tell me: its name, what it covers, and which question about our people it helps answer.

Then tell me anything the files disagree on, or any point one file raises that the others miss. Name the file behind every point. Do not change any file.
   ```

4. The files do not fully agree. The headcount report says total headcount is 88; add up the CSV and see what you get. The exit interview note also warns that flexible working will not fix the warehouse problem, which the headcount report does not mention. Claude should have surfaced both. If it did not, ask it directly what the numbers add up to.
5. Now ask for the summary. Check two figures against the CSV yourself, then write at the end of the summary which claims you verified and which still need the Head of HR to confirm. Prompt to give Claude:

   ```text
   Using only the files in the hr-quarter-files folder, write a two-page people summary for the Head of HR.

Cover: where headcount stands against plan, why people are leaving, and what the hiring pipeline looks like.

Take numbers from the CSV and the headcount report, and wording from the notes. Name the file and section behind every claim.

Where two files disagree, say so and give both figures — do not pick one. Where the files say nothing, write 'need to check'.

Save it as Lumina-Living-People-Summary.docx in this folder.
   ```


**Test it**

The summary covers headcount against plan, why people are leaving and the hiring pipeline; every claim names its file; the disagreement between the headcount report and the CSV is reported with both figures; two figures were checked by hand; and the closing note says what still needs the Head of HR to confirm.

**Troubleshooting**

- Claude cannot see the files — Give it access to this lab folder, not to a single file. Use the plus button, then Add files or photos.
- Claude picked one figure and moved on — That is the finding. Ask it directly: 'what does the CSV add up to, and does that match the headcount report?'
- The summary cites a file that does not exist — Ask it to list the exact file names it used, and compare them with the folder.
- Claude resolved a contradiction on its own — The prompt requires it to report both figures. Re-run it and say so again — an AI that quietly picks a number is the risk this lab is about.

**Challenge**

Turn the approved hand-off workflow into a reusable Cowork skill outline with explicit inputs, checks and approval points.

**Reflection**

Which mattered more here: what the files said, or what they disagreed about?

> **Note:** The matching detailed lab folder is in labs/lab-09-read-a-folder-and-write-a-summary/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 11 — Build a Daily HR Routine with Cowork

Learning outcome: Turn a week of scattered HR work into a repeatable daily routine, and let Cowork run it across your files..

Goal: Ten things landed on the HR desk this week. Cowork finds what actually repeats, writes a daily routine, applies it back to the week, and produces the Monday brief. No terminal, no scripts.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: What should the HR daily routine be, and who owns each step?
- Evidence: This week's HR inbox; The empty routine sheet
- Controls: No invented owners or deadlines; Gaps recorded rather than filled; Head of HR reads the brief before it is acted on

**What you'll build**

A written daily routine covering inbox, reporting and chasing; this week's work assigned an owner and a deadline; and today's daily HR report.   (Tools: Claude Cowork, Claude Desktop, Excel, Word.)

**Prerequisites**

- Lab 0 completed, so Claude Desktop is installed and signed in.
- Cowork available in Claude Desktop. It is on paid plans; if you do not have it, watch the trainer and follow along in the workbook.
- Lumina-Living-Lab-11-This-Week.xlsx from this folder. Everything is local; no terminal and no scripts.

**Process map**

A week of scattered work → Find what repeats → Write the routine → Apply it to the week → Run it: today's report

**Step-by-step**

1. Open Lumina-Living-Lab-11-This-Week.xlsx from this lab folder and look at the This_Week sheet. Ten things landed on the HR desk this week — new starters, leavers, leave requests, probation reviews and questions. Three columns are empty. Doing this by hand every week is the problem this lab solves.
2. Open Claude Desktop and switch to Cowork. Give it access to this lab folder so it can work across the files. Ask it to look at the week and find the work that actually repeats. Prompt to give Claude:

   ```text
   Read Lumina-Living-Lab-11-This-Week.xlsx in this folder and look at the This_Week sheet.

It lists everything that landed on the HR desk this week: new starters, leavers, leave requests, probation reviews and questions.

Group them by what kind of work they are, and tell me which ones happen every single week no matter what. Those are the ones worth turning into a routine. Do not change the sheet yet.
   ```

3. Ask Cowork to design the daily routine and write it into the workbook. Notice the three things it must include: checking the inbox, producing the daily report, and chasing what is overdue. Those are the jobs that happen every day whatever else lands. Prompt to give Claude:

   ```text
   Now design the daily HR routine from that list.

Write it into the Daily_Routine sheet of the same workbook, one row per step.

It must include these three things, because they happen every day whatever else does:
- checking the HR inbox and sorting what came in
- the daily report to the Head of HR
- chasing anything that has passed its deadline

For each row give: when it happens, what to do in one plain sentence, where the information is (name the sheet or file), and who checks it before anything goes out.

Keep it to work that genuinely repeats. Anything that happened only once this week is not a routine.
   ```

4. Now ask it to apply that routine back to this week's list. Every row should get an action, an owner and a deadline — or be marked as not covered yet, which tells you the routine has a gap. Prompt to give Claude:

   ```text
   Using the routine you just wrote, fill in the three empty columns on the This_Week sheet for every row: what must happen, who owns it, and by when.

Base the owner and the deadline on the routine, not on guesswork. Where the routine does not cover something, write 'not in the routine yet' rather than inventing an owner.
   ```

5. Finally, ask Cowork to run the routine and produce today's report. Open it, check two items against the workbook, and decide whether you would send it to the Head of HR as it stands. This is the routine working: the same report, the same way, every morning. Prompt to give Claude:

   ```text
   Using the routine, produce today's daily HR report as a new Word document called Lumina-Living-Daily-HR-Report.docx in this folder.

Three short sections:
- What came in today, from the This_Week sheet
- What is due or overdue, with the owner named
- What needs a decision from the Head of HR

Name the row behind every item. Where something has no owner, say so plainly rather than filling the gap. Keep it to one page — it is read standing up.
   ```


**Test it**

The Daily_Routine sheet covers checking the inbox, the daily report and chasing overdue items, each with when, what, where and who. Every row of This_Week has an action, an owner and a deadline, or is marked as not covered. Lumina-Living-Daily-HR-Report.docx exists, fits one page, and names the row behind every item.

**Troubleshooting**

- Cowork is not in Claude Desktop — It is available on paid plans. If it is missing, do the same steps in a normal Claude Desktop conversation with folder access — the routine is the point, not the mode.
- Cowork cannot see the workbook — Give it access to this lab folder, not to a single file.
- It invented an owner — Ask again and say 'write not in the routine yet where the routine does not cover something'. An invented owner is worse than an admitted gap.
- The routine includes one-off work — Ask it to remove anything that happened only once this week. A routine is what repeats.

**Challenge**

Add a dry-run flag that reports proposed cell changes and mail-query scope without writing any output.

**Reflection**

Which part of your own week would still work if you were away tomorrow?

> **Note:** The matching detailed lab folder is in labs/lab-11-build-a-daily-hr-routine-with-cowork/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 12 — Automate an HR Pipeline with a Project

Learning outcome: Set up a Claude project that holds the HR team's materials and rules, then run a repeatable pipeline inside it..

Goal: A project keeps the policy library, the staff data and the house rules in one workspace. Set it up once, then run the new starter pipeline twice without attaching a file or restating a rule.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: Can the new starter workflow run the same way every time?
- Evidence: The policy library; The staff workbook; The quarter files
- Controls: Only project materials used; Every fact names its file; Nothing sent without sign-off

**What you'll build**

A Lumina Living HR project with materials and standing instructions, and a new starter pipeline run twice from it.   (Tools: Claude Projects, Claude Desktop, project instructions, uploaded materials.)

**Prerequisites**

- Lab 0 completed, so Claude Desktop is installed and signed in.
- Labs 5, 6 and 9 completed, so you have the materials to upload.
- Projects available in your Claude plan. If it is missing, follow the trainer and use a normal conversation with folder access.

**Process map**

Create the project → Upload the materials → Set the standing rules → Run the pipeline → Run it again in one line

**Step-by-step**

1. Open Claude Desktop and select Projects in the sidebar, then New project. Name it Lumina Living HR. A project is a workspace that remembers its materials and its rules, so you stop re-uploading and re-explaining the same things every time.
2. Upload the materials the HR team works from. Take them from the earlier lab folders: the three policy PDFs from Lab 5's hr-policy-library, the staff workbook from Lab 6, and the quarter files from Lab 9. This is the HR team's shared context, in one place.
3. Set the project instructions. In the project, open its settings and paste the text below into the custom instructions. These are the standing rules for everything the project produces — the same rules you have been typing into every prompt so far. Prompt to give Claude:

   ```text
   You are working as part of the Lumina Living HR team.

Whenever you produce anything for this project:
- Use only the materials uploaded to this project. Never invent a date, an amount, a notice period or an entitlement.
- Name the file and section behind every fact.
- Where the materials are silent, write 'need to check' instead of guessing.
- Never state a legal conclusion. Flag it for review instead.
- Plain English, short sentences.
- Nothing is sent, published or approved without a named person signing it off.
   ```

4. Now run a real HR pipeline inside the project. Start a new conversation in it and ask for the new starter workflow. Notice what you did not have to do: no files attached, no rules restated. Prompt to give Claude: ```text Using only the materials in this project, run the new starter pipeline for Rachel Sim, who starts in Online on 3 March. Produce, in order:
5. A checklist of everything HR must do before her first day, with the owner for each item
6. A short welcome note to her, in our house tone
7. A one-line entry for the daily HR report saying what is still outstanding Name the file behind every rule you apply. Where the materials do not cover something, say 'need to check' rather than filling the gap. ```
8. Run it again for a second new starter, in one line. The project holds the materials and the rules, so the pipeline repeats itself. Check both outputs name their source files, then decide which parts of this you would let run without a person reading it first. Prompt to give Claude:

   ```text
   Now run the same pipeline for Terrence Wong, who starts in Office on 10 March. Do not ask me for the rules again.
   ```


**Test it**

A project named Lumina Living HR exists with the policy PDFs, the staff workbook and the quarter files uploaded, and custom instructions set. The new starter pipeline produced a checklist with owners, a welcome note and a report line for two different starters, every fact naming its source file, with gaps marked 'need to check'.

**Troubleshooting**

- Projects is not in the sidebar — It depends on your Claude plan. Follow the trainer demonstration; the idea of standing context still applies.
- Claude ignores the project instructions — Open the project settings and check they saved. Instructions apply to new conversations in the project, not to ones started outside it.
- It used a file that is not in the project — Ask it to list the files it used. Anything outside the project is a finding.
- The second run asked for the rules again — Check you started the conversation inside the project, not in a new window.

**Challenge**

Write a second Skill for a task you repeat every week, and give it to a colleague to run.

**Reflection**

Which is more valuable for your own team: a saved method, or a shared workspace?

> **Note:** The matching detailed lab folder is in labs/lab-12-automate-an-hr-pipeline-with-a-project/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 10 — Draft an Outlook Reply with Claude in Chrome

Learning outcome: Use Claude for Chrome to draft a reply inside Outlook on the web, review it, and send it yourself..

Goal: Claude in Chrome works on the page in front of you. Open a staff message in Outlook web, have Claude draft the reply into the real compose box, check it, and decide whether it goes.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: Is this reply accurate enough to send, and who approves it?
- Evidence: The open staff message; The Lumina Living handbook
- Controls: Manual approval mode only; No invented dates or entitlements; A person presses Send

**What you'll build**

A reviewed reply drafted in Outlook on the web, sent only after you approved it or deliberately left in Drafts.   (Tools: Claude for Chrome, Outlook on the web, per-action approval.)

**Prerequisites**

- Lab 0 completed, with Claude for Chrome installed, pinned and set to Manually approve.
- Google Chrome. Claude for Chrome does not work in other browsers.
- Outlook on the web, signed in with your training account.
- If Chrome or the extension is unavailable, follow the trainer demonstration and record it; Lab 8 covers the same reply work locally.

**Process map**

Open Outlook in Chrome → Open the message → Claude drafts into the reply box → Check it in Outlook → You press Send

**Step-by-step**

1. Open Google Chrome and sign in to Outlook on the web with your training account. Open the Claude for Chrome side panel — you installed and pinned it in Lab 0. Check the permission mode says Manually approve, never Skip all approvals.
2. Open one staff message that needs a reply. Use a message from your own training mailbox, or the trainer will point you at one. Claude in Chrome reads the page you are looking at, so the message must be open on screen before you ask for anything.
3. Type the request into the Claude panel on the right of your browser window — the Claude for Chrome side panel, not the Outlook message box. When Chrome asks whether Claude may act on this page, choose Allow for this action only. Watch the draft appear in the Outlook compose window: not in the panel, but in the real reply box. Prompt to give Claude:

   ```text
   Draft a reply to the message that is open in Outlook.

Use only what that message and the Lumina Living handbook actually say. Keep it under 120 words, plain English.

Say clearly what happens next and who is doing it. Where you do not have a fact — a date, an amount, an entitlement — write 'need to check' rather than inventing one.

Leave the draft open in Outlook. Do not send it.
   ```

4. Read the draft in Outlook itself, not in the chat. Check the recipient, the subject, and every fact. Then ask Claude to check its own work before you commit to anything. Prompt to give Claude:

   ```text
   Before I send this, check it for me.

Tell me: is the recipient right, does anything in the reply state a rule the handbook does not contain, and is there any figure or date you cannot trace?

Do not change the draft. Just tell me what you find.
   ```

5. You decide what happens next. If the reply is right and the trainer approves it, press Send yourself. If anything is wrong, correct it in Outlook or leave it in Drafts. Claude drafted it; you are the one who sends it, and that has been true in every lab on this course.

**Test it**

A reply was drafted into the Outlook compose box, the recipient and every fact were checked, anything unsupported is marked 'need to check', and the message was either sent after approval or deliberately left in Drafts. Permission mode stayed on Manually approve throughout.

**Troubleshooting**

- Claude cannot see the message — Refresh the Outlook tab and make sure the message is open on screen. Claude in Chrome reads the visible page.
- Chrome did not ask for approval — Check the permission mode in the side panel. It must be Manually approve; never use Skip all approvals on a real mailbox.
- The draft appeared only in the chat — Ask again and say 'draft it into the Outlook reply box, not here'.
- Claude invented an entitlement — That is the finding. Correct it, and note that the same rule applies here as in every other lab: no fact without a source.
- The extension will not install — It needs Chrome and a paid plan. Record it and watch the trainer; Lab 8 teaches the same review discipline without a browser.

**Challenge**

Name one HR question you could only answer if Claude could see the whole team's files, not just yours.

**Reflection**

What would have to be true before you let a reply go out without reading it?

> **Note:** The matching detailed lab folder is in labs/lab-10-draft-outlook-replies-with-chrome/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 13 — Add Skills and Connectors to the Project

Learning outcome: Bring your saved skill and the Microsoft 365 connector into the HR project, so one request runs the whole workflow..

Goal: The project holds the materials and the rules. Add the hr-policy-draft skill so it knows your method, and the Microsoft 365 connector so it can reach real files and mail. Then run the full HR workflow end to end.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: Which parts of the HR workflow can run from one request, and which must stay manual?
- Evidence: The HR project materials; The hr-policy-draft skill; Microsoft 365 through the connector
- Controls: Read-only connector use; Every fact names its source; Nothing sent without a named approver

**What you'll build**

An HR project with materials, standing rules, a skill and a connector, running one request that produces a policy draft, a summary and an Outlook draft.   (Tools: Claude Projects, Claude Skills, Microsoft 365 connector, Cowork.)

**Prerequisites**

- Lab 12 completed, with the Lumina Living HR project set up.
- Lab 5 completed, so the hr-policy-draft skill exists.
- Lab 0 completed, with the Microsoft 365 connector connected — or recorded as unavailable, in which case the local files still work.

**Process map**

Materials and rules → Add the skill → Add the connector → Run the whole workflow → Decide what stays automatic

**Step-by-step**

1. Open the Lumina Living HR project you built in Lab 12. Check its materials and instructions are still there. You are about to give it two more things: a method, and reach beyond its own uploads.
2. Add your skill to the project. In the project, open the plus menu, then Skills, and enable hr-policy-draft — the skill you created in Lab 5. The project now knows both what to work on and how you want it written.
3. Add the Microsoft 365 connector. In Claude Desktop, open Customize > Connectors and confirm Microsoft 365 is connected. Inside the project, ask Claude what it can now reach. If the connector is unavailable, record it and continue with the uploaded materials only. Prompt to give Claude:

   ```text
   What materials and tools do you have access to in this project? List the uploaded files, any skills that are enabled, and whether you can reach Microsoft 365. Do not use any of them yet.
   ```

4. Now run the whole workflow from one request. Watch how many separate steps it does without you moving between apps. Prompt to give Claude: ```text Using this project, run the March HR workflow for me. Do three things in order:
5. Draft the flexible working policy section, applying my hr-policy-draft skill
6. Write a short summary of where headcount stands, from the uploaded quarter files
7. Prepare a draft email to the Head of HR with both attached for review, and leave it unsent Name the file behind every fact. Where the materials are silent, write 'need to check'. Do not send anything. ```
8. Read all three outputs. Check the policy follows your skill's rules, the summary names its files, and the email is a draft and nothing more. Then write down which of these three steps you would let run unattended tomorrow morning, and which you would always read first. That judgment is what you take back to work.

**Test it**

The project has the hr-policy-draft skill enabled and the connector state recorded. One request produced a policy draft following the skill's rules, a headcount summary naming its source files, and an unsent Outlook draft. Nothing was sent, and you have written which steps may run unattended and which always need a person.

**Troubleshooting**

- Skills is not available inside the project — Check the skill exists in Settings > Skills. If skills are not on your plan, paste the rules from Lab 5's standard into the project instructions instead.
- The connector is not reachable — Record it and run the workflow on the uploaded materials alone. Nothing in this lab depends on the connector working.
- Claude did all three steps but skipped the citations — Ask again and name the rule: 'name the file behind every fact'. A project's instructions apply, but a long request can still drift.
- It sent the email — It should not. The request says leave it unsent. If it sent, check the recipient immediately and report it — that is exactly why the approval gate exists.

**Challenge**

Remove the skill from the project, run the same request, and compare the policy draft.

**Reflection**

Now that one request can do three jobs, what would you want to see before you trusted it unattended?

> **Note:** The matching detailed lab folder is in labs/lab-13-add-skills-and-connectors-to-the-project/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 14 — Upload a Shared Skill for Slides

Learning outcome: Import a slide standard written by someone else, so every HR deck in the team looks the same..

Goal: Your company has a house standard for decks, written once and shared as a file. Upload it as a skill and apply it to a weak draft deck.

**Company use case**

- Department: Human Resources
- Sponsor: Head of HR
- Decision: Should the deck standard be shared as one file everyone imports?
- Evidence: The house deck standard file; The draft deck in this folder
- Controls: Keep the company slide master; Source note under every figure; Flag any figure that cannot be traced

**What you'll build**

An uploaded deck-design-standard skill, and a rebuilt deck where every title states a conclusion.   (Tools: Claude Skills, Claude for PowerPoint, Upload a skill.)

**Prerequisites**

- Lab 7 completed, so you have built a deck by hand.
- PowerPoint installed, with the Claude panel available from the ribbon.
- A Claude account you can sign in to on claude.ai. Skills is available on paid plans.
- Lumina-Living-Lab-14-Draft-Deck.pptx and deck-design-standard.md from this folder.

**Process map**

A standard written once → Upload it → Apply it to a weak deck → Compare with your own version → Choose the right method

**Step-by-step**

1. Open Lumina-Living-Lab-14-Draft-Deck.pptx from this lab folder. It is a six-slide HR update where every title names a topic instead of stating a conclusion. Your company has a house standard for decks, and it has been shared with you as a file.
2. Open deck-design-standard.md from this lab folder and read it. This is a skill written by someone else — the same rules you applied by hand in Lab 7, written down once for the whole team.
3. In the Claude panel, select the plus button, then Skills, then Manage skills. On claude.ai select Add, then choose Upload a skill, and upload deck-design-standard.md. This is how a team shares one standard instead of everyone writing their own.
4. Go back to PowerPoint. Select the plus button, then Skills, then /deck-design-standard. Watch every slide title change from a topic to a conclusion, and a source note appear under each figure. Prompt to give Claude:

   ```text
   /deck-design-standard
   ```

5. Compare the deck with the version you built by hand in Lab 7. Write one sentence in the speaker notes of slide 1: which of the three ways of creating a skill — writing the instructions, letting Claude create it, or uploading one — you would use for your own team, and why.

**Test it**

The deck-design-standard skill was uploaded from the supplied file, running it changed every slide title to a conclusion and added source notes, the slide master is unchanged, and slide 1's speaker notes say which of the ways of creating a skill you would use and why.

**Troubleshooting**

- Upload a skill will not accept the file — It expects a Markdown file. Use deck-design-standard.md exactly as supplied.
- The skill changed the slide master — Undo, and check the standard file says to keep the master. A shared skill is only as safe as its rules.
- Titles still name topics — Ask it to rewrite only the titles, and quote the rule from the standard back to it.

**Challenge**

Pick one weekly HR task and decide whether it needs a plugin, a Skill, or just a clear request.

**Reflection**

When is uploading someone else's standard better than writing your own?

> **Note:** The matching detailed lab folder is in labs/lab-14-upload-a-shared-skill-for-slides/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


## Wrap-Up — One Governed Company Workflow

You have built a connected Lumina Living planning and management pack rather than a collection of isolated AI demonstrations.

**Business outputs**

- Hiring plans, people plans and staff policy drafts that use company templates and named reviewers.
- A financial analysis and dashboard with dynamic formulas, controls and management-ready visuals.
- An editable executive deck with native charts, a coherent decision story and source notes.

**Operating controls**

- A permission and source map, prompt contract, review log and human approval boundary.
- An Outlook triage-and-draft pattern that does not silently send mail.
- A scoped Cowork workflow and a Claude Code daily-brief automation with explicit tool approvals.

---


## Next Steps

- Re-run the full Lumina Living flow and verify that every figure and recommendation remains consistent across files.
- Adapt one activity to an approved recurring process in your organisation and define a baseline for time, quality and review effort.
- Ask your Microsoft 365 and Claude administrators which add-ins, connectors, write tools and Cowork surfaces are approved for your role.
- Keep prompts, source registers, decision logs and approval evidence with the final work product.


## Glossary

- **Claude for Microsoft 365** — Anthropic's in-app assistants for Word, Excel, PowerPoint and Outlook.
- **Microsoft 365 connector** — A delegated connection that lets Claude work with authorised SharePoint, OneDrive, Outlook and Teams context.
- **Claude Cowork** — Anthropic's task-oriented desktop mode for multi-step work across scoped files and connected tools.
- **Copilot Cowork** — A separate Microsoft 365 Copilot experience with Microsoft licensing, governance, Work IQ and action approvals.
- **Claude Code** — Anthropic's command-line agent that can work with local files, scripts and approved MCP connectors.
- **MCP** — Model Context Protocol, a standard that lets Claude connect to approved tools and data sources.
- **Delegated permission** — Access exercised on behalf of the signed-in user and limited by that user's existing permissions.
- **Write tool** — A connector capability that can create or update content and therefore needs stronger consent and review.
- **Evidence chain** — The trace from a claim or chart back to its source file, cell, message or approved assumption.
- **Human send gate** — The required user review and approval before an email, invitation or other consequential action is sent.
- **Claude in Chrome** — Anthropic's Chrome extension for reading and acting on approved websites through a permission-controlled browser side panel.


## References and Further Learning

- Claude for Microsoft 365 overview: https://claude.com/claude-for-microsoft-365
- Claude for Microsoft 365 add-ins overview: https://claude.com/docs/office-agents/overview
- Use Claude for Word: https://claude.com/docs/office-agents/word
- Use Claude for Outlook: https://claude.com/docs/office-agents/outlook
- Get started with Claude in Chrome: https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome
- Claude in Chrome permissions guide: https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide
- Use Claude in Chrome safely: https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely
- Set up the Microsoft 365 connector: https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector
- Connect to Microsoft 365: https://support.claude.com/en/articles/15183774-connect-to-microsoft-365
- Use Claude for Microsoft 365 with third-party platforms: https://claude.com/docs/office-agents/third-party-platforms
- Get started in Claude Cowork in three steps: https://claude.com/resources/tutorials/get-started-in-claude-cowork-in-three-steps
- Connect Claude Code to tools via MCP: https://code.claude.com/docs/en/mcp
- Copilot Cowork overview: https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
- Microsoft 365 Copilot with Anthropic models: https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-anthropic-apps
- Syracuse University: Claude Microsoft 365 connector: https://its.syr.edu/your-work-apps-meet-your-ai-assistant-using-claudes-microsoft-365-connector/
- Claude for Microsoft 365 setup and use cases: https://justinmckelvey.com/blog/claude-for-microsoft-365
