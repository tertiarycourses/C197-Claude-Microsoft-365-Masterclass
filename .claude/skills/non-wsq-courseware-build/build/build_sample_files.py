#!/usr/bin/env python3
"""Generate realistic, fictional company Office files for every C197 lab."""

from datetime import date, datetime, timedelta
import csv
import glob
import importlib
import json
import math
import os
import random
import re
import sys

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor as DocRGB
from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.worksheet.table import Table, TableStyleInfo
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches as PIn, Pt as PPt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C

NAVY = "172B4D"; BLUE = "1F6FEB"; TEAL = "10B981"; VIOLET = "7C3AED"
AMBER = "F59E0B"; RED = "DC2626"; GREY = "5B6372"; LINE = "DDE5EF"
LIGHT = "F5F8FC"; ICE = "EAF2FF"; MINT = "EAF8F3"; WHITE = "FFFFFF"


def repo_root(start):
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    raise RuntimeError("Course repository not found")


def load_activities():
    acts = []
    for path in sorted(glob.glob(os.path.join(HERE, "data_domain[0-9]*.py"))):
        name = os.path.basename(path)[:-3]
        if not re.fullmatch(r"data_domain\d+", name):
            continue
        n = re.search(r"\d+", name).group()
        acts.extend(getattr(importlib.import_module(name), f"DOMAIN{n}"))
    return sorted(acts, key=lambda a: a["num"])


REPO = repo_root(HERE)
ACTS = load_activities()


def lab_folder(a):
    path = os.path.join(REPO, "labs", f"lab-{a['num']:02d}-{C.LAB_SLUGS[a['num']]}")
    os.makedirs(os.path.join(path, "templates"), exist_ok=True)
    return path


def stem(a):
    return f"Lumina-Living-Lab-{a['num']:02d}"


def shade(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def set_doc_defaults(doc):
    sec = doc.sections[0]
    sec.top_margin = Inches(0.62); sec.bottom_margin = Inches(0.62)
    sec.left_margin = Inches(0.72); sec.right_margin = Inches(0.72)
    normal = doc.styles["Normal"]
    normal.font.name = "Arial"; normal.font.size = Pt(10.5); normal.font.color.rgb = DocRGB.from_string(NAVY)
    for name, size, color in [("Title", 28, NAVY), ("Heading 1", 17, BLUE), ("Heading 2", 13, NAVY), ("Heading 3", 11, TEAL)]:
        style = doc.styles[name]
        style.font.name = "Arial"; style.font.size = Pt(size); style.font.bold = True; style.font.color.rgb = DocRGB.from_string(color)


def add_doc_brand(doc, label):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = p.add_run(label.upper())
    r.bold = True; r.font.size = Pt(8.5); r.font.color.rgb = DocRGB.from_string(TEAL)


def callout(doc, title, body, fill=ICE):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0); shade(cell, fill); cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
    p = cell.paragraphs[0]
    r = p.add_run(title + "  "); r.bold = True; r.font.color.rgb = DocRGB.from_string(BLUE)
    p.add_run(body)


def add_table(doc, headers, rows, widths=None):
    table = doc.add_table(rows=1, cols=len(headers)); table.style = "Table Grid"; table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]; cell.text = header; shade(cell, BLUE)
        for run in cell.paragraphs[0].runs:
            run.font.color.rgb = DocRGB(255, 255, 255); run.bold = True; run.font.size = Pt(9)
    for row in rows:
        cells = table.add_row().cells
        for i, value in enumerate(row):
            cells[i].text = str(value)
            for run in cells[i].paragraphs[0].runs: run.font.size = Pt(8.8)
    if widths:
        for row in table.rows:
            for i, width in enumerate(widths): row.cells[i].width = Inches(width)
    return table


def save_company_brief(a, folder):
    doc = Document(); set_doc_defaults(doc); add_doc_brand(doc, f"{C.COURSE_CODE} · Lab {a['num']} · Company source")
    doc.add_paragraph(C.COMPANY, style="Title")
    p = doc.add_paragraph(a["title"]); p.runs[0].bold = True; p.runs[0].font.size = Pt(18); p.runs[0].font.color.rgb = DocRGB.from_string(TEAL)
    p = doc.add_paragraph("FICTIONAL COMPANY TRAINING MATERIAL · FY2027 PLANNING CYCLE")
    p.runs[0].bold = True; p.runs[0].font.color.rgb = DocRGB.from_string(GREY)
    callout(doc, "Decision required", a["case"]["decision"], MINT)
    doc.add_heading("1. Company and mandate", level=1)
    doc.add_paragraph(C.COMPANY_CONTEXT)
    add_table(doc, ["Field", "Company detail"], [
        ("Department", a["case"]["department"]), ("Executive sponsor", a["case"]["sponsor"]),
        ("Business challenge", a["case"]["challenge"]), ("Planning horizon", "FY2027 with Q1 execution milestones"),
        ("Status", "Draft for classroom management review"),
    ], [1.6, 5.2])
    doc.add_heading("2. Evidence available", level=1)
    for source in a["case"]["sources"]:
        doc.add_paragraph(source, style="List Bullet")
    doc.add_heading("3. Required management outputs", level=1)
    add_table(doc, ["Output", "Acceptance evidence", "Owner"], [
        (value, "Source-linked, template-compliant and reviewed", a["case"]["sponsor"]) for value in a["case"]["outputs"]
    ], [2.2, 3.3, 1.3])
    doc.add_heading("4. Measures", level=1)
    add_table(doc, ["Measure", "Definition", "Source owner", "Review frequency"], [
        (metric, f"Company definition for {metric.lower()}", a["case"]["department"], "Monthly") for metric in a["case"]["metrics"]
    ], [1.6, 2.7, 1.5, 1.0])
    doc.add_heading("5. Controls and approval", level=1)
    for control in a["case"]["controls"]:
        doc.add_paragraph(control, style="List Bullet")
    callout(doc, "Evidence rule", "Facts cite their source; calculations cite workbook cells; assumptions name an owner and review date; final release requires the named sponsor.")
    doc.add_heading("6. Management questions", level=1)
    questions = [
        "What decision must be made, and by whom?", "Which evidence is authoritative?",
        "Which assumption could change the recommendation?", "What action, owner and date follow from approval?",
    ]
    for q in questions: doc.add_paragraph(q, style="List Number")
    path = os.path.join(folder, f"{stem(a)}-Company-Brief.docx")
    doc.save(path); print("Saved", path)


