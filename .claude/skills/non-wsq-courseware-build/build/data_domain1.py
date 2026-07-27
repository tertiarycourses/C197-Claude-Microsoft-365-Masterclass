"""
Domain 1 — Getting Started with Claude for Microsoft 365. Labs 1-4.

THE CONNECTED PROJECT STARTS HERE, IN LAB 1.

Every lab works the SAME deliverable: the Q3 business-review pack for a small
retailer, "Lumina Living". In Lab 1 you get Claude set up and running a first
prompt; each lab after that adds one skill — connecting your files, prompting
effectively, and using AI safely — that you then apply, in Domain 2, to write the
report, analyse the numbers, build the slides and send the emails. Wherever
possible use your OWN non-confidential work; the Lumina Living sample material is
provided for everyone to follow along.
"""

SCENARIO = (
 "Lumina Living is a small home-and-lifestyle retailer. The quarter has just closed and "
 "your manager needs the Q3 business-review pack — a short written report, the numbers "
 "behind it, a slide deck for the management meeting, and the emails that send it out — by "
 "the end of the day. You have a rough brief, a sales workbook and a handful of facts to work "
 "from. Across this course you use Claude alongside Microsoft 365 to turn that raw material "
 "into a finished, checked pack. Use this scenario only if you cannot use real, non-confidential "
 "work of your own; your own material is always preferred."
)

PROJECT_NOTE = (
 "BUILDING BLOCK — what you do in this lab becomes part of your Lumina Living Q3 review pack, "
 "the single deliverable you write, analyse, present and send across all 8 labs."
)

