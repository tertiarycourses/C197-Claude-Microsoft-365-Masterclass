#!/usr/bin/env python3
"""Replace the steps= block of every lab with a short, local-only sequence.

Design rules agreed with the trainer:
  * 3-5 steps per lab, no more.
  * One lab folder, local files only.  No tenant, no connector, no OneDrive,
    no SharePoint, no sending mail.
  * Every step must produce something the learner can see on screen.
  * Each prompt names the exact open file so it can never dangle.
"""

import re
import sys

# num -> list of (instruction, prompt)
STEPS = {}

STEPS[1] = [
    ("Open Lumina-Living-Lab-01-Surface-Readiness-Workbook.xlsx from this lab folder and click the Lab01_Checklist tab. This one workbook is your whole deliverable for Lab 1.", ""),
    ("Open any Word, Excel or PowerPoint file and open the Claude panel from the ribbon: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac. In the Lab01_Checklist tab, record what you actually see: Ready, Not available or Admin approval required.", ""),
    ("Open the Claude Desktop app and look at Customize > Connectors. Record whether Microsoft 365 appears, and whether it is connected. You are only recording what you see; do not connect anything and do not sign in to a work account.", ""),
    ("With the checklist workbook still open, ask Claude in the Excel panel to review your own entries. Read the answer on screen.", "Review the states I recorded on this Lab01_Checklist sheet. For each row, tell me what work I can and cannot do with that surface today, and which surface I should use for editing a document I already have open. Cite the row. Do not change the sheet."),
    ("Complete every row of Lab01_Checklist and write one sentence at the bottom naming which surface you would use for editing an open document, and which for searching across many files.", ""),
]

STEPS[2] = [
    ("Open Lumina-Living-Lab-02-Working-Workbook.xlsx from this lab folder, then click the Source_Register tab at the bottom of the Excel window. There is no separate 'Source Register' file; it is a tab inside this one workbook. Read its four rows, S01 to S04.", ""),
    ("Open the Claude panel in Excel: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac. Ask Claude to assess the four sources. Read the answer on screen.", "Review the four sources listed on this Source_Register sheet. For each row, state the business risk if Claude were given write access instead of read-only access, and say who should approve that access. Cite the row ID. Do not change the sheet."),
    ("In the Status column of the Source_Register tab, type Read-only or Needs approval for each of the four rows, based on what you just decided.", ""),
    ("Click the Management_Control tab of the same workbook and record the permission map: user group, source, read or write scope, owner and fallback for each of the four sources.", ""),
    ("Ask Claude to check your completed work, then fix anything it flags yourself.", "Compare the Status column on the Source_Register sheet with the Management_Control sheet in this workbook. Point out any source where the recorded status and the permission map disagree, or where an owner is missing. Cite the row ID for every finding. Do not change the workbook."),
]

STEPS[3] = [
    ("Open Lumina-Living-Lab-03-Company-Brief.docx from this lab folder, then open the Claude panel in Word: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac.", ""),
    ("Type this deliberately vague request and read what comes back. Notice that it invents structure and cannot tell you where anything came from.", "Improve our plan."),
    ("Now type the same request as a proper prompt contract. Compare this answer with the previous one.", "Using the open Lumina-Living-Lab-03-Company-Brief.docx, draft a new 'Strategic choices' section for the Executive Committee, placed after '3. Required management outputs'. Preserve the existing Heading 1 styles. For each choice include rationale, owner, measure and Q1 milestone. Use only facts stated in the brief, cite the source heading, and flag anything the brief does not state. Show the proposed text and do not edit the document."),
    ("Open templates/Prompt-and-Review-Template.docx from this lab folder and write down the five parts of the prompt you just used: business result, approved evidence, constraints, output format and approval gate.", ""),
    ("Write one sentence in the template naming the single change that made the second answer more useful than the first.", ""),
]

STEPS[4] = [
    ("Open Lumina-Living-Lab-04-Company-Brief.docx from this lab folder and read section 2, Evidence available. Open the Claude panel in Word.", ""),
    ("Ask Claude to propose the marketing choices from the brief only. Read the answer on screen.", "Using only the open Lumina-Living-Lab-04-Company-Brief.docx, propose three FY2027 marketing choices for Lumina Living and one activity we should not fund. For each choice give the evidence, the target segment, the expected effect, the risk and the measure. Cite the source heading for every claim and flag anything the brief does not state. Show the proposal and do not edit the document."),
    ("Ask Claude to draft the plan into the document, keeping the existing styles.", "Draft an FY2027 marketing plan into the open document using its existing Heading styles. Sections: Executive decision, Priority segments, Channel choices, 90-day campaigns, Measures, Approval. Use only facts stated in this brief, cite the source heading for each claim, and write 'evidence needed' wherever the brief is silent. Show the proposed text before changing the document."),
    ("Read the draft. Delete any recommendation that is not supported by the brief, and check every 'evidence needed' marker.", ""),
    ("Save the reviewed file as Lumina-Living-FY2027-Marketing-Plan-Reviewed.docx inside this lab folder.", ""),
]

