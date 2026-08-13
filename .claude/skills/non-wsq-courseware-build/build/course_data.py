"""Single source of truth for C197 Claude Microsoft 365 Masterclass.

The course is a one-day, non-WSQ commercial masterclass.  Slides teach the
operating model, decisions and process architecture.  Detailed procedures,
copy-ready prompts and commands live only in the Learner Guide and lab folders.
All company names, people, messages and figures are fictional training data.
"""

TITLE = "Claude Microsoft 365 Masterclass (C197)"
SHORT_TITLE = "Claude Microsoft 365 Masterclass (C197)"
COURSE_CODE = "C197"
VERSION = "v3.0"
VERSION_DATE = "13 August 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Jim Gan Chiu Liang (JL)"
DAYS = 1
MODE = "Instructor-led, company-scenario workshops and hands-on practical labs"
DARK_THEME = False
COURSE_MATERIALS_URL = "https://www.tertiarycourses.com.sg/learnerlogin"
LEARNER_DEFAULT_PASSWORD = "student12345"

COMPANY = "Lumina Living Pte Ltd"
COMPANY_CONTEXT = (
    "Lumina Living is a fictional Singapore home-and-lifestyle company with retail, "
    "online and warehouse teams. Learners join its HR department to prepare the FY2027 "
    "hiring plan, staff policies and the weekly people update."
)

LEARNING_OUTCOMES = [
    'LO1: Choose the right place to use Claude for an HR task.',
    'LO2: Decide what staff information Claude may read, and what it must never change.',
    'LO3: Write a request that says what you want, what to use, what to leave alone and when to stop.',
    'LO4: Write a hiring plan in Word using only what the brief actually says.',
    'LO5: Draft leave and flexible-work policy wording that flags every point needing legal review.',
    'LO6: Build a headcount and turnover analysis in Excel using live formulas.',
    'LO7: Build a leadership update deck where every slide title states a conclusion.',
    'LO8: Sort the HR inbox and draft one reply ready for approval.',
    'LO9: Have Claude read one folder and write a people summary that says where each fact came from.',
    'LO10: Automate a weekly people update on your own computer.',
    'LO11: Save a working method as a Skill so the whole team applies the same standard.',
    'LO12: Use the Microsoft 365 connector to find HR files stored in SharePoint.',
    'LO13: Add a plugin, and judge when a task needs one and when it does not.',
]

LO_TITLES = [
    'Pick the right place',
    'Decide what Claude reads',
    'Ask clearly',
    'Plan the hiring',
    'Check the policy wording',
    'People numbers',
    'Tell leadership',
    'Handle the inbox',
    'One folder, one summary',
    'Automate the update',
    'Save it as a Skill',
    'Connect SharePoint',
    'Add a plugin',
]

