# C197 Project Instructions

## Course contract

- This is a one-day, 7.5-instructional-hour non-WSQ commercial course.
- The single source of truth is `.claude/skills/non-wsq-courseware-build/build/course_data.py` plus canonical `data_domainN.py` files.
- Build the PPT before the Lesson Plan and Learner Guide so slide, schedule and lab mappings stay aligned.
- The PPT teaches concepts, decisions, process architecture, prompt anatomy and realistic work samples. Do not put click-by-click procedures or command sequences in the PPT.
- Detailed procedures, complete prompts, commands, troubleshooting and verification belong in the Learner Guide and matching lab README.
- Do not introduce WSQ, SSG, SkillsFuture, TRAQOM, attendance, funding or formal-assessment language.

## Scenario and artifacts

- Use one fictional company, Lumina Living Pte Ltd, across all four topics and 11 labs.
- Every lab folder must be self-contained with realistic Word, Excel and PowerPoint files plus reusable templates.
- Lab 7 is the financial model/dashboard anchor; Lab 8 is the executive strategy and marketing presentation; Lab 11 is the Claude Code automation anchor.
- Preserve native Office structures: Word styles, Excel formulas/charts, PowerPoint masters/editable charts and Outlook drafts.
- Keep human approval gates for consequential save, write, invite, release and send actions.

## Presentation standard

- Use a highly visual all-white Tertiary design system with substantive cards, process maps, readable artifact exhibits and visual rhythm.
- Avoid sparse teaching slides and bullet walls. Section dividers may be intentionally minimal.
- Apply Fade transitions to all slides and perform render, visual inspection, correction and re-render before publication.

## Security and publication

- Classroom credentials are local-only in ignored `.env.training`; published materials use placeholders.
- Never place passwords, tokens or private company information in prompts, screenshots, generated Office files, Git or Drive.
- Dry-run Drive and LMS publication first. Verify the exact destination content before any archive or mirror action.
- Stage only the intended C197 package and verify the remote GitHub SHA after pushing.

Project context: `CONTEXT.md`.
