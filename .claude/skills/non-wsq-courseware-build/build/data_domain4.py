"""Topic 4 — agentic coordination with Outlook, Cowork and Claude Code."""

DOMAIN4 = [
    dict(
        num=8, topic=4,
        title='Sort the HR Inbox and Draft One Reply',
        objective='Sort a set of staff messages by what each one needs, and draft one reply for approval.',
        desc='Work through a set of fictional staff messages held in a local workbook. Claude sorts them by what each one needs and drafts one reply. Then the Microsoft 365 connector turns that reply into a real Outlook draft — which you review and send yourself.',
        build='Every message sorted, one reply drafted, the person who would approve it named, and the reply created as an Outlook draft ready for review.',
        services="Claude for Outlook beta, Outlook categories, thread citations, reply templates, calendar, approval queue",
        deck_flow=["Classify", "Summarise with citations", "Select approved template", "Draft in native form", "Review recipients and send"],
        deck_cards=[
            ("Rules before generation", "Define category, priority, SLA, reply eligibility and escalation before asking Claude to draft."),
            ("Thread evidence", "Capture decisions, owners and deadlines with citations to the specific message."),
            ("Auto-draft, not auto-send", "Claude for Outlook leaves drafts and invitations in Outlook for the authorised user."),
            ("Consequential details", "Recipients, attachments, dates, amounts and promises receive explicit human checks."),
        ],
        case=dict(
            department='Human Resources',
            sponsor='Head of HR',
            challenge='Keep on top of staff questions without letting anything go out unchecked.',
            decision='Which messages need a reply from HR, and which need someone else to decide?',
            sources=[
                'Staff messages sheet',
            ],
            metrics=[
                'Messages sorted',
                'Reply drafted',
                'Approver named',
            ],
            outputs=[
                'Sorted staff messages',
                'One draft reply',
            ],
            controls=[
                'Nothing is sent',
                'No invented dates or entitlements',
                'A named person approves the reply',
            ],
        ),
        prerequisites=[
            'Excel installed, with the Claude panel available from the ribbon.',
            'Lumina-Living-Lab-08-Staff-Questions.xlsx from this folder.',
            'No mailbox, no Outlook and no work account are required. Nothing in this lab is sent.',
        ],
        steps=[
            ('Open Lumina-Living-Lab-08-Staff-Questions.xlsx from this lab folder and click the Staff_Messages tab. These are fictional messages from Lumina Living staff. Everything here is local; you will not open Outlook and nothing is ever sent.', ''),
            ('Open the Claude panel in Excel and ask Claude to sort the messages. Read the answer on screen.', 'Read the messages on the Staff_Messages sheet in this open workbook. Sort them into four groups: needs a reply from HR today, needs a decision from someone else, is just information, and needs nothing. Give your reason and say which Message_ID you mean for each one. Do not change the sheet.'),
            ('In the Action column of the Staff_Messages tab, write the group you agree with for each message.', ''),
            ('Pick one message that needs a reply and ask Claude to draft it. Read the draft on screen.', "Draft a short reply to the message I have selected on the Staff_Messages sheet. Use only what that message and this workbook actually say. Keep it under 120 words, say clearly what happens next and who is doing it, and write 'need to check' rather than inventing any date, amount or entitlement. Show me the draft. Do not send anything and do not change the workbook."),
            ('Now put the reply into Outlook. Open Claude Desktop, where you connected Microsoft 365 in Lab 0, and ask it to create the draft. It creates a draft only — nothing is sent, and you are still the one who presses Send. If your connector is not available, record it and read the draft you wrote in Excel instead; the approval lesson is the same.', "Using the Microsoft 365 connector, create a draft reply in Outlook to the message I chose on the Staff_Messages sheet.\n\nUse the reply I wrote in the Draft_Reply column, exactly as it stands. Do not reword it.\nAddress it to the sender of that message only. Use the original subject with 'Re:' in front.\n\nCreate it as a draft. Do not send it. Tell me where to find it when you are done."),
        ],
        test='Every message has an answer in the Action column, one reply under 120 words is written in the Draft_Reply column, its approver is named, and the reply exists as an unsent draft in Outlook or the connector state is recorded. Nothing was sent.',
        troubleshooting=[
            ('You expected to open Outlook to read the messages', 'The messages are in the workbook so the lab runs on any computer. Outlook is used only at the end, to create the draft.'),
            ('The connector is not available', 'Record it and stop at the Excel draft. Every earlier step works without Outlook.'),
            ('Claude reworded my reply', "Ask again and say 'use the text exactly as it stands, do not reword'. The point is that you approve the words, not Claude."),
            ('Claude sent the message', 'It should not. The prompt says create a draft and do not send. If it sent, report it and check the recipient immediately.'),
            ('Claude invents a figure or a date', "Re-run the prompt; it instructs Claude to write 'need to check' instead of inventing."),
        ],
        challenge="Create an escalation rule for messages that contain a financial commitment, legal interpretation or personal data.",
        reflection="Which part of email handling should remain human even if drafting becomes nearly automatic?",
    ),
    dict(
        num=9, topic=4,
        title='Read a Whole Folder and Write the Summary',
        objective='Have Claude read across a folder of HR files and write one summary, reporting what the files disagree on rather than resolving it.',
        desc="A quarter's worth of HR reports sits in one folder as PDFs, with a CSV of the numbers. No single file answers the question. Claude reads them all and writes one summary, naming the file behind every claim.",
        build='A two-page people summary built only from the folder, naming the file behind every claim, with disagreements reported rather than settled.',
        services="Claude Cowork, work folder, Projects, plugins, Microsoft 365 connector, multi-step execution, approvals",
        deck_flow=["Scope the folder", "Connect approved context", "Plan the task", "Watch and steer", "Review files in Microsoft 365"],
        deck_cards=[
            ("Bounded workspace", "Give Cowork one project folder or Project, not uncontrolled access to unrelated files."),
            ("Connector supplies context", "Search approved SharePoint, OneDrive, Outlook and Teams evidence through delegated permissions."),
            ("Cowork executes over steps", "It can inspect inputs, create real files, update the plan and surface checkpoints."),
            ("Office add-ins finish the work", "Open generated Word, Excel and PowerPoint files in the native apps for tracked review and approval."),
        ],
        case=dict(
            department='Human Resources',
            sponsor='Head of HR',
            challenge='Add a file of your own to the folder that contradicts one of the others, and see whether Claude notices.',
            decision='What does the HR head need to know this week?',
            sources=[
                'HR files in this folder',
            ],
            metrics=[
                'Files read',
                'Claims with a named file',
                'Disagreements reported',
            ],
            outputs=[
                'Two-page people summary',
            ],
            controls=[
                'Only files in this folder',
                'Every claim names its file',
                'Disagreements reported, not resolved',
            ],
        ),
        prerequisites=[
            'Lab 0 completed, so Claude Desktop is installed and signed in.',
            'The hr-quarter-files folder from this lab folder: three PDF reports and a CSV.',
            'No work account or connector is needed. Everything is read from your own computer.',
        ],
        steps=[
            ("Open the hr-quarter-files folder inside this lab folder. It holds what an HR team actually receives in a quarter: three reports as PDFs — headcount, exit interview themes and the hiring pipeline — plus a CSV of team numbers. Skim them. No single file answers the question 'how are our people doing?', and you cannot edit a PDF to find out.", ''),
            ('Open the Claude Desktop app. Select the plus button, then Add files or photos, and give it access to this lab folder. The Office panel can only see one open file; Desktop can read the whole folder at once, which is what this job needs.', ''),
            ('Ask Claude to read across the folder first, before writing anything. Read what it found, and pay attention to the last part of the answer.', 'Read every file in the hr-quarter-files folder here. There are three PDF reports and a CSV.\n\nFor each file tell me: its name, what it covers, and which question about our people it helps answer.\n\nThen tell me anything the files disagree on, or any point one file raises that the others miss. Name the file behind every point. Do not change any file.'),
            ('The files do not fully agree. The headcount report says total headcount is 88; add up the CSV and see what you get. The exit interview note also warns that flexible working will not fix the warehouse problem, which the headcount report does not mention. Claude should have surfaced both. If it did not, ask it directly what the numbers add up to.', ''),
            ('Now ask for the summary. Check two figures against the CSV yourself, then write at the end of the summary which claims you verified and which still need the Head of HR to confirm.', "Using only the files in the hr-quarter-files folder, write a two-page people summary for the Head of HR.\n\nCover: where headcount stands against plan, why people are leaving, and what the hiring pipeline looks like.\n\nTake numbers from the CSV and the headcount report, and wording from the notes. Name the file and section behind every claim.\n\nWhere two files disagree, say so and give both figures — do not pick one. Where the files say nothing, write 'need to check'.\n\nSave it as Lumina-Living-People-Summary.docx in this folder."),
        ],
        test='The summary covers headcount against plan, why people are leaving and the hiring pipeline; every claim names its file; the disagreement between the headcount report and the CSV is reported with both figures; two figures were checked by hand; and the closing note says what still needs the Head of HR to confirm.',
        troubleshooting=[
            ('Claude cannot see the files', 'Give it access to this lab folder, not to a single file. Use the plus button, then Add files or photos.'),
            ('Claude picked one figure and moved on', "That is the finding. Ask it directly: 'what does the CSV add up to, and does that match the headcount report?'"),
            ('The summary cites a file that does not exist', 'Ask it to list the exact file names it used, and compare them with the folder.'),
            ('Claude resolved a contradiction on its own', 'The prompt requires it to report both figures. Re-run it and say so again — an AI that quietly picks a number is the risk this lab is about.'),
        ],
        challenge="Turn the approved hand-off workflow into a reusable Cowork skill outline with explicit inputs, checks and approval points.",
        reflection='Which mattered more here: what the files said, or what they disagreed about?',
    ),
    dict(
        num=11, topic=4,
        title='Build a Daily HR Routine with Cowork',
        objective='Turn a week of scattered HR work into a repeatable daily routine, and let Cowork run it across your files.',
        desc='Ten things landed on the HR desk this week. Cowork finds what actually repeats, writes a daily routine, applies it back to the week, and produces the Monday brief. No terminal, no scripts.',
        build="A written daily routine covering inbox, reporting and chasing; this week's work assigned an owner and a deadline; and today's daily HR report.",
        services='Claude Cowork, Claude Desktop, Excel, Word',
        deck_flow=[
            'A week of scattered work',
            'Find what repeats',
            'Write the routine',
            'Apply it to the week',
            "Run it: today's report",
        ],
        deck_cards=[
            ('Cowork works across files', 'Give it a folder and it moves between the workbook and the documents on its own.'),
            ('Routine beats memory', 'Work that repeats every week should not depend on someone remembering it.'),
            ('Gaps are findings', 'If the routine cannot place a task, that is a hole in the routine, not a mistake to paper over.'),
            ('A person still reads it', 'The brief goes nowhere until the Head of HR has seen it.'),
        ],
        case=dict(
            department='Human Resources',
            sponsor='Head of HR',
            challenge='Add one more item to This_Week that the routine does not cover, and see whether Cowork spots the gap.',
            decision='What should the HR daily routine be, and who owns each step?',
            sources=[
                "This week's HR inbox",
                'The empty routine sheet',
            ],
            metrics=[
                'Repeating work identified',
                'Routine written',
                'Every item owned',
                'Monday brief produced',
            ],
            outputs=[
                'A daily HR routine',
                'A Monday morning brief',
            ],
            controls=[
                'No invented owners or deadlines',
                'Gaps recorded rather than filled',
                'Head of HR reads the brief before it is acted on',
            ],
        ),
        prerequisites=[
            'Lab 0 completed, so Claude Desktop is installed and signed in.',
            'Cowork available in Claude Desktop. It is on paid plans; if you do not have it, watch the trainer and follow along in the workbook.',
            'Lumina-Living-Lab-11-This-Week.xlsx from this folder. Everything is local; no terminal and no scripts.',
        ],
        steps=[
            ('Open Lumina-Living-Lab-11-This-Week.xlsx from this lab folder and look at the This_Week sheet. Ten things landed on the HR desk this week — new starters, leavers, leave requests, probation reviews and questions. Three columns are empty. Doing this by hand every week is the problem this lab solves.', ''),
            ('Open Claude Desktop and switch to Cowork. Give it access to this lab folder so it can work across the files. Ask it to look at the week and find the work that actually repeats.', 'Read Lumina-Living-Lab-11-This-Week.xlsx in this folder and look at the This_Week sheet.\n\nIt lists everything that landed on the HR desk this week: new starters, leavers, leave requests, probation reviews and questions.\n\nGroup them by what kind of work they are, and tell me which ones happen every single week no matter what. Those are the ones worth turning into a routine. Do not change the sheet yet.'),
            ('Ask Cowork to design the daily routine and write it into the workbook. Notice the three things it must include: checking the inbox, producing the daily report, and chasing what is overdue. Those are the jobs that happen every day whatever else lands.', 'Now design the daily HR routine from that list.\n\nWrite it into the Daily_Routine sheet of the same workbook, one row per step.\n\nIt must include these three things, because they happen every day whatever else does:\n- checking the HR inbox and sorting what came in\n- the daily report to the Head of HR\n- chasing anything that has passed its deadline\n\nFor each row give: when it happens, what to do in one plain sentence, where the information is (name the sheet or file), and who checks it before anything goes out.\n\nKeep it to work that genuinely repeats. Anything that happened only once this week is not a routine.'),
            ("Now ask it to apply that routine back to this week's list. Every row should get an action, an owner and a deadline — or be marked as not covered yet, which tells you the routine has a gap.", "Using the routine you just wrote, fill in the three empty columns on the This_Week sheet for every row: what must happen, who owns it, and by when.\n\nBase the owner and the deadline on the routine, not on guesswork. Where the routine does not cover something, write 'not in the routine yet' rather than inventing an owner."),
            ("Finally, ask Cowork to run the routine and produce today's report. Open it, check two items against the workbook, and decide whether you would send it to the Head of HR as it stands. This is the routine working: the same report, the same way, every morning.", "Using the routine, produce today's daily HR report as a new Word document called Lumina-Living-Daily-HR-Report.docx in this folder.\n\nThree short sections:\n- What came in today, from the This_Week sheet\n- What is due or overdue, with the owner named\n- What needs a decision from the Head of HR\n\nName the row behind every item. Where something has no owner, say so plainly rather than filling the gap. Keep it to one page — it is read standing up."),
        ],
        test='The Daily_Routine sheet covers checking the inbox, the daily report and chasing overdue items, each with when, what, where and who. Every row of This_Week has an action, an owner and a deadline, or is marked as not covered. Lumina-Living-Daily-HR-Report.docx exists, fits one page, and names the row behind every item.',
        troubleshooting=[
            ('Cowork is not in Claude Desktop', 'It is available on paid plans. If it is missing, do the same steps in a normal Claude Desktop conversation with folder access — the routine is the point, not the mode.'),
            ('Cowork cannot see the workbook', 'Give it access to this lab folder, not to a single file.'),
            ('It invented an owner', "Ask again and say 'write not in the routine yet where the routine does not cover something'. An invented owner is worse than an admitted gap."),
            ('The routine includes one-off work', 'Ask it to remove anything that happened only once this week. A routine is what repeats.'),
        ],
        challenge="Add a dry-run flag that reports proposed cell changes and mail-query scope without writing any output.",
        reflection='Which part of your own week would still work if you were away tomorrow?',
    ),
]