TOPICS = [
    dict(
        num=1, code='01', title='Getting Claude Ready for HR Work',
        subtitle='Where to use Claude · what it may read · asking for what you want',
        weighting='24%', concepts=[
            'Three places to use Claude — inside Word, Excel and PowerPoint; in the Claude Desktop app; and in the browser. Each one sees different things.',
            'The panel inside Office works on the file you already have open, and keeps your headings, formulas and slide layouts.',
            'The Claude Desktop app can read a whole folder at once, so use it when the answer spans several files.',
            'HR files hold information about real people. Decide what Claude may read, and what it must never change, before you start.',
            'Ask Claude to say where each fact came from — which file, which sheet, which line — so you can check it before it reaches a staff member.',
            'You decide, not Claude. Nothing is sent, published or approved until a named person says yes.',
        ]),
    dict(
        num=2, code='02', title='Hiring Plans, Policies and Staff Documents',
        subtitle='Hiring plan · leave and flexible-work policy · handbook wording · who signs off',
        weighting='28%', concepts=[
            'A hiring plan makes choices: which roles now, which can wait, and what the budget will not cover.',
            'Every role needs a hiring manager, a start date, a salary range and the reason the role exists.',
            'Policy wording carries real consequences. Anything about pay, leave, notice or conduct needs proper review before release.',
            'Keep three things apart: what the policy says, how it works day to day, and what needs legal advice.',
            'Work inside the company template so the document looks like every other HR document staff receive.',
            'Say plainly what you do not yet know, rather than filling the gap with a confident guess.',
        ]),
    dict(
        num=3, code='03', title='People Numbers and Reporting to Leadership',
        subtitle='Headcount and turnover in Excel · what the numbers say · the leadership update',
        weighting='25%', concepts=[
            'Keep the staff data, the assumptions and the results on separate sheets so anyone can follow the working.',
            'Use live formulas that point at the source data. A number typed in by hand cannot be checked or updated.',
            'Compare actual headcount and cost against plan, month by month and team by team, before you explain the result.',
            'Pick the chart that answers the question leadership asked. More charts is not more insight.',
            'Every slide title should say what you concluded, not name a topic.',
            'Put the source under any figure on a slide, so the room can challenge it.',
        ]),
    dict(
        num=4, code='04', title='Staff Questions, Repeatable Work and Advanced Claude',
        subtitle='Sorting the HR inbox · one folder, one summary · the weekly update · Skills, connectors and plugins',
        weighting='23%', concepts=[
            'Sort staff messages by what each one needs: a reply from you, a decision from someone else, or nothing at all.',
            'Claude drafts the reply; you check the facts, the tone and the recipient, and you are the one who sends it.',
            'Point Claude Desktop at one folder and it can pull a summary together from everything inside it.',
            "When two files disagree, that disagreement is the finding. It is not Claude's job to settle it quietly.",
            'Work you repeat every week is worth automating once, with a backup taken before anything is overwritten.',
            'An automated update still needs a person to read it before it goes to anyone else.',
        ]),
]

DAY_THEMES = {1: "From setting up Claude to a complete Lumina Living HR workflow: hiring plan, policy wording, people numbers and the weekly update"}

def SCHEDULE(lab_titles):
    return {1: (DAY_THEMES[1], [
        ("9:30", "9:45", 15, "admin", "Welcome, course orientation and the Lumina Living HR scenario"),
        ("9:45", "10:05", 20, "topic", "TOPIC 01 — Getting Claude Ready for HR Work"),
        ("10:05", "11:15", 70, "lab", "Hands-on: " + lab_titles([0, 1, 2])),
        ("11:15", "11:30", 15, "break", "Tea break"),
        ("11:30", "11:45", 15, "topic", "TOPIC 02 — Hiring Plans, Policies and Staff Documents"),
        ("11:45", "13:00", 75, "lab", "Hands-on: " + lab_titles([3, 4, 5])),
        ("13:00", "14:00", 60, "lunch", "Lunch break"),
        ("14:00", "14:15", 15, "topic", "TOPIC 03 — People Numbers and Reporting to Leadership"),
        ("14:15", "15:30", 75, "lab", "Hands-on: " + lab_titles([6, 7, 8])),
        ("15:30", "15:45", 15, "break", "Tea break"),
        ("15:45", "16:00", 15, "topic", "TOPIC 04 — Staff Questions, Repeatable Work and Advanced Claude"),
        ("16:00", "17:00", 60, "lab", "Hands-on: " + lab_titles([9, 10, 11])),
        ("17:00", "18:15", 75, "lab", "Hands-on: " + lab_titles([12, 13, 14, 15])),
        ("18:15", "18:30", 15, "recap", "Integrated workflow review, transfer to work and next steps"),
    ])}

