"""Shared helpers for generating the legislative package .docx files.

Memo documents: Times New Roman 12 pt, 1-inch margins, US Letter.
Bill document: Century Schoolbook (renders as C059 on Linux), exact 24-pt
line pitch, per-page restarting line numbers, cut-in indentation by level,
modeled on GPO-printed House bills (BILLS-118hr2000ih) and the House
Legislative Counsel Manual on Drafting Style (2022).
"""
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

EMDASH = "—"
WJ = "\u2060"  # word joiner: prevents a line break before an em dash
LQ, RQ = "“", "”"
LSQ, RSQ = "‘", "’"


# ---------------------------------------------------------------- low level
def _set_cell_border(cell, **kwargs):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = tcPr.find(qn("w:tcBorders"))
    if borders is None:
        borders = OxmlElement("w:tcBorders")
        tcPr.append(borders)
    for edge, val in kwargs.items():
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), val.get("val", "single"))
        el.set(qn("w:sz"), str(val.get("sz", 4)))
        el.set(qn("w:color"), val.get("color", "000000"))
        el.set(qn("w:space"), "0")
        borders.append(el)


def _field(run, instr):
    """Turn `run` into a complex field (begin/instr/separate/result/end), each run carrying run's rPr."""
    import copy
    rpr = run._r.find(qn("w:rPr"))
    parent = run._r.getparent()
    anchor = run._r

    def mk(*children):
        r = OxmlElement("w:r")
        if rpr is not None:
            r.append(copy.deepcopy(rpr))
        for c in children:
            r.append(c)
        anchor.addprevious(r)

    def fc(kind):
        e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), kind); return e
    it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = f" {instr} "
    t = OxmlElement("w:t"); t.text = "1"
    mk(fc("begin")); mk(it); mk(fc("separate")); mk(t); mk(fc("end"))
    parent.remove(anchor)


def _font(style_or_run, name, size=None, bold=None, italic=None):
    f = style_or_run.font
    f.name = name
    rpr = style_or_run.element.get_or_add_rPr() if hasattr(style_or_run, "element") else None
    if rpr is not None:
        rfonts = rpr.find(qn("w:rFonts"))
        if rfonts is None:
            rfonts = OxmlElement("w:rFonts"); rpr.append(rfonts)
        for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
            rfonts.set(qn(a), name)
        for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
            if rfonts.get(qn(a)) is not None:
                del rfonts.attrib[qn(a)]
    if size is not None:
        f.size = Pt(size)
    if bold is not None:
        f.bold = bold
    if italic is not None:
        f.italic = italic
    f.color.rgb = RGBColor(0, 0, 0)


def _core(doc, title):
    cp = doc.core_properties
    cp.title = title
    cp.author = "Discussion draft (not an official congressional document)"
    cp.comments = "Prepared for review by congressional staff and legislative counsel."


def keep_with_next(p, on=True):
    p.paragraph_format.keep_with_next = on


