#!/usr/bin/env python3
"""Apply the HR theme across course_data.py and all four data_domain files."""

import re
import sys

import hr_theme

sys.path.insert(0, ".")


def block(src, name):
    """Return (start, end) of a top-level `NAME = [...]` assignment."""
    m = re.search(rf"^{name} = \[", src, re.M)
    start = m.start()
    i = src.index("[", start)
    depth = 0
    while i < len(src):
        if src[i] == "[":
            depth += 1
        elif src[i] == "]":
            depth -= 1
            if depth == 0:
                break
        i += 1
    return start, i + 1


def render_topics(topics):
    out = ["TOPICS = ["]
    for t in topics:
        out.append("    dict(")
        out.append(f"        num={t['num']}, code={t['code']!r}, title={t['title']!r},")
        out.append(f"        subtitle={t['subtitle']!r},")
        out.append(f"        weighting={t['weighting']!r}, concepts=[")
        for c in t["concepts"]:
            out.append(f"            {c!r},")
        out.append("        ]),")
    out.append("]")
    return "\n".join(out)


def render_list(name, items):
    out = [f"{name} = ["]
    for x in items:
        out.append(f"    {x!r},")
    out.append("]")
    return "\n".join(out)


def patch_course_data():
    src = open("course_data.py").read()
    for name, text in (
        ("TOPICS", render_topics(hr_theme.TOPICS)),
        ("LEARNING_OUTCOMES", render_list("LEARNING_OUTCOMES", hr_theme.LEARNING_OUTCOMES)),
        ("LO_TITLES", render_list("LO_TITLES", hr_theme.LO_TITLES)),
    ):
        s, e = block(src, name)
        src = src[:s] + text + src[e:]

    # The company context now describes an HR team.
    src = re.sub(
        r"COMPANY_CONTEXT = \(.*?\n\)",
        'COMPANY_CONTEXT = (\n'
        '    "Lumina Living is a fictional Singapore home-and-lifestyle company with retail, "\n'
        '    "online and warehouse teams. Learners join its HR department to prepare the FY2027 "\n'
        '    "hiring plan, staff policies and the weekly people update."\n'
        ')',
        src, flags=re.S)
    open("course_data.py", "w").write(src)
    print("Patched course_data.py")


def patch_labs():
    import fix_meta
    fix_meta.FIELDS = hr_theme.LABS
    fix_meta.patch("data_domain1.py", [1, 2, 3])
    fix_meta.patch("data_domain2.py", [4, 5, 6])
    fix_meta.patch("data_domain3.py", [7, 8])
    fix_meta.patch("data_domain4.py", [9, 10, 11])


if __name__ == "__main__":
    patch_course_data()
    patch_labs()