COURSE_OVERVIEW = dict(
    section_title="The Lumina Living Management Challenge",
    concepts_title="One Company, One Connected Evidence Chain",
    concepts=[
        "Plan the year — turn the company's hiring needs into a plan, staff policies and clear approvals.",
        "Work the numbers — check headcount, staff cost and budget assumptions in an Excel workbook you can follow.",
        "Communicate the decision — build a company-standard executive deck using verified Word and Excel content.",
        "Coordinate the work — triage Outlook, use Cowork for multi-file execution and use Claude Code for a repeatable daily brief.",
    ],
    framework_title="The FRAME Control Loop",
    framework=[
        ("Frame", "Name the decision, audience, permitted sources and definition of done."),
        ("Retrieve", "Bring only authorised files, messages and ranges into context."),
        ("Act", "Ask Claude to draft or edit the smallest useful unit in the native work product."),
        ("Measure", "Verify figures, claims, formulas, formatting and policy constraints."),
        ("Endorse", "Record assumptions and obtain the named human approval before save, send or release."),
    ],
    statement=dict(
        headline="A polished output is not a trusted output until its evidence, logic and owner are visible.",
        body="The presentation teaches the business architecture. The Learner Guide and lab folders contain the exact prompts, commands, source files and review checks.",
        kicker="THE PROFESSIONAL STANDARD",
    ),
    pillars_title="The Company Pack You Will Build",
    pillars=[
        ("Plans and policies", ["Hiring plan", "One-page people plan", "Leave and flexible-work drafts"]),
        ("Analysis and story", ["Headcount analysis", "People numbers", "Leadership update deck"]),
        ("Agentic coordination", ["Outlook draft workflow", "Cowork project", "Claude Code daily brief"]),
    ],
    arc_title="How Every Activity Connects",
    arc=[
        "Open the lab folder and inspect its realistic Word, Excel and PowerPoint company artifacts.",
        "Use the named evidence and prompt contract to create or improve a work product.",
        "Challenge the result against formulas, sources, policy boundaries and company templates.",
        "Record the approval, retain the verified artifact and pass only approved context to the next activity.",
    ],
)

PROMPT_PLAYBOOK = dict(
    principles=[
        ("Name the business result", "State the decision, audience and artifact—not merely the app you are using."),
        ("Ground the work", "Name the open file, table, sheet, section or approved message set Claude may use."),
        ("Constrain the edit", "Define scope, length, style, formula method, layout and anything Claude must not change."),
        ("Demand evidence", "Require cell, range, heading or email citations and ask Claude to flag missing information."),
        ("Set the approval gate", "Ask for proposed changes first; verify them before accepting, saving, sending or publishing."),
    ],
    intro=(
        "READ THIS FIRST. The prompts below are worked examples that show what a good prompt looks "
        "like. They are NOT lab steps. Every lab has its own numbered steps in its own section later "
        "in this guide. Every example below uses ONE folder only, so you never have to jump between "
        "labs: labs/lab-03-ask-claude-clearly/. Open the labs folder that "
        "came with your course materials, then open the lab-03-build-an-auditable-prompt-and-review-"
        "contract folder inside it. The Word, Excel and PowerPoint files named below are all sitting "
        "in that one folder. Double-click the named file to open it before you type anything. Each "
        "prompt deliberately stops at proposed changes: reading the proposal and choosing NOT to "
        "accept it is the correct result, because that is the human approval gate this course teaches."
    ),
    groups=[
        dict(
            surface="Group A — Type these into the Claude panel INSIDE Word, Excel or PowerPoint",
            how_steps=[
                "Double-click the file named above the prompt so it opens in Word, Excel or PowerPoint.",
                "Open the Claude panel from that app's ribbon. On Windows select Home, then Add-ins, then Claude. On Mac select Tools, then Add-ins, then Claude.",
                "The Claude panel opens as a narrow column on the RIGHT-HAND side of your document.",
                "Type the prompt into the box at the bottom of that panel. Do NOT type it into the document itself.",
                "Read what Claude proposes, then stop. Do not accept the change.",
            ],
            how_note="In Group A, Claude can only see and change the one file you have open in front of you.",
            examples=[
                dict(app="Word", title="Draft a decision-ready strategy section",
                     open_file="labs/lab-03-ask-claude-clearly/Lumina-Living-Lab-03-HR-Brief.docx",
                     prompt="Using the open Lumina-Living-Lab-03-HR-Brief.docx, write a new 'What we will do' section for the HR leadership team, placed after '3. Required management outputs'. Preserve the existing Heading 1 styles. For each action give the reason, who owns it, how we will know it worked, and the date. Use only facts stated in the brief; cite the source heading and flag missing evidence. Show proposed text before editing the document."),
                dict(app="Excel", title="Build an auditable management view",
                     open_file="labs/lab-03-ask-claude-clearly/Lumina-Living-Lab-03-Working-Workbook.xlsx",
                     prompt="Using the table on the Management_Control sheet of the open Lumina-Living-Lab-03-Working-Workbook.xlsx, build a formula-driven summary of control status by owner on the Summary sheet. Use native formulas, cite the source rows you counted, and do not paste hardcoded totals. Before editing, list the formulas and checks you will apply."),
                dict(app="PowerPoint", title="Create an executive planning story",
                     open_file="labs/lab-03-ask-claude-clearly/Lumina-Living-Lab-03-Executive-Starter.pptx",
                     prompt="Using the open Lumina-Living-Lab-03-Executive-Starter.pptx, together with Lumina-Living-Lab-03-HR-Brief.docx and Lumina-Living-Lab-03-Working-Workbook.xlsx from the same lab-03 folder, suggest a six-slide update for the HR leadership team. Use conclusion-led titles, one message per slide and concise speaker notes. Preserve the slide master and brand rules. Add a source note to each data slide and flag any figure that does not reconcile. Show the proposed outline before changing any slide."),
            ],
        ),
        dict(
            surface="Group B — Type these into the Claude Desktop app instead",
            how_steps=[
                "Do NOT open any Office file. This group does not use one.",
                "Open the Claude Desktop application on your computer.",
                "Select Customize, then Connectors, and check that Microsoft 365 shows as connected. If it does not, stop and record Admin approval required.",
                "Type the prompt into the main chat box in the middle of the Claude Desktop window.",
                "Read what Claude returns and check that every item carries a source citation.",
            ],
            how_note="This is the difference that matters: Group A changes the one file you have open, while Group B searches across your authorised Microsoft 365 files without opening any of them.",
            examples=[
                dict(app="Claude Desktop", title="Find an authorised source before you draft",
                     before="Do not open any Office file. Confirm the Microsoft 365 connector is connected in Claude Desktop at Customize > Connectors.",
                     prompt="Find the latest fictional Lumina Living FY2027 planning item available to this training account. Return only its title, Microsoft 365 service and source citation. Do not draft, create, update, send or delete anything."),
                dict(app="Claude Desktop", title="Compare evidence across Microsoft 365",
                     before="Do not open any Office file. Confirm the Microsoft 365 connector is connected in Claude Desktop at Customize > Connectors.",
                     prompt="Search my authorised Microsoft 365 content for Lumina Living FY2027 planning material. List each item with its title, service, owner and last modified date, and cite the source for every row. Report only what you can cite and state clearly what you could not find. Do not create, edit, send or delete anything."),
            ],
        ),
    ],
)

