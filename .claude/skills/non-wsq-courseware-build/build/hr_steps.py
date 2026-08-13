#!/usr/bin/env python3
"""HR-themed steps for all 11 labs.

Rules: 5 steps, local files only, plain words, every prompt names the file it
needs, every step produces something the learner can see.  Tab names avoid
technical language: Where_Info_Is_Kept, What_Claude_May_Do, Staff_Messages.
"""

STEPS = {}

STEPS[1] = [
    ("Open Lumina-Living-Lab-01-Checklist.xlsx from this lab folder and click the My_Checklist tab. This one workbook is your whole deliverable for Lab 1.", ""),
    ("Open any Word, Excel or PowerPoint file and look for the Claude panel: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac. In My_Checklist, write what you actually see: Works, Not there, or Need IT approval.", ""),
    ("Open the Claude Desktop app and look at Customize > Connectors. Write down whether Microsoft 365 appears in the list. You are only recording what you see; do not connect anything and do not sign in to a work account.", ""),
    ("With the checklist still open in Excel, open the Claude panel and ask it to review what you wrote. Read the answer on screen.", "Look at what I recorded on this My_Checklist sheet. For each row, tell me what HR work I can and cannot do with that option today. Then tell me which one to use when I want to change a document I already have open, and which one to use when my answer needs several files at once. Say which row you mean. Do not change the sheet."),
    ("Finish every row of My_Checklist. At the bottom, write one sentence: which option you would use to edit a document you already have open, and which to look across many files.", ""),
]

STEPS[2] = [
    ("Open Lumina-Living-Lab-02-Staff-Information.xlsx from this lab folder. Click the Where_Info_Is_Kept tab at the bottom of the Excel window. It lists the four places HR keeps staff information. Read the four rows.", ""),
    ("Open the Claude panel in Excel: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac. Type the request below and read the answer. Keep it on screen; you will compare it next.", "Look at the four places listed on this Where_Info_Is_Kept sheet. For each one, tell me what could go wrong if Claude were allowed to change what is stored there instead of only reading it, and who in HR should decide that. Say which row you mean. Do not change the sheet."),
    ("Now open the Claude Desktop app and give it access to this lab folder. Type exactly the same request again. Put the two answers side by side. The Excel panel can only see the sheet in front of it; the Desktop app can read every file in the folder. Write down which answer helped more, and why.", "Look at the four places listed on this Where_Info_Is_Kept sheet. For each one, tell me what could go wrong if Claude were allowed to change what is stored there instead of only reading it, and who in HR should decide that. Say which row you mean. Do not change the sheet."),
    ("Go back to Excel and click the What_Claude_May_Do tab. The four places are already listed. Fill in the empty columns yourself: type 'Read only' or 'Read and change', name who owns it, put a date to review it, and say what you would do if that place were unavailable.", ""),
    ("Ask Claude to check your two tabs against each other, then fix whatever it finds.", "Compare the What_Claude_May_Do sheet with the Where_Info_Is_Kept sheet in this workbook. Tell me any place that has no owner, no read-or-change decision, or where the two sheets disagree. Say which row you mean. Do not change the workbook."),
]

STEPS[3] = [
    ("Open Lumina-Living-Lab-03-HR-Brief.docx from this lab folder, then open the Claude panel in Word: Home > Add-ins > Claude on Windows, or Tools > Add-ins > Claude on Mac.", ""),
    ("Type this vague request and read what comes back. Notice that it invents its own structure and cannot tell you where anything came from.", "Improve our plan."),
    ("Now type the same request properly. Compare this answer with the one before it.", "Using the open Lumina-Living-Lab-03-HR-Brief.docx, write a new 'What we will do' section for the HR leadership team, placed after '3. What we need to produce'. Keep the existing headings exactly as they are. For each action give the reason, who owns it, how we will know it worked, and the date. Use only what this brief actually says, name the heading you took each fact from, and write 'need to check' for anything the brief does not say. Show me the text and do not change the document."),
    ("Open templates/Request-Checklist.docx from this lab folder and write down the five parts of the request you just used: what you wanted, which file to use, what to leave alone, what to show you, and where to stop.", ""),
    ("Write one sentence in that checklist saying which single change made the second answer more useful than the first.", ""),
]

