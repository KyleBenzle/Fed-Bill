import sys
from docx.shared import Pt
from docbase import Memo

OUT = sys.argv[1]
m = Memo("Sponsor Brief", "Sponsor Brief — Discussion Draft of November 1, 2026")
# Brief is denser: 11-pt body
from docbase import _font
_font(m.doc.styles["Normal"], "Times New Roman", 11)
m.doc.styles["Normal"].paragraph_format.space_after = Pt(5)

m.title("Families First Act of 2027",
        "Sponsor Brief — Discussion Draft for Congressional Staff",
        "November 1, 2026")

m.lead("Issue. ",
       "Federal law pays States an annual child support incentive that grows with the amount of support they collect, "
       "and collections generally rise with the amounts ordered. This gives State programs a financial interest in larger "
       "obligations. The draft removes that interest and reverses it. The draft does not assume that the incentive "
       "changes how courts set support or decide custody; that effect has not been established.")
m.lead("Current law. ",
       "Section 458 of the Social Security Act (42 U.S.C. 658a), enacted in the Child Support Performance and Incentive "
       "Act of 1998, divides a fixed, CPI-indexed pool among States: $678.8 million in FY2023 and $755.4 million in FY2026. "
       "Each State’s share equals its total collections (public-assistance collections count double) multiplied by five "
       "performance scores. Separately, the federal government reimburses 66 percent of State program costs ($4.22 billion "
       "in FY2025, preliminary); that reimbursement is not tied to amounts ordered or collected and is unchanged.")
m.lead("Proposed change. ",
       "The draft replaces total collections with an “order-adjusted base”: a benchmark amount (bracketed at $1,000) for "
       "each month in which a case has current support owed, minus the total current support owed. Each added dollar of "
       "support owed lowers the base by one dollar. Because the pool is fixed, the effect on actual payments is small, "
       "about one cent per dollar owed. The draft also drops the cost-effectiveness score, which rises with dollars "
       "collected. It keeps the scores for paternity establishment, order establishment, current collections rate, and "
       "arrears. Safeguards: unreliable data disqualify a State from incentives; cases with no current order earn nothing; "
       "HHS must publish each State’s data; GAO must evaluate the effects.")
m.lead("Why federal legislation. ",
       "The formula is set in statute, and HHS cannot change it administratively. The draft amends two sections of the Act "
       "and does not touch State custody law, State guidelines (section 467), or any existing order.")
m.lead("Fiscal considerations. ",
       "The pool is unchanged, so direct federal incentive spending does not change. The proposal redistributes the pool: "
       "in an illustrative FY2023 simulation, 27 jurisdictions gain and 27 lose, and States with higher average orders "
       "lose share (for example, New Jersey −63 percent). Ohio would receive about $46.5 million, compared with $36.8 "
       "million under the current formula simulated the same way ($37.4 million actually paid). Indirect effects include lower retained public-assistance collections if orders fall, "
       "plus reporting and systems costs. CBO has not estimated the proposal. Paying the benchmark minus the order in "
       "actual dollars would cost about $60.5 billion a year and is not proposed.")
m.lead("Law affected. ",
       "Social Security Act sections 458(b)(4), (5), and (6) and new 458(g) (42 U.S.C. 658a); section 455(a)(4)(C)(iii) "
       "(conforming); and 45 CFR 305.2 and 305.31 (regulations to be updated). Committees of jurisdiction: Ways and "
       "Means (House) and Finance (Senate).")
m.lead("Requested action. ",
       "Review the discussion draft; request technical drafting assistance from the Office of the Legislative Counsel; "
       "and request technical assistance from HHS and, if pursued, an informal CBO consultation. Policy choices left "
       "open: the benchmark amount, the effective year, and any adjustment for State income levels.")
from docbase import add_hyperlink
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
cp = m.para(("Contact. ", "b"), "Kyle Benzle  \u00b7  ")
add_hyperlink(cp, "kbe@gmx.us", "mailto:kbe@gmx.us")
cp.add_run("  \u00b7  614-505-9532  \u00b7  ")
add_hyperlink(cp, "FamiliesFirstBill.us", "https://www.familiesfirstbill.us")
cp.paragraph_format.space_before = Pt(10)
ppr = cp._p.get_or_add_pPr()
bdr = OxmlElement("w:pBdr"); top = OxmlElement("w:top")
for k, v in (("val", "single"), ("sz", "4"), ("space", "6"), ("color", "000000")):
    top.set(qn("w:" + k), v)
bdr.append(top); ppr.append(bdr)
m.save(OUT)
print("saved", OUT)
