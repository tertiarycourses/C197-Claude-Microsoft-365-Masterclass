# Lab 12 — Automate an HR Pipeline with a Project

**Topic 04:** Staff Questions, Repeatable Work and Advanced Claude  |  **Day 1**  |  **Approx. 20 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update.

A project keeps the policy library, the staff data and the house rules in one workspace. Set it up once, then run the new starter pipeline twice without attaching a file or restating a rule.

## Goal

Set up a Claude project that holds the HR team's materials and rules, then run a repeatable pipeline inside it.

## What you'll build

A Lumina Living HR project with materials and standing instructions, and a new starter pipeline run twice from it.

**Tools and techniques:** Claude Projects, Claude Desktop, project instructions, uploaded materials

## Company use case

- **Department:** Human Resources
- **Sponsor:** Head of HR
- **Business challenge:** Add one more policy to the project and see whether the next pipeline run picks it up.
- **Decision:** Can the new starter workflow run the same way every time?
- **Evidence:** The policy library; The staff workbook; The quarter files
- **Measures:** Project created; Materials uploaded; Rules set; Pipeline run twice
- **Controls:** Only project materials used; Every fact names its file; Nothing sent without sign-off

## Files in this lab folder

- `Lumina-Living-Lab-12-HR-Brief.docx`
- `Lumina-Living-Lab-12-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-12-Working-Workbook.xlsx`
- `Lumina-Living-Lab-12-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Lab 0 completed, so Claude Desktop is installed and signed in.
- Labs 5, 6 and 9 completed, so you have the materials to upload.
- Projects available in your Claude plan. If it is missing, follow the trainer and use a normal conversation with folder access.

## Process map

Create the project → Upload the materials → Set the standing rules → Run the pipeline → Run it again in one line

## Steps

### Step 1

Open Claude Desktop and select Projects in the sidebar, then New project. Name it Lumina Living HR. A project is a workspace that remembers its materials and its rules, so you stop re-uploading and re-explaining the same things every time.

### Step 2

Upload the materials the HR team works from. Take them from the earlier lab folders: the three policy PDFs from Lab 5's hr-policy-library, the staff workbook from Lab 6, and the quarter files from Lab 9. This is the HR team's shared context, in one place.

### Step 3

Set the project instructions. In the project, open its settings and paste the text below into the custom instructions. These are the standing rules for everything the project produces — the same rules you have been typing into every prompt so far.

**Prompt to give Claude:**

```text
You are working as part of the Lumina Living HR team.

Whenever you produce anything for this project:
- Use only the materials uploaded to this project. Never invent a date, an amount, a notice period or an entitlement.
- Name the file and section behind every fact.
- Where the materials are silent, write 'need to check' instead of guessing.
- Never state a legal conclusion. Flag it for review instead.
- Plain English, short sentences.
- Nothing is sent, published or approved without a named person signing it off.
```

### Step 4

Now run a real HR pipeline inside the project. Start a new conversation in it and ask for the new starter workflow. Notice what you did not have to do: no files attached, no rules restated.

**Prompt to give Claude:**

```text
Using only the materials in this project, run the new starter pipeline for Rachel Sim, who starts in Online on 3 March.

Produce, in order:
1. A checklist of everything HR must do before her first day, with the owner for each item
2. A short welcome note to her, in our house tone
3. A one-line entry for the daily HR report saying what is still outstanding

Name the file behind every rule you apply. Where the materials do not cover something, say 'need to check' rather than filling the gap.
```

### Step 5

Run it again for a second new starter, in one line. The project holds the materials and the rules, so the pipeline repeats itself. Check both outputs name their source files, then decide which parts of this you would let run without a person reading it first.

**Prompt to give Claude:**

```text
Now run the same pipeline for Terrence Wong, who starts in Office on 10 March. Do not ask me for the rules again.
```

## Test it

A project named Lumina Living HR exists with the policy PDFs, the staff workbook and the quarter files uploaded, and custom instructions set. The new starter pipeline produced a checklist with owners, a welcome note and a report line for two different starters, every fact naming its source file, with gaps marked 'need to check'.

## Troubleshooting

- **Projects is not in the sidebar.** It depends on your Claude plan. Follow the trainer demonstration; the idea of standing context still applies.
- **Claude ignores the project instructions.** Open the project settings and check they saved. Instructions apply to new conversations in the project, not to ones started outside it.
- **It used a file that is not in the project.** Ask it to list the files it used. Anything outside the project is a finding.
- **The second run asked for the rules again.** Check you started the conversation inside the project, not in a new window.

## Challenge

Write a second Skill for a task you repeat every week, and give it to a colleague to run.

## Reflection

Which is more valuable for your own team: a saved method, or a shared workspace?

## Deliverable

A Lumina Living HR project with materials and standing instructions, and a new starter pipeline run twice from it.

## Current product references

- [Claude for Microsoft 365 overview](https://claude.com/claude-for-microsoft-365)
- [Claude for Microsoft 365 add-ins overview](https://claude.com/docs/office-agents/overview)
- [Set up the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector)
- [Connect to Microsoft 365](https://support.claude.com/en/articles/15183774-connect-to-microsoft-365)
- [Use Claude for Microsoft 365 with third-party platforms](https://claude.com/docs/office-agents/third-party-platforms)
- [Get started in Claude Cowork in three steps](https://claude.com/resources/tutorials/get-started-in-claude-cowork-in-three-steps)
- [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)
- [Copilot Cowork overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/)
- [Microsoft 365 Copilot with Anthropic models](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-anthropic-apps)
- [Syracuse University: Claude Microsoft 365 connector](https://its.syr.edu/your-work-apps-meet-your-ai-assistant-using-claudes-microsoft-365-connector/)
- [Claude for Microsoft 365 setup and use cases](https://justinmckelvey.com/blog/claude-for-microsoft-365)

---

*Claude Microsoft 365 Masterclass (C197) · C197 · Version v3.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
