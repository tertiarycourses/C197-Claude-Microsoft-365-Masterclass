# Lab 2 — Connect Claude to Your Microsoft 365 Files and Apps

**Topic 01:** Getting Started with Claude for Microsoft 365  |  **Day 1**  |  **Approx. 25 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Scenario

Lumina Living is a small home-and-lifestyle retailer. The quarter has just closed and your manager needs the Q3 business-review pack — a short written report, the numbers behind it, a slide deck for the management meeting, and the emails that send it out — by the end of the day. You have a rough brief, a sales workbook and a handful of facts to work from. Across this course you use Claude alongside Microsoft 365 to turn that raw material into a finished, checked pack. Use this scenario only if you cannot use real, non-confidential work of your own; your own material is always preferred.

## Goal

Give Claude your working files by uploading and pasting, and keep them together in a Project.

## What you'll build

A Claude Project (or a single well-prepared chat) holding your Q3 files, with Claude confirmed to have read them.

**Tools and techniques:** Claude Projects, file upload, custom instructions, connectors (optional)

## Prerequisites

- Lab 1 complete — you are signed in to Claude and have your renamed 'Lumina Living Q3' chat.
- The sample 'Lumina Living — Q3 Sales.xlsx' workbook and the Q3 brief to hand (or your own non-confidential equivalents).
- Microsoft 365 with Excel, so you can open and compare the workbook.
- Chrome or Edge, signed in — or the Claude desktop app.

## Steps

### Step 1

Attach a file to the chat: click the paperclip (or drag the file in) and upload the sample 'Lumina Living — Q3 Sales.xlsx' workbook. Claude accepts Word, Excel, PowerPoint, PDF, CSV and images.

### Step 2

Confirm Claude has read it, and check the answer against the file itself.

Prompt to give Claude (paste into the chat):

```text
From the workbook I just uploaded, list the column headings and tell me how many rows of data there are.
```

### Step 3

Create a Project to hold the whole task (if your plan has Projects): open Projects > New project, name it 'Lumina Living — Q3 Review', and add both the brief and the workbook to it. If you do not have Projects, keep working in your renamed Lab 1 chat and re-attach files as needed.

### Step 4

Give the Project standing instructions so every chat starts the same way. Put this in the Project's custom instructions.

Prompt to give Claude (paste into the Project's custom instructions):

```text
You are helping me prepare Lumina Living's Q3 business review. Use only the files in this project. Keep a professional, concise tone. When you give figures, show where in the data they come from so I can check them.
```

### Step 5

Optional — connect a source instead of uploading: if your account offers connectors, open Settings > Connectors and connect OneDrive, SharePoint or Google Drive, then point Claude at the folder. Skip this if your account does not offer it.

### Step 6

Prove the context works: start a fresh chat inside the Project and ask a question without re-attaching anything.

Prompt to give Claude (paste into the chat):

```text
Without me re-uploading, what files do you have for this review, and what is in each?
```

### Step 7

Confirm Claude answers from the Project's files. Your working set is now connected and reusable.

## Test it

Claude has correctly listed the workbook's columns and row count, your Q3 files sit in a Project (or a prepared chat), and a fresh chat can answer from them without re-uploading.

## Troubleshooting

- **You don't have Projects on your plan.** Projects and custom instructions are paid-plan features. Use the fallback: keep working in your renamed 'Lumina Living Q3' chat from Lab 1, re-attach the brief and workbook whenever you start a related chat, and paste the standing-instructions text (Step 4) at the top of each new chat so Claude begins with the same context.
- **The upload is rejected.** Check the file is a supported type (Word, Excel, PowerPoint, PDF, CSV or image) and within the size limit — a very large workbook may be refused. Trim it to the sheet you need, or save the key sheet as a CSV and upload that instead.
- **The Connectors option isn't offered.** Connectors to OneDrive, SharePoint or Google Drive are only available on supported plans and must be enabled by an admin on a work account. If it is not there, skip Step 5 entirely — uploading the files does the same job for this course.

## Challenge

Add one more file to the Project — for example a short PDF of last quarter's headline numbers — and ask Claude to point out which figures in the Q3 workbook it can and cannot compare against. This gives your connected Lumina Living Q3 pack a like-for-like reference for later analysis.

## Reflection

LO2 — Give Claude your working files by uploading and pasting, and keep them together in a Project. In your own words, how will you use this in your own work, and how will you check Claude got it right?

## Deliverable

Save your work — this connected Project of Q3 files becomes the shared source for the connected **Lumina Living Q3 review pack**, the single deliverable you complete and send in Lab 8.

---

*Claude Microsoft 365 Masterclass (C197) · C197 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
