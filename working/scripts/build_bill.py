import sys
from docbase import Bill, LQ, RQ, EMDASH

OUT = sys.argv[1]
BENCH = "[$1,000]"  # bracketed: policy placeholder for legislative counsel / sponsor decision
FY0 = "[2030]"

b = Bill("Families First Act of 2027 (Discussion Draft)",
         "DISCUSSION DRAFT — Not introduced. Prepared for review by legislative counsel. Draft of November 1, 2026.")

b.front("[DISCUSSION DRAFT]", align="c", size=12, bold=True, space_after=18)
p = b.front("", space_after=0)
r = p.add_run("120TH CONGRESS"); r.font.size = 10
p.add_run("\t\t\t")
r = p.add_run("H. R. ______"); r.bold = True; r.font.size = 18
b.front("1ST SESSION", size=10, space_after=14)
b.front("To amend part D of title IV of the Social Security Act to update and improve the fair distribution of Federal child support incentive payments to States based on updated and improved metrics, and for other purposes.",
        size=10.5, align="j", indent_hang=14, space_after=14)
b.rule()
b.front("IN THE HOUSE OF REPRESENTATIVES", align="c", size=11, space_after=4)
b.front("______________", align="c", size=10, smallcaps=True, space_after=6)
b.front("M__. __________ introduced the following bill; which was referred to the Committee on "
        "__________", size=10, align="j", indent_hang=14, space_after=14)
b.rule()
b.front("A BILL", align="c", size=20, bold=True, space_after=10)
b.front("To amend part D of title IV of the Social Security Act to update and improve the fair distribution of Federal child support incentive payments to States based on updated and improved metrics, and for other purposes.",
        size=12, align="j", indent_hang=14, space_after=12)

b.text(0, body="Be it enacted by the Senate and House of Representatives of the United States of America in Congress assembled,",
       italic_body=True)

# SECTION 1
b.section("SECTION 1.", "Short title.")
b.text(0, body="This Act may be cited as the " + LQ + "Families First Act of 2027" + RQ + ".")

# SECTION 2
b.section("SEC. 2.", "Incentive payments to States adjusted for current support owed.")
b.text(1, "(a)", "Order-Adjusted Base", "Section 458(b)(5) of the Social Security Act (42 U.S.C. 658a(b)(5)) is amended" + EMDASH)
b.text(2, "(1)", None, "in subparagraph (A)" + EMDASH)
b.text(3, "(A)", None, "by striking " + LQ + "State collections base" + RQ + " each place it appears and inserting "
       + LQ + "State order-adjusted base" + RQ + "; and")
b.text(3, "(B)", None, "in clause (ii), by striking " + LQ + "measures described in subparagraphs (D) and (E)" + RQ
       + " and inserting " + LQ + "measure described in subparagraph (D)" + RQ + "; and")
b.text(2, "(2)", None, "by striking subparagraph (C) and inserting the following:")
b.text(3, "(C)", "State Order-Adjusted Base", "", quote_open=True)
b.text(4, "(i)", "In General", "For purposes of subparagraph (A), the State order-adjusted base for a fiscal year is the amount (if any) by which" + EMDASH)
b.text(5, "(I)", None, "the benchmark amount for the fiscal year, multiplied by the number of case-months of the State for the fiscal year; exceeds")
b.text(5, "(II)", None, "the total amount of current support owed during the fiscal year in all cases under the State plan approved under this part.")
b.text(4, "(ii)", "Case-Month", "In this subparagraph, the term " + "‘" + "case-month" + "’"
       + " means, with respect to a case under the State plan approved under this part, a month for which current support is owed in the case.")
b.text(4, "(iii)", "Benchmark Amount", "The benchmark amount is" + EMDASH)
b.text(5, "(I)", None, f"for fiscal year {FY0}, {BENCH}; and")
b.text(5, "(II)", None, "for any succeeding fiscal year, the benchmark amount for the preceding fiscal year, increased by the "
       "percentage (if any) by which the CPI (as defined in paragraph (2)(B)) for such preceding fiscal year exceeds "
       "the CPI for the second preceding fiscal year, rounded to the nearest dollar.")
b.text(4, "(iv)", "Data", "The number of case-months and the total amount of current support owed shall be determined on the basis "
       "of data submitted by the State pursuant to section 454(15)(B). Subparagraph (B) shall apply with respect to such data "
       "as if such data were used to determine each performance level described in paragraph (4).", close=RQ + ".")
b.text(1, "(b)", "Elimination of Cost-Effectiveness Measure", "Section 458(b) of such Act (42 U.S.C. 658a(b)) is amended" + EMDASH)
b.text(2, "(1)", None, "in paragraph (4), by striking subparagraph (E); and")
b.text(2, "(2)", None, "in paragraph (6), by striking subparagraph (E).")
b.text(1, "(c)", "Publication", "Section 458 of such Act (42 U.S.C. 658a) is amended by adding at the end the following:")
b.text(1, "(g)", "Publication", "For each fiscal year, the Secretary shall publish, for each State, the number of case-months, "
       "the total amount of current support owed, the State order-adjusted base (as such terms are used in subsection (b)(5)(C)), "
       "the applicable percentage for each performance measure, and the amount of the incentive payment under this section.",
       quote_open=True, close=RQ + ".")
b.text(1, "(d)", "Conforming Amendment", "Section 455(a)(4)(C)(iii) of such Act (42 U.S.C. 655(a)(4)(C)(iii)) is amended by "
       "striking " + LQ + "20 percent" + RQ + " and inserting " + LQ + "25 percent" + RQ + ".")
b.text(1, "(e)", "Rule of Construction", "Nothing in this section, or the amendments made by this section, shall be construed" + EMDASH)
b.text(2, "(1)", None, "to modify the requirements of section 467 of the Social Security Act (42 U.S.C. 667) relating to "
       "guidelines for child support award amounts;")
b.text(2, "(2)", None, "to reduce, extinguish, or otherwise modify any support obligation established before, on, or after the "
       "date of the enactment of this Act; or")
b.text(2, "(3)", None, "to affect any determination of child custody or parenting time.")
b.text(1, "(f)", "Effective Date", f"The amendments made by this section shall apply with respect to incentive payments under "
       f"section 458 of the Social Security Act (42 U.S.C. 658a) for fiscal year {FY0} and each succeeding fiscal year.")

# SECTION 3
b.section("SEC. 3.", "Evaluation.")
b.text(0, body="Not later than [September 30, 2033], the Comptroller General of the United States shall submit to the "
       "Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate a report "
       "that evaluates the effects of the amendments made by section 2, including effects on" + EMDASH)
b.text(2, "(1)", None, "the amounts of current support ordered and owed in cases under State plans approved under part D of title IV "
       "of the Social Security Act;")
b.text(2, "(2)", None, "the amount of support collected and distributed to families;")
b.text(2, "(3)", None, "State practices relating to the establishment of support orders, the opening and closing of cases, "
       "and the reporting of data; and")
b.text(2, "(4)", None, "the distribution of incentive payments among States.")

b.save(OUT)
print("saved", OUT)
