import sys
from docbase import Memo

OUT = sys.argv[1]
m = Memo("Section-by-Section Summary", "Section-by-Section Summary — Discussion Draft of November 1, 2026")
m.title("Families First Act of 2027",
        "Section-by-Section Summary of Discussion Draft",
        "November 1, 2026")

m.para("The draft amends section 458 of the Social Security Act (42 U.S.C. 658a), which governs federal incentive "
       "payments to State child support (title IV-D) programs. All references below are to the Social Security Act "
       "unless otherwise noted. The draft has not been introduced and has not been reviewed by legislative counsel.",
       align="j")

m.h1("Section 1. Short title")
m.para("Names the bill the “Families First Act of 2027.”")

m.h1("Section 2. Incentive payments to States adjusted for current support owed")
m.lead("Current law. ", "Each year HHS divides a fixed national incentive pool among States (section 458(b)(1)–(2)). "
       "A State’s share depends on (1) five performance scores (paternity establishment, support order establishment, "
       "current collections rate, arrearage cases paid, and cost-effectiveness) and (2) a “State collections base” "
       "equal to total IV-D collections, with collections in public-assistance cases counted twice (section 458(b)(5)(C)). "
       "Because each performance score is multiplied by collections, a State with larger collections receives a larger "
       "share, all else equal.", align="j")
m.lead("Subsection (a) — Order-adjusted base. ",
       "Replaces the State collections base with a “State order-adjusted base”: a fixed benchmark amount multiplied "
       "by the State’s number of case-months with current support owed, minus the total current support owed in the "
       "State during the year. The base cannot fall below zero. Each additional dollar of current support owed lowers the "
       "base by one dollar, so the State’s share of the pool falls as ordered support rises, all else equal. Cases with no "
       "current support obligation add nothing to the base. The benchmark is a bracketed placeholder ([$1,000] per "
       "case-month in fiscal year [2030]) to be set by the sponsor, then indexed to the CPI using the measure already used "
       "for the incentive pool. The data must come from existing State reporting under section 454(15)(B) and are "
       "subject to the existing federal audit rule: if the data are not complete and reliable, the State’s incentive is zero.",
       align="j")
m.lead("Subsection (b) — Cost-effectiveness measure. ",
       "Strikes the cost-effectiveness measure (total collections divided by total expenditures), the only performance "
       "measure that rises directly with the dollar amount collected. The paternity, support order, current collections "
       "rate, and arrearage measures are retained unchanged, as are the related penalty provisions in section 409(a)(8) "
       "and 45 CFR 305.61, which do not use the cost-effectiveness measure.", align="j")
m.lead("Subsection (c) — Publication. ",
       "Adds section 458(g), requiring HHS to publish each State’s case-months, current support owed, order-adjusted base, "
       "performance percentages, and incentive payment each year.", align="j")
m.lead("Subsection (d) — Conforming amendment. ",
       "Section 455(a)(4)(C)(iii) reduces a disbursement-unit penalty by 20 percent for each incentive measure on which a "
       "State earns full credit. With four measures instead of five, the draft changes 20 to 25 percent so the maximum "
       "reduction remains 100 percent.", align="j")
m.lead("Subsection (e) — Rule of construction. ",
       "Provides that the section does not change State guideline requirements under section 467, does not reduce or "
       "modify any support obligation, and does not affect custody or parenting-time determinations.", align="j")
m.lead("Subsection (f) — Effective date. ",
       "Applies the amendments to incentive payments for fiscal year [2030] and later years, allowing time for HHS "
       "regulations (45 CFR 305.2 and 305.31) and State reporting changes.", align="j")

m.h1("Section 3. Evaluation")
m.para("Requires a Government Accountability Office report to the Committee on Ways and Means and the Committee on "
       "Finance by [September 30, 2033] on changes in amounts ordered, collections distributed to families, State case "
       "and reporting practices, and the distribution of incentive payments.", align="j")

m.h1("Provisions of current law not changed")
for t in ("The size and CPI indexing of the national incentive pool (section 458(b)(2)).",
          "Federal reimbursement of 66 percent of State administrative costs (section 455(a)), which is not tied to "
          "the amount of support ordered or collected.",
          "The reinvestment requirement for incentive payments (section 458(f)) and the bar on using them as State "
          "match (section 455(a)(1)).",
          "State guidelines for support amounts (section 467), the four retained performance measures, and the "
          "performance penalty system."):
    m.bullet(t)

m.save(OUT)
print("saved", OUT)