LAB_SLUGS = {
    0: "set-up-claude-for-microsoft-365",
    1: "screen-candidates-in-excel",
    2: "analyse-staff-data-in-excel",
    3: "ask-claude-clearly-in-word",
    4: "write-a-hiring-plan-in-word",
    5: "draft-hr-policy-in-word",
    6: "build-a-headcount-analysis-in-excel",
    7: "build-a-leadership-update-in-powerpoint",
    8: "sort-the-hr-inbox-and-draft-one-reply",
    9: "read-a-folder-and-write-a-summary",
    10: "draft-outlook-replies-with-chrome",
    11: "build-a-daily-hr-routine-with-cowork",
    12: "automate-an-hr-pipeline-with-a-project",
    13: "add-skills-and-connectors-to-the-project",
    14: "upload-a-shared-skill-for-slides",
    15: "use-a-skill-across-excel-and-word",
}

LAB_DURATIONS = {0: 20, 1: 20, 2: 20, 3: 15, 4: 20, 5: 25, 6: 25, 7: 30, 8: 20, 9: 20, 10: 20, 11: 20, 12: 20, 13: 20, 14: 15, 15: 15}

LAB_SHOTS = {
    0: [
        ("claude-skills-add-menu.png", "Where Skills Live",
         "Settings > Skills on claude.ai. Add offers three ways to make one: Create with Claude, "
         "Write skill instructions, or Upload a skill."),
    ],
    5: [
        ("claude-skills-add-menu.png", "Creating the HR Policy Skill",
         "Settings > Skills > Add. Lab 5 uses Create with Claude, handing it the policy library "
         "and the written standard."),
    ],
    11: [
        ("claude-scheduled-tasks.png", "Scheduled Tasks",
         "Claude Desktop > Scheduled. Daily brief and Weekly review are ready-made task types; "
         "New task builds your own. Delete a task when the class ends."),
    ],
    12: [
        ("claude-projects.png", "Projects",
         "Claude Desktop > Projects > New project. Upload the HR materials once and set standing "
         "instructions, so every conversation in the project starts with the same context."),
    ],
}