STEPS[5] = [
    ("Open Lumina-Living-Lab-05-Company-Brief.docx from this lab folder and open the Claude panel in Word.", ""),
    ("Ask Claude to separate what the brief proves from what it only implies. Read the answer on screen.", "Using only the open Lumina-Living-Lab-05-Company-Brief.docx, list what this brief states as fact, what is an interpretation, and what is an assumption with no evidence. Cite the source heading for each item. Do not edit the document."),
    ("Ask Claude to turn that into a strategy on one page, with an owner and a measure for every choice.", "Draft a one-page FY2027 strategy into the open document using its existing Heading styles. For each strategic choice give the rationale, a named owner role, one measure and a Q1 milestone. Use only facts stated in this brief, cite the source heading, and write 'evidence needed' where the brief is silent. Show the proposed text before changing the document."),
    ("Open templates/Decision-and-Approval-Log.xlsx from this lab folder and record one decision, its owner and the approval status.", ""),
    ("Check that every choice in the strategy has an owner and a measure. Fix any that do not.", ""),
]

STEPS[6] = [
    ("Open Lumina-Living-Lab-06-Company-Brief.docx from this lab folder and open the Claude panel in Word.", ""),
    ("Ask Claude to draft a sustainability reporting section that admits what it cannot evidence. Read the answer on screen.", "Using only the open Lumina-Living-Lab-06-Company-Brief.docx, draft a short sustainability reporting section. For every figure state the reporting boundary, the method and the source. Where the brief does not give a figure, write 'not measured' rather than estimating. Cite the source heading for each claim. Show the proposed text and do not edit the document."),
    ("Ask Claude to draft the HR policy section, keeping policy separate from legal interpretation.", "Using only the open Lumina-Living-Lab-06-Company-Brief.docx, draft a short HR policy section with three parts clearly labelled: policy intent, the operational procedure, and the points that require qualified HR or legal review before release. Do not state legal conclusions. Cite the source heading for each claim. Show the proposed text and do not edit the document."),
    ("Read both drafts. Mark every 'not measured' item and every point flagged for legal review; these are the findings you would take to the source owner.", ""),
    ("Save the reviewed drafts into this lab folder.", ""),
]

STEPS[7] = [
    ("Open Lumina-Living-Lab-07-Working-Workbook.xlsx from this lab folder. Click the Transactions tab to see the source data, then the Assumptions tab. Open the Claude panel in Excel.", ""),
    ("Ask Claude to plan the analysis before it changes anything. Read the answer on screen.", "Look at the tblFinance table on the Transactions sheet and the Assumptions sheet of this open workbook. List the formulas and checks you would use to build an Actual versus Budget comparison by month and channel. Name the source ranges. Do not change the workbook yet."),
    ("Ask Claude to build the analysis with live formulas, not pasted numbers.", "On the Analysis sheet of this open workbook, build a formula-driven Actual versus Budget comparison by month and channel using tblFinance on the Transactions sheet and the Budget sheet. Include Revenue, Gross Profit and Gross Margin. Use native Excel formulas that reference the source ranges. Do not paste hardcoded totals. Keep every assumption on the Assumptions sheet."),
    ("Click into two of the result cells and read the formula bar. Confirm each one references a real range and is not a typed-in number.", ""),
    ("Change one figure on the Assumptions tab and confirm the Analysis sheet updates. Record the check on the Audit_Log tab.", ""),
]

STEPS[8] = [
    ("Open Lumina-Living-Lab-08-Executive-Starter.pptx from this lab folder and look at the slide master. Open the Claude panel in PowerPoint.", ""),
    ("Ask Claude to plan the story before building any slide. Read the answer on screen.", "Using the open Lumina-Living-Lab-08-Executive-Starter.pptx and Lumina-Living-Lab-08-Company-Brief.docx from the same lab folder, propose six conclusion-led slide titles for an Executive Committee decision. Each title must state a conclusion, not a topic. For each slide name the single message and the evidence behind it. Show the outline and do not change any slide."),
    ("Ask Claude to build the deck inside the supplied template.", "Build the six slides you proposed into the open presentation. Keep the existing slide master, layouts, fonts and colours. One message per slide, with a short source note on every slide that shows a figure. Write concise speaker notes. Flag any figure you cannot trace to the company brief."),
    ("Read every slide title aloud. Replace any that names a topic instead of stating a conclusion.", ""),
    ("Save the deck into this lab folder.", ""),
]