STEPS[4] = [
    ("Open Lumina-Living-Lab-04-HR-Brief.docx from this lab folder and read section 2, 'What we know'. Open the Claude panel in Word.", ""),
    ("Ask Claude to suggest the hiring choices using only the brief. Read the answer on screen.", "Using only the open Lumina-Living-Lab-04-HR-Brief.docx, suggest which roles Lumina Living should fill in FY2027 and one role we should hold back. For each role give the reason it exists, the team, the hiring manager, the target start date and what happens if we do not fill it. Name the heading you took each fact from, and write 'need to check' for anything the brief does not say. Show me the suggestion and do not change the document."),
    ("Ask Claude to write the plan into the document, keeping the headings that are already there.", "Write an FY2027 hiring plan into the open document using the headings it already has. Sections: What we are asking for, Roles to fill, Roles to hold back, Cost, Timing, Who approves. Use only what this brief says, name the heading behind each claim, and write 'need to check' wherever the brief is silent. Show me the text before you change the document."),
    ("Read the draft. Delete any role the brief does not support, and look at every 'need to check' marker.", ""),
    ("Save the reviewed file as Lumina-Living-FY2027-Hiring-Plan-Reviewed.docx inside this lab folder.", ""),
]

STEPS[5] = [
    ("Open Lumina-Living-Lab-05-HR-Brief.docx from this lab folder and open the Claude panel in Word.", ""),
    ("Ask Claude to separate what the brief proves from what it only suggests. Read the answer on screen.", "Using only the open Lumina-Living-Lab-05-HR-Brief.docx, list what this brief states as fact, what is someone's opinion, and what is being assumed with nothing to back it up. Name the heading for each item. Do not change the document."),
    ("Ask Claude to turn that into a one-page plan where every action has an owner and a date.", "Write a one-page people plan into the open document using the headings it already has. For each action give the reason, who owns it, one way to tell if it worked, and the date it is due. Use only what this brief says, name the heading behind each claim, and write 'need to check' where the brief is silent. Show me the text before you change the document."),
    ("Open templates/Decision-Log.xlsx from this lab folder and write down one decision, who owns it and whether it is approved.", ""),
    ("Check that every action on the page has an owner and a date. Fix any that do not.", ""),
]

STEPS[6] = [
    ("Open Lumina-Living-Lab-06-HR-Brief.docx from this lab folder and open the Claude panel in Word.", ""),
    ("Ask Claude to draft the leave policy wording. Read the answer on screen.", "Using only the open Lumina-Living-Lab-06-HR-Brief.docx, draft a short leave policy section with three clearly separate parts: what the policy says, how it works day to day, and the points that need legal advice before we publish. Do not state any legal conclusion yourself. Name the heading behind each claim. Show me the text and do not change the document."),
    ("Ask Claude to draft the flexible-work wording the same way.", "Using only the open Lumina-Living-Lab-06-HR-Brief.docx, draft a short flexible-work section with the same three separate parts: what the policy says, how it works day to day, and the points that need legal advice before we publish. Where the brief gives no rule, write 'not decided yet' instead of inventing one. Show me the text and do not change the document."),
    ("Read both drafts. Mark every 'not decided yet' and every point flagged for legal advice. These are what you would take to the HR head before anything is published.", ""),
    ("Save both reviewed drafts into this lab folder.", ""),
]

STEPS[7] = [
    ("Open Lumina-Living-Lab-07-People-Numbers.xlsx from this lab folder. Click the Staff_List tab to see the people data, then the Assumptions tab. Open the Claude panel in Excel.", ""),
    ("Ask Claude to plan the analysis before it changes anything. Read the answer on screen.", "Look at the Staff_List sheet and the Assumptions sheet in this open workbook. Tell me the formulas and checks you would use to compare actual headcount and staff cost against the plan, month by month and team by team. Name the sheets and columns you would use. Do not change the workbook yet."),
    ("Ask Claude to build the analysis with live formulas, not typed-in numbers.", "On the Analysis sheet of this open workbook, build a comparison of actual headcount and staff cost against plan, by month and by team, using the Staff_List and Plan sheets. Show headcount, staff cost and the gap against plan. Use Excel formulas that point at the source data. Do not type in any total by hand. Keep every assumption on the Assumptions sheet."),
    ("Click into two of the result cells and read the formula bar. Check each one points at real data and is not a number someone typed.", ""),
    ("Change one figure on the Assumptions tab and check the Analysis sheet updates. Write the check on the Checks tab.", ""),
]