SAMPLE_GALLERIES = [
    dict(title="Claude-Generated Planning and Policy Samples", kicker="REALISTIC COMPANY WORK",
         items=[(4, "FY2027 Hiring Plan"), (5, "One-Page People Plan"), (6, "Leave and Flexible-Work Drafts")]),
    dict(title="Claude-Generated Analysis and Executive Samples", kicker="NATIVE OFFICE ARTIFACTS",
         items=[(7, "Headcount Analysis in Excel"), (8, "Leadership Update Deck"), (9, "Sorted HR Inbox and Draft Reply")]),
]

DASHBOARD_EXHIBIT = dict(
    title="Inside the Claude-Generated Excel Dashboard",
    kicker="READABLE NATIVE EXCEL CHARTS",
    kpis="lab-07-kpis.png",
    charts=[
        ("lab-07-revenue-chart.png", "Actual vs Plan", "Shows whether headcount is on plan and where the gap appears each month."),
        ("lab-07-contribution-chart.png", "Staff Cost by Team", "Separates team size from team cost so leadership can act on the right one."),
    ],
)

LG_INTRO = (
    "This Learner Guide accompanies C197 and contains the complete procedures for eleven connected "
    "company activities. It is the operational companion to the concept-led slide deck."
)
LG_INTRO2 = (
    COMPANY_CONTEXT + " Every activity uses the same evidence chain so the hiring plan, people plan, "
    "policies, financial dashboard, presentation, Outlook hand-off, Cowork task and Claude Code daily brief remain consistent."
)
LG_SETUP = dict(
    needs=[
        "A current Windows or Mac laptop with Google Chrome, Microsoft 365 Word, Excel, PowerPoint and Outlook on the web.",
        "A paid Claude plan for the Office add-ins and Claude in Chrome. Lab 01 also distinguishes the Microsoft 365 connector in Claude Desktop and uses Claude in Chrome when the Outlook add-in is unavailable.",
        "Claude desktop with Cowork access for Lab 10 and Claude Code installed for Lab 11.",
        "An organisational Microsoft 365 account in an Entra tenant. The Microsoft 365 connector requires administrator consent; personal Outlook.com accounts are not supported.",
        "The self-contained Office files and templates inside each labs/lab-NN-*/ folder.",
    ],
    verify_text="Confirm the visible availability of every required surface before class. Missing add-ins, connector consent or Cowork access are real environment states and require the authorised administrator or the documented fallback.",
    verify_code="open Word / Excel / PowerPoint add-ins  ·  open Claude Desktop > Customize > Connectors  ·  verify Claude in Chrome is pinned and set to Manual approval",
    conventions=[
        "All Lumina Living information is fictional and safe for training; do not replace it with confidential or personal data without approval.",
        "Shaded blocks are copy-ready prompts or commands. Replace angle-bracket placeholders before use.",
        "Every material figure must trace to a workbook cell, table or approved source note.",
        "Draft, save, write and send actions remain subject to the named human approval gate.",
    ],
)

LAB_NOTE = (
    "Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. "
    "Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity."
)

LG_SAMPLE_FILES = [
    "Each lab folder contains a realistic company brief (.docx), working workbook (.xlsx), executive starter deck (.pptx) and reusable review templates.",
    "Lab 7 contains the headcount and staff-cost analysis; Lab 8 contains the leadership update deck that uses its checked figures.",
    "Lab 11 also contains a safe local automation starter for Excel updates and daily-brief generation; Microsoft 365 search uses the approved connector visible in Claude Code.",
]

