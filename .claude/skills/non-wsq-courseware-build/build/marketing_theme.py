#!/usr/bin/env python3
"""Re-theme the whole course as one marketing team's working day.

Every lab is now Lumina Living's marketing department doing marketing work:
campaign briefs, customer groups, channel results, the campaign inbox and the
campaign dashboard.  Technical vocabulary ("source register", "permission map",
"governance", "triage", "artifact") is replaced with words a marketer uses.
"""

TOPICS = [
    dict(
        num=1, code="01", title="Getting Claude Ready for Marketing Work",
        subtitle="Where to use Claude · what it may read · writing a request that works",
        weighting="24%",
        concepts=[
            "Three places to use Claude — inside Word, Excel and PowerPoint; in the Claude Desktop app; and in the browser. Each sees different things.",
            "The panel inside Office works on the file you already have open, and keeps your styles, formulas and slide layouts.",
            "The Claude Desktop app can read a whole folder at once, so it is the one to use when your answer spans several files.",
            "Marketing data is customer data. Decide what Claude may read, and what it may never change, before you start.",
            "Ask Claude to show its work — which file, which sheet, which line — so you can check a claim before it reaches a customer.",
            "You approve, not Claude. Nothing is sent, published or spent until a named person says yes.",
        ]),
    dict(
        num=2, code="02", title="Planning Campaigns and Customer Messages",
        subtitle="Campaign plan · customer groups · brand and offer wording · sign-off",
        weighting="28%",
        concepts=[
            "A campaign plan makes choices: which customers, which channels, what you will not spend on.",
            "Group customers by what they actually do, not by what is easy to describe.",
            "Every campaign needs an owner, a budget, a start date and one number that says whether it worked.",
            "Offer and brand wording carries risk. Claims about price, savings or results need someone to approve them.",
            "Work inside the company template so the plan looks like every other plan the team produces.",
            "Say plainly what you do not yet know, rather than filling the gap with a confident guess.",
        ]),
    dict(
        num=3, code="03", title="Campaign Numbers and the Story You Tell",
        subtitle="Channel results in Excel · what the numbers say · the leadership deck",
        weighting="25%",
        concepts=[
            "Keep the raw channel data, the assumptions and the results on separate sheets so anyone can follow the working.",
            "Use live formulas that point at the source data. A number typed in by hand cannot be checked or updated.",
            "Compare what you spent with what you planned, by month and by channel, before you explain the result.",
            "Pick the chart that answers the question. More charts is not more insight.",
            "Every slide title should say what you concluded, not name a topic.",
            "Put the source under any figure on a slide, so the room can challenge it.",
        ]),
    dict(
        num=4, code="04", title="Handling the Inbox and Repeating Work",
        subtitle="Sorting messages · replies for approval · one folder, one brief · the daily update",
        weighting="23%",
        concepts=[
            "Sort messages by what each one needs from you: a reply, someone else's decision, or nothing at all.",
            "Claude drafts the reply; you check the facts, the tone and the recipient, and you send it.",
            "Point Claude Desktop at one folder and it can pull a brief together from everything inside it.",
            "When files disagree, that disagreement is the finding. It is not Claude's job to settle it quietly.",
            "Work you repeat every week is worth automating once, with a backup taken before anything is overwritten.",
            "An automated update still needs a person to read it before it goes to anyone else.",
        ]),
]

LEARNING_OUTCOMES = [
    "LO1: Choose the right place to use Claude for a marketing task.",
    "LO2: Decide what customer and campaign information Claude may read, and what it may never change.",
    "LO3: Write a request that says what you want, what to use, what to leave alone and when to stop.",
    "LO4: Write a campaign plan in Word using only what the brief actually says.",
    "LO5: Turn a marketing brief into a one-page plan where every choice has an owner and a number.",
    "LO6: Draft customer-facing offer and brand wording that flags every claim needing approval.",
    "LO7: Build a channel performance analysis in Excel using live formulas.",
    "LO8: Build a leadership deck where every slide title states a conclusion.",
    "LO9: Sort a campaign inbox and draft one reply ready for approval.",
    "LO10: Have Claude read one folder and write a campaign brief that cites its sources.",
    "LO11: Automate a weekly campaign update and daily brief on your own computer.",
]

LO_TITLES = [
    "Pick the right place", "Decide what Claude reads", "Write a clear request",
    "Plan the campaign", "One-page plan", "Check the wording",
    "Channel numbers", "Tell the story", "Handle the inbox",
    "One folder, one brief", "Automate the update",
]
