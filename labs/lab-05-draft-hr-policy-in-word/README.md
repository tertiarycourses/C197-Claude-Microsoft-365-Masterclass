# Lab 5 — Build an HR Policy Skill from Your Real Policies

**Topic 02:** Hiring Plans, Policies and Staff Documents  |  **Day 1**  |  **Approx. 25 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update.

Your house style already exists in the policies you have published and the template you write them into. Hand Claude the examples, the rules and the template, turn that into a skill, then draft two new policies from a real consultation note.

## Goal

Create a skill from your company's existing policy documents, then use it to draft new policy wording that matches them.

## What you'll build

An hr-policy-draft skill built from your real policy library and template, and two new policies on the company letterhead.

**Tools and techniques:** Claude Skills, Upload a skill, Claude for Word

## Company use case

- **Department:** Human Resources
- **Sponsor:** Head of HR
- **Business challenge:** Add a fourth policy to the library, rebuild the skill, and see whether the wording improves.
- **Decision:** What can we publish now, and what must go to legal first?
- **Evidence:** HR brief; Existing staff handbook
- **Measures:** Sections drafted; Points sent for legal advice; Gaps marked
- **Controls:** Policy, practice and legal advice kept separate; No legal conclusions stated; Legal review before release

## Files in this lab folder

- `Lumina-Living-Lab-05-HR-Brief.docx`
- `Lumina-Living-Lab-05-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-05-Working-Workbook.xlsx`
- `Lumina-Living-Lab-05-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Labs 1 to 4 completed.
- Word installed, with the Claude panel available from the ribbon.
- A Claude account you can sign in to on claude.ai or in Claude Desktop. Skills is available on paid plans.
- The hr-policy-library folder, how-we-write-hr-policy.md, templates/HR-Policy-Template.docx and Lumina-Living-Lab-05-HR-Consultation-Note.docx from this folder.

## Process map

Define boundary → Verify metrics → Draft narrative → Separate policy from procedure → Obtain specialist approval

## Steps

### Step 1

Open the hr-policy-library folder inside this lab folder. It holds three approved Lumina Living policies as PDFs: annual leave, notice period and probation. Open one and see how it is written — company letterhead, four numbered sections, every gap marked, approval table at the end. Then open Lumina-Living-Lab-05-HR-Consultation-Note.docx: this is your source, and it separates what the management team has agreed from what is still open.

### Step 2

Open Claude Desktop or go to claude.ai and start a new conversation. Attach how-we-write-hr-policy.md, all three PDFs from hr-policy-library, and templates/HR-Policy-Template.docx. Then ask Claude to build the skill. It learns your house style from real examples and the layout from your own template.

**Prompt to give Claude:**

```text
I am attaching four things from our HR folder: how-we-write-hr-policy.md, three approved policies from our policy library, and our blank HR-Policy-Template.docx.

Create a skill called hr-policy-draft that I can use whenever I draft HR policy wording for staff.

Base it on all of them:
- the rules in the markdown file
- the way the three approved policies are actually written: their four-part structure, their tone, and how they cross-reference each other by name in single quotes
- the blank template, which is the layout every new policy must follow, including the letterhead, the version and approver line, and the approval table at the end

The skill must always produce policy wording that drops straight into that template. Keep every rule. Do not simplify them.
```

### Step 3

Check it saved. Open Settings > Skills and confirm hr-policy-draft is listed with you as the author. Read what Claude wrote: does it capture the four sections, the rule about marking gaps, and the template layout? Add anything it missed — you own the standard, not Claude.

### Step 4

Open templates/HR-Policy-Template.docx from this lab folder and immediately save a copy into the lab folder as Flexible-Working-Policy.docx. Close every other Word window, so this copy is the only document open — the Claude panel writes into whichever document is active, so having the brief open as well will confuse it. Now open the Claude panel: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac.

**Prompt to give Claude:**

```text
Apply my hr-policy-draft skill and write the flexible working policy into this open document.

This document is our blank HR policy template. Fill in the policy name, the four numbered sections and the approval table. Keep the letterhead exactly as it is.

Take the source material from sections 2 and 3 of Lumina-Living-Lab-05-HR-Consultation-Note.docx, in this same folder. Section 2 is what has been agreed; section 3 lists what is still open. Every point in section 3 must appear under 'Still to confirm' rather than being decided by you.
```

### Step 5

Check it: the letterhead is untouched, the four sections are filled, every fact names the heading it came from, gaps are marked 'need to check', no legal conclusion is stated, and the approval table is still there. Put it beside a policy from hr-policy-library — it should look like one of them. Save. Then make a second copy of the template, call it Leave-Carry-Over-Policy.docx, close the first one, and draft again in one line.

**Prompt to give Claude:**

```text
Apply my hr-policy-draft skill and write the leave carry-over policy into this open document, the same way. Keep the letterhead, fill the four sections and the approval table, and take the source material from sections 4 and 5 of Lumina-Living-Lab-05-HR-Consultation-Note.docx in this folder.
```

## Test it

A skill named hr-policy-draft is listed in Settings > Skills, both new policies use the company letterhead and the four numbered sections, every fact traces to the consultation note, every open point from the note appears under 'Still to confirm', no legal conclusion is stated, the approval table is intact, and both files are saved in the lab folder.

## Troubleshooting

- **Claude says it is bound to the wrong document.** The Word panel writes into whichever document is active. Close every other Word window, leave only your copy of the template open, and ask again.
- **Claude will not attach the PDFs.** Attach how-we-write-hr-policy.md on its own and paste one policy's text into the conversation as an example.
- **Skills is not in the menu.** Skills is available on paid Claude plans. If it is missing, paste the rules from how-we-write-hr-policy.md into your request each time.
- **The letterhead disappeared.** Undo with Ctrl+Z or Cmd+Z. Ask again and say 'keep the letterhead exactly as it is' — a skill only protects what its rules mention.
- **A legal conclusion appears.** That breaks the standard. Correct it, and add the rule to the skill so it cannot recur.

## Challenge

Add a methodology-change disclosure showing how a revised conversion factor affects comparability.

## Reflection

What did Claude learn from the example policies that the written rules alone did not say?

## Deliverable

An hr-policy-draft skill built from your real policy library and template, and two new policies on the company letterhead.

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