def sample_sections(a):
    by_lab = {
        4: [("Executive decision", "Prioritise repeat customers and profitable digital growth while pausing broad discount-led acquisition."),
            ("Marketing choices", "Focus owned channels, targeted lifecycle campaigns and higher-margin product stories."),
            ("90-day action", "Launch two measured pilots with stop/go rules, accountable owners and a reconciled budget.")],
        5: [("Strategic ambition", "Build a profitable omnichannel growth engine with a differentiated home-lifestyle proposition."),
            ("Strategic choices", "Win in curated ranges, integrate customer journeys and strengthen commercial execution."),
            ("Governance", "Six initiatives report through a quarterly scorecard with explicit dependencies and risk owners.")],
        6: [("Reporting boundary", "Singapore retail, office and directly controlled e-commerce operations for FY2026."),
            ("Sustainability performance", "Energy and waste movements are reported with method notes and limitations; no unsupported green claim is made."),
            ("Flexible-work policy", "Eligibility is role-based, decisions are documented and exceptions have a transparent review route.")],
        7: [("CFO headline", "Revenue finished ahead of budget, but contribution quality differs materially by channel."),
            ("Driver", "Digital growth supported the top line while discount and fulfilment economics weakened selected contribution rates."),
            ("Decision", "Protect margin through targeted discount controls and channel-specific action owners.")],
        8: [("Executive story", "Approve three strategic choices, a focused marketing allocation and Q1 financial guardrails."),
            ("Evidence", "The storyline reconciles the approved strategy, marketing plan and financial dashboard."),
            ("Presentation standard", "Native charts, company layouts, conclusion-led titles and source notes keep the deck editable and defensible.")],
        9: [("Thread summary", "The Executive Committee needs the reviewed pack, three owned actions and a confirmed review date."),
            ("Draft response", "A concise reply confirms decisions and attachments and remains unsent until recipient and version checks are complete."),
            ("Meeting brief", "Purpose, agenda, pre-read and one decision required are explicit.")],
        10: [("Cowork hand-off", "The scoped project reconciles source files before generating a two-page management brief."),
             ("Discrepancy control", "Figures, owners, dates, versions and approvals are resolved in the authoritative source."),
             ("Native review", "Generated files return to Word, Excel and PowerPoint for tracked human review.")],
        11: [("Daily headline", "One margin exception and two overdue actions require management attention today."),
             ("Evidence", "KPI exceptions cite workbook cells and decisions cite approved Outlook messages."),
             ("Automation control", "The run is idempotent, creates a backup, logs changes and does not send email.")],
    }
    return by_lab.get(a["num"], [
        ("Management outcome", a["objective"]), ("Evidence boundary", "; ".join(a["case"]["sources"])),
        ("Approval", f"Final approval: {a['case']['sponsor']}"),
    ])


def save_work_sample(a, folder):
    doc = Document(); set_doc_defaults(doc); add_doc_brand(doc, f"{C.COURSE_CODE} · Claude-generated work sample")
    doc.add_paragraph(a["title"], style="Title")
    p = doc.add_paragraph(f"{C.COMPANY} · Illustrative reviewed output")
    p.runs[0].bold = True; p.runs[0].font.color.rgb = DocRGB.from_string(TEAL)
    callout(doc, "Management outcome", a["case"]["decision"], MINT)
    for title, body in sample_sections(a):
        doc.add_heading(title, level=1)
        doc.add_paragraph(body)
        if title.lower() in ("marketing choices", "strategic choices", "driver", "evidence"):
            add_table(doc, ["Finding / choice", "Evidence", "Owner", "Next review"], [
                (f"{title} item {i}", a["case"]["sources"][(i-1) % len(a["case"]["sources"])], a["case"]["department"], f"Q{i} FY2027") for i in range(1, 4)
            ], [2.0, 2.4, 1.5, 0.9])
    doc.add_heading("Source and approval note", level=1)
    doc.add_paragraph("Illustrative output generated for training from fictional Lumina Living sources. Figures and claims require source reconciliation. Release status: Pending named human approval.")
    path = os.path.join(folder, f"{stem(a)}-Claude-Generated-Work-Sample.docx")
    doc.save(path); print("Saved", path)


