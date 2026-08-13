#!/usr/bin/env python3
"""Realign lab metadata with the local-only, five-step lab rewrite.

Labs 1, 2, 9, 10 and 11 still described tenant work — connectors, mailboxes,
sending mail — that the steps no longer do.  This rewrites the descriptive
fields so the guide, the PDFs and the deck all tell the same local story.
"""

import re

FIELDS = {
    1: dict(
        objective="Recognise the three ways to reach Claude and record which are available on your own machine.",
        desc="Record which Claude surfaces are available to you, then use the Claude panel in Excel to review your own findings. Everything is local; no work account is required.",
        build="One completed Lab01_Checklist recording each surface state and a one-sentence conclusion.",
        test="Every row of Lab01_Checklist has a recorded state, and the closing sentence names which surface edits an open document and which searches across many files.",
        prerequisites=[
            "A Claude account with the Office add-in available.",
            "Word, Excel or PowerPoint installed on your own computer.",
            "The Claude Desktop app installed. You only look at its Connectors screen; you do not connect anything.",
            "All files for this lab are in this folder. Nothing is stored in the cloud.",
        ],
        troubleshooting=[
            ("The Claude panel is missing in Office", "Open Home > Add-ins on Windows or Tools > Add-ins on Mac. If installation is blocked by policy, record Admin approval required in the checklist; that is a valid result for this lab."),
            ("Claude Desktop shows no Microsoft 365 connector", "Record Not available. This lab only asks you to observe the screen; the labs never require a connected work account."),
            ("You cannot complete a row", "Record Not checked and note why. An honest record of your own environment is the deliverable."),
        ],
    ),
    2: dict(
        desc="Use the Claude panel in Excel to assess a supplied register of four information sources, decide the access each needs, and reconcile your decisions against the permission map. All data is in one local workbook.",
        test="All four rows of Source_Register have a status, the Management_Control tab records an owner and scope for each source, and any disagreement Claude found has been resolved.",
        prerequisites=[
            "Lab 1 completed.",
            "Excel installed, with the Claude panel available from the ribbon.",
            "Lumina-Living-Lab-02-Working-Workbook.xlsx from this folder. No work account and no connector are needed.",
        ],
        troubleshooting=[
            ("You cannot find the Source Register", "It is not a separate file. Open Lumina-Living-Lab-02-Working-Workbook.xlsx and click the Source_Register tab at the bottom of the Excel window."),
            ("The Claude panel is missing in Excel", "Open Home > Add-ins on Windows or Tools > Add-ins on Mac, then select Claude."),
            ("Claude changed the sheet", "Every prompt in this lab ends with an instruction not to change the workbook. Undo with Ctrl+Z or Cmd+Z and run the prompt again exactly as written."),
        ],
    ),
    9: dict(
        objective="Triage a supplied inbox and prepare an approval-ready reply without sending anything.",
        desc="Work through a set of fictional Lumina Living messages held in a local workbook. Claude sorts them by required action and drafts one reply for review. Outlook is never opened and nothing is sent.",
        build="A triaged inbox with a category for every message and one drafted reply recorded with its named approver.",
        test="Every message on the Inbox tab has a category, one reply is drafted in the Draft_Reply column, and the approver for that reply is named.",
        prerequisites=[
            "Excel installed, with the Claude panel available from the ribbon.",
            "Lumina-Living-Lab-09-Working-Workbook.xlsx from this folder.",
            "No mailbox, no Outlook and no work account are required. Nothing in this lab is sent.",
        ],
        troubleshooting=[
            ("You expected to open Outlook", "This lab is deliberately local. The Inbox tab of the workbook holds the fictional messages so the lab works on any computer."),
            ("Claude invents a figure or a date", "Re-run the prompt exactly as written; it instructs Claude to write 'evidence needed' instead of inventing. Report any invented value as a finding."),
            ("The reply is too long", "The prompt caps the reply at 120 words. Ask Claude to shorten it and state the next action and owner only."),
        ],
    ),
    10: dict(
        prerequisites=[
            "The Claude Desktop app installed on your own computer.",
            "This lab folder available locally, with its Word and Excel files.",
            "You will give Claude access to this folder only. No cloud account, connector or upload is used.",
        ],
        troubleshooting=[
            ("Claude cannot see the files", "Confirm you granted access to this lab folder in Claude Desktop, and that you opened the folder itself rather than a single file."),
            ("The brief cites a file that does not exist", "That is a finding. Ask Claude to list the exact file names it used, and compare them with the folder."),
            ("Claude resolves a contradiction on its own", "The prompt requires it to report disagreements rather than settle them. Re-run the prompt and record what it flags."),
        ],
    ),
    11: dict(
        objective="Use Claude Code to update a local workbook and generate a cited daily brief entirely on your own computer.",
        desc="Run two supplied local scripts through Claude Code: one updates a control workbook from a local CSV, the other builds a daily brief from that workbook and a local findings file. No connector, no mailbox and no network service are used.",
        build="An updated control workbook with a backup, and a generated daily brief in the outputs folder with a citation for every figure.",
        test="The workbook backup exists, existing formulas still calculate, the generated brief is in the outputs folder, and every KPI exception cites a workbook cell and every mail finding cites a message ID.",
        troubleshooting=[
            ("Claude Code cannot find a file", "Confirm the terminal is open in this lab folder. Every path in the prompts is relative to this folder."),
            ("The script fails to run", "Ask Claude Code to read the script and report the error before changing anything. Do not let it rewrite the workbook until the run succeeds."),
            ("The brief has an uncited figure", "That is a finding. The prompt requires a workbook cell reference for every KPI exception; ask Claude Code to add the citation or remove the figure."),
        ],
    ),
}


