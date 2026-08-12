"""Single source of truth for C197 Claude Microsoft 365 Masterclass.

The course is a one-day, non-WSQ commercial masterclass.  Slides teach the
operating model, decisions and process architecture.  Detailed procedures,
copy-ready prompts and commands live only in the Learner Guide and lab folders.
All company names, people, messages and figures are fictional training data.
"""

TITLE = "Claude Microsoft 365 Masterclass (C197)"
SHORT_TITLE = "Claude Microsoft 365 Masterclass (C197)"
COURSE_CODE = "C197"
VERSION = "v2.0"
VERSION_DATE = "12 August 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Jim Gan Chiu Liang (JL)"
DAYS = 1
MODE = "Instructor-led, company-scenario workshops and hands-on practical labs"
DARK_THEME = False

COMPANY = "Lumina Living Pte Ltd"
COMPANY_CONTEXT = (
    "Lumina Living is a fictional Singapore omnichannel home-and-lifestyle company "
    "with retail, e-commerce and marketplace operations. Learners join its Business "
    "Transformation Office to prepare an integrated FY2027 planning and management pack."
)

LEARNING_OUTCOMES = [
    "LO1: Select the right Claude and Microsoft 365 operating surface for a governed company task.",
    "LO2: Connect approved Microsoft 365 context and map permissions, sources and evidence boundaries.",
    "LO3: Direct Claude with an auditable prompt contract and a human approval gate.",
    "LO4: Produce a decision-ready marketing plan in Word from approved company evidence.",
    "LO5: Develop an aligned strategic plan with choices, initiatives, owners, measures and risks.",
    "LO6: Draft a sustainability report section and HR policy using source, legal and management review controls.",
    "LO7: Build a formula-driven financial analysis and executive dashboard in Excel.",
    "LO8: Create a highly visual strategic and marketing PowerPoint with native Excel charts and evidence traceability.",
    "LO9: Triage Outlook messages and prepare approval-based replies without bypassing the human send gate.",
    "LO10: Use Claude Cowork with Microsoft 365 context to coordinate a multi-file planning workflow.",
    "LO11: Use Claude Code and approved connectors to update Excel, search Outlook and produce a daily management brief.",
]

LO_TITLES = [
    "Choose the right Claude surface", "Connect governed context", "Prompt with an audit trail",
    "Plan marketing", "Shape strategy", "Draft sustainability and HR content",
    "Analyse finance in Excel", "Tell the story in PowerPoint", "Coordinate Outlook safely",
    "Orchestrate with Claude Cowork", "Automate with Claude Code",
]

