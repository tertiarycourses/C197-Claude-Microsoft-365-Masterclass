# Lab 4 — Write a Hiring Plan in Word

**Topic 02:** Hiring Plans, Policies and Staff Documents  |  **Day 1**  |  **Approx. 20 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update.

Section 2 of the brief lists five roles the teams want and the budget that limits them. Claude works out what fits, writes the plan into your document, then exports it as a standalone document for approval.

## Goal

Write an FY2027 hiring plan in Word using only what the HR brief actually says.

## What you'll build

A hiring plan section written into the brief, and a separate Lumina-Living-FY2027-Hiring-Plan.docx ready for the Head of HR.

**Tools and techniques:** Claude for Word, company templates, evidence checks, human approval

## Company use case

- **Department:** Human Resources
- **Sponsor:** Head of HR
- **Business challenge:** Decide which roles Lumina Living fills in FY2027 and which wait.
- **Decision:** Which roles do we fill now, and which do we hold back?
- **Evidence:** HR brief; Team headcount list; Salary bands; Budget limit
- **Measures:** Roles to fill; Roles held back; Cost against budget; Start dates
- **Controls:** No invented salary figures; Cost stays within budget; Head of HR approves

## Files in this lab folder

- `Lumina-Living-Lab-04-HR-Brief.docx`
- `Lumina-Living-Lab-04-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-04-Working-Workbook.xlsx`
- `Lumina-Living-Lab-04-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Labs 1 to 3 completed.
- Word installed, with the Claude panel available from the ribbon.
- Lumina-Living-Lab-04-HR-Brief.docx from this folder.

## Process map

Read the role table → Work out what fits → Write it into the brief → Check every figure → Export for approval

## Steps

### Step 1

Open Lumina-Living-Lab-04-HR-Brief.docx from this lab folder. Go to section 2 and read the table of five roles the teams have asked for, and the budget line underneath it. In Lab 2 you found the warehouse team is losing people fastest; three of these five roles are warehouse and online replacements. Open the Claude panel in Word.

### Step 2

Ask Claude to work out what fits. Read the answer and check the arithmetic yourself before you go on. Claude answers in the panel only — your document will not change yet. That happens in the next step.

**Prompt to give Claude:**

```text
Using the open Lumina-Living-Lab-04-HR-Brief.docx, look at the table of roles requested for FY2027 in section 2, and at the budget line under it.\n\nTell me which roles we should fill and which we should hold back, so that we stay inside both the budget and the headcount cap.\n\nFor each role give: the team, how many, the salary band from the table, the cost if we fill it, and the reason.\nAdd up the total and show it against the budget and the cap.\nUse the salary bands exactly as written. Do not invent a figure.\n\nShow me your answer here. Do not change the document yet.
```

### Step 3

Now ask Claude to write the plan into the document. This is the step that changes the document. Watch the new section appear after section 3, then press Cmd+S or Ctrl+S to save.

**Prompt to give Claude:**

```text
Now write that hiring plan into the open Lumina-Living-Lab-04-HR-Brief.docx, straight after the section '3. Required management outputs'.\n\nUse the same heading style as the other sections. Call it 'FY2027 hiring plan' and include:\n- Roles to fill: team, how many, salary band, cost, hiring manager\n- Roles to hold back, with the reason\n- Total added monthly cost against the $38,000 budget and the 10-role cap\n- Who approves the plan\n\nTake every figure from the table in section 2 and name the section you took it from. Where the brief says nothing, write 'need to check'.
```

### Step 4

Read the new section. Check every salary against the table in section 2, check the total, and check that anything the brief does not say is marked 'need to check'. Correct anything wrong yourself.

### Step 5

Now ask Claude to pull that section out into a document of its own. This is the version that goes to the Head of HR, without the rest of the brief attached.

**Prompt to give Claude:**

```text
Create a new Word document called Lumina-Living-FY2027-Hiring-Plan.docx in this lab folder.\n\nPut only the 'FY2027 hiring plan' section into it — the roles to fill, the roles to hold back, the cost against budget and the approver. Do not include the rest of the brief.\n\nAdd a short heading at the top: 'FY2027 Hiring Plan — for approval by the Head of HR'. Keep the figures exactly as they are in the brief.
```

## Test it

The brief has an 'FY2027 hiring plan' section after section 3 with every salary matching the table in section 2, the total is shown against the $38,000 budget and the 10-role cap, and a separate file named Lumina-Living-FY2027-Hiring-Plan.docx exists in the folder containing only the plan.

## Troubleshooting

- **Claude says every field needs checking.** Confirm you are looking at section 2 of the Lab 04 brief. The role table with salary bands must be visible in the open document.
- **The total does not match.** Ask Claude to show the arithmetic role by role, then check it against the table yourself.
- **Claude changed the document at step 2.** That step ends with 'do not change the document yet'. Undo with Ctrl+Z or Cmd+Z and run it again exactly as written.
- **The exported plan includes the whole brief.** Ask again, naming only the 'FY2027 hiring plan' section.

## Challenge

Change the budget to $30,000 and ask Claude which role now has to go.

## Reflection

Which role was hardest to hold back, and what evidence would change your mind?

## Deliverable

A hiring plan section written into the brief, and a separate Lumina-Living-FY2027-Hiring-Plan.docx ready for the Head of HR.

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