def save_prompt_template(a, folder):
    doc = Document(); set_doc_defaults(doc); add_doc_brand(doc, f"{C.COURSE_CODE} · Reusable template")
    doc.add_paragraph("Prompt and Review Contract", style="Title")
    p = doc.add_paragraph(f"Lab {a['num']} · {a['title']}"); p.runs[0].bold = True; p.runs[0].font.color.rgb = DocRGB.from_string(TEAL)
    for heading, hint in [
        ("1. Business result", "Decision, audience and artifact required"),
        ("2. Approved evidence", "Open files, tables, ranges, sections or messages Claude may use"),
        ("3. Constraints", "Scope, style, formulas, length, preservation rules and prohibited actions"),
        ("4. Output contract", "Required structure, format, citations and exception handling"),
        ("5. Verification", "Checks the user will perform independently"),
        ("6. Approval gate", "Named person who accepts, saves, writes, sends or releases"),
    ]:
        doc.add_heading(heading, level=1)
        callout(doc, "Complete this field", hint, LIGHT)
        doc.add_paragraph("\n")
    doc.add_heading("Review checklist", level=1)
    add_table(doc, ["Check", "Evidence", "Result", "Reviewer"], [
        ("Sources cited", "", "Pending", ""), ("Figures reconciled", "", "Pending", ""),
        ("Template preserved", "", "Pending", ""), ("Risks and assumptions labelled", "", "Pending", ""),
        ("Approval recorded", "", "Pending", ""),
    ], [2.0, 2.5, 1.1, 1.2])
    path = os.path.join(folder, "templates", "Prompt-and-Review-Template.docx")
    doc.save(path); print("Saved", path)


def style_header(ws, row=1):
    for cell in ws[row]:
        if cell.value is None: continue
        cell.font = Font(name="Arial", bold=True, color=WHITE)
        cell.fill = PatternFill("solid", fgColor=BLUE)
        cell.alignment = Alignment(wrap_text=True, vertical="center")


def style_sheet(ws, widths=None, freeze="A2"):
    ws.sheet_view.showGridLines = False
    if freeze: ws.freeze_panes = freeze
    for col, width in (widths or {}).items(): ws.column_dimensions[col].width = width
    ws.page_setup.orientation = "landscape"; ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True


MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def add_readme_sheet(wb, a):
    ws = wb.active; ws.title = "Read_Me"; ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 3; ws.column_dimensions["B"].width = 25; ws.column_dimensions["C"].width = 90
    ws.merge_cells("B2:C3"); ws["B2"] = f"{C.COMPANY.upper()} · LAB {a['num']:02d}"
    ws["B2"].font = Font(name="Arial", size=22, bold=True, color=WHITE); ws["B2"].fill = PatternFill("solid", fgColor=NAVY); ws["B2"].alignment = Alignment(vertical="center")
    rows = [("Activity", a["title"]), ("Decision", a["case"]["decision"]), ("Department", a["case"]["department"]),
            ("Sponsor", a["case"]["sponsor"]), ("Fictional data", "All names, messages and figures are synthetic training material."),
            ("Acceptance", a["test"])]
    for r, (label, value) in enumerate(rows, 5):
        ws[f"B{r}"] = label; ws[f"C{r}"] = value
        ws[f"B{r}"].font = Font(name="Arial", bold=True, color=BLUE); ws[f"B{r}"].fill = PatternFill("solid", fgColor=ICE)
        ws[f"C{r}"].alignment = Alignment(wrap_text=True, vertical="top")
    ws.print_area = "B2:C10"; ws.page_setup.fitToHeight = 1


def add_control_data(wb, a):
    ws = wb.create_sheet("Management_Control")
    style_sheet(ws, {"A": 12, "B": 24, "C": 16, "D": 16, "E": 16, "F": 16, "G": 18, "H": 18})
    headers = ["Month", "Measure", "Budget", "Actual", "Variance", "Variance_Pct", "Owner", "Status"]
    ws.append(headers); style_header(ws)
    random.seed(1970 + a["num"])
    row = 2
    for month_i, month in enumerate(MONTHS, 1):
        for metric_i, metric in enumerate(a["case"]["metrics"][:4], 1):
            budget = 80000 + a["num"] * 1700 + metric_i * 6200 + month_i * 1250
            factor = 0.91 + random.random() * 0.20
            actual = round(budget * factor, 2)
            ws.append([month, metric, budget, actual, f"=D{row}-C{row}", f'=IF(C{row}=0,0,E{row}/C{row})', a["case"]["department"], f'=IF(ABS(F{row})<=0.05,"On track",IF(F{row}>0.05,"Above","Attention"))'])
            ws[f"C{row}"].number_format = "$#,##0"; ws[f"D{row}"].number_format = "$#,##0"; ws[f"E{row}"].number_format = "$#,##0"; ws[f"F{row}"].number_format = "0.0%"
            row += 1
    table = Table(displayName=f"tblLab{a['num']:02d}Control", ref=f"A1:H{row-1}")
    table.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True, showColumnStripes=False)
    ws.add_table(table); ws.auto_filter.ref = f"A1:H{row-1}"
    return ws


def add_source_register(wb, a):
    ws = wb.create_sheet("Source_Register")
    style_sheet(ws, {"A": 7, "B": 34, "C": 24, "D": 18, "E": 18, "F": 18})
    ws.append(["ID", "Source", "Owner", "Approved use", "Last reviewed", "Status"]); style_header(ws)
    for i, source in enumerate(a["case"]["sources"], 1):
        ws.append([f"S{i:02d}", source, a["case"]["department"], a["case"]["decision"], date(2026, 8, 12), "Approved for training"])
        ws[f"E{i+1}"].number_format = "dd-mmm-yyyy"
    return ws


def add_review_log(wb, title="Review_Log"):
    ws = wb.create_sheet(title)
    style_sheet(ws, {"A": 14, "B": 24, "C": 38, "D": 18, "E": 18, "F": 16})
    ws.append(["Date", "Check", "Evidence / change", "Owner", "Reviewer", "Status"]); style_header(ws)
    ws.append([date(2026, 8, 12), "Starter created", "Fictional training workbook generated", "Courseware team", "", "Open"])
    ws["A2"].number_format = "dd-mmm-yyyy"
    return ws


