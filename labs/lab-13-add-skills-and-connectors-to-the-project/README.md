# Lab 13 — Add Skills and Connectors to the Project

**Topic 04:** Staff Questions, Repeatable Work and Advanced Claude  |  **Day 1**  |  **Approx. 20 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update.

The project holds the materials and the rules. Add the hr-policy-draft skill so it knows your method, and the Microsoft 365 connector so it can reach real files and mail. Then run the full HR workflow end to end.

## Goal

Bring your saved skill and the Microsoft 365 connector into the HR project, so one request runs the whole workflow.

## What you'll build

An HR project with materials, standing rules, a skill and a connector, running one request that produces a policy draft, a summary and an Outlook draft.

**Tools and techniques:** Claude Projects, Claude Skills, Microsoft 365 connector, Cowork

## Company use case

- **Department:** Human Resources
- **Sponsor:** Head of HR
- **Business challenge:** The HR workflow still runs across four different places, so nobody can hand it over.
- **Decision:** Which parts of the HR workflow can run from one request, and which must stay manual?
- **Evidence:** The HR project materials; The hr-policy-draft skill; Microsoft 365 through the connector
- **Measures:** Skill available in the project; Connector reachable; Workflow run end to end; Manual steps agreed
- **Controls:** Read-only connector use; Every fact names its source; Nothing sent without a named approver

## Files in this lab folder

- `Lumina-Living-Lab-13-HR-Brief.docx`
- `Lumina-Living-Lab-13-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-13-Working-Workbook.xlsx`
- `Lumina-Living-Lab-13-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Lab 12 completed, with the Lumina Living HR project set up.
- Lab 5 completed, so the hr-policy-draft skill exists.
- Lab 0 completed, with the Microsoft 365 connector connected — or recorded as unavailable, in which case the local files still work.

## Process map

Materials and rules → Add the skill → Add the connector → Run the whole workflow → Decide what stays automatic

## Steps

### Step 1

Open the Lumina Living HR project you built in Lab 12. Check its materials and instructions are still there. You are about to give it two more things: a method, and reach beyond its own uploads.

### Step 2

Add your skill to the project. In the project, open the plus menu, then Skills, and enable hr-policy-draft — the skill you created in Lab 5. The project now knows both what to work on and how you want it written.

### Step 3

Add the Microsoft 365 connector. In Claude Desktop, open Customize > Connectors and confirm Microsoft 365 is connected. Inside the project, ask Claude what it can now reach. If the connector is unavailable, record it and continue with the uploaded materials only.

**Prompt to give Claude:**

```text
What materials and tools do you have access to in this project? List the uploaded files, any skills that are enabled, and whether you can reach Microsoft 365. Do not use any of them yet.
```

### Step 4

Now run the whole workflow from one request. Watch how many separate steps it does without you moving between apps.

**Prompt to give Claude:**

```text
Using this project, run the March HR workflow for me.

Do three things in order:
1. Draft the flexible working policy section, applying my hr-policy-draft skill
2. Write a short summary of where headcount stands, from the uploaded quarter files
3. Prepare a draft email to the Head of HR with both attached for review, and leave it unsent

Name the file behind every fact. Where the materials are silent, write 'need to check'. Do not send anything.
```

### Step 5

Read all three outputs. Check the policy follows your skill's rules, the summary names its files, and the email is a draft and nothing more. Then write down which of these three steps you would let run unattended tomorrow morning, and which you would always read first. That judgment is what you take back to work.

## Test it

The project has the hr-policy-draft skill enabled and the connector state recorded. One request produced a policy draft following the skill's rules, a headcount summary naming its source files, and an unsent Outlook draft. Nothing was sent, and you have written which steps may run unattended and which always need a person.

## Troubleshooting

- **Skills is not available inside the project.** Check the skill exists in Settings > Skills. If skills are not on your plan, paste the rules from Lab 5's standard into the project instructions instead.
- **The connector is not reachable.** Record it and run the workflow on the uploaded materials alone. Nothing in this lab depends on the connector working.
- **Claude did all three steps but skipped the citations.** Ask again and name the rule: 'name the file behind every fact'. A project's instructions apply, but a long request can still drift.
- **It sent the email.** It should not. The request says leave it unsent. If it sent, check the recipient immediately and report it — that is exactly why the approval gate exists.

## Challenge

Remove the skill from the project, run the same request, and compare the policy draft.

## Reflection

Now that one request can do three jobs, what would you want to see before you trusted it unattended?

## Deliverable

An HR project with materials, standing rules, a skill and a connector, running one request that produces a policy draft, a summary and an Outlook draft.

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