# ---------------------------------------------------------------- memo docs
class Memo:
    BODY = "Times New Roman"

    def __init__(self, title, footer_note):
        self.doc = d = Document()
        _core(d, title)
        s = d.sections[0]
        s.page_width, s.page_height = Inches(8.5), Inches(11)
        for m in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
            setattr(s, m, Inches(1))
        s.header_distance = s.footer_distance = Inches(0.5)
        st = d.styles
        n = st["Normal"]
        _font(n, self.BODY, 12)
        n.paragraph_format.space_after = Pt(6)
        n.paragraph_format.space_before = Pt(0)
        n.paragraph_format.line_spacing = 1.0
        n.paragraph_format.widow_control = True
        for lvl, size, before in ((1, 12, 10), (2, 12, 8)):
            h = st[f"Heading {lvl}"]
            _font(h, self.BODY, size, bold=True, italic=(lvl == 2))
            h.paragraph_format.space_before = Pt(before)
            h.paragraph_format.space_after = Pt(4)
            h.paragraph_format.keep_with_next = True
            h.paragraph_format.line_spacing = 1.0
        t = st["Title"]
        _font(t, self.BODY, 14, bold=True)
        t.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        t.paragraph_format.space_after = Pt(2)
        t.paragraph_format.space_before = Pt(0)
        # remove Title bottom border that python-docx default template adds
        ppr = t.element.get_or_add_pPr()
        for b in ppr.findall(qn("w:pBdr")):
            ppr.remove(b)
        sub = st.add_style("Subtitle Line", WD_STYLE_TYPE.PARAGRAPH)
        sub.base_style = n
        sub.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        sub.paragraph_format.space_after = Pt(0)
        lb = st["List Bullet"]
        _font(lb, self.BODY, 12)
        lb.paragraph_format.space_after = Pt(3)
        ln = st["List Number"]
        _font(ln, self.BODY, 12)
        ln.paragraph_format.space_after = Pt(3)
        src = st.add_style("Source Entry", WD_STYLE_TYPE.PARAGRAPH)
        src.base_style = n
        src.paragraph_format.left_indent = Inches(0.3)
        src.paragraph_format.first_line_indent = Inches(-0.3)
        src.paragraph_format.space_after = Pt(4)
        tb = st.add_style("Table Text", WD_STYLE_TYPE.PARAGRAPH)
        tb.base_style = n
        _font(tb, self.BODY, 10)
        tb.paragraph_format.space_after = Pt(0)
        nt = st.add_style("Table Note", WD_STYLE_TYPE.PARAGRAPH)
        nt.base_style = n
        _font(nt, self.BODY, 9.5)
        nt.paragraph_format.space_before = Pt(2)
        nt.paragraph_format.space_after = Pt(8)
        eq = st.add_style("Formula", WD_STYLE_TYPE.PARAGRAPH)
        eq.base_style = n
        eq.paragraph_format.left_indent = Inches(0.5)
        eq.paragraph_format.space_after = Pt(4)
        # header / footer
        hp = s.header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r = hp.add_run("DISCUSSION DRAFT — NOT AN OFFICIAL CONGRESSIONAL DOCUMENT")
        _font(r, self.BODY, 8)
        fp = s.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = fp.add_run(footer_note + "  |  Page ")
        _font(r, self.BODY, 9)
        r = fp.add_run(); _font(r, self.BODY, 9); _field(r, "PAGE")
        r = fp.add_run(" of "); _font(r, self.BODY, 9)
        r = fp.add_run(); _font(r, self.BODY, 9); _field(r, "NUMPAGES")

    # paragraph helpers -------------------------------------------------
    def title(self, text, *sublines):
        self.doc.add_paragraph(text, style="Title")
        for s in sublines:
            self.doc.add_paragraph(s, style="Subtitle Line")
        if sublines:
            self.doc.paragraphs[-1].paragraph_format.space_after = Pt(10)

    def h1(self, text):
        return self.doc.add_paragraph(text, style="Heading 1")

    def h2(self, text):
        return self.doc.add_paragraph(text, style="Heading 2")

    def para(self, *parts, style=None, align=None, space_after=None, keep=False):
        """parts: str or (str, 'b'|'i'|'bi')"""
        p = self.doc.add_paragraph(style=style)
        for part in parts:
            if isinstance(part, str):
                p.add_run(part)
            else:
                txt, fmt = part
                r = p.add_run(txt)
                r.bold = "b" in fmt
                r.italic = "i" in fmt
        if align == "j":
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        elif align == "c":
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if space_after is not None:
            p.paragraph_format.space_after = Pt(space_after)
        if keep:
            keep_with_next(p)
        return p

    def lead(self, label, *rest, style=None, align="j"):
        """Paragraph beginning with a bold run-in label."""
        return self.para((label, "b"), *rest, style=style, align=align)

    def bullet(self, *parts):
        return self.para(*parts, style="List Bullet")

    def numbered(self, *parts):
        return self.para(*parts, style="List Number")

    def formula(self, text):
        """'\u209b' (subscript s) in text is rendered as a true subscript 's' run."""
        p = self.doc.add_paragraph(style="Formula")
        for i, seg in enumerate(text.split("\u209b")):
            if i:
                r = p.add_run("s"); r.font.subscript = True
            if seg:
                p.add_run(seg)
        return p

    def source(self, *parts):
        return self.para(*parts, style="Source Entry")

    def table(self, header, rows, widths, align=None, note=None):
        doc = self.doc
        t = doc.add_table(rows=1 + len(rows), cols=len(header))
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False
        align = align or ["l"] * len(header)
        for i, row in enumerate([header] + rows):
            tr = t.rows[i]
            trPr = tr._tr.get_or_add_trPr()
            cs = OxmlElement("w:cantSplit"); trPr.append(cs)
            if i == 0:
                th = OxmlElement("w:tblHeader"); trPr.append(th)
            for j, val in enumerate(row):
                c = tr.cells[j]
                c.width = Inches(widths[j])
                p = c.paragraphs[0]
                p.style = doc.styles["Table Text"]
                p.alignment = {"l": WD_ALIGN_PARAGRAPH.LEFT, "r": WD_ALIGN_PARAGRAPH.RIGHT,
                               "c": WD_ALIGN_PARAGRAPH.CENTER}[align[j] if i else ("l" if align[j] == "l" else "c")]
                r = p.add_run(str(val))
                if i == 0:
                    r.bold = True
                if i < len(rows):
                    p.paragraph_format.keep_with_next = True
                edges = {}
                if i == 0:
                    edges["top"] = {"sz": 8}
                    edges["bottom"] = {"sz": 4}
                if i == len(rows):
                    edges["bottom"] = {"sz": 8}
                if edges:
                    _set_cell_border(c, **edges)
                tcPr = c._tc.get_or_add_tcPr()
                mar = OxmlElement("w:tcMar")
                for side in ("top", "bottom"):
                    el = OxmlElement(f"w:{side}"); el.set(qn("w:w"), "20"); el.set(qn("w:type"), "dxa"); mar.append(el)
                for side in ("left", "right"):
                    el = OxmlElement(f"w:{side}"); el.set(qn("w:w"), "70"); el.set(qn("w:type"), "dxa"); mar.append(el)
                tcPr.append(mar)
        # table grid widths
        grid = t._tbl.tblGrid
        for j, gc in enumerate(grid.findall(qn("w:gridCol"))):
            gc.set(qn("w:w"), str(int(widths[j] * 1440)))
        if note:
            self.para(note, style="Table Note")
        else:
            sp = self.para("", space_after=4)
            sp.paragraph_format.line_spacing = Pt(6)
        return t

    def save(self, path):
        self.doc.save(path)