def build_finance_workbook(a):
    wb = Workbook(); add_readme_sheet(wb, a)
    dash = wb.create_sheet("Dashboard", 0); dash.sheet_view.showGridLines = False
    for col in range(1, 15): dash.column_dimensions[chr(64 + col)].width = 10
    dash.merge_cells("B2:M3"); dash["B2"] = "LUMINA LIVING · FY2026 FINANCIAL DASHBOARD"
    dash["B2"].font = Font(name="Arial", size=21, bold=True, color=WHITE); dash["B2"].fill = PatternFill("solid", fgColor=NAVY); dash["B2"].alignment = Alignment(horizontal="center", vertical="center")
    tx = wb.create_sheet("Transactions")
    style_sheet(tx, {"A": 14, "B": 13, "C": 11, "D": 13, "E": 14, "F": 22, "G": 12, "H": 10, "I": 13, "J": 13, "K": 14, "L": 13, "M": 14, "N": 15})
    headers = ["Txn_ID", "Date", "Month", "Region", "Channel", "Product", "Category", "Units", "Unit_Price", "Discount_Pct", "Revenue", "Unit_Cost", "Gross_Profit", "Fulfilment_Cost"]
    tx.append(headers); style_header(tx)
    products = {"Aurora Desk Lamp": ("Lighting", 89, 42), "Halo Floor Lamp": ("Lighting", 159, 79), "Luna Throw": ("Living", 69, 31), "Nest Basket": ("Living", 55, 24), "Arc Side Table": ("Living", 139, 72), "Focus Monitor Stand": ("Workspace", 79, 36)}
    regions = ["North", "South", "East", "West"]; channels = ["Retail", "Online", "Marketplace"]
    random.seed(197); start = date(2026, 1, 1)
    for i in range(1, 721):
        dt = start + timedelta(days=random.randint(0, 364)); month = dt.strftime("%b")
        region = random.choices(regions, [31, 23, 27, 19])[0]; channel = random.choices(channels, [42, 37, 21])[0]
        product = random.choice(list(products)); category, price, cost = products[product]
        units = random.randint(1, 8); discount = random.choices([0, .05, .10, .15, .20], [20, 22, 31, 20, 7])[0]
        r = i + 1; fulfil = 6 if channel == "Retail" else (11 if channel == "Online" else 15)
        tx.append([f"LL-{i:05d}", dt, month, region, channel, product, category, units, price, discount, f"=H{r}*I{r}*(1-J{r})", cost, f"=K{r}-(H{r}*L{r})", f"=H{r}*{fulfil}"])
        for c in (9, 11, 12, 13, 14): tx.cell(r, c).number_format = "$#,##0.00"
        tx.cell(r, 10).number_format = "0%"; tx.cell(r, 2).number_format = "dd-mmm-yyyy"
    table = Table(displayName="tblFinance", ref=f"A1:N{tx.max_row}"); table.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True, showColumnStripes=False); tx.add_table(table)
    budget = wb.create_sheet("Budget"); style_sheet(budget, {"A": 12, "B": 18, "C": 18, "D": 18, "E": 18})
    budget.append(["Month", "Revenue_Budget", "Gross_Profit_Budget", "Marketing_Budget", "Operating_Cost_Budget"]); style_header(budget)
    for i, month in enumerate(MONTHS, 2):
        rev = 72000 + (i - 2) * 2600
        budget.append([month, rev, rev * .43, 9000 + (i % 3) * 1200, 21000 + (i % 4) * 700])
        for c in range(2, 6): budget.cell(i, c).number_format = "$#,##0"
    assumptions = wb.create_sheet("Assumptions"); style_sheet(assumptions, {"A": 26, "B": 16, "C": 48})
    assumptions.append(["Assumption", "Base value", "Definition / control"]); style_header(assumptions)
    for row in [("Unit growth", .08, "Applied only to FY2027 scenario"), ("Average discount", .09, "Weighted average target"), ("Unit-cost inflation", .04, "Supplier planning assumption"), ("Marketing spend change", .06, "Versus FY2026 budget")]: assumptions.append(row)
    for r in range(2, 6): assumptions[f"B{r}"].number_format = "0.0%"
    ana = wb.create_sheet("Analysis"); ana.sheet_view.showGridLines = False
    for col, width in {"A": 3, "B": 22, "C": 18, "D": 18, "E": 4, "F": 17, "G": 17, "H": 17, "I": 17}.items(): ana.column_dimensions[col].width = width
    ana.merge_cells("B2:I2"); ana["B2"] = "FY2026 ACTUAL VS BUDGET ANALYSIS"; ana["B2"].font = Font(name="Arial", size=20, bold=True, color=WHITE); ana["B2"].fill = PatternFill("solid", fgColor=NAVY)
    kpis = [("Revenue", "=SUM(Transactions!K2:K721)"), ("Gross Profit", "=SUM(Transactions!M2:M721)"), ("Gross Margin", "=IF(C4=0,0,C5/C4)"), ("Operating Contribution", "=C5-SUM(Transactions!N2:N721)-SUM(Budget!D2:D13)")]
    for r, (label, formula) in enumerate(kpis, 4):
        ana[f"B{r}"] = label; ana[f"C{r}"] = formula; ana[f"B{r}"].font = Font(name="Arial", bold=True, color=BLUE); ana[f"B{r}"].fill = PatternFill("solid", fgColor=ICE); ana[f"C{r}"].number_format = "0.0%" if label == "Gross Margin" else "$#,##0"
    ana.append([])
    for cell, value in [("B10", "Month"), ("C10", "Actual Revenue"), ("D10", "Budget Revenue"), ("F10", "Channel"), ("G10", "Revenue"), ("H10", "Gross Profit"), ("I10", "Contribution")]: ana[cell] = value
    for cell in ["B10", "C10", "D10", "F10", "G10", "H10", "I10"]: ana[cell].font = Font(name="Arial", bold=True, color=WHITE); ana[cell].fill = PatternFill("solid", fgColor=TEAL)
    for idx, month in enumerate(MONTHS, 11):
        ana[f"B{idx}"] = month; ana[f"C{idx}"] = f'=SUMIF(Transactions!$C$2:$C$721,B{idx},Transactions!$K$2:$K$721)'; ana[f"D{idx}"] = f'=INDEX(Budget!$B$2:$B$13,MATCH(B{idx},Budget!$A$2:$A$13,0))'
        ana[f"C{idx}"].number_format = "$#,##0"; ana[f"D{idx}"].number_format = "$#,##0"
    for idx, channel in enumerate(channels, 11):
        ana[f"F{idx}"] = channel; ana[f"G{idx}"] = f'=SUMIF(Transactions!$E$2:$E$721,F{idx},Transactions!$K$2:$K$721)'; ana[f"H{idx}"] = f'=SUMIF(Transactions!$E$2:$E$721,F{idx},Transactions!$M$2:$M$721)'; ana[f"I{idx}"] = f'=H{idx}-SUMIF(Transactions!$E$2:$E$721,F{idx},Transactions!$N$2:$N$721)'
        for c in "GHI": ana[f"{c}{idx}"].number_format = "$#,##0"
    # Dashboard KPI cards
    cards = [("B5:D5", "B6:D7", "REVENUE", "=Analysis!C4", "$#,##0"), ("E5:G5", "E6:G7", "GROSS PROFIT", "=Analysis!C5", "$#,##0"), ("H5:J5", "H6:J7", "GROSS MARGIN", "=Analysis!C6", "0.0%"), ("K5:M5", "K6:M7", "OPERATING CONTRIBUTION", "=Analysis!C7", "$#,##0")]
    for label_rng, value_rng, label, formula, fmt in cards:
        dash.merge_cells(label_rng); dash.merge_cells(value_rng)
        l = dash[label_rng.split(":")[0]]; v = dash[value_rng.split(":")[0]]
        l.value = label; v.value = formula
        for cell in (l, v): cell.fill = PatternFill("solid", fgColor=ICE); cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        l.font = Font(name="Arial", size=10, bold=True, color=BLUE); v.font = Font(name="Arial", size=18, bold=True, color=NAVY); v.number_format = fmt
    line = LineChart(); line.title = "Monthly revenue: actual vs budget"; line.style = 13; line.y_axis.title = "Revenue ($)"; line.x_axis.title = "Month"
    line.add_data(Reference(ana, min_col=3, max_col=4, min_row=10, max_row=22), titles_from_data=True); line.set_categories(Reference(ana, min_col=2, min_row=11, max_row=22)); line.width = 11.5; line.height = 7.2; dash.add_chart(line, "B10")
    bar = BarChart(); bar.type = "bar"; bar.title = "Operating contribution by channel"; bar.style = 10; bar.x_axis.title = "Contribution ($)"
    bar.add_data(Reference(ana, min_col=9, min_row=10, max_row=13), titles_from_data=True); bar.set_categories(Reference(ana, min_col=6, min_row=11, max_row=13)); bar.width = 11.5; bar.height = 7.2; dash.add_chart(bar, "H10")
    var = BarChart(); var.type = "col"; var.title = "Monthly budget variance"; var.style = 11
    # Use two series for transparency; management can see actual and budget side-by-side.
    var.add_data(Reference(ana, min_col=3, max_col=4, min_row=10, max_row=22), titles_from_data=True); var.set_categories(Reference(ana, min_col=2, min_row=11, max_row=22)); var.width = 12.2; var.height = 7.0; dash.add_chart(var, "B25")
    dash["H25"] = "DEFINITIONS & CONTROLS"; dash["H25"].font = Font(name="Arial", bold=True, color=WHITE); dash["H25"].fill = PatternFill("solid", fgColor=TEAL)
    for i, text in enumerate(["Gross margin = Gross profit / Revenue", "Operating contribution deducts fulfilment and marketing budget", "Scenario assumptions remain separate from actuals", "All data is fictional training material", "Last refreshed: 12 Aug 2026"], 26): dash[f"H{i}"] = text
    dash.print_area = "B2:M34"; dash.page_setup.orientation = "landscape"; dash.page_setup.fitToWidth = 1; dash.page_setup.fitToHeight = 1; dash.sheet_properties.pageSetUpPr.fitToPage = True
    add_source_register(wb, a); add_review_log(wb, "Audit_Log")
    wb.calculation.fullCalcOnLoad = True; wb.calculation.forceFullCalc = True; wb.calculation.calcMode = "auto"
    return wb


