# Lab 14 — Upload a Shared Skill for Slides

**Topic 04:** Staff Questions, Repeatable Work and Advanced Claude  |  **Day 1**  |  **Approx. 15 min**  |  **Course:** Claude Microsoft 365 Masterclass (C197)

## Company scenario

Lumina Living is a fictional Singapore home-and-lifestyle company with retail, online and warehouse teams. Learners join its HR department to prepare the FY2027 hiring plan, staff policies and the weekly people update.

Your company has a house standard for decks, written once and shared as a file. Upload it as a skill and apply it to a weak draft deck.

## Goal

Import a slide standard written by someone else, so every HR deck in the team looks the same.

## What you'll build

An uploaded deck-design-standard skill, and a rebuilt deck where every title states a conclusion.

**Tools and techniques:** Claude Skills, Claude for PowerPoint, Upload a skill

## Company use case

- **Department:** Human Resources
- **Sponsor:** Head of HR
- **Business challenge:** Write your own team's deck standard as a file and share it with one colleague to upload.
- **Decision:** Should the deck standard be shared as one file everyone imports?
- **Evidence:** The house deck standard file; The draft deck in this folder
- **Measures:** Skill uploaded; Deck rebuilt; Method chosen
- **Controls:** Keep the company slide master; Source note under every figure; Flag any figure that cannot be traced

## Files in this lab folder

- `Lumina-Living-Lab-14-HR-Brief.docx`
- `Lumina-Living-Lab-14-Claude-Generated-Work-Sample.docx`
- `Lumina-Living-Lab-14-Working-Workbook.xlsx`
- `Lumina-Living-Lab-14-Executive-Starter.pptx`
- `templates/Prompt-and-Review-Template.docx`
- `templates/Decision-and-Approval-Log.xlsx`

## Prerequisites

- Lab 7 completed, so you have built a deck by hand.
- PowerPoint installed, with the Claude panel available from the ribbon.
- A Claude account you can sign in to on claude.ai. Skills is available on paid plans.
- Lumina-Living-Lab-14-Draft-Deck.pptx and deck-design-standard.md from this folder.

## Process map

A standard written once → Upload it → Apply it to a weak deck → Compare with your own version → Choose the right method

## Steps

### Step 1

Open Lumina-Living-Lab-14-Draft-Deck.pptx from this lab folder. It is a six-slide HR update where every title names a topic instead of stating a conclusion. Your company has a house standard for decks, and it has been shared with you as a file.

### Step 2

Open deck-design-standard.md from this lab folder and read it. This is a skill written by someone else — the same rules you applied by hand in Lab 7, written down once for the whole team.

### Step 3

In the Claude panel, select the plus button, then Skills, then Manage skills. On claude.ai select Add, then choose Upload a skill, and upload deck-design-standard.md. This is how a team shares one standard instead of everyone writing their own.

### Step 4

Go back to PowerPoint. Select the plus button, then Skills, then /deck-design-standard. Watch every slide title change from a topic to a conclusion, and a source note appear under each figure.

**Prompt to give Claude:**

```text
/deck-design-standard
```

### Step 5

Compare the deck with the version you built by hand in Lab 7. Write one sentence in the speaker notes of slide 1: which of the three ways of creating a skill — writing the instructions, letting Claude create it, or uploading one — you would use for your own team, and why.

## Test it

The deck-design-standard skill was uploaded from the supplied file, running it changed every slide title to a conclusion and added source notes, the slide master is unchanged, and slide 1's speaker notes say which of the ways of creating a skill you would use and why.

## Troubleshooting

- **Upload a skill will not accept the file.** It expects a Markdown file. Use deck-design-standard.md exactly as supplied.
- **The skill changed the slide master.** Undo, and check the standard file says to keep the master. A shared skill is only as safe as its rules.
- **Titles still name topics.** Ask it to rewrite only the titles, and quote the rule from the standard back to it.

## Challenge

Pick one weekly HR task and decide whether it needs a plugin, a Skill, or just a clear request.

## Reflection

When is uploading someone else's standard better than writing your own?

## Deliverable

An uploaded deck-design-standard skill, and a rebuilt deck where every title states a conclusion.

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