# ---------------------------------------------------------------- bill doc
class Bill:
    FONT = "Century Schoolbook"
    EM = 12  # points; one em at 12 pt
    PITCH = 24  # exact line pitch in points

    def __init__(self, title, footer_note):
        self.doc = d = Document()
        _core(d, title)
        s = d.sections[0]
        s.page_width, s.page_height = Inches(8.5), Inches(11)
        s.left_margin = Inches(1.75)
        s.right_margin = Inches(1.6)
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.header_distance = s.footer_distance = Inches(0.5)
        st = d.styles
        n = st["Normal"]
        _font(n, self.FONT, 12)
        pf = n.paragraph_format
        pf.space_after = Pt(0); pf.space_before = Pt(0)
        pf.line_spacing_rule = WD_LINE_SPACING.EXACTLY
        pf.line_spacing = Pt(self.PITCH)
        pf.widow_control = True
        # Text styles by level (0 = section-level text, 1 = (a), 2 = (1), ...)
        self.level_styles = {}
        names = {0: "Bill Text", 1: "Bill Subsection", 2: "Bill Paragraph",
                 3: "Bill Subparagraph", 4: "Bill Clause", 5: "Bill Subclause"}
        for lvl, nm in names.items():
            sty = st.add_style(nm, WD_STYLE_TYPE.PARAGRAPH)
            sty.base_style = n
            sty.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            left = max(0, lvl - 1) * 2 * self.EM
            sty.paragraph_format.left_indent = Pt(left)
            sty.paragraph_format.first_line_indent = Pt(2 * self.EM)
            self.level_styles[lvl] = nm
        sh = st.add_style("Bill Section Heading", WD_STYLE_TYPE.PARAGRAPH)
        sh.base_style = n
        sh.font.bold = True
        sh.paragraph_format.left_indent = Pt(5.5 * self.EM)
        sh.paragraph_format.first_line_indent = Pt(-5.5 * self.EM)
        sh.paragraph_format.keep_with_next = True
        # Front-matter styles (no line numbers)
        fm = st.add_style("Bill Front Matter", WD_STYLE_TYPE.PARAGRAPH)
        fm.base_style = n
        fm.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        fm.paragraph_format.space_after = Pt(6)
        _set_suppress_ln(fm)
        # Header and footer
        hp = s.header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r = hp.add_run(); _font(r, self.FONT, 10); _field(r, "PAGE")
        fp = s.footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = fp.add_run(footer_note); _font(r, self.FONT, 8)
        # line numbering: restart each page, numbers every line
        sectPr = s._sectPr
        ln = OxmlElement("w:lnNumType")
        ln.set(qn("w:countBy"), "1")
        ln.set(qn("w:distance"), str(int(0.35 * 1440)))
        ln.set(qn("w:restart"), "newPage")
        # lnNumType must come before pgNumType/cols etc.; insert after pgMar
        pgMar = sectPr.find(qn("w:pgMar"))
        pgMar.addnext(ln)
        # Line-number style
        try:
            lns = st["Line Number"]
        except KeyError:
            lns = st.add_style("Line Number", WD_STYLE_TYPE.CHARACTER)
        _font(lns, self.FONT, 10)

    def front(self, text, align="l", size=12, bold=False, italic=False, smallcaps=False,
              space_after=6, indent_hang=None):
        p = self.doc.add_paragraph(style="Bill Front Matter")
        p.alignment = {"l": WD_ALIGN_PARAGRAPH.LEFT, "c": WD_ALIGN_PARAGRAPH.CENTER,
                       "r": WD_ALIGN_PARAGRAPH.RIGHT, "j": WD_ALIGN_PARAGRAPH.JUSTIFY}[align]
        if text:
            r = p.add_run(text)
            r.font.size = Pt(size); r.bold = bold; r.italic = italic; r.font.small_caps = smallcaps
        p.paragraph_format.space_after = Pt(space_after)
        if indent_hang:
            p.paragraph_format.left_indent = Pt(indent_hang)
            p.paragraph_format.first_line_indent = Pt(-indent_hang)
        return p

    def rule(self, width_in=2.2):
        p = self.doc.add_paragraph(style="Bill Front Matter")
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        ppr = p._p.get_or_add_pPr()
        bdr = OxmlElement("w:pBdr")
        b = OxmlElement("w:bottom")
        b.set(qn("w:val"), "single"); b.set(qn("w:sz"), "12"); b.set(qn("w:space"), "1"); b.set(qn("w:color"), "000000")
        bdr.append(b); ppr.append(bdr)
        side = (6.0 - 1.75 - 1.6 + 2.5 - width_in) / 2  # text width approx 5.15 in
        tw = 8.5 - 1.75 - 1.6
        side = (tw - width_in) / 2
        p.paragraph_format.left_indent = Inches(side)
        p.paragraph_format.right_indent = Inches(side)
        p.paragraph_format.space_after = Pt(14)
        return p

    def section(self, label, heading):
        """SEC. 2. HEADING."""
        p = self.doc.add_paragraph(style="Bill Section Heading")
        r = p.add_run(f"{label} "); r.bold = True
        r = p.add_run(heading.upper()); r.bold = True
        return p

    def text(self, level, label=None, heading=None, body="", quote_open=False,
             italic_body=False, close=None):
        """Level-structured provision.
        label: '(a)' etc.; heading rendered in caps-and-small-caps; body plain.
        quote_open: prefix an opening quotation mark (inserted matter).
        close: closing punctuation appended after body (e.g. '”.' or '”; and').
        """
        p = self.doc.add_paragraph(style=self.level_styles[level])
        if quote_open:
            p.add_run(LQ)
        if label:
            p.add_run(label + " ")
        if heading:
            r = p.add_run(heading)
            r.font.small_caps = True
            p.add_run("." + WJ + EMDASH)
        if body:
            body = body.replace(EMDASH, WJ + EMDASH)
            r = p.add_run(body)
            r.italic = italic_body
        if close:
            p.add_run(close)
        return p

    def save(self, path):
        self.doc.save(path)


def _set_suppress_ln(style):
    ppr = style.element.get_or_add_pPr()
    el = OxmlElement("w:suppressLineNumbers")
    ppr.append(el)