STEPS[9] = [
    ("Open Lumina-Living-Lab-09-Working-Workbook.xlsx from this lab folder and click the Inbox tab. These are the fictional Lumina Living messages you will work with. Everything in this lab is local; you will not open Outlook or send anything.", ""),
    ("Open the Claude panel in Excel and ask Claude to triage the inbox. Read the answer on screen.", "Read the messages on the Inbox sheet of this open workbook. Sort them into four groups: needs a reply today, needs a decision from someone else, is only information, and needs no action. Give the reason and cite the Message_ID for every message. Do not change the sheet."),
    ("In the Category column of the Inbox tab, record the group you agree with for each message.", ""),
    ("Pick one message that needs a reply and ask Claude to draft it. Read the draft on screen.", "Draft a short reply to the message I have selected on the Inbox sheet. Use only facts stated in that message and in this workbook. Keep it under 120 words, state clearly what happens next and who owns it, and write 'evidence needed' rather than inventing any figure or date. Show the draft text. Do not send anything and do not change the workbook."),
    ("Paste the reply into the Draft_Reply column and write who would need to approve it before it could be sent.", ""),
]

STEPS[10] = [
    ("Open the Claude Desktop app. Give it access to this lab folder only, so it can read the Lumina Living files on your own computer. Do not connect any cloud account.", ""),
    ("Ask Claude to read across the lab folder and report what it found. Read the answer on screen.", "Read the Lumina Living files in this lab folder. List each file, what it contains, and which planning question it answers. Cite the file name for every point. Tell me what is missing if I need to produce one management brief. Do not change any file."),
    ("Ask Claude to produce the management brief from those files.", "Using only the files in this lab folder, write a two-page management brief for the Executive Committee. Take figures from the workbook, narrative from the Word documents, and cite the file name and location for every material claim. Where the files disagree or are silent, say so instead of resolving it yourself. Save it as Lumina-Living-Management-Brief.docx in this folder."),
    ("Open the brief it produced. Check two cited figures against the workbook yourself.", ""),
    ("Record in the brief which claims you verified and which still need an owner's confirmation.", ""),
]

STEPS[11] = [
    ("Open a terminal in this lab folder and start Claude Code. Everything in this lab runs on your own computer; there is no cloud connector and no email is sent.", "claude"),
    ("Look at inputs/daily-input.csv and inputs/outlook-findings.json in this folder. These are the local stand-ins for today's figures and today's message findings.", ""),
    ("Ask Claude Code to update the workbook from the local input file, taking a backup first.", "Read automation/update_daily_control.py in this folder. Run it so it updates Lumina-Living-Daily-Control.xlsx from inputs/daily-input.csv. Back the workbook up before writing, keep every existing formula intact, and show me what changed before you write anything."),
    ("Ask Claude Code to build the daily brief from the local inputs.", "Run automation/generate_daily_brief.py to produce the daily brief from Lumina-Living-Daily-Control.xlsx and inputs/outlook-findings.json, using templates/Daily-Brief-Template.docx. Cite the workbook cell for every KPI exception and the message ID for every mail finding. Write the result into the outputs folder."),
    ("Open the generated brief in the outputs folder. Confirm the backup exists, the formulas still work, and every figure carries a citation.", ""),
]


def replace_steps(path, nums):
    src = open(path).read()
    for num in nums:
        # Find this activity's dict, then its steps= block.
        anchor = src.index(f"num={num}, topic=")
        start = src.index("steps=[", anchor)
        end = src.index("\n        ],", start) + len("\n        ],")
        body = ["        steps=["]
        for instr, prompt in STEPS[num]:
            body.append(f"            ({instr!r}, {prompt!r}),")
        body.append("        ],")
        src = src[:start - 8] + "\n".join(body) + src[end:]
    open(path, "w").write(src)
    print("Rewrote", path, "labs", nums)


if __name__ == "__main__":
    replace_steps("data_domain1.py", [1, 2, 3])
    replace_steps("data_domain2.py", [4, 5, 6])
    replace_steps("data_domain3.py", [7, 8])
    replace_steps("data_domain4.py", [9, 10, 11])