def fmt(value, indent=" " * 8):
    if isinstance(value, str):
        return repr(value)
    if isinstance(value, dict):
        inner = "\n".join(f"{indent}    {k}={fmt(v, indent + '    ')}," for k, v in value.items())
        return "dict(\n" + inner + f"\n{indent})"
    if isinstance(value, list) and value and isinstance(value[0], tuple):
        inner = "\n".join(f"{indent}    ({', '.join(repr(x) for x in t)})," for t in value)
        return "[\n" + inner + f"\n{indent}]"
    inner = "\n".join(f"{indent}    {v!r}," for v in value)
    return "[\n" + inner + f"\n{indent}]"


def patch(path, nums):
    src = open(path).read()
    for num in nums:
        anchor = src.index(f"num={num}, topic=")
        # The activity dict ends at the closing "    )," of this dict entry.
        stop = src.index("\n    ),", anchor)
        chunk = src[anchor:stop]
        for key, value in FIELDS[num].items():
            m = re.search(rf"^(\s*){key}=", chunk, re.M)
            if not m:
                print(f"  !! lab {num}: could not locate {key}")
                continue
            # Scan forward from the '=' balancing brackets/quotes so the value
            # ends exactly at its own trailing comma — never at a later key's.
            i = chunk.index("=", m.start()) + 1
            depth, in_str, quote, esc = 0, False, "", False
            while i < len(chunk):
                ch = chunk[i]
                if in_str:
                    if esc:
                        esc = False
                    elif ch == "\\":
                        esc = True
                    elif ch == quote:
                        in_str = False
                elif ch in "\"'":
                    in_str, quote = True, ch
                elif ch in "[({":
                    depth += 1
                elif ch in "])}":
                    if depth == 0:
                        break
                    depth -= 1
                elif ch == "," and depth == 0:
                    break
                i += 1
            end = i + 1 if i < len(chunk) and chunk[i] == "," else i
            chunk = chunk[:m.start()] + f"{m.group(1)}{key}={fmt(value)}," + chunk[end:]
        src = src[:anchor] + chunk + src[stop:]
    open(path, "w").write(src)
    print("Patched", path, nums)


if __name__ == "__main__":
    patch("data_domain1.py", [1, 2])
    patch("data_domain4.py", [9, 10, 11])