DOMAIN1 = [
 dict(
 num=1, topic=1,
 title="Get Started with Claude for Microsoft 365",
 objective="Sign in to Claude, understand how it works alongside Microsoft 365, and run a first prompt on your task.",
 desc="This lab gets Claude working for you. You sign in at claude.ai, start a new chat, and paste in "
 "the Q3 brief so Claude can summarise your task and list what the review pack needs — so you see the "
 "ask-check loop before you rely on it. " + PROJECT_NOTE,
 build="A working Claude account with your first, verified answer — a plain-language summary of the Q3 task and a checklist of what the pack must contain.",
 services="claude.ai (or the Claude desktop app), Microsoft 365, a web browser",
 steps=[
 ("Sign in at claude.ai (or open the Claude desktop app) and click 'New chat'. This is where you will work with Claude all day.", ""),
 ("Open the sample 'Lumina Living — Q3 Review Brief' (a short Word document the trainer shares), or use a short brief of your own non-confidential work.", ""),
 ("Copy the brief's text and paste it into the Claude chat with this instruction so Claude tells you what the task involves.",
  "Here is the brief for a quarterly business review. In plain language, summarise what I am being asked to produce, then list the separate items the final pack should contain."),
 ("Read Claude's answer. Check it against the brief: does its list match what the brief actually asks for? Add anything it missed.", ""),
 ("Ask one follow-up so you see Claude reason over your material.",
  "For each item in that list, say which Microsoft 365 app I would use to produce it — Word, Excel, PowerPoint or Outlook."),
 ("Confirm the ground rule: Claude has only read text you gave it, and nothing has changed in your files. Claude drafts; you decide what to keep.", ""),
 ("Save this chat — rename it 'Lumina Living Q3'. You now have Claude set up and a clear, checked picture of the task.", ""),
 ],
 test="You are signed in to Claude, and you have a first answer — a summary of the Q3 task and a checklist of the pack's items — that you have checked against the brief and corrected where needed.",
 ),
 dict(
 num=2, topic=1,
 title="Connect Claude to Your Microsoft 365 Files and Apps",
 objective="Give Claude your working files by uploading and pasting, and keep them together in a Project.",
 desc="Now you give Claude your real material to work on. You upload the Q3 brief and the sales workbook, "
 "gather them into a Project with standing instructions, and confirm Claude can read what you gave it — so "
 "every later chat starts with the right context. " + PROJECT_NOTE,
 build="A Claude Project (or a single well-prepared chat) holding your Q3 files, with Claude confirmed to have read them.",
 services="Claude Projects, file upload, custom instructions, connectors (optional)",
 steps=[
 ("Attach a file to the chat: click the paperclip (or drag the file in) and upload the sample 'Lumina Living — Q3 Sales.xlsx' workbook. Claude accepts Word, Excel, PowerPoint, PDF, CSV and images.", ""),
 ("Confirm Claude has read it, and check the answer against the file itself.",
  "From the workbook I just uploaded, list the column headings and tell me how many rows of data there are."),
 ("Create a Project to hold the whole task (if your plan has Projects): open Projects > New project, name it 'Lumina Living — Q3 Review', and add both the brief and the workbook to it. If you do not have Projects, keep working in your renamed Lab 1 chat and re-attach files as needed.", ""),
 ("Give the Project standing instructions so every chat starts the same way. Put this in the Project's custom instructions.",
  "You are helping me prepare Lumina Living's Q3 business review. Use only the files in this project. Keep a professional, concise tone. When you give figures, show where in the data they come from so I can check them."),
 ("Optional — connect a source instead of uploading: if your account offers connectors, open Settings > Connectors and connect OneDrive, SharePoint or Google Drive, then point Claude at the folder. Skip this if your account does not offer it.", ""),
 ("Prove the context works: start a fresh chat inside the Project and ask a question without re-attaching anything.",
  "Without me re-uploading, what files do you have for this review, and what is in each?"),
 ("Confirm Claude answers from the Project's files. Your working set is now connected and reusable.", ""),
 ],
 test="Claude has correctly listed the workbook's columns and row count, your Q3 files sit in a Project (or a prepared chat), and a fresh chat can answer from them without re-uploading.",
 ),
 dict(
 num=3, topic=1,
 title="Write Effective Prompts for Everyday Work Tasks",
 objective="Compare a vague prompt with a specific one and capture a reusable four-part prompt pattern for work tasks.",
 desc="A result is only as good as the prompt. You run a vague prompt, then a specific one that states the "
 "role, context, task and output format, see the difference, and distil what worked into a reusable pattern "
 "you will use for the rest of the course. " + PROJECT_NOTE,
 build="A written four-part prompt pattern (Role · Context · Task · Output) and one strong, tested prompt saved for reuse.",
 services="Prompt design, role/context/task/output, refinement",
 steps=[
 ("Run a deliberately vague prompt in the Project and note how generic the answer is.",
  "Write something about our sales."),
 ("Now run a specific prompt for the same intent and compare the result.",
  "You are my business analyst. Context: this is Lumina Living's Q3 sales workbook. Task: write three short paragraphs summarising how the quarter went for a management audience. Output: plain paragraphs, no jargon, with the key figure named in each."),
 ("Write down the four parts that made the second prompt work: the Role, the Context, the Task, and the Output format.", ""),
 ("Capture your reusable pattern where you can find it — a notes doc, or pinned in the Project.",
  "ROLE: who Claude should act as | CONTEXT: which file/task | TASK: what to produce | OUTPUT: format, length, tone, and what to include"),
 ("Add the conditions that keep results trustworthy: name the file, ask Claude to show where figures come from, and state the length and tone you need.", ""),
 ("Rewrite one request of your own about the Q3 pack using the pattern, and run it.", ""),
 ("Refine once: change the Output part (for example 'make it half as long', or 'more formal') and re-run to see the result change. Keep the better version.", ""),
 ("Save your best prompt in the Project — you will reuse this pattern in every remaining lab.", ""),
 ],
 test="You can show two answers for the same intent (vague vs specific), a written four-part prompt pattern, and one refined prompt that produced the output you specified in the format you asked for.",
 ),
 dict(
 num=4, topic=1,
 title="Use AI Responsibly, Securely and Privately at Work",
 objective="Decide what is safe to share with AI, and write a personal safe-use checklist you apply to the review pack.",
 desc="Before you rely on AI at work, you set the rules. You review what should never go into a prompt, "
 "practise removing sensitive details before sharing, confirm that Claude's output must always be verified, "
 "and write a safe-use checklist you apply to your own material. " + PROJECT_NOTE,
 build="A personal safe-use checklist, and one prompt you have rewritten to remove sensitive data before sending.",
 services="Data privacy, redaction, verification, safe-use checklist",
 steps=[
 ("List the kinds of data that should not go into an AI prompt without approval: passwords and keys, customer names and contact details, staff personal data, unreleased financials, and anything under NDA.", ""),
 ("Practise redacting: take a sentence that names a real customer and rewrite it to make the same request safely.",
  "Rewrite this so it asks the same question without naming anyone: 'Summarise why customer Tan Wei Ming from 12 Orchard Road cancelled his order.'"),
 ("Ask Claude for good practice, then sanity-check its advice against your own organisation's policy.",
  "What should I avoid putting into an AI prompt when working with real company data, and how can I get the same help safely?"),
 ("Confirm the verification rule with a quick test: ask Claude for a specific figure from the workbook, then check it in Excel — never accept a number you cannot tie back to the source.",
  "What was the single best-selling product in the Q3 workbook, and what was its total sales value? Tell me which cells you used."),
 ("Note who is accountable: Claude drafts, but you are responsible for what you send. Decide where you will record that AI helped (for example a note in the document's properties).", ""),
 ("Draft your safe-use checklist — keep confidential data out of prompts; redact before sharing; verify every figure, name and claim; keep a human decision on anything that goes out; record where AI was used.", ""),
 ("Apply the checklist to your Lab 3 prompt: check it contains nothing sensitive, and adjust it if it does.", ""),
 ],
 test="You have a written safe-use checklist, a prompt you rewrote to remove a real name, and a figure from the workbook that you verified in Excel before trusting it.",
 ),
]