def save_workbook(a, folder):
    if a["num"] == 7:
        wb = build_finance_workbook(a)
    else:
        wb = Workbook(); add_readme_sheet(wb, a); add_control_data(wb, a); add_source_register(wb, a); add_review_log(wb)
        # Put a simple management chart on a Summary sheet for realistic use.
        summary = wb.create_sheet("Summary", 0); summary.sheet_view.showGridLines = False
        summary.merge_cells("B2:J3"); summary["B2"] = f"{C.COMPANY.upper()} · {a['title'].upper()}"
        summary["B2"].font = Font(name="Arial", size=18, bold=True, color=WHITE); summary["B2"].fill = PatternFill("solid", fgColor=NAVY); summary["B2"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        summary["B5"] = "Decision"; summary["C5"] = a["case"]["decision"]; summary["B5"].font = Font(name="Arial", bold=True, color=BLUE); summary["B5"].fill = PatternFill("solid", fgColor=ICE); summary["C5"].alignment = Alignment(wrap_text=True)
        summary.column_dimensions["B"].width = 18; summary.column_dimensions["C"].width = 78
        summary["B8"] = "Use Management_Control for detailed fictional measures and Review_Log for approvals."
        summary.merge_cells("B8:J9"); summary["B8"].alignment = Alignment(wrap_text=True, vertical="center")
        summary.print_area = "B2:J12"; summary.page_setup.orientation = "landscape"; summary.page_setup.fitToWidth = 1; summary.page_setup.fitToHeight = 1; summary.sheet_properties.pageSetUpPr.fitToPage = True
    path = os.path.join(folder, f"{stem(a)}-Working-Workbook.xlsx")
    wb.save(path); print("Saved", path)


def save_decision_log(a, folder):
    wb = Workbook(); ws = wb.active; ws.title = "Decision_Log"
    style_sheet(ws, {"A": 12, "B": 34, "C": 28, "D": 24, "E": 18, "F": 15, "G": 16})
    ws.append(["Decision_ID", "Decision / approval", "Evidence", "Options considered", "Owner", "Due date", "Status"]); style_header(ws)
    for i, output in enumerate(a["case"]["outputs"], 1):
        ws.append([f"D-{a['num']:02d}-{i:02d}", f"Approve {output}", "; ".join(a["case"]["sources"][:2]), "Approve / revise / defer", a["case"]["sponsor"], date(2026, 9, min(28, 5 + i * 4)), "Pending"])
        ws[f"F{i+1}"].number_format = "dd-mmm-yyyy"
    ws2 = wb.create_sheet("Approval_Checklist"); style_sheet(ws2, {"A": 30, "B": 20, "C": 24, "D": 18})
    ws2.append(["Control", "Evidence location", "Reviewer", "Status"]); style_header(ws2)
    for control in a["case"]["controls"]:
        ws2.append([control, "", "", "Pending"])
    path = os.path.join(folder, "templates", "Decision-and-Approval-Log.xlsx")
    wb.save(path); print("Saved", path)


def ppt_rect(slide, x, y, w, h, fill, radius=True, line=None):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE, PIn(x), PIn(y), PIn(w), PIn(h))
    shape.fill.solid(); shape.fill.fore_color.rgb = RGBColor.from_string(fill); shape.line.color.rgb = RGBColor.from_string(line or fill)
    return shape


