# Claude Microsoft 365 Masterclass (C197) — Learner Guide

**Course Code:** C197  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v2.0 · 12 August 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Prompt Best Practices for Word, Excel and PowerPoint](#prompt-best-practices-for-word-excel-and-powerpoint)
- [Topic 01 — Governed Foundations for Claude and Microsoft 365  (24%)](#topic-01--governed-foundations-for-claude-and-microsoft-365--24)
  - [Lab 1 — Choose and Activate the Right Claude Surface](#lab-1--choose-and-activate-the-right-claude-surface)
  - [Lab 2 — Connect Microsoft 365 Context and Map Permissions](#lab-2--connect-microsoft-365-context-and-map-permissions)
  - [Lab 3 — Build an Auditable Prompt and Review Contract](#lab-3--build-an-auditable-prompt-and-review-contract)
- [Topic 02 — Company Planning, Reporting and Policy Work  (28%)](#topic-02--company-planning-reporting-and-policy-work--28)
  - [Lab 4 — Create a Company Marketing Plan in Word](#lab-4--create-a-company-marketing-plan-in-word)
  - [Lab 5 — Develop a Strategic Plan with Owners and Measures](#lab-5--develop-a-strategic-plan-with-owners-and-measures)
  - [Lab 6 — Draft Sustainability Reporting and HR Policy](#lab-6--draft-sustainability-reporting-and-hr-policy)
- [Topic 03 — Financial Analysis and Executive Storytelling  (25%)](#topic-03--financial-analysis-and-executive-storytelling--25)
  - [Lab 7 — Build Financial Analysis and an Excel Dashboard](#lab-7--build-financial-analysis-and-an-excel-dashboard)
  - [Lab 8 — Create an Executive Strategy and Marketing Deck](#lab-8--create-an-executive-strategy-and-marketing-deck)
- [Topic 04 — Agentic Coordination with Outlook, Cowork and Claude Code  (23%)](#topic-04--agentic-coordination-with-outlook-cowork-and-claude-code--23)
  - [Lab 9 — Triage and Prepare Approved Outlook Replies](#lab-9--triage-and-prepare-approved-outlook-replies)
  - [Lab 10 — Coordinate the Planning Pack with Claude Cowork](#lab-10--coordinate-the-planning-pack-with-claude-cowork)
  - [Lab 11 — Automate Excel, Outlook and a Daily Brief with Claude Code](#lab-11--automate-excel-outlook-and-a-daily-brief-with-claude-code)
- [Wrap-Up — One Governed Company Workflow](#wrap-up--one-governed-company-workflow)
- [Next Steps](#next-steps)
- [Glossary](#glossary)
- [References and Further Learning](#references-and-further-learning)


## Introduction

This Learner Guide accompanies C197 and contains the complete procedures for eleven connected company activities. It is the operational companion to the concept-led slide deck.

Lumina Living is a fictional Singapore omnichannel home-and-lifestyle company with retail, e-commerce and marketplace operations. Learners join its Business Transformation Office to prepare an integrated FY2027 planning and management pack. Every activity uses the same evidence chain so the marketing plan, strategy, policies, financial dashboard, presentation, Outlook hand-off, Cowork task and Claude Code daily brief remain consistent.


## Course Learning Outcomes

- LO1: Select the right Claude and Microsoft 365 operating surface for a governed company task.
- LO2: Connect approved Microsoft 365 context and map permissions, sources and evidence boundaries.
- LO3: Direct Claude with an auditable prompt contract and a human approval gate.
- LO4: Produce a decision-ready marketing plan in Word from approved company evidence.
- LO5: Develop an aligned strategic plan with choices, initiatives, owners, measures and risks.
- LO6: Draft a sustainability report section and HR policy using source, legal and management review controls.
- LO7: Build a formula-driven financial analysis and executive dashboard in Excel.
- LO8: Create a highly visual strategic and marketing PowerPoint with native Excel charts and evidence traceability.
- LO9: Triage Outlook messages and prepare approval-based replies without bypassing the human send gate.
- LO10: Use Claude Cowork with Microsoft 365 context to coordinate a multi-file planning workflow.
- LO11: Use Claude Code and approved connectors to update Excel, search Outlook and produce a daily management brief.


## Before You Start — Preparation

**What you need**

- A current Windows or Mac laptop with Chrome or Edge, Microsoft 365 Word, Excel, PowerPoint and Outlook.
- A paid Claude plan for Claude for Word, Excel, PowerPoint and Outlook; a trainer-approved upload fallback may be used when an add-in is unavailable.
- Claude desktop with Cowork access for Lab 10 and Claude Code installed for Lab 11.
- An organisational Microsoft 365 account in an Entra tenant. The Microsoft 365 connector requires administrator consent; personal Outlook.com accounts are not supported.
- The self-contained Office files and templates inside each labs/lab-NN-*/ folder.

**Verify your setup**

Confirm the visible availability of every required surface before class. Missing add-ins, connector consent or Cowork access are real environment states and require the authorised administrator or the documented fallback.

```bash
claude --version  ·  claude mcp list  ·  open Word / Excel / PowerPoint / Outlook  ·  verify the Claude task pane
```

**Conventions used in every lab**

- All Lumina Living information is fictional and safe for training; do not replace it with confidential or personal data without approval.
- Shaded blocks are copy-ready prompts or commands. Replace angle-bracket placeholders before use.
- Every material figure must trace to a workbook cell, table or approved source note.
- Draft, save, write and send actions remain subject to the named human approval gate.

**Supplied sample files**

- Each lab folder contains a realistic company brief (.docx), working workbook (.xlsx), executive starter deck (.pptx) and reusable review templates.
- Lab 7 contains the master financial model and dashboard; Lab 8 contains the executive strategy-and-marketing deck that incorporates its verified charts.
- Lab 11 also contains a safe local automation starter for Excel updates and daily-brief generation; Microsoft 365 search uses the approved connector visible in Claude Code.


## Prompt Best Practices for Word, Excel and PowerPoint

A professional prompt is a compact work contract. It defines the result, evidence, constraints, output and approval boundary before Claude edits the work product.

**Five practices**

- Name the business result — State the decision, audience and artifact—not merely the app you are using.
- Ground the work — Name the open file, table, sheet, section or approved message set Claude may use.
- Constrain the edit — Define scope, length, style, formula method, layout and anything Claude must not change.
- Demand evidence — Require cell, range, heading or email citations and ask Claude to flag missing information.
- Set the approval gate — Ask for proposed changes first; verify them before accepting, saving, sending or publishing.

**Word example — Draft a decision-ready strategy section**

```bash
Using the open FY2027 strategy brief, draft only the 'Strategic choices' section for the Executive Committee. Preserve the existing Heading 1/2 styles. For each choice include rationale, owner, measure and Q1 milestone. Use only facts stated in the brief; cite the source heading and flag missing evidence. Show proposed text before editing the document.
```

**Excel example — Build an auditable financial view**

```bash
Using tblFinance in the open workbook, build a formula-driven Actual vs Budget analysis by month and channel. Include Revenue, Gross Profit, Gross Margin and Operating Contribution. Use native formulas or pivots, cite source ranges, keep assumptions on the Assumptions sheet, and do not paste hardcoded totals. Before editing, list the formulas and checks you will apply.
```

**PowerPoint example — Create an executive planning story**

```bash
Using the open company template, the approved strategy document and verified Excel dashboard, build an eight-slide Executive Committee story. Use conclusion-led titles, one message per slide, native editable charts linked to the approved summary ranges, and concise speaker notes. Preserve the slide master and brand rules. Add a source note to each data slide and flag any figure that does not reconcile.
```


## Topic 01 — Governed Foundations for Claude and Microsoft 365  (24%)

Operating surfaces · Microsoft 365 connector · permissions · evidence · prompting · human approval

**Key concepts**

- Four operating surfaces — distinguish Claude for Microsoft 365 add-ins, the Microsoft 365 connector in Claude, Anthropic Claude Cowork, and Claude-powered experiences inside Microsoft 365 Copilot.
- Open-file context — the Word, Excel, PowerPoint and Outlook add-ins work with the active item and preserve native structures such as styles, formulas and slide masters.
- Connected work context — the Microsoft 365 connector can search authorised SharePoint, OneDrive, Outlook and Teams content; optional write tools require additional tenant consent.
- Least privilege — access follows the signed-in user's existing permissions; broad access is not a substitute for a well-scoped business task.
- Evidence contract — every material claim names its source location, confidence and unresolved gap before the output is polished.
- Human accountability — reviewed changes, formulas, recipients and approval records make AI-assisted work defensible.


### Lab 1 — Choose and Activate the Right Claude Surface

Learning outcome: Select and activate the Claude surface that fits a governed Lumina Living task..

Goal: Compare the Office add-ins, Microsoft 365 connector, Claude Cowork and Claude-powered Microsoft 365 Copilot experiences before touching company data.

**Company use case**

- Department: Business Transformation Office
- Sponsor: Chief Operating Officer
- Decision: Which Claude surface should each planning, analysis and communication task use?
- Evidence: IT acceptable-use note; Microsoft 365 tenant capability register; FY2027 planning brief
- Controls: No shared password in learner files; No permission bypass; Named system owner approval

**What you'll build**

A completed operating-surface decision matrix and environment-readiness record.   (Tools: Claude for Microsoft 365, Claude connector, Claude Cowork, Microsoft 365 Copilot, admin deployment.)

**Prerequisites**

- The trainer has privately assigned a classroom account; credentials are not written in this lab or repository.
- Word, Excel, PowerPoint and Outlook are installed or available on the web.
- Claude desktop and Claude Code are installed for later labs, where available.

**Process map**

Define the task → Compare surfaces → Check licence and tenant → Activate the approved route → Record the fallback

**Step-by-step**

1. Open the lab folder and inspect the company brief, readiness workbook and executive starter deck before signing in anywhere.
2. Classify four example tasks—edit a strategy section, analyse finance, search recent Outlook decisions and coordinate a multi-file pack—against the four operating surfaces.
3. Open Word, Excel and PowerPoint, locate the Claude add-in and sign in with the trainer-issued classroom account. Record the visible state in the Readiness workbook.
4. Open Outlook and check whether Claude for Outlook is present. If the tenant shows an approval requirement, record it as an environment constraint; do not attempt a workaround.
5. In Claude, open Customize > Connectors and inspect Microsoft 365. Record whether organisation enablement, Entra administrator consent and write tools are available.
6. Open Claude desktop and confirm whether Cowork appears in the mode picker. Do not grant folder access yet.
7. Open Microsoft 365 Copilot only if your tenant provides it. Record it as a distinct Microsoft surface, not as the Anthropic Office add-in.
8. Complete the decision matrix: task, preferred surface, required permission, human approval, fallback and owner.
9. Use Claude to challenge your matrix without asking it to change the file. Prompt to give Claude:

   ```bash
   Act as an enterprise AI adoption lead. Review this operating-surface matrix for mismatched tasks, excessive permissions, missing approval owners and unrealistic fallbacks. Cite the row for every finding. Do not edit the workbook.
   ```

10. Correct the matrix yourself and save the approved copy in the lab folder.

**Test it**

Every example task has one preferred surface, one governed fallback, a permission owner and a human approval point; no credential is stored in any learner-facing file.

**Troubleshooting**

- An add-in is missing — Treat the visible state as real. Record it, use the approved upload fallback for class and ask the authorised administrator about deployment.
- Connector authentication fails — Confirm a business Entra account and tenant admin consent; personal Outlook.com accounts cannot use this connector.
- Two products are both labelled Cowork — Distinguish Anthropic Claude Cowork from Microsoft 365 Copilot Cowork by host, licensing, data boundary and approval model.

**Challenge**

Add one recurring task from your role and justify the lowest-privilege surface that can complete it.

**Reflection**

What evidence would convince your system owner that the selected surface is appropriate?

> **Note:** The matching detailed lab folder is in labs/lab-01-choose-and-activate-the-right-claude-surface/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 2 — Connect Microsoft 365 Context and Map Permissions

Learning outcome: Connect approved Microsoft 365 context and map what Claude may read or write..

Goal: Build a source-and-permission register for Lumina Living's SharePoint, OneDrive, Outlook and Teams planning evidence.

**Company use case**

- Department: Information Governance
- Sponsor: Head of IT and Data Protection Officer
- Decision: Which sources and tools should be enabled for each role?
- Evidence: SharePoint Strategy site; OneDrive project folder; Outlook planning mailbox; Teams leadership chat
- Controls: Least privilege; Business Entra tenant; Per-user access boundary; No Teams write claim

**What you'll build**

A least-privilege source register with access status, evidence owner, retention note and approved use.   (Tools: Microsoft 365 connector, Microsoft Entra, delegated permissions, SharePoint, OneDrive, Outlook, Teams.)

**Prerequisites**

- Lab 1 completed.
- The trainer has confirmed whether Entra administrator consent is already present.
- Use only the fictional Lumina Living sources supplied in this folder.

**Process map**

Inventory sources → Assign owners → Grant tenant consent → Connect individually → Test read before write

**Step-by-step**

1. Review the Source Register workbook and identify the business owner, sensitivity, retention need and intended Claude use for every source.
2. In Claude, navigate to Customize > Connectors > Microsoft 365. Connect only if the organisation and tenant consent are already approved.
3. Record the connector's visible tools and whether they are read or write. Do not assume write access from a successful sign-in.
4. Ask Claude to search only the approved FY2027 planning context and return a source inventory rather than a narrative. Prompt to give Claude:

   ```bash
   Search the approved Microsoft 365 planning sources for Lumina Living FY2027. Return a table with item title, service, owner if stated, last modified date and direct source citation. Do not infer missing owners and do not create or update anything.
   ```

5. Compare the results with the supplied register. Mark missing, duplicate, stale or inaccessible sources.
6. Test an Outlook read query for planning messages and require per-message citations. Prompt to give Claude:

   ```bash
   Find the fictional FY2027 planning messages approved for this exercise. List sender, date, subject, decision and unresolved action with a citation to each message. Do not draft or send email.
   ```

7. If write tools are not approved, record the limitation and retain read-only operation. If approved, perform only the trainer-authorised low-risk draft-to-self test. Prompt to give Claude:

   ```bash
   Draft an email to my own training account summarising the connector test. Leave it as a draft and do not send it.
   ```

8. Update the Permission Map with the user group, source, tool, scope, owner, review date and fallback.
9. Ask Claude to identify excessive or missing permissions, then resolve each finding with the source owner. Prompt to give Claude:

   ```bash
   Review this permission map for least-privilege issues. Flag any source or write capability that is not necessary for the stated business outcome. Cite the row and propose a narrower alternative.
   ```


**Test it**

The source register reconciles to the connector results, every source has an owner and approved use, and write tools are either explicitly authorised or documented as unavailable.

**Troubleshooting**

- Admin approval is required — Stop the connection attempt and escalate to the authorised Entra Global Administrator.
- A source is missing — Check the signed-in user's existing Microsoft 365 permission and the source location; do not request broad tenant access as a shortcut.
- A Teams action is requested — The Claude Microsoft 365 connector can read supported Teams context but does not provide tools to post Teams messages or change Teams settings.

**Challenge**

Design a read-only pilot group and a separate, smaller write-enabled group for the company rollout.

**Reflection**

Which permission would create the largest consequence if misused, and who should approve it?

> **Note:** The matching detailed lab folder is in labs/lab-02-connect-microsoft-365-context-and-permissions/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 3 — Build an Auditable Prompt and Review Contract

Learning outcome: Write reusable prompts that ground evidence, constrain edits and define human approval..

Goal: Turn vague requests into professional prompt contracts for Word, Excel and PowerPoint, then log evidence and review outcomes.

**Company use case**

- Department: Business Transformation Office
- Sponsor: Director, Strategy
- Decision: Which prompt elements are mandatory for a company-standard AI workflow?
- Evidence: FY2027 planning brief; Company style guide; Data dictionary; Approval matrix
- Controls: No unstated assumptions; No fabricated citations; Smallest useful edit; Human approval

**What you'll build**

A reusable cross-app prompt library, prompt test log and acceptance checklist.   (Tools: Prompt architecture, evidence clauses, stop rules, output contracts, review log.)

**Prerequisites**

- Labs 1–2 completed.
- Word, Excel and PowerPoint sample files open.
- The approved source register is available.

**Process map**

Business outcome → Named evidence → Constraints → Output contract → Verification and approval

**Step-by-step**

1. Open the Prompt Library document and the Prompt Test Log workbook.
2. Run the vague request 'Improve our plan' against the supplied Word brief and record why the result is difficult to verify. Prompt to give Claude:

   ```bash
   Improve our plan.
   ```

3. Rewrite it with the five-part structure: business outcome, evidence, constraints, output contract and approval gate. Prompt to give Claude:

   ```bash
   Using the open FY2027 brief, draft only the Executive summary for the Lumina Living leadership team. Preserve the current heading styles and keep it under 180 words. Use only stated facts, cite the source heading for each material claim and list missing evidence separately. Show proposed text before editing the document.
   ```

4. Create an Excel prompt that requires formula-first analysis, cell citations and a review plan before edits. Prompt to give Claude:

   ```bash
   Using tblFinance in the open workbook, propose a formula-driven Actual vs Budget analysis for Revenue, Gross Profit, Gross Margin and Operating Contribution. Cite source ranges, keep assumptions on the Assumptions sheet and do not hardcode totals. List the formulas and validation checks before applying changes.
   ```

5. Create a PowerPoint prompt that preserves the company template and demands native charts, conclusion-led titles and source notes. Prompt to give Claude:

   ```bash
   Using the open company template, approved strategy document and verified Excel summary ranges, propose an eight-slide Executive Committee story. Preserve the slide master, use one conclusion-led message per slide, native editable charts and concise speaker notes. Add a source note to every data slide and flag unreconciled figures before building.
   ```

6. Test each prompt once. Log the input sources, output quality, citation accuracy, time to review and corrections required.
7. Add a stop rule to any prompt that encouraged guessing. Prompt to give Claude:

   ```bash
   If the approved sources do not contain a required fact, stop that part of the task, name the missing evidence and ask one precise question. Do not invent a value, owner, date or citation.
   ```

8. Ask Claude to critique the three prompts against the company standard. Prompt to give Claude:

   ```bash
   Audit these Word, Excel and PowerPoint prompts. For each, score outcome clarity, grounding, constraints, output contract, verification and approval from 1 to 5. Cite the exact missing phrase and propose the smallest correction.
   ```

9. Save the approved prompts as company templates for Labs 4, 7 and 8.

**Test it**

The Word, Excel and PowerPoint prompts each name a business result, approved evidence, constraints, output format, verification method, stop rule and human approval gate.

**Troubleshooting**

- Claude still guesses — Add an explicit missing-evidence stop rule and require the source location for every material claim.
- The prompt is too long — Separate stable company instructions from the task-specific prompt and remove repeated context.
- The edit is too broad — Name the exact selected section, sheet, range, slide or object to change.

**Challenge**

Create a prompt rubric that a colleague can use without knowing how the prompt was written.

**Reflection**

Which prompt clause most reduced your review effort, and why?

> **Note:** The matching detailed lab folder is in labs/lab-03-build-an-auditable-prompt-and-review-contract/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


## Topic 02 — Company Planning, Reporting and Policy Work  (28%)

Marketing planning · strategic planning · sustainability reporting · HR policy · management review

**Key concepts**

- Marketing planning — connect business goals, customer segments, channel choices, campaign actions, budget and measurable outcomes.
- Strategic planning — turn evidence into explicit choices, initiatives, owners, dependencies, targets and review dates.
- Sustainability reporting — define the reporting boundary, method, source owner and limitation before drafting a credible narrative.
- HR policy — separate policy intent, operational procedure and legal interpretation; require authorised HR and legal review before release.
- Template fidelity — work inside approved Word styles and tables so outputs fit the company's document system rather than becoming detached chat text.
- Management review — label facts, calculations, assumptions and recommendations so decision makers can challenge each layer.


### Lab 4 — Create a Company Marketing Plan in Word

Learning outcome: Produce a decision-ready FY2027 marketing plan in the Lumina Living Word template..

Goal: Turn an approved commercial brief, customer evidence and budget envelope into a structured marketing plan with objectives, segments, channels, actions, KPIs and approvals.

**Company use case**

- Department: Marketing and E-commerce
- Sponsor: Chief Commercial Officer
- Decision: Which segments, channels and campaigns should receive the marketing budget?
- Evidence: FY2026 channel results; Customer segment note; Campaign calendar; Marketing budget envelope
- Controls: No invented market facts; Budget reconciles; Claims cite source; CCO approval

**What you'll build**

A reviewed FY2027 marketing plan in Word with an evidence appendix and management decision page.   (Tools: Claude for Word, company styles, selected-text editing, comments, tracked changes, evidence register.)

**Prerequisites**

- Labs 1–3 completed.
- Open the lab's marketing brief, workbook and Word template.
- Confirm the marketing plan is fictional training material.

**Process map**

Commercial objective → Customer evidence → Channel choices → Campaign plan → Measures and approval

**Step-by-step**

1. Read the marketing brief yourself and list the decision, audience, planning horizon and non-negotiable constraints.
2. Ask Claude to map the source documents and identify missing evidence before drafting. Prompt to give Claude:

   ```bash
   Map the open marketing brief and workbook for FY2027 planning. Return: objective, customer evidence, channel performance, budget limits, stated risks and missing evidence. Cite the source heading or workbook range. Do not edit Word yet.
   ```

3. Ask Claude to propose three strategic marketing choices and one explicit non-priority. Prompt to give Claude:

   ```bash
   Propose three FY2027 marketing choices for Lumina Living and one activity we should not prioritise. For each choice state the evidence, target segment, channel, expected business effect, key risk and success measure. Use only the approved sources and label interpretation.
   ```

4. Review the choices with the budget workbook. Remove any recommendation that cannot be funded or evidenced.
5. Draft the plan inside the Word template using its existing styles and tables. Prompt to give Claude:

   ```bash
   Draft the FY2027 marketing plan in the open template. Sections: Executive decision, Situation, Objectives, Priority segments, Channel strategy, 90-day campaigns, Budget, KPIs, Risks and Approval. Preserve all styles and numbering. Cite source headings or workbook ranges and flag missing values rather than guessing.
   ```

6. Select the campaign table and ask Claude to populate only that table with campaign, segment, channel, owner, timing, budget, KPI and approval status. Prompt to give Claude:

   ```bash
   Populate only the selected campaign table with a realistic 90-day plan from the approved brief. Keep the existing columns and formatting. Do not add campaigns outside the approved budget envelope.
   ```

7. Turn on tracked changes. Ask Claude to reduce jargon and sharpen the executive decision page without changing figures. Prompt to give Claude:

   ```bash
   Rewrite only the selected Executive decision page for senior management. Use plain business language, state the three choices, quantify the approved budget and name the decision required. Preserve every verified figure and show tracked changes.
   ```

8. Resolve comments, verify the total budget in Excel, check every cited source and record the CCO approval status.
9. Save the final file as 'Lumina Living FY2027 Marketing Plan — Reviewed.docx'.

**Test it**

The Word plan uses company styles, reconciles to the marketing budget, contains three clear choices and one non-priority, and every material claim has a source or missing-evidence flag.

**Troubleshooting**

- The plan becomes generic — Require the named segments, channel results, budget envelope and decision owner from the supplied sources.
- Word formatting drifts — Select the target section, preserve named styles and request a local edit rather than a full-document rewrite.
- Campaign costs exceed budget — Reconcile in Excel and ask Claude to reprioritise—not to invent additional funding.

**Challenge**

Add a stop/go decision rule for the weakest campaign after four weeks of evidence.

**Reflection**

Which marketing recommendation became stronger after you forced it to cite evidence?

> **Note:** The matching detailed lab folder is in labs/lab-04-create-a-company-marketing-plan-in-word/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 5 — Develop a Strategic Plan with Owners and Measures

Learning outcome: Develop an aligned strategic plan with explicit choices, initiatives, owners, measures and risks..

Goal: Translate Lumina Living's ambition into a strategy-on-a-page, initiative portfolio and governance rhythm that management can execute.

**Company use case**

- Department: Corporate Strategy
- Sponsor: Chief Executive Officer
- Decision: Which strategic choices and initiatives should the Executive Committee approve?
- Evidence: CEO ambition note; Commercial performance summary; Operations capability review; Risk register
- Controls: Explicit trade-offs; Named owners; Target source; Risk dependency review

**What you'll build**

A three-year strategic plan, initiative portfolio and quarterly review scorecard in Word and Excel.   (Tools: Claude for Word, Claude for Excel, strategy-on-a-page, initiative portfolio, risk and dependency review.)

**Prerequisites**

- Labs 1–4 completed.
- Open the strategic planning brief, scorecard workbook and strategy template.
- Use the reviewed marketing plan as one input, not as the whole strategy.

**Process map**

Ambition → Diagnosis → Strategic choices → Initiative portfolio → Measures and governance

**Step-by-step**

1. Ask Claude to separate facts, interpretations and assumptions in the strategy brief. Prompt to give Claude:

   ```bash
   Analyse the open strategy brief into three tables: verified facts with citations, interpretations to test, and assumptions requiring an owner and validation date. Do not draft a strategy yet.
   ```

2. Build a concise diagnosis across market, customer, economics, operations and capability. Prompt to give Claude:

   ```bash
   Using only the verified facts, draft a one-page strategic diagnosis. State the central challenge, three strengths, three constraints and two uncertainties. Cite each source and avoid unsupported causal claims.
   ```

3. Generate alternative strategic choices and compare their trade-offs in the workbook. Prompt to give Claude:

   ```bash
   Propose three coherent strategic choice sets. For each: where to play, how to win, required capability, investment implication, key risk and what Lumina Living will stop doing. Keep choices mutually distinct and cite the evidence behind them.
   ```

4. Select one choice set and record the management rationale in the Decision Log.
5. Ask Claude to draft the strategy-on-a-page in Word using the existing company template. Prompt to give Claude:

   ```bash
   Draft the strategy-on-a-page in the open template: ambition, strategic diagnosis, three choices, six initiatives, outcome measures and governance. Preserve styles. Each initiative must have an owner, Q1 milestone, 12-month target, dependency and risk.
   ```

6. Populate the initiative portfolio and balanced scorecard in Excel. Verify that every measure has a definition, baseline, target, source and review frequency. Prompt to give Claude:

   ```bash
   Build the initiative portfolio and balanced scorecard in the open workbook. Use formulas for status and variance. Do not invent baselines; mark missing values as 'Owner to confirm'.
   ```

7. Run a sceptical strategy review. Prompt to give Claude:

   ```bash
   Act as a sceptical board adviser. Test this strategy for conflicting choices, unfunded initiatives, missing capabilities, weak measures, dependency collisions and risks without owners. Rank findings by decision impact and cite the plan section or workbook row.
   ```

8. Resolve the top findings, update tracked changes and record the Executive Committee decision status.
9. Save the reviewed Word plan and Excel scorecard in the lab folder.

**Test it**

The strategy contains explicit choices and trade-offs, six owned initiatives, balanced measures with sources, a governance cadence and a resolved high-impact risk review.

**Troubleshooting**

- The strategy is a wish list — Force trade-offs: name what will not be prioritised and connect each initiative to one approved choice.
- Measures are vague — Require definition, unit, baseline, target, source owner and review frequency.
- Owners are generic departments — Assign one accountable role and list supporting roles separately.

**Challenge**

Create a scenario trigger that would cause management to revisit one strategic choice.

**Reflection**

Which trade-off made the strategy more executable?

> **Note:** The matching detailed lab folder is in labs/lab-05-develop-a-strategic-plan-with-owners-and-measures/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 6 — Draft Sustainability Reporting and HR Policy

Learning outcome: Draft source-aware sustainability reporting and an HR policy with appropriate review controls..

Goal: Create a management sustainability report section and a flexible-work HR policy while separating evidence, interpretation, procedure and legal review.

**Company use case**

- Department: Sustainability and People
- Sponsor: Chief People and Sustainability Officer
- Decision: Is the evidence and control environment strong enough for internal release?
- Evidence: Energy and waste register; Travel summary; Workforce profile; Flexible-work pilot feedback
- Controls: Reporting boundary; Method note; No green claims without evidence; HR and legal approval

**What you'll build**

A sustainability performance section, metric register and flexible-work policy draft with review and approval records.   (Tools: Claude for Word, reporting boundary, metric methodology, HR policy drafting, comments, approval workflow.)

**Prerequisites**

- Labs 1–5 completed.
- Open the sustainability metric workbook and HR source note.
- Do not treat this exercise as legal or regulatory advice.

**Process map**

Define boundary → Verify metrics → Draft narrative → Separate policy from procedure → Obtain specialist approval

**Step-by-step**

1. Review the metric register and flag missing owner, unit, method, boundary, period or evidence.
2. Ask Claude to create a reporting-boundary statement before drafting performance commentary. Prompt to give Claude:

   ```bash
   Using the open metric register, draft a reporting-boundary statement for FY2026. Include entities, Singapore sites, reporting period, included metrics, exclusions, calculation methods and data limitations. Cite the workbook rows and do not invent an assurance level.
   ```

3. Ask Claude to draft a factual performance section that separates results from interpretation. Prompt to give Claude:

   ```bash
   Draft a 500-word internal sustainability performance section. Structure: boundary, energy, waste, travel, people metrics, limitations and next actions. Cite each metric row. Label interpretation and avoid words such as 'leading', 'green' or 'net zero' unless the evidence explicitly supports them.
   ```

4. Verify all units, denominators, direction-of-change statements and limitations against Excel.
5. Map the HR policy source note into purpose, scope, eligibility, principles, process, manager decision rights, information security, health and safety, exceptions, records and review.
6. Ask Claude to draft only the policy—not legal conclusions or employee-specific decisions. Prompt to give Claude:

   ```bash
   Draft a flexible-work policy in the open company template. Use the mapped sections, plain language and neutral criteria. Distinguish policy from procedure. Add placeholders for jurisdiction-specific legal review and do not make claims about statutory entitlement that are absent from the approved source note.
   ```

7. Run an equity and operational review. Prompt to give Claude:

   ```bash
   Review this policy for inconsistent eligibility, hidden bias, unclear manager discretion, privacy risk, security gaps, inaccessible language and missing appeal or exception routes. Cite the clause and propose a precise revision. Do not approve the policy.
   ```

8. Use tracked changes to resolve approved findings. Add HR, legal, IT security and management review rows to the approval table.
9. Save both reviewed drafts and the completed metric register.

**Test it**

The sustainability section states its boundary and limitations and reconciles every metric; the HR policy separates policy from procedure and carries named HR, legal, security and management reviews.

**Troubleshooting**

- Claude overstates sustainability performance — Require neutral wording, metric citations, limitations and a ban on unsupported leadership or net-zero claims.
- Policy sounds legally definitive — Replace legal conclusions with review placeholders and obtain authorised jurisdiction-specific advice.
- Units do not reconcile — Check numerator, denominator, reporting period and conversion method in the metric register before editing the narrative.

**Challenge**

Add a methodology-change disclosure showing how a revised conversion factor affects comparability.

**Reflection**

Which control most reduced the risk of a misleading sustainability or HR statement?

> **Note:** The matching detailed lab folder is in labs/lab-06-draft-sustainability-reporting-and-hr-policy/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


## Topic 03 — Financial Analysis and Executive Storytelling  (25%)

Excel modelling · controls · KPI dashboard · native charts · strategic and marketing PowerPoint

**Key concepts**

- Financial model architecture — separate assumptions, transaction data, calculations, outputs and review notes so changes remain traceable.
- Formula-first analysis — use dynamic formulas, tables and pivot-ready structures instead of pasted totals or unexplained AI answers.
- Decision-led dashboard — combine a small set of KPIs, trends, variances and definitions around the questions management must answer.
- Chart integrity — choose the visual for the question, keep native Excel sources, verify scale and units, and avoid implying causation without evidence.
- Message-first presentation — every slide title states a conclusion; supporting detail goes into speaker notes, appendix or source register.
- Beyond one-click slides — professional value comes from an editable company template, native charts, coherent narrative, source traceability and deliberate visual hierarchy.


### Lab 7 — Build Financial Analysis and an Excel Dashboard

Learning outcome: Build an auditable financial model and management dashboard in Excel with Claude..

Goal: Move from transaction data and budget assumptions to formula-driven analysis, scenario testing, native charts and a one-screen management dashboard.

**Company use case**

- Department: Finance and Business Performance
- Sponsor: Chief Financial Officer
- Decision: Which revenue, margin and cost actions should management prioritise?
- Evidence: FY2026 transaction ledger; Monthly budget; Product cost table; Scenario assumptions
- Controls: Dynamic formulas; No formula errors; Source ranges cited; Independent KPI checks

**What you'll build**

A controlled FY2026 financial workbook with actual-vs-budget analysis, scenarios, three native charts and an executive dashboard.   (Tools: Claude for Excel, tables, formulas, pivots, scenarios, chart selection, dashboard, audit log.)

**Prerequisites**

- Labs 1–6 completed.
- Open the supplied Finance Model workbook and Data Dictionary.
- Use only the fictional transaction data supplied in this lab.

**Process map**

Understand the model → Validate inputs → Build formulas → Explain drivers → Dashboard and senior review

**Step-by-step**

1. Inspect the workbook manually: identify input, calculation, output and control sheets before using Claude.
2. Ask Claude to map the workbook and cite the key ranges without editing. Prompt to give Claude:

   ```bash
   Map this workbook before making changes. For each sheet state its purpose, input ranges, formula ranges, outputs, named tables, charts and control checks. Cite cells or table names and flag any ambiguity.
   ```

3. Validate the transaction and budget tables for duplicates, blanks, invalid dates, unexpected categories, negative values and inconsistent formula columns. Prompt to give Claude:

   ```bash
   Audit tblFinance and tblBudget for duplicates, blanks, invalid dates, unrecognised regions/channels/products, negative amounts and formula inconsistencies. Create a Data_Quality summary with issue count, affected rows and proposed fix. Do not silently delete or overwrite data.
   ```

4. Approve only justified fixes and require a change-log entry for each edit. Prompt to give Claude:

   ```bash
   Apply only the approved data-quality corrections. Record old value, new value, reason, source and reviewer in Audit_Log. Re-run the checks and stop if any high-impact issue remains.
   ```

5. Build formula-driven Actual vs Budget analysis by month, channel and product. Prompt to give Claude:

   ```bash
   Using tblFinance and tblBudget, build a formula-driven Actual vs Budget analysis for Revenue, Gross Profit, Gross Margin and Operating Contribution by month and channel. Use formulas or pivots, cite source ranges, keep assumptions on the Assumptions sheet and do not hardcode totals. List the formulas and checks before editing.
   ```

6. Trace and explain the Gross Margin and Operating Contribution formulas. Check for range, sign, timing and allocation errors. Prompt to give Claude:

   ```bash
   Explain the Gross Margin and Operating Contribution formulas, trace their precedents and test whether each range includes all twelve months. Audit for hardcoded totals, inconsistent signs, omitted rows, circular references and #REF!, #VALUE!, #N/A or #DIV/0! errors.
   ```

7. Create Base, Upside and Downside scenarios using explicit growth, discount and cost assumptions. Keep the assumptions separate from actuals. Prompt to give Claude:

   ```bash
   Create Base, Upside and Downside scenarios for FY2027. Inputs: unit growth, average discount, unit-cost inflation and marketing spend. Keep scenario inputs on Assumptions, calculate Revenue, Gross Profit, Gross Margin and Operating Contribution dynamically, and show the change versus Base.
   ```

8. Ask Claude to recommend charts by decision question, then approve a monthly trend, actual-vs-budget variance and contribution by channel visual. Prompt to give Claude:

   ```bash
   Recommend three management charts. For each state the decision question, source range, chart type, scale, unit and risk of misinterpretation. Prioritise monthly performance, budget variance and contribution by channel.
   ```

9. Create native editable charts and a one-screen Dashboard with four KPI cards, three charts, definitions, scenario selector note and last-refreshed timestamp. Prompt to give Claude:

   ```bash
   Build a one-screen Executive Dashboard using the verified Analysis outputs. Include Revenue, Gross Profit, Gross Margin and Operating Contribution KPI cards; the three approved native charts; definitions; selected scenario; and last-refreshed note. Use restrained company colours and no 3D effects.
   ```

10. Run a sceptical CFO review. Prompt to give Claude:

   ```bash
   Act as a sceptical CFO. Review the model for weak assumptions, hardcodes, timing or allocation errors, misleading scales, unsupported causal claims and decision-relevant sensitivities. Rank findings by financial impact and cite the cell, range or chart source.
   ```

11. Resolve material findings, recalculate the workbook, independently reproduce two KPIs and complete the Audit Log.

**Test it**

The model has no formula errors, all four KPIs reconcile, scenarios change through named assumptions, three native charts answer management questions and the audit log records independent checks.

**Troubleshooting**

- A KPI does not recalculate — Trace precedents and replace any pasted value with a formula tied to the approved table.
- The variance sign is confusing — Define favourable/unfavourable logic once and apply it consistently across tables, charts and narrative.
- The dashboard is crowded — Keep four KPIs and three decision charts; move details to Analysis and document definitions.

**Challenge**

Add a sensitivity table showing which assumption has the largest effect on Operating Contribution.

**Reflection**

Which model control gave you the strongest evidence that the dashboard can be trusted?

> **Note:** The matching detailed lab folder is in labs/lab-07-build-financial-analysis-and-an-excel-dashboard/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 8 — Create an Executive Strategy and Marketing Deck

Learning outcome: Create a highly visual, editable PowerPoint that integrates strategy, marketing and verified Excel charts..

Goal: Build a company-standard Executive Committee presentation with a coherent decision story, native charts, process maps, evidence notes and meaningful speaker notes.

**Company use case**

- Department: Corporate Strategy and Marketing
- Sponsor: Chief Executive Officer
- Decision: Approve the strategic choices, marketing allocation, financial guardrails and owners.
- Evidence: Reviewed marketing plan; Reviewed strategic plan; Verified financial dashboard; Sustainability and people commitments
- Controls: Company slide master; One message per slide; Native editable visuals; Figure reconciliation

**What you'll build**

A ten-slide strategic and marketing presentation with native Excel charts, varied layouts and an executive decision page.   (Tools: Claude for PowerPoint, slide master, native Excel charts, process maps, executive narrative, speaker notes, visual QA.)

**Prerequisites**

- Labs 1–7 completed.
- Open the lab PowerPoint template, reviewed Word plans and verified Excel Dashboard.
- Confirm the Excel workbook is the source of truth for financial figures.

**Process map**

Decision question → Message map → Template system → Native evidence visuals → Executive rehearsal and approval

**Step-by-step**

1. Inspect the PowerPoint template: slide master, layouts, typography, colours, placeholder rules and existing example slides.
2. Ask Claude to analyse the template and source pack before building slides. Prompt to give Claude:

   ```bash
   Analyse the open company template, reviewed strategy and marketing documents, and verified Excel dashboard. Return the available layouts, the management decision, five evidence points, unresolved mismatches and a recommended ten-slide story. Do not create slides yet.
   ```

3. Resolve every mismatch in the source Word or Excel file before building the presentation.
4. Create a message map with ten conclusion-led titles: decision, context, strategic choices, marketing priorities, financial outlook, drivers, sustainability/people commitments, Q1 roadmap, risks and approval. Prompt to give Claude:

   ```bash
   Create a ten-slide Executive Committee message map. Each title must state a conclusion, not a topic. For every slide specify purpose, evidence source, visual form and decision implication. Use one message per slide and flag any unsupported claim.
   ```

5. Ask Claude to build in the existing template using native text, shapes, tables, charts and diagrams. Prompt to give Claude:

   ```bash
   Build the ten slides in the open company template. Preserve the slide master, fonts, colours, margins and footer. Use native editable charts linked to the approved Excel summary ranges, native process maps and decision cards. Do not paste screenshots of charts. Add a concise source note to each data slide.
   ```

6. Replace any generic bullet wall with a scorecard, comparison, timeline, process map, chart or decision-card layout. Prompt to give Claude:

   ```bash
   Review the deck for text-heavy slides. For each, choose the most suitable native visual—scorecard, comparison, timeline, process map, chart or decision cards—without changing the verified conclusion. Keep body text at presentation size and preserve whitespace.
   ```

7. Integrate the Excel monthly trend, budget variance and contribution-by-channel charts. Verify axes, scales, currency, period and source range.
8. Add short speaker notes to every content slide: point, evidence, caveat, transition and decision request. Prompt to give Claude:

   ```bash
   Add speaker notes to each content slide: management point, evidence, caveat, transition and decision request. Do not repeat the visible slide text and do not add new figures.
   ```

9. Run a content and visual review against the quality rubric: evidence, narrative, hierarchy, variety, alignment, contrast, overflow, chart integrity and executive usability. Prompt to give Claude:

   ```bash
   Act as a presentation director and finance reviewer. Audit every slide for message clarity, evidence traceability, visual hierarchy, native editability, layout variety, tiny text, overflow, inconsistent spacing, misleading chart choices and unsupported figures. Rank required fixes and cite the slide number.
   ```

10. Apply pinpoint fixes, rehearse the ten-minute story and save the reviewed deck as 'Lumina Living FY2027 Executive Plan — Reviewed.pptx'.

**Test it**

The ten-slide deck uses the company master, shows verified native Excel charts, contains varied substantive visuals and speaker notes, and reconciles every figure and decision with the approved source pack.

**Troubleshooting**

- Claude ignores the master — Analyse and name the existing layouts first; require use of those layouts and edit selected slides rather than rebuilding the file.
- Slides look generic — Use company evidence, conclusion-led titles, native charts, specific decision cards and the approved visual motif.
- A chart changes from Excel — Correct the source workbook, confirm the approved range and replace only the affected chart.
- Text becomes too small — Split the idea or move detail to speaker notes; never shrink body text to rescue an overloaded slide.

**Challenge**

Create an appendix slide that reconciles every deck KPI to its Excel source cell and owner.

**Reflection**

Which design decision made the deck more useful to management than a generic one-click presentation?

> **Note:** The matching detailed lab folder is in labs/lab-08-create-an-executive-strategy-and-marketing-deck/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


## Topic 04 — Agentic Coordination with Outlook, Cowork and Claude Code  (23%)

Outlook triage and replies · Claude Cowork · Claude Code · Excel updates · email search · daily brief

**Key concepts**

- Outlook control — Claude can triage and draft, but Claude for Outlook leaves replies and invitations in native compose forms for the authorised user to review and send.
- Claude Cowork — a task-oriented Claude desktop mode that works across scoped folders, Projects, plugins and connected tools to produce real files over multiple steps.
- Cowork plus Microsoft 365 — retrieve approved organisational context through the connector, work in a bounded project folder, then review the resulting Office files in the native add-ins.
- Copilot Cowork is distinct — Microsoft's Cowork experience lives inside Microsoft 365 Copilot and has its own licensing, governance and action-approval model even when Anthropic models are used.
- Claude Code automation — local scripts and approved MCP connectors can update a workbook, search relevant mail and assemble a repeatable daily brief with explicit tool approvals.
- Safe automation boundary — read and draft first, validate recipients and versions, and reserve consequential write or send actions for explicit approval.


### Lab 9 — Triage and Prepare Approved Outlook Replies

Learning outcome: Triage Outlook messages and prepare consistent replies with a human send gate..

Goal: Use Claude for Outlook and approved Microsoft 365 context to classify planning mail, summarise threads, prepare draft replies and coordinate meetings without silently sending anything.

**Company use case**

- Department: Executive Office
- Sponsor: Chief of Staff
- Decision: Which messages need escalation, a standard draft, a tailored reply or no action?
- Evidence: Planning inbox sample; Reply policy; Executive tone guide; Meeting calendar
- Controls: No silent send; Recipient verification; Attachment/version check; Escalation rules

**What you'll build**

A triage queue, cited thread summary, approved reply templates, draft responses and an unsent meeting invitation.   (Tools: Claude for Outlook beta, Outlook categories, thread citations, reply templates, calendar, approval queue.)

**Prerequisites**

- Labs 1–8 completed.
- Open the supplied fictional Outlook thread export and Reply Policy.
- Claude for Outlook may require tenant deployment and Graph consent for inbox-wide features.

**Process map**

Classify → Summarise with citations → Select approved template → Draft in native form → Review recipients and send

**Step-by-step**

1. Review the Reply Policy and configure four categories in the Triage Queue: Executive decision, Draft eligible, Information only and Escalate.
2. Open the supplied planning thread in Outlook or use the trainer-prepared mailbox. Activate Claude in the message ribbon.
3. Ask for a cited thread summary before drafting. Prompt to give Claude:

   ```bash
   Summarise this planning thread into decisions made, unresolved questions, owner, deadline and required reply. Cite the source email for every item and flag any contradictory date, amount or attachment version. Do not draft or send yet.
   ```

4. Compare the summary with the Word and Excel source files. Resolve any figure or version mismatch in the source artifact.
5. If inbox-wide access is approved, ask Claude to classify only the fictional planning messages against the four categories. Prompt to give Claude:

   ```bash
   Classify the approved FY2027 planning messages into Executive decision, Draft eligible, Information only or Escalate. For each, state reason, priority, SLA and source citation. Do not move, archive, delete, reply or send.
   ```

6. Select a Draft eligible message and choose the matching approved reply template.
7. Ask Claude to prepare the response in the native compose form and leave it unsent. Prompt to give Claude:

   ```bash
   Draft a reply using the approved Executive Office template and tone guide. Confirm the decision, list the agreed actions with owners, cite the correct attached file versions and request comments by the stated deadline. Keep it under 160 words. Place it in Outlook as a draft and do not send.
   ```

8. Review To, Cc, Bcc, subject, names, dates, amounts, commitments, attachments, sensitivity and tone. Record the reviewer in the queue.
9. Ask Claude to find a 30-minute review slot and prepare an invitation with purpose, agenda, pre-read and decision required. Leave it unsent. Prompt to give Claude:

   ```bash
   Find a 30-minute review time for the people on this thread. Prepare an Outlook invitation with purpose, three-item agenda, named pre-read files and the decision required. Leave the invitation unsent for review.
   ```

10. The authorised user may send only after trainer approval in the classroom simulation; otherwise retain or discard the draft.

**Test it**

The triage queue is complete, the thread summary cites every decision, each draft uses an approved template and the reviewer has checked recipients, content, attachments and deadline before any send action.

**Troubleshooting**

- Outlook requests admin approval — Treat the visible state as real and use the supplied thread export for the exercise; the authorised administrator must grant the required access.
- Claude is ready to draft but not send — This is the expected Claude for Outlook control. Review in the native compose form and retain the human send gate.
- The summary misses context — Open the full conversation, ask for per-message citations and compare the source thread manually.

**Challenge**

Create an escalation rule for messages that contain a financial commitment, legal interpretation or personal data.

**Reflection**

Which part of email handling should remain human even if drafting becomes nearly automatic?

> **Note:** The matching detailed lab folder is in labs/lab-09-triage-and-prepare-approved-outlook-replies/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 10 — Coordinate the Planning Pack with Claude Cowork

Learning outcome: Use Claude Cowork and Microsoft 365 context to coordinate a bounded multi-file company task..

Goal: Set up a scoped Cowork project, bring in approved Microsoft 365 evidence, create a multi-step plan and deliver reviewed Office files back to the company workflow.

**Company use case**

- Department: Business Transformation Office
- Sponsor: Chief Operating Officer
- Decision: Can the planning pack proceed to Executive Committee review without unresolved evidence or version conflicts?
- Evidence: Approved lab outputs; Microsoft 365 planning messages; Decision log; Source register
- Controls: Scoped folder; Read-first connector; Checkpoint approvals; Native Office review

**What you'll build**

A Cowork project folder, execution plan, consolidated management brief, discrepancy log and reviewed Office hand-off.   (Tools: Claude Cowork, work folder, Projects, plugins, Microsoft 365 connector, multi-step execution, approvals.)

**Prerequisites**

- Labs 1–9 completed.
- Claude desktop with Cowork access.
- The Microsoft 365 connector is approved or the supplied local source pack is used as fallback.

**Process map**

Scope the folder → Connect approved context → Plan the task → Watch and steer → Review files in Microsoft 365

**Step-by-step**

1. Create a clean work folder inside the Lab 10 folder and copy only the reviewed Word, Excel and PowerPoint outputs from earlier labs.
2. Open Claude desktop, select Cowork and run the guided setup if required. Choose only the Lab 10 work folder. Command or in-app command:

   ```bash
   /setup-cowork
   ```

3. Inspect the active plugins, connectors and folder boundary. Record unavailable capabilities rather than requesting broad access.
4. Give Cowork a result-oriented task and require a plan before file changes. Prompt to give Claude:

   ```bash
   Using only this work folder and the approved Microsoft 365 planning context, prepare a consolidated FY2027 Executive Committee hand-off. First show a plan with inputs, reconciliation checks, output files and approval checkpoints. Do not modify or create files until I approve the plan.
   ```

5. Review the plan. Confirm source priority: verified Excel for figures, approved Word documents for narrative, Outlook for decisions and the source register for ownership.
6. Approve the analysis phase only. Ask Cowork to create a discrepancy log covering figures, dates, owners, versions, commitments and missing approvals. Prompt to give Claude:

   ```bash
   Create a discrepancy log before drafting the brief. Compare the approved files and planning messages for figures, dates, owners, version names, commitments and approvals. Cite every source and do not resolve conflicts by guessing.
   ```

7. Resolve high-impact discrepancies in the source files with the named owner. Replace the work-folder copy with the reviewed version.
8. Ask Cowork to create a two-page management brief and updated hand-off index in the folder. Prompt to give Claude:

   ```bash
   Create a two-page management brief and hand-off index from the reconciled sources. Include decision required, strategic choices, marketing priorities, financial outlook, sustainability/people commitments, Q1 milestones, risks and approvals. Cite the source file or message for each section.
   ```

9. Open the generated Word, Excel and PowerPoint files in their native apps. Use Claude for Microsoft 365 to make only selected, tracked corrections.
10. Record final approvals and keep the Cowork task, discrepancy log and source files together as the audit trail.

**Test it**

Cowork worked only inside the scoped project, produced a visible plan and discrepancy log, and every generated Office artifact was reviewed in its native app before the hand-off was approved.

**Troubleshooting**

- Cowork cannot access Microsoft 365 — Use the local approved source pack and record the connector limitation; do not widen permissions merely to complete the lab.
- Cowork writes too early — Require a plan-first approval and give staged approval for analysis, drafting and final file creation.
- Files disagree — Resolve the conflict in the authoritative source with its owner, then rerun only the affected output.

**Challenge**

Turn the approved hand-off workflow into a reusable Cowork skill outline with explicit inputs, checks and approval points.

**Reflection**

Which checkpoint gave you the most control over a multi-step agentic task?

> **Note:** The matching detailed lab folder is in labs/lab-10-coordinate-the-planning-pack-with-claude-cowork/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


### Lab 11 — Automate Excel, Outlook and a Daily Brief with Claude Code

Learning outcome: Use Claude Code and approved connectors to update Excel, search Outlook and produce a daily management brief..

Goal: Build a safe, repeatable work process that refreshes a local Excel control workbook, searches approved planning mail and generates a source-linked daily brief without embedding secrets or auto-sending messages.

**Company use case**

- Department: Business Performance
- Sponsor: Chief Operating Officer
- Decision: Which KPI exception, decision request or overdue action needs management attention today?
- Evidence: Daily control workbook; Approved Outlook planning mail; Brief template; Automation configuration
- Controls: No secrets in source; Explicit MCP approval; No auto-send; Idempotent update and backup

**What you'll build**

A reviewed automation plan, local workbook-update script, connector-assisted Outlook search and generated daily brief with run log.   (Tools: Claude Code, MCP, Microsoft 365 connector, Python, openpyxl, python-docx, run log, approval gates.)

**Prerequisites**

- Labs 1–10 completed.
- Claude Code installed and authenticated with the approved Claude.ai account.
- Python 3 with openpyxl and python-docx available; the lab provides an offline-ready starter.

**Process map**

Plan and inspect → Verify MCP and files → Update Excel locally → Search approved Outlook context → Generate and review daily brief

**Step-by-step**

1. Open a terminal in the Lab 11 folder and inspect every supplied file before starting Claude Code. Command or in-app command:

   ```bash
   pwd
find . -maxdepth 2 -type f -print | sort
   ```

2. Create and activate a local virtual environment, then install only the two required document libraries if they are not already present. Command or in-app command:

   ```bash
   python3 -m venv .venv
source .venv/bin/activate
python -m pip install openpyxl python-docx
   ```

3. Start Claude Code and verify its version and MCP status. The approved Microsoft 365 connector configured in Claude.ai should appear when the same subscription authentication is active. Command or in-app command:

   ```bash
   claude --version
claude mcp list
   ```

4. Inside Claude Code, open /mcp, authenticate the approved Microsoft 365 connector if prompted and inspect the available read/write tools. Do not approve a write tool for this exercise. Command or in-app command:

   ```bash
   /mcp
   ```

5. Ask Claude Code to inspect the workbook, brief template and starter script, then propose a plan before editing. Prompt to give Claude:

   ```bash
   Inspect this lab folder. Explain the workbook sheets, formulas and control cells; the daily-brief template; the starter Python script; and the run-log contract. Propose the smallest safe implementation. Do not edit or run anything until I approve the plan.
   ```

6. Approve the local-file phase. Ask Claude Code to complete or review the workbook updater so it writes today's approved inputs, preserves formulas and formats, creates a timestamped backup and appends a run-log row. Prompt to give Claude:

   ```bash
   Implement the local workbook update only. Preserve formulas, named tables, charts and formats; create a timestamped backup; make the update idempotent; validate expected sheets and columns; and append date, input file, rows changed, status and reviewer placeholder to Run_Log. Do not access Outlook yet.
   ```

7. Run the updater on the fictional input file and inspect the workbook output. Command or in-app command:

   ```bash
   python automation/update_daily_control.py --input inputs/daily-input.csv --workbook Lumina-Living-Daily-Control.xlsx --output outputs/Lumina-Living-Daily-Control-Updated.xlsx
   ```

8. Ask Claude Code to use the approved Microsoft 365 connector to search only the fictional planning messages for the last business day. Require source citations and no draft/send action. Prompt to give Claude:

   ```bash
   Search the approved Lumina Living planning mailbox context for the last business day. Return only decisions requested, overdue actions, material risks and changed deadlines. Cite each message. Do not create, update, draft or send anything in Microsoft 365.
   ```

9. Provide the cited mail findings to the local brief generator and require workbook cell citations for KPI exceptions. Prompt to give Claude:

   ```bash
   Generate today's management brief from outputs/Lumina-Living-Daily-Control-Updated.xlsx and the cited Outlook findings. Use the supplied Word template. Include KPI exceptions with cell citations, decisions requested with message citations, overdue actions, risks, and a reviewer checklist. Do not invent missing information or send the brief.
   ```

10. Run the local brief generator and open the DOCX for review. Command or in-app command:

   ```bash
   python automation/generate_daily_brief.py --workbook outputs/Lumina-Living-Daily-Control-Updated.xlsx --mail inputs/outlook-findings.json --template templates/Daily-Brief-Template.docx --output outputs/Lumina-Living-Daily-Brief.docx
   ```

11. Verify backup creation, formula integrity, cited messages, cited cells, no embedded secrets and a completed run log. Record the human approval without sending the file.

**Test it**

The reviewed scripts run successfully, the updated workbook preserves formulas and charts, the daily brief cites Excel and Outlook evidence, the run log is complete and no email was sent or secret stored.

**Troubleshooting**

- The M365 connector is absent in Claude Code — Run /status to confirm Claude.ai subscription authentication, configure the connector in Claude.ai, then use /mcp; do not hardcode tokens or unreviewed endpoints.
- The workbook loses formulas or formatting — Write only designated input cells, load without data_only, preserve styles and validate formulas before saving.
- The updater duplicates rows — Use a stable business key and make the update idempotent before rerunning.
- Mail search returns too much — Narrow the date, mailbox context, subject prefix and allowed output fields; require citations.

**Challenge**

Add a dry-run flag that reports proposed cell changes and mail-query scope without writing any output.

**Reflection**

Which automation step needs the strongest approval boundary, and how would you monitor it in production?

> **Note:** The matching detailed lab folder is in labs/lab-11-automate-excel-outlook-and-a-daily-brief-with-claude-code/. Use the matching lab folder and its supplied fictional Office files. Claude interfaces and availability can change by plan, platform and tenant. Do not widen permissions, bypass administrator controls or send externally merely to complete a classroom activity.

---


## Wrap-Up — One Governed Company Workflow

You have built a connected Lumina Living planning and management pack rather than a collection of isolated AI demonstrations.

**Business outputs**

- Marketing, strategy, sustainability and HR drafts that use company templates and named reviewers.
- A financial analysis and dashboard with dynamic formulas, controls and management-ready visuals.
- An editable executive deck with native charts, a coherent decision story and source notes.

**Operating controls**

- A permission and source map, prompt contract, review log and human approval boundary.
- An Outlook triage-and-draft pattern that does not silently send mail.
- A scoped Cowork workflow and a Claude Code daily-brief automation with explicit tool approvals.

---


## Next Steps

- Re-run the full Lumina Living flow and verify that every figure and recommendation remains consistent across files.
- Adapt one activity to an approved recurring process in your organisation and define a baseline for time, quality and review effort.
- Ask your Microsoft 365 and Claude administrators which add-ins, connectors, write tools and Cowork surfaces are approved for your role.
- Keep prompts, source registers, decision logs and approval evidence with the final work product.


## Glossary

- **Claude for Microsoft 365** — Anthropic's in-app assistants for Word, Excel, PowerPoint and Outlook.
- **Microsoft 365 connector** — A delegated connection that lets Claude work with authorised SharePoint, OneDrive, Outlook and Teams context.
- **Claude Cowork** — Anthropic's task-oriented desktop mode for multi-step work across scoped files and connected tools.
- **Copilot Cowork** — A separate Microsoft 365 Copilot experience with Microsoft licensing, governance, Work IQ and action approvals.
- **Claude Code** — Anthropic's command-line agent that can work with local files, scripts and approved MCP connectors.
- **MCP** — Model Context Protocol, a standard that lets Claude connect to approved tools and data sources.
- **Delegated permission** — Access exercised on behalf of the signed-in user and limited by that user's existing permissions.
- **Write tool** — A connector capability that can create or update content and therefore needs stronger consent and review.
- **Evidence chain** — The trace from a claim or chart back to its source file, cell, message or approved assumption.
- **Human send gate** — The required user review and approval before an email, invitation or other consequential action is sent.


## References and Further Learning

- Claude for Microsoft 365 overview: https://claude.com/claude-for-microsoft-365
- Set up the Microsoft 365 connector: https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector
- Use Claude for Microsoft 365 with third-party platforms: https://claude.com/docs/office-agents/third-party-platforms
- Get started in Claude Cowork in three steps: https://claude.com/resources/tutorials/get-started-in-claude-cowork-in-three-steps
- Connect Claude Code to tools via MCP: https://code.claude.com/docs/en/mcp
- Copilot Cowork overview: https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
- Microsoft 365 Copilot with Anthropic models: https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-anthropic-apps
- Syracuse University: Claude Microsoft 365 connector: https://its.syr.edu/your-work-apps-meet-your-ai-assistant-using-claudes-microsoft-365-connector/
- Claude for Microsoft 365 setup and use cases: https://justinmckelvey.com/blog/claude-for-microsoft-365
