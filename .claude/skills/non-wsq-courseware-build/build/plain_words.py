#!/usr/bin/env python3
"""Rewrite lab titles, goals and completion checks in plain English.

Trainers reported the labs read as jargon.  Words like "auditable",
"least-privilege", "decision-ready", "governance cadence" and "artifact" are
replaced with what the learner actually does and sees.  Only learner-facing
wording changes; the steps, files and structure are untouched.
"""

import re

from fix_meta import fmt, patch as _patch  # reuse the balanced-scan patcher

FIELDS = {
    1: dict(
        title="Find the Right Place to Use Claude",
        objective="Find the three places you can use Claude and record which ones work on your computer.",
        build="A completed checklist showing which places work, and one sentence saying which to use when.",
        test="Every row of the checklist has an answer, and your closing sentence says which place to use for editing a file you already have open, and which for searching across many files.",
    ),
    2: dict(
        title="Decide What Claude Is Allowed to Read",
        objective="Decide whether Claude should be allowed to read, or also change, each company information source.",
        build="A completed table showing, for each source, who uses it, whether Claude may read or also write, and who owns it.",
        test="All four sources have a read-or-write decision, an owner and a fallback, and anything Claude flagged as inconsistent has been fixed.",
    ),
    3: dict(
        title="Write a Prompt That Can Be Checked",
        objective="Write a prompt that says what you want, what to use, what not to change, and when to stop.",
        build="A filled-in prompt template plus a note on what made the good prompt better than the vague one.",
        test="You ran a vague request and a detailed one on the same file, and you can point to what the detailed prompt added: the file to use, what to keep, what to cite and where to stop.",
    ),
    4: dict(
        objective="Write an FY2027 marketing plan in Word using only what the company brief actually says.",
        build="A marketing plan in Word where every claim points back to the brief, and gaps are marked instead of guessed.",
        test="The plan keeps the document's existing styles, names three choices and one thing not to fund, and every claim either cites a heading in the brief or is marked 'evidence needed'.",
    ),
    5: dict(
        title="Turn a Brief into a One-Page Strategy",
        objective="Turn the company brief into a one-page strategy where every choice has an owner and a measure.",
        build="A one-page strategy in Word plus one decision recorded in the approval log.",
        test="Every strategic choice has a named owner, one measure and a Q1 milestone, and one decision with its approver is recorded in the log.",
    ),
    6: dict(
        title="Draft a Sustainability Section and an HR Policy",
        objective="Draft two sensitive documents that say plainly what cannot yet be evidenced.",
        build="A sustainability section and an HR policy draft, both marking what is unmeasured or needs legal review.",
        test="Every sustainability figure names its source and method or says 'not measured', and the HR draft keeps policy, procedure and points needing legal review clearly separate.",
    ),
    7: dict(
        title="Build a Financial Analysis in Excel",
        objective="Build an Actual versus Budget analysis in Excel using live formulas, not typed-in numbers.",
        build="An analysis sheet where every result is a formula that points back to the source data.",
        test="Two result cells checked in the formula bar show real formulas referencing the source ranges, and changing an assumption updates the analysis.",
    ),
    8: dict(
        title="Build an Executive Deck in PowerPoint",
        objective="Build a six-slide deck where every title states a conclusion, not a topic.",
        build="A six-slide deck in the company template with a source note on every slide showing a figure.",
        test="Every slide title states a conclusion, the company template and slide master are unchanged, and each figure has a source note or is flagged as untraceable.",
    ),
    9: dict(
        title="Sort an Inbox and Draft One Reply",
        objective="Sort a set of company messages by what each one needs, and draft one reply for approval.",
        build="Every message sorted into a category, one reply drafted, and the person who would approve it named.",
        test="Every message has a category, one reply under 120 words is written in the Draft_Reply column, and its approver is named. Nothing was sent.",
    ),
    10: dict(
        title="Let Claude Read a Folder and Write a Brief",
        objective="Point Claude Desktop at one folder on your computer and have it write a brief from those files.",
        build="A two-page management brief built only from the files in this folder, with the file name cited for every claim.",
        test="The brief cites a file name for every material claim, you checked two figures yourself against the workbook, and anything the files disagree on is reported rather than resolved.",
    ),
    11: dict(
        title="Automate a Workbook and a Daily Brief",
        objective="Use Claude Code to update a workbook and build a daily brief, all on your own computer.",
        build="An updated workbook with a backup, and a daily brief where every figure says where it came from.",
        test="The backup exists, the workbook's formulas still calculate, the brief is in the outputs folder, and every figure cites a workbook cell or a message ID.",
    ),
}


def main():
    import fix_meta
    fix_meta.FIELDS = FIELDS
    fix_meta.patch("data_domain1.py", [1, 2, 3])
    fix_meta.patch("data_domain2.py", [4, 5, 6])
    fix_meta.patch("data_domain3.py", [7, 8])
    fix_meta.patch("data_domain4.py", [9, 10, 11])


if __name__ == "__main__":
    main()