def ppt_text(slide, x, y, w, h, text, size=18, color=NAVY, bold=False, align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(PIn(x), PIn(y), PIn(w), PIn(h)); tf = box.text_frame; tf.clear(); tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    box.text_frame.margin_left = 0; box.text_frame.margin_right = 0
    box.text_frame.margin_top = 0; box.text_frame.margin_bottom = 0
    p = tf.paragraphs[0]; p.alignment = align
    run = p.add_run(); run.text = text; run.font.name = "Arial"; run.font.size = PPt(size); run.font.bold = bold; run.font.color.rgb = RGBColor.from_string(color)
    return box


def slide_base(prs, title, kicker, number):
    s = prs.slides.add_slide(prs.slide_layouts[6]); ppt_rect(s, 0, 0, 13.333, 7.5, WHITE, False)
    ppt_rect(s, 0, 0, .18, 7.5, TEAL, False); ppt_text(s, .75, .28, 11.6, .3, kicker.upper(), 11, TEAL, True)
    ppt_text(s, .75, .72, 11.8, .72, title, 27, NAVY, True); ppt_rect(s, .75, 1.62, 11.8, .02, LINE, False)
    ppt_text(s, .75, 7.08, 8.5, .2, f"{C.COMPANY} · Fictional training material", 8.5, GREY)
    ppt_text(s, 12.0, 7.05, .55, .22, str(number), 9, GREY, True, PP_ALIGN.RIGHT)
    return s


def add_cards(slide, items, y=2.0):
    cols = 2; card_w = 5.55; card_h = 1.55; gap_x = .55; gap_y = .38
    colors = [BLUE, TEAL, VIOLET, AMBER]
    for i, (head, body) in enumerate(items[:4]):
        row, col = divmod(i, cols); x = .85 + col * (card_w + gap_x); yy = y + row * (card_h + gap_y)
        ppt_rect(slide, x, yy, card_w, card_h, LIGHT, True, LINE); ppt_rect(slide, x, yy, .12, card_h, colors[i], False)
        ppt_text(slide, x + .28, yy + .13, card_w - .48, .38, head, 16, colors[i], True)
        ppt_text(slide, x + .28, yy + .56, card_w - .48, .78, body, 12.5, NAVY)


def add_flow(slide, steps, y=2.65):
    n = len(steps); gap = .22; total = 11.55; w = (total - gap * (n - 1)) / n
    for i, step in enumerate(steps):
        x = .88 + i * (w + gap); color = [BLUE, TEAL, VIOLET, AMBER, BLUE][i % 5]
        ppt_rect(slide, x, y, w, 1.6, LIGHT, True, LINE); ppt_text(slide, x + .12, y + .12, .42, .42, f"{i+1:02d}", 12, color, True)
        ppt_text(slide, x + .12, y + .58, w - .24, .7, step, 12.5, NAVY, True, PP_ALIGN.CENTER)
        if i < n - 1: ppt_text(slide, x + w, y + .55, gap, .45, "›", 22, GREY, True, PP_ALIGN.CENTER)


def add_native_chart(slide, x, y, w, h, title, categories, series):
    data = CategoryChartData(); data.categories = categories
    for name, values in series: data.add_series(name, values)
    chart = slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, PIn(x), PIn(y), PIn(w), PIn(h), data).chart
    chart.has_title = True; chart.chart_title.text_frame.text = title; chart.has_legend = True; chart.legend.position = XL_LEGEND_POSITION.BOTTOM
    chart.value_axis.has_major_gridlines = True
    return chart


