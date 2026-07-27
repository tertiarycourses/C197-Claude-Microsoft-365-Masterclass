"""
Domain 2 — Boosting Productivity Across Microsoft 365 with Claude. Labs 5-8.

Continues the SAME Lumina Living Q3 review pack from Domain 1. Having set Claude up,
connected your files, learned to prompt well and set your safe-use rules, you now
PRODUCE the pack: the written report in Word, the data analysis in Excel, the slide
deck in PowerPoint, and the emails that send it in Outlook and Teams. Lab 8 is the
capstone — it sends the finished pack out.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you do in this lab becomes part of your Lumina Living Q3 review pack, "
 "the single deliverable you write, analyse, present and send across all 8 labs."
)

DOMAIN2 = [
 dict(
 num=5, topic=2,
 title="Write, Rewrite and Summarise in Word",
 objective="Use Claude to draft, restructure and tighten a document, and to summarise a long one, then finish it in Word.",
 desc="You produce the written report. You have Claude draft the Q3 review from the brief and the workbook, "
 "restructure and shorten it, adjust the tone for a management audience, and summarise a longer background "
 "note into key points — pasting the checked result into Word. " + PROJECT_NOTE,
 build="A finished Q3 review report in Microsoft Word, drafted and refined with Claude and checked by you.",
 services="Microsoft Word, Claude (draft / rewrite / summarise), copy-paste, Word > Home formatting",
 steps=[
 ("In your Project, ask Claude to draft the report from the material it already has.",
  "Using the brief and the Q3 workbook in this project, draft a one-page business-review report for management. Structure it as: Overview, What sold well, What to watch, and Recommended actions. Name the key figure in each section and say where it comes from."),
 ("Read the draft and check every figure it names against the workbook. Mark anything you cannot confirm — you will not keep unverified numbers.", ""),
 ("Restructure and tighten with a follow-up prompt.",
  "Good. Now cut it to about 250 words, put the Recommended actions as three bullet points, and make the tone confident but plain — no jargon."),
 ("Adjust the tone for the audience if needed (for example more formal, or warmer), then choose the version you will keep.",
  "Give me the same report in a slightly more formal tone suitable for a board paper."),
 ("Summarise a longer input: paste a longer background note (or the brief's appendix) and ask for a short summary you can use as an intro.",
  "Summarise this background note into four bullet points I can use as context at the top of the report."),
 ("Open Microsoft Word, paste your chosen report in, and format it: a title, headings for each section, and the three action bullets (Home > Styles).", ""),
 ("Do the final human check: re-read the whole page, confirm every figure ties to the workbook, and fix any wording. Save it as 'Lumina Living — Q3 Review Report.docx'.", ""),
 ],
 test="You have a saved Word report of about 250 words with the four sections and three action bullets, in which every figure has been checked against the Q3 workbook.",
 ),
 dict(
 num=6, topic=2,
 title="Analyse and Explain Data in Excel",
 objective="Use Claude to analyse a dataset, build the formulas you need, and explain a formula — verifying every figure in Excel.",
 desc="You produce the numbers behind the report. You have Claude analyse the Q3 sales workbook, ask it for "
 "the Excel formulas to compute the key figures, paste those formulas into Excel to verify them, and have "
 "Claude explain an unfamiliar formula — trusting no figure you have not confirmed yourself. " + PROJECT_NOTE,
 build="A verified Q3 analysis in Microsoft Excel — key figures computed by formulas you checked, and one formula you can explain.",
 services="Microsoft Excel, Claude (analysis / formula generation / formula explanation), SUM, SUMIF, AVERAGE",
 steps=[
 ("Ask Claude to analyse the workbook and surface the figures the report needs.",
  "From the Q3 sales workbook, give me: total sales for the quarter, the best- and worst-selling product by value, the top region, and the month-by-month trend. Show the figure for each and say which columns you used."),
 ("Ask Claude for the exact Excel formula for the headline figure so you can reproduce it.",
  "Give me the Excel formula to compute total Q3 sales from the Total column, assuming the data is in rows 2 to 500."),
 ("In Excel, put that formula in an empty cell and confirm it matches the figure Claude reported.",
  "=SUM(F2:F500)"),
 ("Ask for a conditional formula and verify it too — for example sales for the top region.",
  "Give me an Excel formula that totals the Total column only for rows where the Region column equals \"North\"."),
 ("Paste it into Excel and cross-check by filtering the sheet to that region and reading the status-bar Sum.",
  "=SUMIF(D2:D500,\"North\",F2:F500)"),
 ("Learn from a formula: paste an unfamiliar one and ask Claude to explain it step by step.",
  "Explain, step by step, what this Excel formula does: =IF(F2>500,\"Large\",\"Standard\")"),
 ("Set the rule and record the checked figures: never accept a number you cannot tie back to a formula in the sheet. Note the verified headline figures where the report can reuse them.", ""),
 ],
 test="Your key Q3 figures each match an Excel formula you ran yourself, one conditional total agrees with a filtered status-bar Sum, and you can explain in one sentence what the =IF formula does.",
 ),
 dict(
 num=7, topic=2,
 title="Generate Slide Outlines and Content for PowerPoint",
 objective="Use Claude to turn the report and analysis into a slide-by-slide outline with titles, bullets and speaker notes.",
 desc="You produce the deck for the management meeting. You have Claude turn the checked report and figures "
 "into a slide-by-slide outline — titles, three bullets each and short speaker notes — refine the flow and "
 "length, then build the slides in PowerPoint from that outline. " + PROJECT_NOTE,
 build="A Q3 review slide deck in Microsoft PowerPoint, built from a Claude-generated outline you refined and checked.",
 services="Microsoft PowerPoint, Claude (slide outline / speaker notes), Outline view, copy-paste",
 steps=[
 ("Ask Claude to convert your report and verified figures into a slide outline.",
  "Turn the Q3 review report and the verified figures into a 6-slide deck for a 10-minute management meeting. For each slide give a title, no more than three short bullets, and two lines of speaker notes. Keep every figure consistent with the report."),
 ("Read the outline and check the figures on each slide against your verified numbers from Lab 6. Fix any that drift.", ""),
 ("Refine the flow with a follow-up.",
  "Reorder so the recommended actions are the final slide, and make the opening slide a single headline that states how the quarter went."),
 ("Tighten wording so no bullet runs over one line.",
  "Shorten every bullet to at most eight words, keeping the meaning."),
 ("Build the slides: open PowerPoint, use View > Outline, and paste the titles and bullets so each slide is created from the outline (Tab to demote a line to a bullet).", ""),
 ("Add the speaker notes: for each slide, paste Claude's two lines into the Notes pane (View > Notes).", ""),
 ("Do the final human check: click through the deck, confirm every figure matches the report and workbook, then save it as 'Lumina Living — Q3 Review.pptx'.", ""),
 ],
 test="You have a saved 6-slide PowerPoint deck with a headline opener and an actions closer, one-line bullets, and speaker notes — with every figure consistent with your Word report and Excel analysis.",
 ),
 dict(
 num=8, topic=2,
 title="Draft and Reply to Email in Outlook and Teams",
 objective="Use Claude to draft, adjust the tone of, and reply to work messages, then send the pack — verifying before it goes.",
 desc="The capstone. You send the pack out. You have Claude draft the stakeholder email that carries the "
 "review, adjust its tone and length, draft a reply to a likely question, and write a short Teams "
 "announcement — checking every detail before anything is sent. " + PROJECT_NOTE,
 build="A ready-to-send Outlook email carrying the Q3 pack, a drafted reply, and a short Teams announcement — all checked by you.",
 services="Microsoft Outlook, Microsoft Teams, Claude (draft / tone / reply), copy-paste",
 steps=[
 ("Ask Claude to draft the covering email for the management team.",
  "Draft a short email to the management team introducing the attached Q3 business-review report and slide deck. Say what the quarter's headline was, list the three recommended actions, and ask for comments by Friday. Professional and warm, under 150 words."),
 ("Read it and verify: the headline and the three actions must match your report exactly. Fix any drift, and confirm no confidential detail is included.", ""),
 ("Adjust the tone or length if needed, and keep the version you will send.",
  "Make it a little more concise and add a one-line thank-you at the end."),
 ("Draft a reply to a question you can expect, so you are ready.",
  "Draft a brief, friendly reply to a manager who asks: 'Can you confirm the total Q3 sales figure and which region led?' Leave placeholders <TOTAL> and <REGION> for me to fill from the verified data."),
 ("Fill the placeholders from your verified Lab 6 figures — never from memory — and check they are right.", ""),
 ("Write a short Teams announcement for the team channel.",
  "Write a 2-sentence Microsoft Teams message announcing that the Q3 review pack is ready and where to find it, friendly and clear."),
 ("Send safely: open Outlook, paste the covering email, attach 'Q3 Review Report.docx' and 'Q3 Review.pptx', check the recipients and the attachments, and only then send. Post the Teams message to the channel.", ""),
 ],
 test="You have a checked covering email in Outlook with the correct headline, the three matching actions and both files attached; a reply drafted with verified figures; and a short Teams announcement — and you confirmed every figure and name before sending.",
 ),
]
