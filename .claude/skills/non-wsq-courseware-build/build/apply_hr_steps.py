#!/usr/bin/env python3
"""Apply HR steps and HR case data to every lab."""

import sys

sys.path.insert(0, ".")

import fix_meta
import hr_steps

# Case data drives the briefs, the workbook contents and the deck cards, so it
# has to become HR too or the generated files stay retail/marketing.
CASES = {
    1: dict(department="Human Resources", sponsor="Head of HR",
            challenge="Work out which Claude options are usable on the HR team's own laptops.",
            decision="Which option do we use for which kind of HR task?",
            sources=["Trainer demonstration", "Your own laptop", "HR team laptops"],
            metrics=["Options checked", "Answers recorded", "Conclusion written"],
            outputs=["My_Checklist sheet"],
            controls=["Record only what you see", "Do not sign in to a work account", "No staff data used"]),
    2: dict(department="Human Resources", sponsor="Head of HR",
            challenge="Decide what Claude may read, and what it must never change, across the four places HR keeps staff information.",
            decision="For each place, may Claude read only, or also change what is stored?",
            sources=["Staff records folder", "Hiring files", "Payroll summary", "HR mailbox"],
            metrics=["Places reviewed", "Owners named", "Review dates set"],
            outputs=["What_Claude_May_Do sheet"],
            controls=["Read only unless HR head approves", "Every place has a named owner", "No staff names used in class"]),
    3: dict(department="Human Resources", sponsor="Head of HR",
            challenge="Get useful answers from Claude instead of confident guesses.",
            decision="What must a request include before we trust the answer?",
            sources=["HR brief", "Request checklist"],
            metrics=["Vague request tried", "Clear request tried", "Difference written down"],
            outputs=["Completed request checklist"],
            controls=["Claude shows text before changing a document", "Every fact names its heading"]),
    4: dict(department="Human Resources", sponsor="Head of HR",
            challenge="Decide which roles Lumina Living fills in FY2027 and which wait.",
            decision="Which roles do we fill now, and which do we hold back?",
            sources=["HR brief", "Team headcount list", "Salary bands", "Budget limit"],
            metrics=["Roles to fill", "Roles held back", "Cost against budget", "Start dates"],
            outputs=["FY2027 hiring plan"],
            controls=["No invented salary figures", "Cost stays within budget", "Head of HR approves"]),
    5: dict(department="Human Resources", sponsor="Head of HR",
            challenge="Turn a long brief into one page the leadership team can act on.",
            decision="What are we actually doing, who owns it, and by when?",
            sources=["HR brief", "Decision log"],
            metrics=["Actions listed", "Owners named", "Dates set"],
            outputs=["One-page people plan", "Decision log entry"],
            controls=["Every action has an owner", "Every action has a date", "No action without evidence"]),
    6: dict(department="Human Resources", sponsor="Head of HR",
            challenge="Draft staff-facing policy wording without accidentally giving legal advice.",
            decision="What can we publish now, and what must go to legal first?",
            sources=["HR brief", "Existing staff handbook"],
            metrics=["Sections drafted", "Points sent for legal advice", "Gaps marked"],
            outputs=["Leave policy section", "Flexible-work section"],
            controls=["Policy, practice and legal advice kept separate", "No legal conclusions stated", "Legal review before release"]),
    7: dict(department="Human Resources", sponsor="Head of HR",
            challenge="Explain to leadership why headcount and staff cost differ from plan.",
            decision="Where are we above or below plan, and why?",
            sources=["Staff list", "Headcount plan", "Assumptions"],
            metrics=["Headcount", "Staff cost", "Gap against plan", "Leavers"],
            outputs=["Headcount analysis sheet"],
            controls=["Formulas point at source data", "No typed-in totals", "Assumptions kept on one sheet"]),
    8: dict(department="Human Resources", sponsor="Head of HR",
            challenge="Give the leadership team a short update they can act on.",
            decision="What do we want leadership to decide after this update?",
            sources=["HR brief", "People numbers workbook", "Company template"],
            metrics=["Slides", "Conclusions stated", "Figures with a source"],
            outputs=["Six-slide leadership update"],
            controls=["Company template unchanged", "Every figure has a source note", "Untraceable figures flagged"]),
    9: dict(department="Human Resources", sponsor="Head of HR",
            challenge="Keep on top of staff questions without letting anything go out unchecked.",
            decision="Which messages need a reply from HR, and which need someone else to decide?",
            sources=["Staff messages sheet"],
            metrics=["Messages sorted", "Reply drafted", "Approver named"],
            outputs=["Sorted staff messages", "One draft reply"],
            controls=["Nothing is sent", "No invented dates or entitlements", "A named person approves the reply"]),
    10: dict(department="Human Resources", sponsor="Head of HR",
             challenge="Pull one summary together from several HR files without missing what they disagree on.",
             decision="What does the HR head need to know this week?",
             sources=["HR files in this folder"],
             metrics=["Files read", "Claims with a named file", "Disagreements reported"],
             outputs=["Two-page people summary"],
             controls=["Only files in this folder", "Every claim names its file", "Disagreements reported, not resolved"]),
    11: dict(department="Human Resources", sponsor="Head of HR",
             challenge="Stop rebuilding the same weekly people update by hand.",
             decision="Can the weekly update be produced the same way every week?",
             sources=["People tracker workbook", "Weekly input file", "Staff questions file"],
             metrics=["Workbook updated", "Backup taken", "Update produced", "Figures with a source"],
             outputs=["Updated people tracker", "Weekly people update"],
             controls=["Backup before writing", "Formulas preserved", "A person reads it before it goes out"]),
}


def main():
    files = {"data_domain1.py": [1, 2, 3], "data_domain2.py": [4, 5, 6],
             "data_domain3.py": [7, 8], "data_domain4.py": [9, 10, 11]}

    # 1) steps
    fix_meta.FIELDS = {n: dict(steps=hr_steps.STEPS[n]) for n in CASES}
    for path, nums in files.items():
        fix_meta.patch(path, nums)

    # 2) case data
    fix_meta.FIELDS = {n: dict(case=CASES[n]) for n in CASES}
    for path, nums in files.items():
        fix_meta.patch(path, nums)


if __name__ == "__main__":
    main()