def save_presentation(a, folder):
    prs = Presentation(); prs.slide_width = PIn(13.333); prs.slide_height = PIn(7.5)
    cover = prs.slides.add_slide(prs.slide_layouts[6]); ppt_rect(cover, 0, 0, 13.333, 7.5, WHITE, False); ppt_rect(cover, 0, 0, .22, 7.5, TEAL, False)
    ppt_text(cover, .9, 1.0, 10.8, .35, f"{C.COMPANY.upper()} · FY2027", 14, TEAL, True)
    ppt_text(cover, .9, 1.65, 11.3, 1.45, a["title"], 36, NAVY, True)
    ppt_text(cover, .9, 3.45, 10.8, .8, a["case"]["decision"], 19, GREY)
    ppt_rect(cover, .9, 5.15, 3.7, .72, ICE, True); ppt_text(cover, 1.15, 5.28, 3.2, .4, f"LAB {a['num']:02d} · EDITABLE STARTER", 11, BLUE, True, PP_ALIGN.CENTER)
    ppt_text(cover, .9, 6.7, 10.8, .25, "Fictional company training material · Pending management approval", 10, GREY)
    s = slide_base(prs, "The business decision", "Executive context", 2)
    callouts = [("Challenge", a["case"]["challenge"]), ("Sponsor", a["case"]["sponsor"]), ("Outputs", "; ".join(a["case"]["outputs"])), ("Controls", "; ".join(a["case"]["controls"]))]
    add_cards(s, callouts)
    s = slide_base(prs, "Evidence-to-decision process", "Native process map", 3); add_flow(s, a["deck_flow"])
    s = slide_base(prs, "Management evidence", "Editable visual", 4)
    add_native_chart(s, .8, 1.95, 7.5, 4.75, "Illustrative monthly performance", MONTHS[:6], [("Budget", [82, 85, 88, 91, 94, 98]), ("Actual", [79, 87, 90, 88, 99, 104])])
    ppt_rect(s, 8.65, 1.95, 3.8, 4.75, LIGHT, True, LINE); ppt_text(s, 8.95, 2.25, 3.2, .35, "WHAT MANAGEMENT NEEDS", 11, TEAL, True)
    y = 2.85
    for metric in a["case"]["metrics"][:4]:
        ppt_text(s, 8.95, y, 3.05, .45, "• " + metric, 15, NAVY, True); y += .72
    s = slide_base(prs, "Professional practice", "Decision and control cards", 5); add_cards(s, a["deck_cards"])
    s = slide_base(prs, "Decision and approval", "Executive close", 6)
    cards = [("Decision required", a["case"]["decision"]), ("Evidence check", "Reconcile sources, cells, versions and owners."), ("Approval", f"Named sponsor: {a['case']['sponsor']}"), ("Next step", a["build"])]
    add_cards(s, cards)
    # Lab 8 carries a richer sample with an integrated strategic/marketing story.
    if a["num"] == 8:
        s = slide_base(prs, "Profitable growth requires three choices", "Strategy", 7)
        add_cards(s, [("Curated differentiation", "Invest in ranges where design, advice and margin reinforce one another."), ("Connected customer journey", "Use owned channels to move from discovery to repeat purchase."), ("Commercial discipline", "Tie campaign, discount and fulfilment decisions to contribution."), ("Explicit non-priority", "Avoid broad discount-led growth without a measurable stop/go rule.")])
        s = slide_base(prs, "Marketing allocation follows customer and margin evidence", "Marketing", 8)
        add_native_chart(s, .8, 1.95, 7.6, 4.75, "Illustrative channel contribution", ["Retail", "Online", "Marketplace"], [("Revenue", [420, 360, 220]), ("Contribution", [165, 132, 55])])
        ppt_rect(s, 8.75, 1.95, 3.7, 4.75, LIGHT, True, LINE); ppt_text(s, 9.0, 2.25, 3.15, .45, "DECISION LOGIC", 12, TEAL, True)
        ppt_text(s, 9.0, 3.0, 3.1, 2.9, "1  Protect profitable retail\n\n2  Scale owned digital\n\n3  Tighten marketplace economics", 17, NAVY, True)
        s = slide_base(prs, "Q1 roadmap converts choices into accountable work", "Execution", 9); add_flow(s, ["Confirm owners", "Launch two pilots", "Review economics", "Scale or stop", "Report to ExCo"])
        s = slide_base(prs, "Approve the plan with four guardrails", "Executive decision", 10); add_cards(s, [("Budget", "Release in stages against evidence."), ("Margin", "No growth target without contribution control."), ("Capability", "Fund analytics and lifecycle execution."), ("Governance", "Monthly review; quarterly choice reset.")])
    # Uniform Fade transition.
    from lxml import etree
    from pptx.oxml.ns import qn
    xml = '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" spd="med"><p:fade/></p:transition>'
    for slide in prs.slides:
        if slide.element.find(qn("p:transition")) is None: slide.element.append(etree.fromstring(xml))
    path = os.path.join(folder, f"{stem(a)}-Executive-Starter.pptx")
    prs.save(path); print("Saved", path)