STEPS[8] = [
    ("Open Lumina-Living-Lab-08-Leadership-Update.pptx from this lab folder and look at the slide design. Open the Claude panel in PowerPoint.", ""),
    ("Ask Claude to plan the story before building any slide. Read the answer on screen.", "Using the open Lumina-Living-Lab-08-Leadership-Update.pptx and Lumina-Living-Lab-08-HR-Brief.docx from the same folder, suggest six slide titles for an HR update to the leadership team. Every title must say what you concluded, not name a topic. For each slide tell me the single message and what it is based on. Show me the outline and do not change any slide."),
    ("Ask Claude to build those slides inside the supplied template.", "Build the six slides you suggested into the open presentation. Keep the existing slide design, layouts, fonts and colours exactly as they are. One message per slide, and put a short source note under any figure. Write short speaker notes. Tell me about any figure you cannot trace back to the HR brief."),
    ("Read every slide title out loud. Replace any that names a topic instead of saying what you concluded.", ""),
    ("Save the deck into this lab folder.", ""),
]

STEPS[9] = [
    ("Open Lumina-Living-Lab-09-Staff-Questions.xlsx from this lab folder and click the Staff_Messages tab. These are fictional messages from Lumina Living staff. Everything here is local; you will not open Outlook and nothing is ever sent.", ""),
    ("Open the Claude panel in Excel and ask Claude to sort the messages. Read the answer on screen.", "Read the messages on the Staff_Messages sheet in this open workbook. Sort them into four groups: needs a reply from HR today, needs a decision from someone else, is just information, and needs nothing. Give your reason and say which Message_ID you mean for each one. Do not change the sheet."),
    ("In the Action column of the Staff_Messages tab, write the group you agree with for each message.", ""),
    ("Pick one message that needs a reply and ask Claude to draft it. Read the draft on screen.", "Draft a short reply to the message I have selected on the Staff_Messages sheet. Use only what that message and this workbook actually say. Keep it under 120 words, say clearly what happens next and who is doing it, and write 'need to check' rather than inventing any date, amount or entitlement. Show me the draft. Do not send anything and do not change the workbook."),
    ("Paste the reply into the Draft_Reply column and write down who would need to approve it before it could be sent.", ""),
]

STEPS[10] = [
    ("Open the Claude Desktop app. Give it access to this lab folder only, so it can read the Lumina Living HR files on your own computer. Do not connect any cloud account.", ""),
    ("Ask Claude to read across the folder and tell you what is there. Read the answer on screen.", "Read the Lumina Living HR files in this folder. List each file, what is in it, and which people question it helps answer. Name the file for every point you make. Then tell me what is missing if I need to write one summary for the HR head. Do not change any file."),
    ("Ask Claude to write the summary from those files.", "Using only the files in this folder, write a two-page people summary for the HR head. Take numbers from the workbook and wording from the Word documents, and name the file and section behind every claim. Where the files disagree or say nothing, tell me instead of deciding for yourself. Save it as Lumina-Living-People-Summary.docx in this folder."),
    ("Open the summary it wrote. Check two of the numbers yourself against the workbook.", ""),
    ("Write in the summary which claims you checked, and which still need the HR head to confirm.", ""),
]

STEPS[11] = [
    ("Open a terminal in this lab folder and start Claude Code. Everything in this lab runs on your own computer. There is no cloud connection and nothing is emailed.", "claude"),
    ("Look at inputs/weekly-input.csv and inputs/staff-questions.json in this folder. These stand in for this week's numbers and this week's staff questions.", ""),
    ("Ask Claude Code to update the workbook from the local file, taking a backup first.", "Read automation/update_people_workbook.py in this folder. Run it so it updates Lumina-Living-People-Tracker.xlsx from inputs/weekly-input.csv. Back the workbook up before writing anything, keep every existing formula working, and show me what will change before you change it."),
    ("Ask Claude Code to build the weekly update from the local files.", "Run automation/generate_weekly_update.py to build the weekly people update from Lumina-Living-People-Tracker.xlsx and inputs/staff-questions.json, using templates/Weekly-Update-Template.docx. Name the workbook cell behind every number and the message reference behind every staff question. Save the result in the outputs folder."),
    ("Open the update in the outputs folder. Check the backup exists, the formulas still work, and every figure says where it came from.", ""),
]
