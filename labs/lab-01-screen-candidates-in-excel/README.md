# Lab 1 — Shortlist Candidates with AI Experience

**Topic 01:** Getting Claude Ready for HR Work  |  **Day 1**  |  **Approx. 20 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update.

Twenty-four people applied for HR roles. Claude fills in the shortlist directly in your Excel sheet, you check its decisions, then you run the same request in the Claude Desktop app and see that it hands you a downloaded copy instead of editing your file.

## Goal

Use Claude to shortlist job applicants, and see the difference between the Excel panel and the Claude Desktop app.

## What you'll build

A saved shortlist in your own workbook, a second copy saved from the Desktop app, and one sentence on which way suits work that must stay in one file.

**Tools and techniques:** Claude for Word, Claude Skills, natural-language skill creation

## Company use case

- **Department:** Human Resources
- **Sponsor:** Head of HR
- **Business challenge:** Add one more rule to the skill that matters in your own organisation.
- **Decision:** What are our rules for HR wording, and can we make them stick?
- **Evidence:** The staff handbook in this folder
- **Measures:** Section drafted; Method corrected; Skill saved
- **Controls:** No invented dates or entitlements; No legal conclusions; Legal review before release

## Files in this lab folder

- `README.md`
- `TRAINER-GUIDE.md`
- `Lumina-Living-Lab-01-Candidates.xlsx`
- `templates/Lab-01-Trainer-Demonstration-Guide.docx`

## Prerequisites

- Excel installed, with the Claude panel available from the ribbon.
- The Claude Desktop app installed on your own computer.
- Lumina-Living-Lab-01-Candidates.xlsx from this folder. No work account is needed and nothing is stored in the cloud.

## Trainer delivery plan

**Lab 01 is a 20-minute demonstration and guided practice. It is not a prompt-contract exercise.**

| Time | Trainer action | What to teach | Learner evidence |
|---|---|---|---|
| 0–3 min | Explain | Show the three routes and the simple rule: add-in for an open Office item, connector for authorised Microsoft 365 search, Chrome for the Outlook web exercise. | Learners name the three routes. |
| 3–6 min | Demonstrate | Open one Office app and show Home/Tools > Add-ins. Install only if classroom policy permits. | Learners record Ready, Not available or Admin approval required. |
| 6–10 min | Demonstrate | In Claude Desktop show Customize > Connectors > Add > Browse, then the Microsoft 365 connection screens. | Learners connect only when consent is already approved; otherwise they record Admin approval required. |
| 10–17 min | Coach | Help learners install/pin Claude in Chrome, use Manual approval and draft the Outlook reminder. | Learners review the live draft and send only after explicit trainer approval. |
| 17–20 min | Check | Verify Sent Items or Drafts and initial the completed checklist. | Learners submit one completed Lab01_Checklist. |

### Before class

- Confirm the training mailbox and trainer-approved recipient before class.
- Prepare one Office app with Home/Tools > Add-ins visible; the supplied screenshots do not show this route.
- Use the five connector screenshots and two Outlook screenshots when those live demonstrations are unavailable.
- Decide whether learners may send the reminder; if not, the correct outcome is Left in Drafts.

### Do not teach in Lab 01

- Do not teach prompt architecture or reusable review templates; that starts in Lab 03.
- Do not require learners to deploy tenant add-ins or grant organisation consent.
- Do not teach Claude Cowork, Microsoft 365 Copilot or a multi-file decision matrix in this lab.

## Process map

Ask for it your way → Correct until right → Save it in one sentence → Check it is listed → Stop repeating yourself

## Steps

### Step 1

Open Lumina-Living-Lab-01-Candidates.xlsx from this lab folder and click the Candidates tab. It lists 24 people who applied for HR roles at Lumina Living. Read a few of the Experience notes and see how long it would take you to find the right people by hand. The last two columns, Shortlist and Why, are empty. Claude is about to fill them in.

### Step 2

Open the Claude panel in Excel: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac. Type the request below. Watch the two columns fill in on the sheet, then press Cmd+S or Ctrl+S to save. Your own file now holds the shortlist.

**Prompt to give Claude:**

```text
I am shortlisting people for an HR job. Only shortlist someone if they have actually used an AI tool at work.

On the Candidates sheet, fill in two columns for all 24 rows:
- In the Shortlist column, write Yes or No.
- In the Why column, copy the words from the Experience notes that made you decide.

Write Yes only if the notes show they used an AI tool in their job.
Write No if the notes show no AI tool, or if they only studied AI or attended a course.

Do not change any other column.
```

### Step 3

Check what Claude decided. Row C-011 attended an AI course and row C-013 is studying for a certificate. Neither has used an AI tool at work, so both should be No. Rows C-006, C-012 and C-017 say 'piloted', 'trialled' and 'experimented with' — you decide whether trying something at work counts as using it. Type over any row you disagree with.

### Step 4

Now open the Claude Desktop app, give it access to this lab folder, and type exactly the same request again. Watch what happens: it reads your workbook and offers a filled copy to download rather than typing into the sheet you have open. Select Download and open, then File > Save As into this folder as Lumina-Living-Lab-01-Candidates-Desktop.xlsx.

**Prompt to give Claude:**

```text
I am shortlisting people for an HR job. Only shortlist someone if they have actually used an AI tool at work.

On the Candidates sheet, fill in two columns for all 24 rows:
- In the Shortlist column, write Yes or No.
- In the Why column, copy the words from the Experience notes that made you decide.

Write Yes only if the notes show they used an AI tool in their job.
Write No if the notes show no AI tool, or if they only studied AI or attended a course.

Do not change any other column.
```

### Step 5

Open both files side by side. They hold the same shortlist but they are two separate files, and only the first is the one the hiring manager opens. Write one sentence at the bottom of your original sheet: if the shortlist must stay in one agreed file, which of the two would you use, and why?

## Test it

All 24 rows have Yes or No with a quoted reason and the file is saved, rows C-011 and C-013 are marked No, a second file named Lumina-Living-Lab-01-Candidates-Desktop.xlsx exists in the folder, and you have written which of the two ways keeps the shortlist in one agreed file.

## Troubleshooting

- **Claude does not save the skill.** Say it plainly: 'Save that as a skill called hr-draft.' If nothing happens, try /skillify instead.
- **Skills is not in the plus menu.** Skills is available on paid Claude plans. Record it and keep the written method to reuse by hand in the next lab.
- **Claude states a legal conclusion.** Correct it before you save. Whatever you save is what you get every future time.

## Challenge

Explain in one sentence which route you would choose for work on an open Word document and which route you would choose to search authorised Microsoft 365 content.

## Reflection

Which of your corrections would have been most costly to leave out?

## Deliverable

A saved shortlist in your own workbook, a second copy saved from the Desktop app, and one sentence on which way suits work that must stay in one file.

## Current product references

- [Claude for Microsoft 365 overview](https://claude.com/claude-for-microsoft-365)
- [Claude for Microsoft 365 add-ins overview](https://claude.com/docs/office-agents/overview)
- [Use Claude for Word](https://claude.com/docs/office-agents/word)
- [Use Claude for Outlook](https://claude.com/docs/office-agents/outlook)
- [Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)
- [Claude in Chrome permissions guide](https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide)
- [Use Claude in Chrome safely](https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely)
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