LG_WRAPUP = dict(
    title="Wrap-Up — One Governed Company Workflow",
    intro="You have built a connected Lumina Living planning and management pack rather than a collection of isolated AI demonstrations.",
    sections=[
        dict(title="Business outputs", bullets=[
            "Hiring plans, people plans and staff policy drafts that use company templates and named reviewers.",
            "A financial analysis and dashboard with dynamic formulas, controls and management-ready visuals.",
            "An editable executive deck with native charts, a coherent decision story and source notes.",
        ]),
        dict(title="Operating controls", bullets=[
            "A permission and source map, prompt contract, review log and human approval boundary.",
            "An Outlook triage-and-draft pattern that does not silently send mail.",
            "A scoped Cowork workflow and a Claude Code daily-brief automation with explicit tool approvals.",
        ]),
    ],
)

LG_NEXT_STEPS = [
    "Re-run the full Lumina Living flow and verify that every figure and recommendation remains consistent across files.",
    "Adapt one activity to an approved recurring process in your organisation and define a baseline for time, quality and review effort.",
    "Ask your Microsoft 365 and Claude administrators which add-ins, connectors, write tools and Cowork surfaces are approved for your role.",
    "Keep prompts, source registers, decision logs and approval evidence with the final work product.",
]

LG_GLOSSARY = [
    ("Claude for Microsoft 365", "Anthropic's in-app assistants for Word, Excel, PowerPoint and Outlook."),
    ("Microsoft 365 connector", "A delegated connection that lets Claude work with authorised SharePoint, OneDrive, Outlook and Teams context."),
    ("Claude Cowork", "Anthropic's task-oriented desktop mode for multi-step work across scoped files and connected tools."),
    ("Copilot Cowork", "A separate Microsoft 365 Copilot experience with Microsoft licensing, governance, Work IQ and action approvals."),
    ("Claude Code", "Anthropic's command-line agent that can work with local files, scripts and approved MCP connectors."),
    ("MCP", "Model Context Protocol, a standard that lets Claude connect to approved tools and data sources."),
    ("Delegated permission", "Access exercised on behalf of the signed-in user and limited by that user's existing permissions."),
    ("Write tool", "A connector capability that can create or update content and therefore needs stronger consent and review."),
    ("Evidence chain", "The trace from a claim or chart back to its source file, cell, message or approved assumption."),
    ("Human send gate", "The required user review and approval before an email, invitation or other consequential action is sent."),
    ("Claude in Chrome", "Anthropic's Chrome extension for reading and acting on approved websites through a permission-controlled browser side panel."),
]

VERSION_HISTORY = [
    ("1.0", "27 July 2026", "Initial release.", TRAINER),
    ("1.1", "12 August 2026", "Visual redesign with current Office add-ins and connected review-pack labs.", TRAINER),
    ("2.0", "12 August 2026", "Expanded single-company curriculum; individual lab folders with realistic Office artifacts; planning, sustainability, HR, finance, Outlook, Cowork and Claude Code workflows.", TRAINER),
    ("2.1", "13 August 2026", "Added the learner LMS login page with OTP sign-in instructions and the default-password fallback for course-material downloads.", TRAINER),
    ("2.2", "13 August 2026", "Clarified Lab 01, added the Claude in Chrome Outlook web fallback and screenshot, and introduced an explicit Surface Readiness workbook.", TRAINER),
    ("2.3", "13 August 2026", "Expanded Lab 01 to install and compare Office add-ins and the Microsoft 365 connector, then added an approval-gated Claude in Chrome draft-and-send demonstration.", TRAINER),
    ("2.4", "13 August 2026", "Imported all seven screenshots from the root screenshot deck, including the connector directory, consent flow, Chrome draft and Sent Items confirmation; privacy-safe copies replace identifying screens.", TRAINER),
    ("3.0", "14 August 2026", "Rebuilt as a single HR scenario across 16 labs: setup, Excel screening and analysis, Word policy and hiring, PowerPoint reporting, Outlook replies via the connector and Claude for Chrome, then Skills, Cowork, Scheduled tasks and Projects. All labs run on local files with five plain-English steps each.", TRAINER),
    ("2.6", "13 August 2026", "Rebuilt the whole course around one HR scenario in plain English: 11 labs of five local steps each, no tenant or connector dependency, renamed lab folders and workbooks, and Lab 01 rewritten as a candidate shortlisting exercise that writes directly into Excel.", TRAINER),
    ("2.5", "13 August 2026", "Simplified Lab 01 to a trainer-led three-route demonstration, one controlled Outlook exercise and one learner checklist; moved the Prompt and Review Contract back to Lab 03. Corrected the Word, Excel and PowerPoint prompt examples to name the exact file each one requires, and marked the section as illustration rather than lab steps.", TRAINER),
]