TOPICS = [
    dict(
        num=1, code="01", title="Governed Foundations for Claude and Microsoft 365",
        subtitle="Operating surfaces · Microsoft 365 connector · permissions · evidence · prompting · human approval",
        weighting="24%", concepts=[
            "Four operating surfaces — distinguish Claude for Microsoft 365 add-ins, the Microsoft 365 connector in Claude, Anthropic Claude Cowork, and Claude-powered experiences inside Microsoft 365 Copilot.",
            "Open-file context — the Word, Excel, PowerPoint and Outlook add-ins work with the active item and preserve native structures such as styles, formulas and slide masters.",
            "Connected work context — the Microsoft 365 connector can search authorised SharePoint, OneDrive, Outlook and Teams content; optional write tools require additional tenant consent.",
            "Least privilege — access follows the signed-in user's existing permissions; broad access is not a substitute for a well-scoped business task.",
            "Evidence contract — every material claim names its source location, confidence and unresolved gap before the output is polished.",
            "Human accountability — reviewed changes, formulas, recipients and approval records make AI-assisted work defensible.",
        ]),
    dict(
        num=2, code="02", title="Company Planning, Reporting and Policy Work",
        subtitle="Marketing planning · strategic planning · sustainability reporting · HR policy · management review",
        weighting="28%", concepts=[
            "Marketing planning — connect business goals, customer segments, channel choices, campaign actions, budget and measurable outcomes.",
            "Strategic planning — turn evidence into explicit choices, initiatives, owners, dependencies, targets and review dates.",
            "Sustainability reporting — define the reporting boundary, method, source owner and limitation before drafting a credible narrative.",
            "HR policy — separate policy intent, operational procedure and legal interpretation; require authorised HR and legal review before release.",
            "Template fidelity — work inside approved Word styles and tables so outputs fit the company's document system rather than becoming detached chat text.",
            "Management review — label facts, calculations, assumptions and recommendations so decision makers can challenge each layer.",
        ]),
    dict(
        num=3, code="03", title="Financial Analysis and Executive Storytelling",
        subtitle="Excel modelling · controls · KPI dashboard · native charts · strategic and marketing PowerPoint",
        weighting="25%", concepts=[
            "Financial model architecture — separate assumptions, transaction data, calculations, outputs and review notes so changes remain traceable.",
            "Formula-first analysis — use dynamic formulas, tables and pivot-ready structures instead of pasted totals or unexplained AI answers.",
            "Decision-led dashboard — combine a small set of KPIs, trends, variances and definitions around the questions management must answer.",
            "Chart integrity — choose the visual for the question, keep native Excel sources, verify scale and units, and avoid implying causation without evidence.",
            "Message-first presentation — every slide title states a conclusion; supporting detail goes into speaker notes, appendix or source register.",
            "Beyond one-click slides — professional value comes from an editable company template, native charts, coherent narrative, source traceability and deliberate visual hierarchy.",
        ]),
    dict(
        num=4, code="04", title="Agentic Coordination with Outlook, Cowork and Claude Code",
        subtitle="Outlook triage and replies · Claude Cowork · Claude Code · Excel updates · email search · daily brief",
        weighting="23%", concepts=[
            "Outlook control — Claude can triage and draft, but Claude for Outlook leaves replies and invitations in native compose forms for the authorised user to review and send.",
            "Claude Cowork — a task-oriented Claude desktop mode that works across scoped folders, Projects, plugins and connected tools to produce real files over multiple steps.",
            "Cowork plus Microsoft 365 — retrieve approved organisational context through the connector, work in a bounded project folder, then review the resulting Office files in the native add-ins.",
            "Copilot Cowork is distinct — Microsoft's Cowork experience lives inside Microsoft 365 Copilot and has its own licensing, governance and action-approval model even when Anthropic models are used.",
            "Claude Code automation — local scripts and approved MCP connectors can update a workbook, search relevant mail and assemble a repeatable daily brief with explicit tool approvals.",
            "Safe automation boundary — read and draft first, validate recipients and versions, and reserve consequential write or send actions for explicit approval.",
        ]),
]

DAY_THEMES = {1: "From governed Claude setup to a connected Lumina Living planning, analysis and automation workflow"}

def SCHEDULE(lab_titles):
    return {1: (DAY_THEMES[1], [
        ("9:30", "9:45", 15, "admin", "Welcome, course orientation, company scenario and environment readiness"),
        ("9:45", "10:10", 25, "topic", "TOPIC 01 — Governed Foundations for Claude and Microsoft 365"),
        ("10:10", "11:15", 65, "lab", "Hands-on: " + lab_titles([1, 2, 3])),
        ("11:15", "11:30", 15, "break", "Tea break"),
        ("11:30", "11:55", 25, "topic", "TOPIC 02 — Company Planning, Reporting and Policy Work"),
        ("11:55", "13:10", 75, "lab", "Hands-on: " + lab_titles([4, 5, 6])),
        ("13:10", "14:10", 60, "lunch", "Lunch break"),
        ("14:10", "14:35", 25, "topic", "TOPIC 03 — Financial Analysis and Executive Storytelling"),
        ("14:35", "15:25", 50, "lab", "Hands-on: " + lab_titles([7])),
        ("15:25", "15:40", 15, "break", "Tea break"),
        ("15:40", "16:20", 40, "lab", "Hands-on: " + lab_titles([8])),
        ("16:20", "16:40", 20, "topic", "TOPIC 04 — Agentic Coordination with Outlook, Cowork and Claude Code"),
        ("16:40", "17:10", 30, "lab", "Hands-on: " + lab_titles([9])),
        ("17:10", "17:45", 35, "lab", "Hands-on: " + lab_titles([10])),
        ("17:45", "18:15", 30, "lab", "Hands-on: " + lab_titles([11])),
        ("18:15", "18:30", 15, "recap", "Integrated workflow review, transfer to work and next steps"),
    ])}

