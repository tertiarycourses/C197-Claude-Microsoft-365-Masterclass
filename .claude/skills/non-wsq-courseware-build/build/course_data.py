"""
SINGLE SOURCE OF TRUTH — C197 Claude Microsoft 365 Masterclass (non-WSQ).

A beginner, one-day (7.5 hours), hands-on short course on using Claude — Anthropic's
AI assistant — alongside Microsoft 365 to boost everyday work productivity: setting
up and connecting Claude to your files and apps, prompting effectively for work
tasks, applying AI responsibly and securely, and then writing and summarising in
Word, analysing data in Excel, building slide content for PowerPoint, and drafting
email in Outlook and Teams. Every artifact (PPT, LP, LG, LG.md) and every lab is
generated from this module + data_domainN.py so they stay 100% aligned.

NON-WSQ RULES — the engine enforces these, do not reintroduce them here:
  * NO assessment of any kind (no WA/SAQ, no PP, no case study, no marking).
  * NO SSG / SkillsFuture / WSQ funding or subsidy content.
  * NO TRAQOM survey, NO digital attendance, NO 75% attendance rule.
  * NO TGS course reference — this course carries the plain code C197.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Claude Microsoft 365 Masterclass (C197)"
SHORT_TITLE  = "Claude Microsoft 365 Masterclass (C197)"   # used in output filenames
COURSE_CODE  = "C197"                                       # non-WSQ code — never a TGS- ref
VERSION      = "v1.0"
VERSION_DATE = "27 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Jim Gan Chiu Liang (JL)"
DAYS         = 1
MODE         = "Instructor-led, hands-on practical labs"

DARK_THEME = False

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain what Claude is and how it works alongside Microsoft 365, and set up Claude ready for work.",
    "LO2: Connect Claude to your Microsoft 365 files and apps by uploading, pasting and using Projects and connectors.",
    "LO3: Write clear, effective prompts that get accurate, usable results for everyday work tasks.",
    "LO4: Apply AI responsibly, securely and privately — knowing what to share, what to withhold and what to verify.",
    "LO5: Use Claude to write, rewrite and summarise documents in Microsoft Word.",
    "LO6: Use Claude to analyse and explain data, and to build formulas, for Microsoft Excel.",
    "LO7: Use Claude to generate slide outlines and content for Microsoft PowerPoint.",
    "LO8: Use Claude to draft and reply to messages in Microsoft Outlook and Teams.",
]
LO_TITLES = [
    "Understand & set up Claude",
    "Connect files & apps",
    "Prompt effectively",
    "Use AI safely",
    "Write in Word",
    "Analyse in Excel",
    "Build in PowerPoint",
    "Draft in Outlook & Teams",
]

# ------------------------------------------------------------------ topics
# `concepts` are plain strings ("Title — explanation.") so they render cleanly
# as both slide tiles and Learner-Guide bullets. `weighting` = share of course time.
TOPICS = [
    dict(num=1, code="01",
         title="Getting Started with Claude for Microsoft 365",
         subtitle="Introduction to Claude & Microsoft 365 · Connecting Claude to your files and apps · Effective prompting for work tasks · Responsible, secure and private use of AI",
         weighting="50%",
         concepts=[
            "Claude — Anthropic's AI assistant that reads, writes, analyses and explains in plain language, available at claude.ai and in the Claude desktop app.",
            "Claude alongside Microsoft 365 — Claude is a separate assistant you feed your Word, Excel, PowerPoint and Outlook content into, then paste its results back; it complements the Office apps you already use.",
            "Two ways to give Claude your work — upload a file (Word, Excel, PowerPoint, PDF, CSV, images) or paste the text or table directly into the chat.",
            "Projects — a Claude workspace that keeps your files and custom instructions together, so every chat about the same task starts with the right context.",
            "Connectors — an optional way to let Claude read from your cloud storage (such as OneDrive, SharePoint or Google Drive) where your account and plan support it.",
            "Effective prompting — a good work prompt states the role, the context, the task and the output format, so Claude has no room to guess.",
            "Human in the loop — Claude drafts; you decide. Always read, check and edit its output before it becomes your work.",
            "Responsible use — keep confidential and personal data out of prompts unless your organisation has approved it, and verify anything you will rely on.",
         ]),
    dict(num=2, code="02",
         title="Boosting Productivity Across Microsoft 365 with Claude",
         subtitle="Writing, rewriting & summarising in Word · Analysing & explaining data in Excel · Generating slides for PowerPoint · Drafting & replying to email in Outlook and Teams",
         weighting="50%",
         concepts=[
            "Writing in Word — describe the document you need and let Claude draft it, then refine the structure, length and tone with follow-up prompts.",
            "Rewriting and summarising — paste a long document and ask Claude to shorten it, change its tone, or pull out the key points and actions.",
            "Analysing data in Excel — upload or paste a table and ask Claude what it shows: totals, trends, comparisons and a plain-language read of the numbers.",
            "Explaining and building formulas — ask Claude for the Excel formula you need, and paste any formula back to have it explained step by step.",
            "Generating slides for PowerPoint — turn a document or a brief into a slide-by-slide outline with titles, bullet points and speaker notes.",
            "Drafting email in Outlook and Teams — draft, reply to and adjust the tone of work messages, keeping them clear, professional and appropriately brief.",
            "Verify before you send — check every figure, name, date and claim in Claude's output against a source you trust before it leaves your desk.",
            "One connected workflow — the same review pack flows from Word to Excel to PowerPoint to Outlook, with Claude speeding up each step.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Getting set up with Claude for Microsoft 365, then boosting productivity across Word, Excel, PowerPoint, Outlook and Teams",
}

# ------------------------------------------------------------------ schedule
# NON-WSQ: no assessment blocks. The single training day totals exactly 480
# minutes excluding the 1-hour lunch — of which 30 minutes are tea breaks, so
# 450 minutes (7.5 hours) are instructional, matching the advertised duration.
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:30","9:50",20,"admin","Welcome, course introduction, ground rules, and confirming Claude and Microsoft 365 access for the labs"),
        ("9:50","10:45",55,"topic","TOPIC 01 — Getting Started with Claude for Microsoft 365: what Claude is and how it works alongside Office; connecting Claude to your files and apps; effective prompting for work tasks; responsible, secure and private use of AI (concepts + live demo)"),
        ("10:45","11:30",45,"lab","Hands-on: "+lab_titles([1,2])),
        ("11:30","11:45",15,"break","Tea break"),
        ("11:45","13:00",75,"lab","Hands-on: "+lab_titles([3,4])),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","14:50",50,"topic","TOPIC 02 — Boosting Productivity Across Microsoft 365 with Claude: writing, rewriting and summarising in Word; analysing and explaining data in Excel; generating slide content for PowerPoint; drafting and replying to email in Outlook and Teams (concepts + live demo)"),
        ("14:50","15:30",40,"lab","Hands-on: "+lab_titles([5])),
        ("15:30","15:45",15,"break","Tea break"),
        ("15:45","18:15",150,"lab","Hands-on: "+lab_titles([6,7,8])),
        ("18:15","18:30",15,"recap","Course wrap-up, your Claude-for-Microsoft-365 workflow and next steps"),
     ]),
    }

# ------------------------------------------------------------------ deck content
COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="How Claude Works with Microsoft 365",
    concepts=[
        "From doing every step by hand to describing the result — you tell Claude the outcome you want and it drafts the document, the analysis or the slides for you.",
        "It works with the files you already have — upload or paste your Word, Excel and PowerPoint content, and Claude works on your material, not a generic example.",
        "Two ways in — upload or paste a one-off, or keep a Project so every chat about the same task already has your files and instructions.",
        "You stay accountable — Claude drafts and suggests; you read, check and edit every result before it becomes your work.",
    ],
    framework_title="The Ask–Check–Apply Loop",
    framework=[
        ("Prepare", "Know the task: which file, what you want produced, and what a correct, usable result looks like."),
        ("Ask", "Write a clear prompt — the role, the context, the task and the output format."),
        ("Check", "Read Claude's output and verify every figure, name and claim against a source you trust."),
        ("Apply", "Paste the checked result back into Word, Excel, PowerPoint or Outlook and finish it."),
        ("Refine", "Adjust the prompt and re-run until the output is right, then save the prompt to reuse."),
    ],
    statement=dict(
        headline="Claude is fastest when your prompt is specific and your check is honest.",
        body="This course is hands-on: you build one connected business-review pack — a Word report, an Excel analysis, a PowerPoint deck and the emails that send it — using Claude at every step and checking its work before you rely on it.",
        kicker="THE WORKING RULE",
    ),
    pillars_title="What You'll Build",
    pillars=[
        ("A set-up you can trust", ["Claude ready and connected to your files", "A Project holding your review pack", "A reusable prompt pattern and a safe-use checklist"]),
        ("A business-review pack", ["A written report in Word", "A verified data analysis in Excel", "A slide deck in PowerPoint"]),
        ("The messages that send it", ["A clear stakeholder email in Outlook", "A short Teams announcement", "Every figure and claim checked before sending"]),
    ],
    arc_title="How Every Lab Works",
    arc=[
        "The trainer demonstrates the Claude technique on the shared Lumina Living review pack.",
        "You do it yourself with Claude and Microsoft 365 — on the sample material, or on your own non-confidential work.",
        "You verify the result against the lab's explicit 'Test it' check.",
        "You compare Claude's output with a source you can confirm, and refine your prompt if it is off.",
        "You keep the working prompt or output — it becomes part of your Claude-for-Microsoft-365 toolkit.",
    ],
)

# ------------------------------------------------------------------ LG content
LG_INTRO = (
    "This Learner Guide accompanies the Claude Microsoft 365 Masterclass (C197) course, conducted by "
    "Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 8 hands-on labs, in the "
    "order you will run them, together with the concepts each lab depends on."
)
LG_INTRO2 = (
    "The labs build one connected result. You take the role of a coordinator at a small retailer, "
    "'Lumina Living', preparing the quarter's business-review pack, and use Claude alongside Microsoft 365 "
    "to write the report in Word, analyse the numbers in Excel, build the slides in PowerPoint, and draft "
    "the emails that send it in Outlook and Teams — checking Claude's work at every step. Wherever you can, "
    "use your own non-confidential work so you leave with skills applied to your own job; the supplied Lumina "
    "Living sample material is provided for everyone to follow along."
)
LG_SETUP = dict(
    needs=[
        "A laptop (Windows or Mac) with a current Chrome or Edge browser.",
        "A Claude account at claude.ai (a free account is enough to follow every lab; a paid plan adds Projects and larger uploads — the trainer confirms what your account has on the day).",
        "Microsoft 365 with Word, Excel, PowerPoint and Outlook (desktop or the web apps at office.com), and access to Microsoft Teams.",
        "The sample 'Lumina Living — Q3 Review' files (a Word brief, an Excel sales workbook and a short slide starter) — the trainer shares a link; make your own copies — or your own non-confidential documents.",
    ],
    verify_text="Before Lab 1, confirm you can sign in to claude.ai, start a new chat, and open Word, Excel, PowerPoint and Outlook. If Claude or any Office app is not available on your account, tell the trainer.",
    verify_code="Sign in at claude.ai  ·  start a New chat  ·  open Word / Excel / PowerPoint / Outlook  ·  download the sample Lumina Living files",
    conventions=[
        "Placeholders such as <YOUR FILE> or <YOUR NAME> are replaced with your own values.",
        "Prompts you give Claude are shown in a shaded box — paste them into the Claude chat, attaching the file named in the step where one is used.",
        "App paths (e.g., Word > Home > Editor, or File > Info) and menu names are written as you will use them; Claude's own buttons may move over time.",
        "Every lab ends with a 'Test it' step — verify Claude's result against a source you can confirm before you move on.",
    ],
)
LAB_NOTE = (
    "Use only documents and data you are authorised to use. Never paste passwords, personal identifiers or "
    "confidential business data into an AI prompt — use the supplied Lumina Living sample material if in doubt. "
    "Claude's screens, menu names and buttons may differ slightly between accounts and plans and may change "
    "over time; the trainer will point out the current location on the day."
)
LG_WRAPUP = dict(
    title="Wrap-Up",
    intro="In one day you have taken a quarter's raw material — a brief, a spreadsheet and a handful of facts — and turned it into a finished business-review pack, using Claude alongside Microsoft 365 at every step and checking its work before trusting it.",
    sections=[
        dict(title="What you built", bullets=[
            "Claude set up and connected to your Microsoft 365 files, with a Project holding your review pack.",
            "A reusable prompt pattern (role, context, task, output) and a personal safe-use checklist.",
            "A written business-review report in Word, drafted, restructured and tightened with Claude.",
            "A verified data analysis in Excel — figures, trends and formulas you checked yourself.",
            "A PowerPoint deck generated as a slide-by-slide outline with titles, bullets and speaker notes.",
            "A stakeholder email in Outlook and a short Teams announcement, each checked before sending.",
        ]),
        dict(title="What to do next", bullets=[
            "Point these techniques at one real, recurring task in your own week and measure the time saved.",
            "Keep verifying: check every figure, name and claim in Claude's output against a source you trust.",
            "Save your best prompts and your Project so you and your team can reuse them.",
            "Keep confidential data out of prompts, and note where AI helped so your work stays accountable.",
        ]),
    ],
)
LG_NEXT_STEPS = [
    "First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.",
    "Second pass: rebuild the Word-Excel-PowerPoint-Outlook flow on the sample pack from memory, writing your own prompts.",
    "Apply the techniques to a real, non-confidential task from your own organisation.",
    "Review each lab's detailed steps in this guide and re-run the tasks on your own machine.",
]
LG_GLOSSARY = [
    ("Claude", "Anthropic's AI assistant, used here at claude.ai and in the Claude desktop app to read, write, analyse and explain in plain language."),
    ("Anthropic", "The company that makes Claude."),
    ("Microsoft 365", "Microsoft's suite of work apps — including Word, Excel, PowerPoint, Outlook and Teams — used in the browser or as desktop apps."),
    ("Prompt", "The plain-language instruction you give Claude; a good one states the role, context, task and output format."),
    ("Project", "A Claude workspace that keeps files and custom instructions together so related chats start with the right context."),
    ("Connector", "An optional link that lets Claude read from a cloud service such as OneDrive, SharePoint or Google Drive, where your plan supports it."),
    ("Upload", "Attaching a file (Word, Excel, PowerPoint, PDF, CSV or image) to a Claude chat so Claude can work on its contents."),
    ("Artifact", "A self-contained document, table or draft Claude produces in a side panel that you can copy or refine."),
    ("Summarising", "Condensing a long document into its key points, actions or a shorter version."),
    ("Rewriting", "Changing the wording, tone or length of text while keeping its meaning."),
    ("Formula", "An Excel instruction (such as =SUM or =IF) that calculates a result from your data."),
    ("Speaker notes", "The per-slide notes in PowerPoint that guide what you say when presenting."),
    ("Verification", "Checking that an AI result is correct by comparing it against a source you can confirm yourself."),
    ("Hallucination", "A confident but wrong AI output; the reason every AI result must be verified before use."),
    ("Human in the loop", "The practice of a person reviewing and approving AI output before it is relied upon."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial release — C197 Claude Microsoft 365 Masterclass courseware.", TRAINER),
]