# The Learner Guide contains authoritative non-video references only.  Supplied
# videos and community articles are retained in labs/README.md as research and
# further-learning sources, following the presentation-design rule.
LG_REFERENCES = [
    ("Claude for Microsoft 365 overview", "https://claude.com/claude-for-microsoft-365"),
    ("Claude for Microsoft 365 add-ins overview", "https://claude.com/docs/office-agents/overview"),
    ("Use Claude for Word", "https://claude.com/docs/office-agents/word"),
    ("Use Claude for Outlook", "https://claude.com/docs/office-agents/outlook"),
    ("Get started with Claude in Chrome", "https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome"),
    ("Claude in Chrome permissions guide", "https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide"),
    ("Use Claude in Chrome safely", "https://support.claude.com/en/articles/12902428-use-claude-in-chrome-safely"),
    ("Set up the Microsoft 365 connector", "https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector"),
    ("Connect to Microsoft 365", "https://support.claude.com/en/articles/15183774-connect-to-microsoft-365"),
    ("Use Claude for Microsoft 365 with third-party platforms", "https://claude.com/docs/office-agents/third-party-platforms"),
    ("Get started in Claude Cowork in three steps", "https://claude.com/resources/tutorials/get-started-in-claude-cowork-in-three-steps"),
    ("Connect Claude Code to tools via MCP", "https://code.claude.com/docs/en/mcp"),
    ("Copilot Cowork overview", "https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/"),
    ("Microsoft 365 Copilot with Anthropic models", "https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-anthropic-apps"),
    ("Syracuse University: Claude Microsoft 365 connector", "https://its.syr.edu/your-work-apps-meet-your-ai-assistant-using-claudes-microsoft-365-connector/"),
    ("Claude for Microsoft 365 setup and use cases", "https://justinmckelvey.com/blog/claude-for-microsoft-365"),
]

LAB_RESEARCH_SOURCES = [
    ("Video: Claude AI Is Now Inside Microsoft 365", "https://www.youtube.com/watch?v=EHsNORayS3I"),
    ("Video: Claude is Now Inside Microsoft 365 Copilot", "https://www.youtube.com/watch?v=f3aYoq6rKWk"),
    ("Video: Deploy Claude for Microsoft 365 via Admin Center", "https://www.youtube.com/watch?v=ApKpJTO9G1Y"),
    ("Video: Connect Claude to Microsoft 365", "https://www.youtube.com/watch?v=QTfoYDzqXn0"),
    ("Video: How to use Claude in Microsoft Word", "https://www.youtube.com/watch?v=Cktc5apkzH8"),
    ("Video: Claude in Microsoft 365 Copilot", "https://www.youtube.com/watch?v=_zkt0Uj3qdg"),
    ("Video: Activate Claude in Microsoft 365 Copilot", "https://www.youtube.com/watch?v=mmY0GoKFTDw"),
    ("Video: Claude Cowork Is Now in Copilot", "https://www.youtube.com/watch?v=KSncZG26qd4"),
    ("Video: Claude and Cowork in Microsoft 365", "https://www.youtube.com/watch?v=NnflVMXitag"),
    ("Anthropic Academy: Introduction to Claude Cowork", "https://academy.claude.com/courses/introduction-to-claude-cowork"),
    ("Anthropic Academy: Claude for Microsoft 365", "https://academy.claude.com/courses/introduction-to-claude-cowork/claude-for-microsoft-365"),
    ("Community guide: Claude Cowork and Microsoft 365", "https://claudecowork.im/blog/microsoft-365-integration"),
    ("Community tutorials: Claude Cowork", "https://claudecowork.im/blog/cluster/tutorials"),
    ("LinkedIn demonstration: Cowork in Microsoft 365 Copilot", "https://www.linkedin.com/posts/andersjensenorg_claude-cowork-in-copilot-how-to-turn-it-activity-7445809298204418048-oJli"),
]