COURSE_OVERVIEW = dict(
    section_title="The Lumina Living Management Challenge",
    concepts_title="One Company, One Connected Evidence Chain",
    concepts=[
        "Plan the year — translate the company's growth ambition into marketing priorities, strategic initiatives and governed policies.",
        "Model the economics — test revenue, margin, budget and scenario assumptions in an auditable Excel workbook.",
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
        ("Plans and policies", ["Marketing plan", "Strategic plan", "Sustainability and HR drafts"]),
        ("Analysis and story", ["Financial model", "Executive dashboard", "Strategic and marketing deck"]),
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
    examples=[
        dict(app="Word", title="Draft a decision-ready strategy section",
             prompt="Using the open FY2027 strategy brief, draft only the 'Strategic choices' section for the Executive Committee. Preserve the existing Heading 1/2 styles. For each choice include rationale, owner, measure and Q1 milestone. Use only facts stated in the brief; cite the source heading and flag missing evidence. Show proposed text before editing the document."),
        dict(app="Excel", title="Build an auditable financial view",
             prompt="Using tblFinance in the open workbook, build a formula-driven Actual vs Budget analysis by month and channel. Include Revenue, Gross Profit, Gross Margin and Operating Contribution. Use native formulas or pivots, cite source ranges, keep assumptions on the Assumptions sheet, and do not paste hardcoded totals. Before editing, list the formulas and checks you will apply."),
        dict(app="PowerPoint", title="Create an executive planning story",
             prompt="Using the open company template, the approved strategy document and verified Excel dashboard, build an eight-slide Executive Committee story. Use conclusion-led titles, one message per slide, native editable charts linked to the approved summary ranges, and concise speaker notes. Preserve the slide master and brand rules. Add a source note to each data slide and flag any figure that does not reconcile."),
    ],
)

LAB_SLUGS = {
    1: "choose-and-activate-the-right-claude-surface",
    2: "connect-microsoft-365-context-and-permissions",
    3: "build-an-auditable-prompt-and-review-contract",
    4: "create-a-company-marketing-plan-in-word",
    5: "develop-a-strategic-plan-with-owners-and-measures",
    6: "draft-sustainability-reporting-and-hr-policy",
    7: "build-financial-analysis-and-an-excel-dashboard",
    8: "create-an-executive-strategy-and-marketing-deck",
    9: "triage-and-prepare-approved-outlook-replies",
    10: "coordinate-the-planning-pack-with-claude-cowork",
    11: "automate-excel-outlook-and-a-daily-brief-with-claude-code",
}

LAB_DURATIONS = {1: 20, 2: 25, 3: 20, 4: 25, 5: 25, 6: 25, 7: 50, 8: 40, 9: 30, 10: 35, 11: 30}

LAB_SHOTS = {
    n: [(f"lab-{n:02d}-artifact.png", "Claude-Generated Company Work Sample", "A rendered preview of the realistic Word, Excel or PowerPoint artifact supplied in this lab folder.")]
    for n in range(1, 12)
}

SAMPLE_GALLERIES = [
    dict(title="Claude-Generated Planning and Policy Samples", kicker="REALISTIC COMPANY WORK",
         items=[(4, "FY2027 Marketing Plan"), (5, "Three-Year Strategic Plan"), (6, "Sustainability and HR Drafts")]),
    dict(title="Claude-Generated Analysis and Executive Samples", kicker="NATIVE OFFICE ARTIFACTS",
         items=[(7, "Excel Financial Dashboard"), (8, "Strategy and Marketing PowerPoint"), (9, "Outlook Thread and Reply Pack")]),
]

DASHBOARD_EXHIBIT = dict(
    title="Inside the Claude-Generated Excel Dashboard",
    kicker="READABLE NATIVE EXCEL CHARTS",
    kpis="lab-07-kpis.png",
    charts=[
        ("lab-07-revenue-chart.png", "Actual vs Budget", "Tests whether growth is on plan and where monthly variance emerges."),
        ("lab-07-contribution-chart.png", "Contribution by Channel", "Separates revenue scale from contribution quality for resource decisions."),
    ],
)

LG_INTRO = (
    "This Learner Guide accompanies C197 and contains the complete procedures for eleven connected "
    "company activities. It is the operational companion to the concept-led slide deck."
)
LG_INTRO2 = (
    COMPANY_CONTEXT + " Every activity uses the same evidence chain so the marketing plan, strategy, "
    "policies, financial dashboard, presentation, Outlook hand-off, Cowork task and Claude Code daily brief remain consistent."
)
LG_SETUP = dict(
    needs=[
        "A current Windows or Mac laptop with Chrome or Edge, Microsoft 365 Word, Excel, PowerPoint and Outlook.",
        "A paid Claude plan for Claude for Word, Excel, PowerPoint and Outlook; a trainer-approved upload fallback may be used when an add-in is unavailable.",
        "Claude desktop with Cowork access for Lab 10 and Claude Code installed for Lab 11.",
        "An organisational Microsoft 365 account in an Entra tenant. The Microsoft 365 connector requires administrator consent; personal Outlook.com accounts are not supported.",
        "The self-contained Office files and templates inside each labs/lab-NN-*/ folder.",
    ],
    verify_text="Confirm the visible availability of every required surface before class. Missing add-ins, connector consent or Cowork access are real environment states and require the authorised administrator or the documented fallback.",
    verify_code="claude --version  ·  claude mcp list  ·  open Word / Excel / PowerPoint / Outlook  ·  verify the Claude task pane",
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
    "Lab 7 contains the master financial model and dashboard; Lab 8 contains the executive strategy-and-marketing deck that incorporates its verified charts.",
    "Lab 11 also contains a safe local automation starter for Excel updates and daily-brief generation; Microsoft 365 search uses the approved connector visible in Claude Code.",
]

LG_WRAPUP = dict(
    title="Wrap-Up — One Governed Company Workflow",
    intro="You have built a connected Lumina Living planning and management pack rather than a collection of isolated AI demonstrations.",
    sections=[
        dict(title="Business outputs", bullets=[
            "Marketing, strategy, sustainability and HR drafts that use company templates and named reviewers.",
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
]

VERSION_HISTORY = [
    ("1.0", "27 July 2026", "Initial release.", TRAINER),
    ("1.1", "12 August 2026", "Visual redesign with current Office add-ins and connected review-pack labs.", TRAINER),
    ("2.0", VERSION_DATE, "Expanded single-company curriculum; individual lab folders with realistic Office artifacts; planning, sustainability, HR, finance, Outlook, Cowork and Claude Code workflows.", TRAINER),
]

# The Learner Guide contains authoritative non-video references only.  Supplied
# videos and community articles are retained in labs/README.md as research and
# further-learning sources, following the presentation-design rule.
LG_REFERENCES = [
    ("Claude for Microsoft 365 overview", "https://claude.com/claude-for-microsoft-365"),
    ("Set up the Microsoft 365 connector", "https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector"),
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
