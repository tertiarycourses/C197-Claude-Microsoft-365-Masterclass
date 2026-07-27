# C197 — Claude Microsoft 365 Masterclass

Work smarter across **Microsoft 365** with AI. This one-day, hands-on course teaches you to use
**Claude** — Anthropic's AI assistant — alongside Word, Excel, PowerPoint, Outlook and Teams to
draft and summarise documents, analyse and explain data, build slide content, and write email and
chat — always connecting Claude to your files, prompting effectively, and verifying its output
before you trust it.

## Course Information

- **Course Code:** C197
- **Course Title:** Claude Microsoft 365 Masterclass
- **Duration:** 1 day / 7.5 hours
- **Level:** Beginner
- **Mode:** Instructor-led, hands-on practical labs
- **Course Registration:** [Claude Microsoft 365 Masterclass](https://www.tertiarycourses.com.sg/claude-microsoft-365-masterclass.html)

## One Connected Deliverable

Every lab builds the **same** deliverable — the quarterly business-review pack for a fictional
retailer, **Lumina Living**. You start in Lab 1 with a rough brief and a sales workbook and, using
Claude alongside Microsoft 365, turn them into a finished, checked pack — a Word report, an Excel
analysis, a PowerPoint deck and the Outlook/Teams messages that send it — by Lab 8. Wherever
possible you use your **own** non-confidential work, so you leave applying the skills to your own
job; a Lumina Living sample set is supplied for everyone to follow along.

There is **no assessment** — this is a commercial short course. Each lab proves itself with an
explicit *Test it* verification step instead.

## What You'll Learn

| Topic | Coverage |
|---|---|
| 01 — Getting Started with Claude for Microsoft 365 | Introduction to Claude & Microsoft 365 · connecting Claude to your files and apps · effective prompting for work tasks · responsible, secure and private use of AI |
| 02 — Boosting Productivity Across Microsoft 365 with Claude | Writing, rewriting & summarising in Word · analysing & explaining data in Excel · generating slide outlines for PowerPoint · drafting & replying to email in Outlook and Teams |

## Labs

Eight connected hands-on labs (4 per topic). See [labs/README.md](labs/README.md) for the index and
[labs/tools.md](labs/tools.md) for the accounts and apps used.

## Courseware

Built artifacts live in [`courseware/`](courseware/):

- Trainer slide deck — `Claude Microsoft 365 Masterclass (C197)-v1.0.pptx` (+ PDF)
- Learner Guide — `LG-*.docx` (+ PDF); the Markdown mirror is at the repo root
- Lesson Plan — `LP-*.docx` (+ PDF)

## Building the Courseware

Everything is generated from a single source (`course_data.py` + `data_domainN.py`) so the deck,
Lesson Plan, Learner Guide and labs stay 100% aligned:

```bash
bash .claude/skills/non-wsq-courseware-build/build/build_courseware.sh
```

## Non-WSQ

This is a **non-WSQ** commercial short course. It carries **no** WSQ, SSG/SkillsFuture, TRAQOM,
digital-attendance, funding/subsidy or assessment content — those are deliberately excluded.

---

© 2026 Tertiary Infotech Academy Pte Ltd · UEN 201200696W