# ---------------------------------------------------------------------------
# Advanced block — the Claude features that turn one-off work into a repeatable
# way of working: Skills, the Microsoft 365 connector, and plugins.
# ---------------------------------------------------------------------------
SKILL_TEXT = """You are shortlisting candidates for an HR role at Lumina Living.

When I give you a sheet of applicants:
1. Read the Experience notes column for every row.
2. In the Shortlist column write Yes only where the notes show the person has
   actually used the named tool or skill in their job.
3. Write No where they have not, and also No where they only studied it or
   attended a course.
4. In the Why column, copy the exact words from the notes that made you decide.
5. Change no other column, and tell me any row you found genuinely borderline."""

DOMAIN4 += [
    dict(
        num=12, topic=4,
        title='Automate an HR Pipeline with a Project',
        objective="Set up a Claude project that holds the HR team's materials and rules, then run a repeatable pipeline inside it.",
        desc='A project keeps the policy library, the staff data and the house rules in one workspace. Set it up once, then run the new starter pipeline twice without attaching a file or restating a rule.',
        build='A Lumina Living HR project with materials and standing instructions, and a new starter pipeline run twice from it.',
        services='Claude Projects, Claude Desktop, project instructions, uploaded materials',
        deck_flow=[
            'Create the project',
            'Upload the materials',
            'Set the standing rules',
            'Run the pipeline',
            'Run it again in one line',
        ],
        deck_cards=[
            ('A project holds context', 'Materials and instructions live in the workspace, not in each prompt.'),
            ('Skills carry the how', 'A skill is a method; a project is the material that method works on.'),
            ('Set the rules once', 'The standing instructions apply to every conversation in the project.'),
            ('Repeatable, not automatic', 'The pipeline repeats itself; a person still reads what comes out.'),
        ],
        case=dict(
            department='Human Resources',
            sponsor='Head of HR',
            challenge='Add one more policy to the project and see whether the next pipeline run picks it up.',
            decision='Can the new starter workflow run the same way every time?',
            sources=[
                'The policy library',
                'The staff workbook',
                'The quarter files',
            ],
            metrics=[
                'Project created',
                'Materials uploaded',
                'Rules set',
                'Pipeline run twice',
            ],
            outputs=[
                'A new starter checklist',
                'A welcome note',
                'A daily report line',
            ],
            controls=[
                'Only project materials used',
                'Every fact names its file',
                'Nothing sent without sign-off',
            ],
        ),
        prerequisites=[
            'Lab 0 completed, so Claude Desktop is installed and signed in.',
            'Labs 5, 6 and 9 completed, so you have the materials to upload.',
            'Projects available in your Claude plan. If it is missing, follow the trainer and use a normal conversation with folder access.',
        ],
        steps=[
            ('Open Claude Desktop and select Projects in the sidebar, then New project. Name it Lumina Living HR. A project is a workspace that remembers its materials and its rules, so you stop re-uploading and re-explaining the same things every time.', ''),
            ("Upload the materials the HR team works from. Take them from the earlier lab folders: the three policy PDFs from Lab 5's hr-policy-library, the staff workbook from Lab 6, and the quarter files from Lab 9. This is the HR team's shared context, in one place.", ''),
            ('Set the project instructions. In the project, open its settings and paste the text below into the custom instructions. These are the standing rules for everything the project produces — the same rules you have been typing into every prompt so far.', "You are working as part of the Lumina Living HR team.\n\nWhenever you produce anything for this project:\n- Use only the materials uploaded to this project. Never invent a date, an amount, a notice period or an entitlement.\n- Name the file and section behind every fact.\n- Where the materials are silent, write 'need to check' instead of guessing.\n- Never state a legal conclusion. Flag it for review instead.\n- Plain English, short sentences.\n- Nothing is sent, published or approved without a named person signing it off."),
            ('Now run a real HR pipeline inside the project. Start a new conversation in it and ask for the new starter workflow. Notice what you did not have to do: no files attached, no rules restated.', "Using only the materials in this project, run the new starter pipeline for Rachel Sim, who starts in Online on 3 March.\n\nProduce, in order:\n1. A checklist of everything HR must do before her first day, with the owner for each item\n2. A short welcome note to her, in our house tone\n3. A one-line entry for the daily HR report saying what is still outstanding\n\nName the file behind every rule you apply. Where the materials do not cover something, say 'need to check' rather than filling the gap."),
            ('Run it again for a second new starter, in one line. The project holds the materials and the rules, so the pipeline repeats itself. Check both outputs name their source files, then decide which parts of this you would let run without a person reading it first.', 'Now run the same pipeline for Terrence Wong, who starts in Office on 10 March. Do not ask me for the rules again.'),
        ],
        test="A project named Lumina Living HR exists with the policy PDFs, the staff workbook and the quarter files uploaded, and custom instructions set. The new starter pipeline produced a checklist with owners, a welcome note and a report line for two different starters, every fact naming its source file, with gaps marked 'need to check'.",
        troubleshooting=[
            ('Projects is not in the sidebar', 'It depends on your Claude plan. Follow the trainer demonstration; the idea of standing context still applies.'),
            ('Claude ignores the project instructions', 'Open the project settings and check they saved. Instructions apply to new conversations in the project, not to ones started outside it.'),
            ('It used a file that is not in the project', 'Ask it to list the files it used. Anything outside the project is a finding.'),
            ('The second run asked for the rules again', 'Check you started the conversation inside the project, not in a new window.'),
        ],
        challenge="Write a second Skill for a task you repeat every week, and give it to a colleague to run.",
        reflection='Which is more valuable for your own team: a saved method, or a shared workspace?',
    ),
    dict(
        num=10, topic=4,
        title='Draft an Outlook Reply with Claude in Chrome',
        objective='Use Claude for Chrome to draft a reply inside Outlook on the web, review it, and send it yourself.',
        desc='Claude in Chrome works on the page in front of you. Open a staff message in Outlook web, have Claude draft the reply into the real compose box, check it, and decide whether it goes.',
        build='A reviewed reply drafted in Outlook on the web, sent only after you approved it or deliberately left in Drafts.',
        services='Claude for Chrome, Outlook on the web, per-action approval',
        deck_flow=[
            'Open Outlook in Chrome',
            'Open the message',
            'Claude drafts into the reply box',
            'Check it in Outlook',
            'You press Send',
        ],
        deck_cards=[
            ('Chrome sees the page', 'Claude in Chrome works on whatever is open in the browser, so the message must be on screen.'),
            ('Approve each action', 'Manually approve means Claude asks before it touches the page. Never turn that off.'),
            ('The draft is real', 'It lands in the Outlook compose box, not in a chat window.'),
            ('Sending stays yours', 'Claude drafts. A person reads it and presses Send.'),
        ],
        case=dict(
            department='Human Resources',
            sponsor='Head of HR',
            challenge='Ask Claude to draft a reply to a question the handbook does not answer, and check it refuses to invent one.',
            decision='Is this reply accurate enough to send, and who approves it?',
            sources=[
                'The open staff message',
                'The Lumina Living handbook',
            ],
            metrics=[
                'Draft produced in Outlook',
                'Recipient checked',
                'Facts traced',
                'Send decision recorded',
            ],
            outputs=[
                'One reviewed Outlook reply',
            ],
            controls=[
                'Manual approval mode only',
                'No invented dates or entitlements',
                'A person presses Send',
            ],
        ),
        prerequisites=[
            'Lab 0 completed, with Claude for Chrome installed, pinned and set to Manually approve.',
            'Google Chrome. Claude for Chrome does not work in other browsers.',
            'Outlook on the web, signed in with your training account.',
            'If Chrome or the extension is unavailable, follow the trainer demonstration and record it; Lab 8 covers the same reply work locally.',
        ],
        steps=[
            ('Open Google Chrome and sign in to Outlook on the web with your training account. Open the Claude for Chrome side panel — you installed and pinned it in Lab 0. Check the permission mode says Manually approve, never Skip all approvals.', ''),
            ('Open one staff message that needs a reply. Use a message from your own training mailbox, or the trainer will point you at one. Claude in Chrome reads the page you are looking at, so the message must be open on screen before you ask for anything.', ''),
            ('Type the request into the Claude panel on the right of your browser window — the Claude for Chrome side panel, not the Outlook message box. When Chrome asks whether Claude may act on this page, choose Allow for this action only. Watch the draft appear in the Outlook compose window: not in the panel, but in the real reply box.', "Draft a reply to the message that is open in Outlook.\n\nUse only what that message and the Lumina Living handbook actually say. Keep it under 120 words, plain English.\n\nSay clearly what happens next and who is doing it. Where you do not have a fact — a date, an amount, an entitlement — write 'need to check' rather than inventing one.\n\nLeave the draft open in Outlook. Do not send it."),
            ('Read the draft in Outlook itself, not in the chat. Check the recipient, the subject, and every fact. Then ask Claude to check its own work before you commit to anything.', 'Before I send this, check it for me.\n\nTell me: is the recipient right, does anything in the reply state a rule the handbook does not contain, and is there any figure or date you cannot trace?\n\nDo not change the draft. Just tell me what you find.'),
            ('You decide what happens next. If the reply is right and the trainer approves it, press Send yourself. If anything is wrong, correct it in Outlook or leave it in Drafts. Claude drafted it; you are the one who sends it, and that has been true in every lab on this course.', ''),
        ],
        test="A reply was drafted into the Outlook compose box, the recipient and every fact were checked, anything unsupported is marked 'need to check', and the message was either sent after approval or deliberately left in Drafts. Permission mode stayed on Manually approve throughout.",
        troubleshooting=[
            ('Claude cannot see the message', 'Refresh the Outlook tab and make sure the message is open on screen. Claude in Chrome reads the visible page.'),
            ('Chrome did not ask for approval', 'Check the permission mode in the side panel. It must be Manually approve; never use Skip all approvals on a real mailbox.'),
            ('The draft appeared only in the chat', "Ask again and say 'draft it into the Outlook reply box, not here'."),
            ('Claude invented an entitlement', 'That is the finding. Correct it, and note that the same rule applies here as in every other lab: no fact without a source.'),
            ('The extension will not install', 'It needs Chrome and a paid plan. Record it and watch the trainer; Lab 8 teaches the same review discipline without a browser.'),
        ],
        challenge="Name one HR question you could only answer if Claude could see the whole team's files, not just yours.",
        reflection='What would have to be true before you let a reply go out without reading it?',
    ),
    dict(
        num=13, topic=4,
        title="Add Skills and Connectors to the Project",
        objective="Bring your saved skill and the Microsoft 365 connector into the HR project, so one request runs the whole workflow.",
        desc="The project holds the materials and the rules. Add the hr-policy-draft skill so it knows your method, and the Microsoft 365 connector so it can reach real files and mail. Then run the full HR workflow end to end.",
        build="An HR project with materials, standing rules, a skill and a connector, running one request that produces a policy draft, a summary and an Outlook draft.",
        services="Claude Projects, Claude Skills, Microsoft 365 connector, Cowork",
        deck_flow=["Materials and rules", "Add the skill", "Add the connector", "Run the whole workflow", "Decide what stays automatic"],
        deck_cards=[
            ("Three things, one workspace", "Materials say what to work on, the skill says how, the connector says where else to look."),
            ("One request, many steps", "The project can draft, summarise and prepare mail without you moving between apps."),
            ("More reach, more care", "A connector reads real company content, so the read-only boundary matters more, not less."),
            ("Automatic is a choice", "Decide deliberately which steps may run unattended and which always need a person."),
        ],
        case=dict(
            department="Human Resources", sponsor="Head of HR",
            challenge="The HR workflow still runs across four different places, so nobody can hand it over.",
            decision="Which parts of the HR workflow can run from one request, and which must stay manual?",
            sources=["The HR project materials", "The hr-policy-draft skill", "Microsoft 365 through the connector"],
            metrics=["Skill available in the project", "Connector reachable", "Workflow run end to end", "Manual steps agreed"],
            outputs=["A policy draft", "A people summary", "An Outlook draft ready for review"],
            controls=["Read-only connector use", "Every fact names its source", "Nothing sent without a named approver"],
        ),
        prerequisites=[
            "Lab 12 completed, with the Lumina Living HR project set up.",
            "Lab 5 completed, so the hr-policy-draft skill exists.",
            "Lab 0 completed, with the Microsoft 365 connector connected \u2014 or recorded as unavailable, in which case the local files still work.",
        ],
        steps=[
            ("Open the Lumina Living HR project you built in Lab 12. Check its materials and instructions are still there. You are about to give it two more things: a method, and reach beyond its own uploads.", ""),
            ("Add your skill to the project. In the project, open the plus menu, then Skills, and enable hr-policy-draft \u2014 the skill you created in Lab 5. The project now knows both what to work on and how you want it written.", ""),
            ("Add the Microsoft 365 connector. In Claude Desktop, open Customize > Connectors and confirm Microsoft 365 is connected. Inside the project, ask Claude what it can now reach. If the connector is unavailable, record it and continue with the uploaded materials only.", "What materials and tools do you have access to in this project? List the uploaded files, any skills that are enabled, and whether you can reach Microsoft 365. Do not use any of them yet."),
            ("Now run the whole workflow from one request. Watch how many separate steps it does without you moving between apps.", "Using this project, run the March HR workflow for me.\n\nDo three things in order:\n1. Draft the flexible working policy section, applying my hr-policy-draft skill\n2. Write a short summary of where headcount stands, from the uploaded quarter files\n3. Prepare a draft email to the Head of HR with both attached for review, and leave it unsent\n\nName the file behind every fact. Where the materials are silent, write 'need to check'. Do not send anything."),
            ("Read all three outputs. Check the policy follows your skill's rules, the summary names its files, and the email is a draft and nothing more. Then write down which of these three steps you would let run unattended tomorrow morning, and which you would always read first. That judgment is what you take back to work.", ""),
        ],
        test="The project has the hr-policy-draft skill enabled and the connector state recorded. One request produced a policy draft following the skill's rules, a headcount summary naming its source files, and an unsent Outlook draft. Nothing was sent, and you have written which steps may run unattended and which always need a person.",
        troubleshooting=[
            ("Skills is not available inside the project", "Check the skill exists in Settings > Skills. If skills are not on your plan, paste the rules from Lab 5's standard into the project instructions instead."),
            ("The connector is not reachable", "Record it and run the workflow on the uploaded materials alone. Nothing in this lab depends on the connector working."),
            ("Claude did all three steps but skipped the citations", "Ask again and name the rule: 'name the file behind every fact'. A project's instructions apply, but a long request can still drift."),
            ("It sent the email", "It should not. The request says leave it unsent. If it sent, check the recipient immediately and report it \u2014 that is exactly why the approval gate exists."),
        ],
        challenge="Remove the skill from the project, run the same request, and compare the policy draft.",
        reflection="Now that one request can do three jobs, what would you want to see before you trusted it unattended?",
    ),
    dict(
        num=14, topic=4,
        title='Upload a Shared Skill for Slides',
        objective='Import a slide standard written by someone else, so every HR deck in the team looks the same.',
        desc='Your company has a house standard for decks, written once and shared as a file. Upload it as a skill and apply it to a weak draft deck.',
        build='An uploaded deck-design-standard skill, and a rebuilt deck where every title states a conclusion.',
        services='Claude Skills, Claude for PowerPoint, Upload a skill',
        deck_flow=[
            'A standard written once',
            'Upload it',
            'Apply it to a weak deck',
            'Compare with your own version',
            'Choose the right method',
        ],
        deck_cards=[
            ('Upload a skill', 'Use this when the standard already exists and the team should share it.'),
            ('One house standard', "Everyone's deck looks like the company wrote it."),
            ('Read before you upload', "A shared skill applies someone else's rules to your work."),
            ('Three ways to create', 'Write it, have Claude create it, or upload one someone else wrote.'),
        ],
        case=dict(
            department='Human Resources',
            sponsor='Head of HR',
            challenge="Write your own team's deck standard as a file and share it with one colleague to upload.",
            decision='Should the deck standard be shared as one file everyone imports?',
            sources=[
                'The house deck standard file',
                'The draft deck in this folder',
            ],
            metrics=[
                'Skill uploaded',
                'Deck rebuilt',
                'Method chosen',
            ],
            outputs=[
                'A rebuilt leadership deck',
            ],
            controls=[
                'Keep the company slide master',
                'Source note under every figure',
                'Flag any figure that cannot be traced',
            ],
        ),
        prerequisites=[
            'Lab 7 completed, so you have built a deck by hand.',
            'PowerPoint installed, with the Claude panel available from the ribbon.',
            'A Claude account you can sign in to on claude.ai. Skills is available on paid plans.',
            'Lumina-Living-Lab-14-Draft-Deck.pptx and deck-design-standard.md from this folder.',
        ],
        steps=[
            ('Open Lumina-Living-Lab-14-Draft-Deck.pptx from this lab folder. It is a six-slide HR update where every title names a topic instead of stating a conclusion. Your company has a house standard for decks, and it has been shared with you as a file.', ''),
            ('Open deck-design-standard.md from this lab folder and read it. This is a skill written by someone else — the same rules you applied by hand in Lab 7, written down once for the whole team.', ''),
            ('In the Claude panel, select the plus button, then Skills, then Manage skills. On claude.ai select Add, then choose Upload a skill, and upload deck-design-standard.md. This is how a team shares one standard instead of everyone writing their own.', ''),
            ('Go back to PowerPoint. Select the plus button, then Skills, then /deck-design-standard. Watch every slide title change from a topic to a conclusion, and a source note appear under each figure.', '/deck-design-standard'),
            ('Compare the deck with the version you built by hand in Lab 7. Write one sentence in the speaker notes of slide 1: which of the three ways of creating a skill — writing the instructions, letting Claude create it, or uploading one — you would use for your own team, and why.', ''),
        ],
        test="The deck-design-standard skill was uploaded from the supplied file, running it changed every slide title to a conclusion and added source notes, the slide master is unchanged, and slide 1's speaker notes say which of the ways of creating a skill you would use and why.",
        troubleshooting=[
            ('Upload a skill will not accept the file', 'It expects a Markdown file. Use deck-design-standard.md exactly as supplied.'),
            ('The skill changed the slide master', 'Undo, and check the standard file says to keep the master. A shared skill is only as safe as its rules.'),
            ('Titles still name topics', 'Ask it to rewrite only the titles, and quote the rule from the standard back to it.'),
        ],
        challenge="Pick one weekly HR task and decide whether it needs a plugin, a Skill, or just a clear request.",
        reflection="When is uploading someone else's standard better than writing your own?",
    ),
]
