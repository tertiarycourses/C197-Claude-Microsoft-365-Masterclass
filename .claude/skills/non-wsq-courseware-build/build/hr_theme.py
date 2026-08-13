#!/usr/bin/env python3
"""Re-theme the whole course as one HR team's working week.

Every lab is Lumina Living's HR department doing HR work: a hiring plan, an
onboarding pack, leave and flexible-work policy, handbook wording, headcount
and turnover numbers, the HR inbox, and a weekly people update.

Wording rule: no "source register", "permission map", "governance",
"triage", "artifact" or "least privilege".  Say what the learner does.
"""

TOPICS = [
    dict(
        num=1, code="01", title="Getting Claude Ready for HR Work",
        subtitle="Where to use Claude · what it may read · asking for what you want",
        weighting="24%",
        concepts=[
            "Three places to use Claude — inside Word, Excel and PowerPoint; in the Claude Desktop app; and in the browser. Each one sees different things.",
            "The panel inside Office works on the file you already have open, and keeps your headings, formulas and slide layouts.",
            "The Claude Desktop app can read a whole folder at once, so use it when the answer spans several files.",
            "HR files hold information about real people. Decide what Claude may read, and what it must never change, before you start.",
            "Ask Claude to say where each fact came from — which file, which sheet, which line — so you can check it before it reaches a staff member.",
            "You decide, not Claude. Nothing is sent, published or approved until a named person says yes.",
        ]),
    dict(
        num=2, code="02", title="Hiring Plans, Policies and Staff Documents",
        subtitle="Hiring plan · leave and flexible-work policy · handbook wording · who signs off",
        weighting="28%",
        concepts=[
            "A hiring plan makes choices: which roles now, which can wait, and what the budget will not cover.",
            "Every role needs a hiring manager, a start date, a salary range and the reason the role exists.",
            "Policy wording carries real consequences. Anything about pay, leave, notice or conduct needs proper review before release.",
            "Keep three things apart: what the policy says, how it works day to day, and what needs legal advice.",
            "Work inside the company template so the document looks like every other HR document staff receive.",
            "Say plainly what you do not yet know, rather than filling the gap with a confident guess.",
        ]),
    dict(
        num=3, code="03", title="People Numbers and Reporting to Leadership",
        subtitle="Headcount and turnover in Excel · what the numbers say · the leadership update",
        weighting="25%",
        concepts=[
            "Keep the staff data, the assumptions and the results on separate sheets so anyone can follow the working.",
            "Use live formulas that point at the source data. A number typed in by hand cannot be checked or updated.",
            "Compare actual headcount and cost against plan, month by month and team by team, before you explain the result.",
            "Pick the chart that answers the question leadership asked. More charts is not more insight.",
            "Every slide title should say what you concluded, not name a topic.",
            "Put the source under any figure on a slide, so the room can challenge it.",
        ]),
    dict(
        num=4, code="04", title="Handling Staff Questions and Weekly Work",
        subtitle="Sorting the HR inbox · replies for approval · one folder, one summary · the weekly update",
        weighting="23%",
        concepts=[
            "Sort staff messages by what each one needs: a reply from you, a decision from someone else, or nothing at all.",
            "Claude drafts the reply; you check the facts, the tone and the recipient, and you are the one who sends it.",
            "Point Claude Desktop at one folder and it can pull a summary together from everything inside it.",
            "When two files disagree, that disagreement is the finding. It is not Claude's job to settle it quietly.",
            "Work you repeat every week is worth automating once, with a backup taken before anything is overwritten.",
            "An automated update still needs a person to read it before it goes to anyone else.",
        ]),
]

LEARNING_OUTCOMES = [
    "LO1: Choose the right place to use Claude for an HR task.",
    "LO2: Decide what staff information Claude may read, and what it must never change.",
    "LO3: Write a request that says what you want, what to use, what to leave alone and when to stop.",
    "LO4: Write a hiring plan in Word using only what the brief actually says.",
    "LO5: Turn an HR brief into a one-page plan where every action has an owner and a date.",
    "LO6: Draft leave and flexible-work policy wording that flags every point needing legal review.",
    "LO7: Build a headcount and turnover analysis in Excel using live formulas.",
    "LO8: Build a leadership update deck where every slide title states a conclusion.",
    "LO9: Sort the HR inbox and draft one reply ready for approval.",
    "LO10: Have Claude read one folder and write a people summary that says where each fact came from.",
    "LO11: Automate a weekly people update on your own computer.",
]

LO_TITLES = [
    "Pick the right place", "Decide what Claude reads", "Ask clearly",
    "Plan the hiring", "One-page plan", "Check the policy wording",
    "People numbers", "Tell leadership", "Handle the inbox",
    "One folder, one summary", "Automate the update",
]

