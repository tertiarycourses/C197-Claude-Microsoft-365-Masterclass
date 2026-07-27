# Claude Microsoft 365 Masterclass (C197) — Learner Guide

**Course Code:** C197  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 27 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Getting Started with Claude for Microsoft 365  (50%)](#topic-01--getting-started-with-claude-for-microsoft-365--50)
  - [Lab 1 — Get Started with Claude for Microsoft 365](#lab-1--get-started-with-claude-for-microsoft-365)
  - [Lab 2 — Connect Claude to Your Microsoft 365 Files and Apps](#lab-2--connect-claude-to-your-microsoft-365-files-and-apps)
  - [Lab 3 — Write Effective Prompts for Everyday Work Tasks](#lab-3--write-effective-prompts-for-everyday-work-tasks)
  - [Lab 4 — Use AI Responsibly, Securely and Privately at Work](#lab-4--use-ai-responsibly-securely-and-privately-at-work)
- [Topic 02 — Boosting Productivity Across Microsoft 365 with Claude  (50%)](#topic-02--boosting-productivity-across-microsoft-365-with-claude--50)
  - [Lab 5 — Write, Rewrite and Summarise in Word](#lab-5--write-rewrite-and-summarise-in-word)
  - [Lab 6 — Analyse and Explain Data in Excel](#lab-6--analyse-and-explain-data-in-excel)
  - [Lab 7 — Generate Slide Outlines and Content for PowerPoint](#lab-7--generate-slide-outlines-and-content-for-powerpoint)
  - [Lab 8 — Draft and Reply to Email in Outlook and Teams](#lab-8--draft-and-reply-to-email-in-outlook-and-teams)
- [Wrap-Up](#wrap-up)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies the Claude Microsoft 365 Masterclass (C197) course, conducted by Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 8 hands-on labs, in the order you will run them, together with the concepts each lab depends on.

The labs build one connected result. You take the role of a coordinator at a small retailer, 'Lumina Living', preparing the quarter's business-review pack, and use Claude alongside Microsoft 365 to write the report in Word, analyse the numbers in Excel, build the slides in PowerPoint, and draft the emails that send it in Outlook and Teams — checking Claude's work at every step. Wherever you can, use your own non-confidential work so you leave with skills applied to your own job; the supplied Lumina Living sample material is provided for everyone to follow along.


## Course Learning Outcomes

- LO1: Explain what Claude is and how it works alongside Microsoft 365, and set up Claude ready for work.
- LO2: Connect Claude to your Microsoft 365 files and apps by uploading, pasting and using Projects and connectors.
- LO3: Write clear, effective prompts that get accurate, usable results for everyday work tasks.
- LO4: Apply AI responsibly, securely and privately — knowing what to share, what to withhold and what to verify.
- LO5: Use Claude to write, rewrite and summarise documents in Microsoft Word.
- LO6: Use Claude to analyse and explain data, and to build formulas, for Microsoft Excel.
- LO7: Use Claude to generate slide outlines and content for Microsoft PowerPoint.
- LO8: Use Claude to draft and reply to messages in Microsoft Outlook and Teams.


## Before You Start — Preparation

**What you need**

- A laptop (Windows or Mac) with a current Chrome or Edge browser.
- A Claude account at claude.ai (a free account is enough to follow every lab; a paid plan adds Projects and larger uploads — the trainer confirms what your account has on the day).
- Microsoft 365 with Word, Excel, PowerPoint and Outlook (desktop or the web apps at office.com), and access to Microsoft Teams.
- The sample 'Lumina Living — Q3 Review' files (a Word brief, an Excel sales workbook and a short slide starter) — the trainer shares a link; make your own copies — or your own non-confidential documents.

**Verify your setup**

Before Lab 1, confirm you can sign in to claude.ai, start a new chat, and open Word, Excel, PowerPoint and Outlook. If Claude or any Office app is not available on your account, tell the trainer.

```bash
Sign in at claude.ai  ·  start a New chat  ·  open Word / Excel / PowerPoint / Outlook  ·  download the sample Lumina Living files
```

**Conventions used in every lab**

- Placeholders such as <YOUR FILE> or <YOUR NAME> are replaced with your own values.
- Prompts you give Claude are shown in a shaded box — paste them into the Claude chat, attaching the file named in the step where one is used.
- App paths (e.g., Word > Home > Editor, or File > Info) and menu names are written as you will use them; Claude's own buttons may move over time.
- Every lab ends with a 'Test it' step — verify Claude's result against a source you can confirm before you move on.


## Topic 01 — Getting Started with Claude for Microsoft 365  (50%)

Introduction to Claude & Microsoft 365 · Connecting Claude to your files and apps · Effective prompting for work tasks · Responsible, secure and private use of AI

**Key concepts**

- Claude — Anthropic's AI assistant that reads, writes, analyses and explains in plain language, available at claude.ai and in the Claude desktop app.
- Claude alongside Microsoft 365 — Claude is a separate assistant you feed your Word, Excel, PowerPoint and Outlook content into, then paste its results back; it complements the Office apps you already use.
- Two ways to give Claude your work — upload a file (Word, Excel, PowerPoint, PDF, CSV, images) or paste the text or table directly into the chat.
- Projects — a Claude workspace that keeps your files and custom instructions together, so every chat about the same task starts with the right context.
- Connectors — an optional way to let Claude read from your cloud storage (such as OneDrive, SharePoint or Google Drive) where your account and plan support it.
- Effective prompting — a good work prompt states the role, the context, the task and the output format, so Claude has no room to guess.
- Human in the loop — Claude drafts; you decide. Always read, check and edit its output before it becomes your work.
- Responsible use — keep confidential and personal data out of prompts unless your organisation has approved it, and verify anything you will rely on.


### Lab 1 — Get Started with Claude for Microsoft 365

Learning outcome: Sign in to Claude, understand how it works alongside Microsoft 365, and run a first prompt on your task..

Goal: This lab gets Claude working for you. You sign in at claude.ai, start a new chat, and paste in the Q3 brief so Claude can summarise your task and list what the review pack needs — so you see the ask-check loop before you rely on it. BUILDING BLOCK — what you do in this lab becomes part of your Lumina Living Q3 review pack, the single deliverable you write, analyse, present and send across all 8 labs.

**What you'll build**

A working Claude account with your first, verified answer — a plain-language summary of the Q3 task and a checklist of what the pack must contain.   (Tools: claude.ai (or the Claude desktop app), Microsoft 365, a web browser.)

**Step-by-step**

1. Sign in at claude.ai (or open the Claude desktop app) and click 'New chat'. This is where you will work with Claude all day.
2. Open the sample 'Lumina Living — Q3 Review Brief' (a short Word document the trainer shares), or use a short brief of your own non-confidential work.
3. Copy the brief's text and paste it into the Claude chat with this instruction so Claude tells you what the task involves.

   ```bash
   Here is the brief for a quarterly business review. In plain language, summarise what I am being asked to produce, then list the separate items the final pack should contain.
   ```

4. Read Claude's answer. Check it against the brief: does its list match what the brief actually asks for? Add anything it missed.
5. Ask one follow-up so you see Claude reason over your material.

   ```bash
   For each item in that list, say which Microsoft 365 app I would use to produce it — Word, Excel, PowerPoint or Outlook.
   ```

6. Confirm the ground rule: Claude has only read text you gave it, and nothing has changed in your files. Claude drafts; you decide what to keep.
7. Save this chat — rename it 'Lumina Living Q3'. You now have Claude set up and a clear, checked picture of the task.

**Test it**

You are signed in to Claude, and you have a first answer — a summary of the Q3 task and a checklist of the pack's items — that you have checked against the brief and corrected where needed.

> **Note:** Full commands and screenshots are in labs/lab-01-*.md. Use only documents and data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Lumina Living sample material if in doubt. Claude's screens, menu names and buttons may differ slightly between accounts and plans and may change over time; the trainer will point out the current location on the day.

---


### Lab 2 — Connect Claude to Your Microsoft 365 Files and Apps

Learning outcome: Give Claude your working files by uploading and pasting, and keep them together in a Project..

Goal: Now you give Claude your real material to work on. You upload the Q3 brief and the sales workbook, gather them into a Project with standing instructions, and confirm Claude can read what you gave it — so every later chat starts with the right context. BUILDING BLOCK — what you do in this lab becomes part of your Lumina Living Q3 review pack, the single deliverable you write, analyse, present and send across all 8 labs.

**What you'll build**

A Claude Project (or a single well-prepared chat) holding your Q3 files, with Claude confirmed to have read them.   (Tools: Claude Projects, file upload, custom instructions, connectors (optional).)

**Step-by-step**

1. Attach a file to the chat: click the paperclip (or drag the file in) and upload the sample 'Lumina Living — Q3 Sales.xlsx' workbook. Claude accepts Word, Excel, PowerPoint, PDF, CSV and images.
2. Confirm Claude has read it, and check the answer against the file itself.

   ```bash
   From the workbook I just uploaded, list the column headings and tell me how many rows of data there are.
   ```

3. Create a Project to hold the whole task (if your plan has Projects): open Projects > New project, name it 'Lumina Living — Q3 Review', and add both the brief and the workbook to it. If you do not have Projects, keep working in your renamed Lab 1 chat and re-attach files as needed.
4. Give the Project standing instructions so every chat starts the same way. Put this in the Project's custom instructions.

   ```bash
   You are helping me prepare Lumina Living's Q3 business review. Use only the files in this project. Keep a professional, concise tone. When you give figures, show where in the data they come from so I can check them.
   ```

5. Optional — connect a source instead of uploading: if your account offers connectors, open Settings > Connectors and connect OneDrive, SharePoint or Google Drive, then point Claude at the folder. Skip this if your account does not offer it.
6. Prove the context works: start a fresh chat inside the Project and ask a question without re-attaching anything.

   ```bash
   Without me re-uploading, what files do you have for this review, and what is in each?
   ```

7. Confirm Claude answers from the Project's files. Your working set is now connected and reusable.

**Test it**

Claude has correctly listed the workbook's columns and row count, your Q3 files sit in a Project (or a prepared chat), and a fresh chat can answer from them without re-uploading.

> **Note:** Full commands and screenshots are in labs/lab-02-*.md. Use only documents and data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Lumina Living sample material if in doubt. Claude's screens, menu names and buttons may differ slightly between accounts and plans and may change over time; the trainer will point out the current location on the day.

---


### Lab 3 — Write Effective Prompts for Everyday Work Tasks

Learning outcome: Compare a vague prompt with a specific one and capture a reusable four-part prompt pattern for work tasks..

Goal: A result is only as good as the prompt. You run a vague prompt, then a specific one that states the role, context, task and output format, see the difference, and distil what worked into a reusable pattern you will use for the rest of the course. BUILDING BLOCK — what you do in this lab becomes part of your Lumina Living Q3 review pack, the single deliverable you write, analyse, present and send across all 8 labs.

**What you'll build**

A written four-part prompt pattern (Role · Context · Task · Output) and one strong, tested prompt saved for reuse.   (Tools: Prompt design, role/context/task/output, refinement.)

**Step-by-step**

1. Run a deliberately vague prompt in the Project and note how generic the answer is.

   ```bash
   Write something about our sales.
   ```

2. Now run a specific prompt for the same intent and compare the result.

   ```bash
   You are my business analyst. Context: this is Lumina Living's Q3 sales workbook. Task: write three short paragraphs summarising how the quarter went for a management audience. Output: plain paragraphs, no jargon, with the key figure named in each.
   ```

3. Write down the four parts that made the second prompt work: the Role, the Context, the Task, and the Output format.
4. Capture your reusable pattern where you can find it — a notes doc, or pinned in the Project.

   ```bash
   ROLE: who Claude should act as | CONTEXT: which file/task | TASK: what to produce | OUTPUT: format, length, tone, and what to include
   ```

5. Add the conditions that keep results trustworthy: name the file, ask Claude to show where figures come from, and state the length and tone you need.
6. Rewrite one request of your own about the Q3 pack using the pattern, and run it.
7. Refine once: change the Output part (for example 'make it half as long', or 'more formal') and re-run to see the result change. Keep the better version.
8. Save your best prompt in the Project — you will reuse this pattern in every remaining lab.

**Test it**

You can show two answers for the same intent (vague vs specific), a written four-part prompt pattern, and one refined prompt that produced the output you specified in the format you asked for.

> **Note:** Full commands and screenshots are in labs/lab-03-*.md. Use only documents and data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Lumina Living sample material if in doubt. Claude's screens, menu names and buttons may differ slightly between accounts and plans and may change over time; the trainer will point out the current location on the day.

---


### Lab 4 — Use AI Responsibly, Securely and Privately at Work

Learning outcome: Decide what is safe to share with AI, and write a personal safe-use checklist you apply to the review pack..

Goal: Before you rely on AI at work, you set the rules. You review what should never go into a prompt, practise removing sensitive details before sharing, confirm that Claude's output must always be verified, and write a safe-use checklist you apply to your own material. BUILDING BLOCK — what you do in this lab becomes part of your Lumina Living Q3 review pack, the single deliverable you write, analyse, present and send across all 8 labs.

**What you'll build**

A personal safe-use checklist, and one prompt you have rewritten to remove sensitive data before sending.   (Tools: Data privacy, redaction, verification, safe-use checklist.)

**Step-by-step**

1. List the kinds of data that should not go into an AI prompt without approval: passwords and keys, customer names and contact details, staff personal data, unreleased financials, and anything under NDA.
2. Practise redacting: take a sentence that names a real customer and rewrite it to make the same request safely.

   ```bash
   Rewrite this so it asks the same question without naming anyone: 'Summarise why customer Tan Wei Ming from 12 Orchard Road cancelled his order.'
   ```

3. Ask Claude for good practice, then sanity-check its advice against your own organisation's policy.

   ```bash
   What should I avoid putting into an AI prompt when working with real company data, and how can I get the same help safely?
   ```

4. Confirm the verification rule with a quick test: ask Claude for a specific figure from the workbook, then check it in Excel — never accept a number you cannot tie back to the source.

   ```bash
   What was the single best-selling product in the Q3 workbook, and what was its total sales value? Tell me which cells you used.
   ```

5. Note who is accountable: Claude drafts, but you are responsible for what you send. Decide where you will record that AI helped (for example a note in the document's properties).
6. Draft your safe-use checklist — keep confidential data out of prompts; redact before sharing; verify every figure, name and claim; keep a human decision on anything that goes out; record where AI was used.
7. Apply the checklist to your Lab 3 prompt: check it contains nothing sensitive, and adjust it if it does.

**Test it**

You have a written safe-use checklist, a prompt you rewrote to remove a real name, and a figure from the workbook that you verified in Excel before trusting it.

> **Note:** Full commands and screenshots are in labs/lab-04-*.md. Use only documents and data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Lumina Living sample material if in doubt. Claude's screens, menu names and buttons may differ slightly between accounts and plans and may change over time; the trainer will point out the current location on the day.

---


## Topic 02 — Boosting Productivity Across Microsoft 365 with Claude  (50%)

Writing, rewriting & summarising in Word · Analysing & explaining data in Excel · Generating slides for PowerPoint · Drafting & replying to email in Outlook and Teams

**Key concepts**

- Writing in Word — describe the document you need and let Claude draft it, then refine the structure, length and tone with follow-up prompts.
- Rewriting and summarising — paste a long document and ask Claude to shorten it, change its tone, or pull out the key points and actions.
- Analysing data in Excel — upload or paste a table and ask Claude what it shows: totals, trends, comparisons and a plain-language read of the numbers.
- Explaining and building formulas — ask Claude for the Excel formula you need, and paste any formula back to have it explained step by step.
- Generating slides for PowerPoint — turn a document or a brief into a slide-by-slide outline with titles, bullet points and speaker notes.
- Drafting email in Outlook and Teams — draft, reply to and adjust the tone of work messages, keeping them clear, professional and appropriately brief.
- Verify before you send — check every figure, name, date and claim in Claude's output against a source you trust before it leaves your desk.
- One connected workflow — the same review pack flows from Word to Excel to PowerPoint to Outlook, with Claude speeding up each step.


### Lab 5 — Write, Rewrite and Summarise in Word

Learning outcome: Use Claude to draft, restructure and tighten a document, and to summarise a long one, then finish it in Word..

Goal: You produce the written report. You have Claude draft the Q3 review from the brief and the workbook, restructure and shorten it, adjust the tone for a management audience, and summarise a longer background note into key points — pasting the checked result into Word. BUILDING BLOCK — what you do in this lab becomes part of your Lumina Living Q3 review pack, the single deliverable you write, analyse, present and send across all 8 labs.

**What you'll build**

A finished Q3 review report in Microsoft Word, drafted and refined with Claude and checked by you.   (Tools: Microsoft Word, Claude (draft / rewrite / summarise), copy-paste, Word > Home formatting.)

**Step-by-step**

1. In your Project, ask Claude to draft the report from the material it already has.

   ```bash
   Using the brief and the Q3 workbook in this project, draft a one-page business-review report for management. Structure it as: Overview, What sold well, What to watch, and Recommended actions. Name the key figure in each section and say where it comes from.
   ```

2. Read the draft and check every figure it names against the workbook. Mark anything you cannot confirm — you will not keep unverified numbers.
3. Restructure and tighten with a follow-up prompt.

   ```bash
   Good. Now cut it to about 250 words, put the Recommended actions as three bullet points, and make the tone confident but plain — no jargon.
   ```

4. Adjust the tone for the audience if needed (for example more formal, or warmer), then choose the version you will keep.

   ```bash
   Give me the same report in a slightly more formal tone suitable for a board paper.
   ```

5. Summarise a longer input: paste a longer background note (or the brief's appendix) and ask for a short summary you can use as an intro.

   ```bash
   Summarise this background note into four bullet points I can use as context at the top of the report.
   ```

6. Open Microsoft Word, paste your chosen report in, and format it: a title, headings for each section, and the three action bullets (Home > Styles).
7. Do the final human check: re-read the whole page, confirm every figure ties to the workbook, and fix any wording. Save it as 'Lumina Living — Q3 Review Report.docx'.

**Test it**

You have a saved Word report of about 250 words with the four sections and three action bullets, in which every figure has been checked against the Q3 workbook.

> **Note:** Full commands and screenshots are in labs/lab-05-*.md. Use only documents and data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Lumina Living sample material if in doubt. Claude's screens, menu names and buttons may differ slightly between accounts and plans and may change over time; the trainer will point out the current location on the day.

---


### Lab 6 — Analyse and Explain Data in Excel

Learning outcome: Use Claude to analyse a dataset, build the formulas you need, and explain a formula — verifying every figure in Excel..

Goal: You produce the numbers behind the report. You have Claude analyse the Q3 sales workbook, ask it for the Excel formulas to compute the key figures, paste those formulas into Excel to verify them, and have Claude explain an unfamiliar formula — trusting no figure you have not confirmed yourself. BUILDING BLOCK — what you do in this lab becomes part of your Lumina Living Q3 review pack, the single deliverable you write, analyse, present and send across all 8 labs.

**What you'll build**

A verified Q3 analysis in Microsoft Excel — key figures computed by formulas you checked, and one formula you can explain.   (Tools: Microsoft Excel, Claude (analysis / formula generation / formula explanation), SUM, SUMIF, AVERAGE.)

**Step-by-step**

1. Ask Claude to analyse the workbook and surface the figures the report needs.

   ```bash
   From the Q3 sales workbook, give me: total sales for the quarter, the best- and worst-selling product by value, the top region, and the month-by-month trend. Show the figure for each and say which columns you used.
   ```

2. Ask Claude for the exact Excel formula for the headline figure so you can reproduce it.

   ```bash
   Give me the Excel formula to compute total Q3 sales from the Total column, assuming the data is in rows 2 to 500.
   ```

3. In Excel, put that formula in an empty cell and confirm it matches the figure Claude reported.

   ```bash
   =SUM(F2:F500)
   ```

4. Ask for a conditional formula and verify it too — for example sales for the top region.

   ```bash
   Give me an Excel formula that totals the Total column only for rows where the Region column equals "North".
   ```

5. Paste it into Excel and cross-check by filtering the sheet to that region and reading the status-bar Sum.

   ```bash
   =SUMIF(D2:D500,"North",F2:F500)
   ```

6. Learn from a formula: paste an unfamiliar one and ask Claude to explain it step by step.

   ```bash
   Explain, step by step, what this Excel formula does: =IF(F2>500,"Large","Standard")
   ```

7. Set the rule and record the checked figures: never accept a number you cannot tie back to a formula in the sheet. Note the verified headline figures where the report can reuse them.

**Test it**

Your key Q3 figures each match an Excel formula you ran yourself, one conditional total agrees with a filtered status-bar Sum, and you can explain in one sentence what the =IF formula does.

> **Note:** Full commands and screenshots are in labs/lab-06-*.md. Use only documents and data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Lumina Living sample material if in doubt. Claude's screens, menu names and buttons may differ slightly between accounts and plans and may change over time; the trainer will point out the current location on the day.

---


### Lab 7 — Generate Slide Outlines and Content for PowerPoint

Learning outcome: Use Claude to turn the report and analysis into a slide-by-slide outline with titles, bullets and speaker notes..

Goal: You produce the deck for the management meeting. You have Claude turn the checked report and figures into a slide-by-slide outline — titles, three bullets each and short speaker notes — refine the flow and length, then build the slides in PowerPoint from that outline. BUILDING BLOCK — what you do in this lab becomes part of your Lumina Living Q3 review pack, the single deliverable you write, analyse, present and send across all 8 labs.

**What you'll build**

A Q3 review slide deck in Microsoft PowerPoint, built from a Claude-generated outline you refined and checked.   (Tools: Microsoft PowerPoint, Claude (slide outline / speaker notes), Outline view, copy-paste.)

**Step-by-step**

1. Ask Claude to convert your report and verified figures into a slide outline.

   ```bash
   Turn the Q3 review report and the verified figures into a 6-slide deck for a 10-minute management meeting. For each slide give a title, no more than three short bullets, and two lines of speaker notes. Keep every figure consistent with the report.
   ```

2. Read the outline and check the figures on each slide against your verified numbers from Lab 6. Fix any that drift.
3. Refine the flow with a follow-up.

   ```bash
   Reorder so the recommended actions are the final slide, and make the opening slide a single headline that states how the quarter went.
   ```

4. Tighten wording so no bullet runs over one line.

   ```bash
   Shorten every bullet to at most eight words, keeping the meaning.
   ```

5. Build the slides: open PowerPoint, use View > Outline, and paste the titles and bullets so each slide is created from the outline (Tab to demote a line to a bullet).
6. Add the speaker notes: for each slide, paste Claude's two lines into the Notes pane (View > Notes).
7. Do the final human check: click through the deck, confirm every figure matches the report and workbook, then save it as 'Lumina Living — Q3 Review.pptx'.

**Test it**

You have a saved 6-slide PowerPoint deck with a headline opener and an actions closer, one-line bullets, and speaker notes — with every figure consistent with your Word report and Excel analysis.

> **Note:** Full commands and screenshots are in labs/lab-07-*.md. Use only documents and data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Lumina Living sample material if in doubt. Claude's screens, menu names and buttons may differ slightly between accounts and plans and may change over time; the trainer will point out the current location on the day.

---


### Lab 8 — Draft and Reply to Email in Outlook and Teams

Learning outcome: Use Claude to draft, adjust the tone of, and reply to work messages, then send the pack — verifying before it goes..

Goal: The capstone. You send the pack out. You have Claude draft the stakeholder email that carries the review, adjust its tone and length, draft a reply to a likely question, and write a short Teams announcement — checking every detail before anything is sent. BUILDING BLOCK — what you do in this lab becomes part of your Lumina Living Q3 review pack, the single deliverable you write, analyse, present and send across all 8 labs.

**What you'll build**

A ready-to-send Outlook email carrying the Q3 pack, a drafted reply, and a short Teams announcement — all checked by you.   (Tools: Microsoft Outlook, Microsoft Teams, Claude (draft / tone / reply), copy-paste.)

**Step-by-step**

1. Ask Claude to draft the covering email for the management team.

   ```bash
   Draft a short email to the management team introducing the attached Q3 business-review report and slide deck. Say what the quarter's headline was, list the three recommended actions, and ask for comments by Friday. Professional and warm, under 150 words.
   ```

2. Read it and verify: the headline and the three actions must match your report exactly. Fix any drift, and confirm no confidential detail is included.
3. Adjust the tone or length if needed, and keep the version you will send.

   ```bash
   Make it a little more concise and add a one-line thank-you at the end.
   ```

4. Draft a reply to a question you can expect, so you are ready.

   ```bash
   Draft a brief, friendly reply to a manager who asks: 'Can you confirm the total Q3 sales figure and which region led?' Leave placeholders <TOTAL> and <REGION> for me to fill from the verified data.
   ```

5. Fill the placeholders from your verified Lab 6 figures — never from memory — and check they are right.
6. Write a short Teams announcement for the team channel.

   ```bash
   Write a 2-sentence Microsoft Teams message announcing that the Q3 review pack is ready and where to find it, friendly and clear.
   ```

7. Send safely: open Outlook, paste the covering email, attach 'Q3 Review Report.docx' and 'Q3 Review.pptx', check the recipients and the attachments, and only then send. Post the Teams message to the channel.

**Test it**

You have a checked covering email in Outlook with the correct headline, the three matching actions and both files attached; a reply drafted with verified figures; and a short Teams announcement — and you confirmed every figure and name before sending.

> **Note:** Full commands and screenshots are in labs/lab-08-*.md. Use only documents and data you are authorised to use. Never paste passwords, personal identifiers or confidential business data into an AI prompt — use the supplied Lumina Living sample material if in doubt. Claude's screens, menu names and buttons may differ slightly between accounts and plans and may change over time; the trainer will point out the current location on the day.

---


## Wrap-Up

In one day you have taken a quarter's raw material — a brief, a spreadsheet and a handful of facts — and turned it into a finished business-review pack, using Claude alongside Microsoft 365 at every step and checking its work before trusting it.

**What you built**

- Claude set up and connected to your Microsoft 365 files, with a Project holding your review pack.
- A reusable prompt pattern (role, context, task, output) and a personal safe-use checklist.
- A written business-review report in Word, drafted, restructured and tightened with Claude.
- A verified data analysis in Excel — figures, trends and formulas you checked yourself.
- A PowerPoint deck generated as a slide-by-slide outline with titles, bullets and speaker notes.
- A stakeholder email in Outlook and a short Teams announcement, each checked before sending.

**What to do next**

- Point these techniques at one real, recurring task in your own week and measure the time saved.
- Keep verifying: check every figure, name and claim in Claude's output against a source you trust.
- Save your best prompts and your Project so you and your team can reuse them.
- Keep confidential data out of prompts, and note where AI helped so your work stays accountable.

---


## Next Steps

- First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.
- Second pass: rebuild the Word-Excel-PowerPoint-Outlook flow on the sample pack from memory, writing your own prompts.
- Apply the techniques to a real, non-confidential task from your own organisation.
- Review each lab's detailed steps in this guide and re-run the tasks on your own machine.


## Glossary

- **Claude** — Anthropic's AI assistant, used here at claude.ai and in the Claude desktop app to read, write, analyse and explain in plain language.
- **Anthropic** — The company that makes Claude.
- **Microsoft 365** — Microsoft's suite of work apps — including Word, Excel, PowerPoint, Outlook and Teams — used in the browser or as desktop apps.
- **Prompt** — The plain-language instruction you give Claude; a good one states the role, context, task and output format.
- **Project** — A Claude workspace that keeps files and custom instructions together so related chats start with the right context.
- **Connector** — An optional link that lets Claude read from a cloud service such as OneDrive, SharePoint or Google Drive, where your plan supports it.
- **Upload** — Attaching a file (Word, Excel, PowerPoint, PDF, CSV or image) to a Claude chat so Claude can work on its contents.
- **Artifact** — A self-contained document, table or draft Claude produces in a side panel that you can copy or refine.
- **Summarising** — Condensing a long document into its key points, actions or a shorter version.
- **Rewriting** — Changing the wording, tone or length of text while keeping its meaning.
- **Formula** — An Excel instruction (such as =SUM or =IF) that calculates a result from your data.
- **Speaker notes** — The per-slide notes in PowerPoint that guide what you say when presenting.
- **Verification** — Checking that an AI result is correct by comparing it against a source you can confirm yourself.
- **Hallucination** — A confident but wrong AI output; the reason every AI result must be verified before use.
- **Human in the loop** — The practice of a person reviewing and approving AI output before it is relied upon.