def save_lab11_automation(a, folder):
    auto = os.path.join(folder, "automation"); inputs = os.path.join(folder, "inputs"); outputs = os.path.join(folder, "outputs")
    os.makedirs(auto, exist_ok=True); os.makedirs(inputs, exist_ok=True); os.makedirs(outputs, exist_ok=True)
    updater = '''#!/usr/bin/env python3
"""Safe fictional daily-control updater. Review before use."""
import argparse, csv, os, shutil
from datetime import datetime
from openpyxl import load_workbook

p=argparse.ArgumentParser(); p.add_argument("--input",required=True); p.add_argument("--workbook",required=True); p.add_argument("--output",required=True); p.add_argument("--dry-run",action="store_true"); args=p.parse_args()
wb=load_workbook(args.workbook); required={"Management_Control","Review_Log"}; missing=required-set(wb.sheetnames)
if missing: raise SystemExit(f"Missing sheets: {sorted(missing)}")
rows=list(csv.DictReader(open(args.input,encoding="utf-8")))
ws=wb["Management_Control"]; keys={(ws.cell(r,1).value,ws.cell(r,2).value):r for r in range(2,ws.max_row+1)}
changes=[]
for item in rows:
    key=(item["Month"],item["Measure"]); row=keys.get(key)
    if not row: continue
    old=ws.cell(row,4).value; new=float(item["Actual"])
    if old!=new: changes.append((row,old,new))
if args.dry_run:
    print(f"DRY RUN: {len(changes)} proposed changes"); [print(x) for x in changes]; raise SystemExit(0)
backup=args.workbook+"."+datetime.now().strftime("%Y%m%d-%H%M%S")+".bak"; shutil.copy2(args.workbook,backup)
for row,old,new in changes: ws.cell(row,4).value=new
log=wb["Review_Log"]; log.append([datetime.now(),"Daily update",f"{len(changes)} actual values updated",os.getenv("USER","training-user"),"","Pending review"])
os.makedirs(os.path.dirname(args.output) or ".",exist_ok=True); wb.save(args.output); print(args.output)
'''
    brief = '''#!/usr/bin/env python3
"""Generate a source-linked fictional daily management brief."""
import argparse, json
from docx import Document
from openpyxl import load_workbook

p=argparse.ArgumentParser(); p.add_argument("--workbook",required=True); p.add_argument("--mail",required=True); p.add_argument("--template",required=True); p.add_argument("--output",required=True); args=p.parse_args()
wb=load_workbook(args.workbook,data_only=False); ws=wb["Management_Control"]
exceptions=[]
for r in range(2,ws.max_row+1):
    status=ws.cell(r,8).value
    if status and "Attention" in str(status): exceptions.append((ws.cell(r,1).value,ws.cell(r,2).value,f"Management_Control!H{r}"))
mail=json.load(open(args.mail,encoding="utf-8")); doc=Document(args.template)
doc.add_heading("Today's KPI exceptions",level=1)
for month,metric,cite in exceptions[:8]: doc.add_paragraph(f"{month} · {metric} — review required ({cite})",style="List Bullet")
doc.add_heading("Planning decisions and actions",level=1)
for item in mail: doc.add_paragraph(f"{item['summary']} ({item['citation']})",style="List Bullet")
doc.add_heading("Reviewer checklist",level=1)
for item in ["Workbook cells checked","Message citations opened","Recipients and attachments verified","Human approval recorded"]: doc.add_paragraph(item,style="List Bullet")
doc.save(args.output); print(args.output)
'''
    with open(os.path.join(auto, "update_daily_control.py"), "w", encoding="utf-8") as fh: fh.write(updater)
    with open(os.path.join(auto, "generate_daily_brief.py"), "w", encoding="utf-8") as fh: fh.write(brief)
    with open(os.path.join(inputs, "daily-input.csv"), "w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh); writer.writerow(["Month", "Measure", "Actual"])
        for metric, value in zip(a["case"]["metrics"][:4], [93500, 2, 4, 1]): writer.writerow(["Aug", metric, value])
    findings = [{"summary": "Executive Committee requested the reconciled Q1 milestone list by 4 pm.", "citation": "Outlook message LL-MSG-009"}, {"summary": "Finance owner confirmed the revised contribution assumption needs CFO approval.", "citation": "Outlook message LL-MSG-012"}]
    with open(os.path.join(inputs, "outlook-findings.json"), "w", encoding="utf-8") as fh: json.dump(findings, fh, indent=2)
    # The command in the lab expects this convenience filename and template path.
    workbook = os.path.join(folder, f"{stem(a)}-Working-Workbook.xlsx")
    target = os.path.join(folder, "Lumina-Living-Daily-Control.xlsx")
    import shutil; shutil.copy2(workbook, target)
    template = os.path.join(folder, "templates", "Daily-Brief-Template.docx")
    doc = Document(); set_doc_defaults(doc); add_doc_brand(doc, "Daily management brief template")
    doc.add_paragraph("Lumina Living Daily Management Brief", style="Title"); callout(doc, "Control", "Fictional training material. Review every cited cell and message before use.", MINT)
    doc.save(template)
    print("Saved Lab 11 automation starters")


def main():
    for a in ACTS:
        folder = lab_folder(a)
        save_company_brief(a, folder)
        save_work_sample(a, folder)
        save_prompt_template(a, folder)
        save_workbook(a, folder)
        save_decision_log(a, folder)
        save_presentation(a, folder)
        if a["num"] == 11: save_lab11_automation(a, folder)


if __name__ == "__main__":
    main()