# Per-lab replacements: title, plain goal, what you produce, and the finish check.
LABS = {
    1: dict(
        title="Find the Right Place to Use Claude",
        objective="Find the three places you can use Claude and record which ones work on your computer.",
        desc="Record which Claude surfaces are available to you, then use the Claude panel in Excel to review your own findings. Everything is local; no work account is required.",
        build="A completed checklist showing which places work, and one sentence saying which to use when.",
        test="Every row of the checklist has an answer, and your closing sentence says which place to use for editing a file you already have open, and which for looking across many files.",
    ),
    2: dict(
        title="Decide What Claude May Read",
        objective="Decide whether Claude should be allowed to read, or also change, each place HR keeps staff information.",
        desc="HR keeps staff information in four places. Decide what Claude may do with each one, compare the answer you get in Excel with the answer you get in the Claude Desktop app, and write down who owns each decision.",
        build="A completed table showing, for each place, who uses it, whether Claude may read or also change it, and who owns it.",
        test="All four places have a read-or-change decision, an owner and a fallback, and anything Claude flagged as inconsistent has been fixed.",
    ),
    3: dict(
        title="Ask Claude Clearly",
        objective="Write a request that says what you want, what to use, what not to change, and when to stop.",
        desc="Run a vague request and a clear one against the same HR brief, and see the difference for yourself.",
        build="A filled-in request template plus a note on what made the clear request better than the vague one.",
        test="You ran a vague request and a clear one on the same file, and you can point to what the clear one added: the file to use, what to keep, what to cite and where to stop.",
    ),
    4: dict(
        title="Write a Hiring Plan in Word",
        objective="Write an FY2027 hiring plan in Word using only what the HR brief actually says.",
        desc="Turn the HR brief into a hiring plan where every role has a reason, a manager and a date, and anything the brief does not say is marked rather than guessed.",
        build="A hiring plan in Word where every claim points back to the brief, and gaps are marked instead of guessed.",
        test="The plan keeps the document's existing headings, names the roles to fill and one role to defer, and every claim either cites a heading in the brief or is marked 'need to check'.",
    ),
    5: dict(
        title="Turn a Brief into a One-Page Plan",
        objective="Turn the HR brief into a one-page plan where every action has an owner and a date.",
        desc="Separate what the brief proves from what it only suggests, then turn it into a one-page plan leadership can act on.",
        build="A one-page people plan in Word plus one decision recorded in the approval log.",
        test="Every action has a named owner, one measure and a date, and one decision with its approver is recorded in the log.",
    ),
    6: dict(
        title="Draft Leave and Flexible-Work Policy Wording",
        objective="Draft policy wording that says plainly which points need legal review before release.",
        desc="Draft two pieces of staff-facing policy wording, keeping what the policy says, how it works day to day, and what needs legal advice clearly apart.",
        build="A leave policy section and a flexible-work section, both marking what needs legal review before release.",
        test="Each section keeps policy, day-to-day practice and points needing legal review clearly separate, and no legal conclusion has been stated.",
    ),
    7: dict(
        title="Build a Headcount Analysis in Excel",
        objective="Build a headcount and cost analysis in Excel using live formulas, not typed-in numbers.",
        desc="Compare actual headcount and staff cost against plan, month by month and team by team, using formulas that point at the source data.",
        build="An analysis sheet where every result is a formula that points back to the source data.",
        test="Two result cells checked in the formula bar show real formulas pointing at the source data, and changing an assumption updates the analysis.",
    ),
    8: dict(
        title="Build a Leadership Update in PowerPoint",
        objective="Build a six-slide people update where every title states a conclusion, not a topic.",
        desc="Turn the HR brief and the headcount numbers into a short leadership update, using the company template.",
        build="A six-slide update in the company template with a source note on every slide showing a figure.",
        test="Every slide title states a conclusion, the company template is unchanged, and each figure has a source note or is flagged as not yet checked.",
    ),
    9: dict(
        title="Sort the HR Inbox and Draft One Reply",
        objective="Sort a set of staff messages by what each one needs, and draft one reply for approval.",
        desc="Work through a set of fictional staff messages held in a local workbook. Claude sorts them by what each one needs and drafts one reply for you to review. No mailbox is used and nothing is sent.",
        build="Every message sorted, one reply drafted, and the person who would approve it named.",
        test="Every message has an answer in the Action column, one reply under 120 words is written in the Draft_Reply column, and its approver is named. Nothing was sent.",
    ),
    10: dict(
        title="Let Claude Read a Folder and Write a Summary",
        objective="Point Claude Desktop at one folder and have it write a people summary from those files.",
        desc="Give Claude Desktop access to this lab folder only, and have it pull a two-page summary together from the HR files inside it, saying where each fact came from.",
        build="A two-page people summary built only from the files in this folder, naming the file behind every claim.",
        test="The summary names a file for every claim, you checked two figures yourself against the workbook, and anything the files disagree on is reported rather than settled.",
    ),
    11: dict(
        title="Automate the Weekly People Update",
        objective="Use Claude Code to update a workbook and build a weekly people update on your own computer.",
        desc="Run two supplied scripts through Claude Code: one updates the people workbook from a local file, the other builds the weekly update. Everything runs on your computer.",
        build="An updated workbook with a backup, and a weekly update where every figure says where it came from.",
        test="The backup exists, the workbook's formulas still calculate, the update is in the outputs folder, and every figure names a workbook cell or a message reference.",
    ),
}
