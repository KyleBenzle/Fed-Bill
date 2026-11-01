import sys
from docbase import Memo

OUT = sys.argv[1]
m = Memo("Sources and Research Notes", "Sources and Research Notes — Discussion Draft of November 1, 2026")
m.title("Families First Act of 2027",
        "Sources and Research Notes",
        "Research cutoff: November 1, 2026")

m.para("All sources were retrieved between October 31 and November 1, 2026, and are saved in the project’s working/sources "
       "directory. “Preliminary” means HHS data that have not yet passed the annual data-reliability audits.", align="j")

m.h1("A. Statutes and regulations")
S = m.source
S("1. Social Security Act § 458, 42 U.S.C. 658a (incentive payments to States). Office of the Law Revision Counsel (OLRC), "
  "U.S. Code current through Pub. L. 119-136 (Oct. 22, 2026). https://uscode.house.gov/us/usc/119-136/t42/s658a/ — "
  "The section amended by the bill. The OLRC source credit confirms that it is section 458 of the Act (formerly 458A, "
  "renumbered by Pub. L. 105-200, § 201(f)(2)(A)). It has not been amended since 1998.")
S("2. Social Security Act § 455, 42 U.S.C. 655. Same OLRC edition (…/t42/s655/). — 66 percent federal match "
  "(subsection (a)(2)); bar on matching expenditures made from incentive funds (subsection (a)(1)); cross-reference to "
  "section 458(b)(4), (5)(B), and (6) in subsection (a)(4)(C)(iii).")
S("3. Social Security Act §§ 452(a)(4), 452(g), 454(15)(B), 454(22), 409(a)(8), and 467; 42 U.S.C. 652, 654, 609, "
  "and 667 (same OLRC edition). — Data audits and transmission; pass-through of incentives to localities; performance "
  "penalties; State guidelines and the rebuttable presumption (section 467(b)(2)).")
S("4. Child Support Performance and Incentive Act of 1998, Pub. L. 105-200, § 201, 112 Stat. 648 (July 16, 1998). "
  "— Created the current formula, effective October 1, 1999, and fully phased in for FY2002.")
S("5. Deficit Reduction Act of 2005, Pub. L. 109-171, § 7309, effective October 1, 2007; American Recovery and "
  "Reinvestment Act of 2009, Pub. L. 111-5, § 2104 (FY2009–FY2010 exception). Statutory notes to 42 U.S.C. 655. "
  "— Use of incentives as State match.")
S("6. 45 CFR part 305 (§§ 305.2, 305.31, 305.35, 305.61) and 45 CFR 303.11, eCFR current as of Oct. 29, 2026. "
  "https://www.ecfr.gov/current/title-45/part-305 — Regulatory formula, reinvestment, penalty measures (which do not "
  "include cost-effectiveness), and case-closure criteria.")
S("7. HHS, Final Rule, “Child Support Enforcement Program; Incentive Payments, Audit Penalties,” 65 Fed. Reg. 82178 "
  "(Dec. 27, 2000). https://www.govinfo.gov/content/pkg/FR-2000-12-27/pdf/00-32702.pdf")

m.h1("B. Program and fiscal data")
S("8. HHS/ACF Office of Child Support Enforcement, FY 2025 Preliminary Data Report and Data Tables (notice Aug. 3, 2026; "
  "updated Oct. 2, 2026). https://acf.gov/sites/default/files/documents/ocse/FY_2025_Preliminary_Report.pdf and "
  "…/FY_2025_Preliminary_data_tables.xlsx — Table F (pool, FY2001–FY2025); Table P-38 (actual incentives: "
  "FY2023 national $678,795,663, Ohio $37,367,485); P-44 (federal share of administrative costs); P-14 (federal share "
  "of assistance collections); P-83 (current support due).")
S("9. Same office, FY 2023 and FY 2022 Preliminary Data Tables, https://acf.gov/sites/default/files/documents/ocse/ "
  "(fy_2023_preliminary_data_tables.xlsx; fy_2022_preliminary_data_tables.xlsx). — FY2023 simulation inputs: P-4, "
  "P-6, P-7 (collections by assistance status); P-39 (performance levels, FY2023 and FY2022); P-42 (lines 2 and 2e); "
  "P-83 (line 24). The FY2022–FY2023 values match across later editions.")
S("10. Dear Colleague Letter ACF-OCSS-DCL-25-12, “FY 2026 Incentive Payment Pool Amount” ($755,389,396), Dec. 1, "
  "2025. https://acf.gov/ocse/policy-guidance/fy-2026-incentive-payment-pool-amount. Also DCL-24-14 (FY2025, "
  "$735,530,084; Dec. 10, 2024) and DCL-23-14 (FY2024, $713,414,242; Nov. 30, 2023).")
S("11. ACF, Fiscal Year 2027 Justification of Estimates for Appropriations Committees (Apr. 2026). "
  "https://acf.gov/sites/default/files/documents/olab/FY-2027-Final-for-Web-4-3-26.pdf — Budget line for incentive "
  "payments; pool estimated at $775 million for FY2027.")
S("12. Form OCSS-157 and instructions, OMB No. 0970-0177 (expires Mar. 31, 2028). "
  "https://acf.gov/sites/default/files/documents/ocse/omb_0970_0177_instructions.pdf — Definitions of lines 1, 2, 2c, "
  "2e, 24, and 25. No line counts cases or months with current support owed.")
S("13. U.S. Census Bureau, Current Population Survey Child Support Supplement, 2022 detailed tables (Table 2a: median "
  "annual amount due $4,816; mean $6,390; Table 2b: 14.3 percent due $10,000 or more). "
  "https://www.census.gov/data/tables/2022/demo/families/2022-cps-childsupport.html — Survey data covering all "
  "custodial parents, not only IV-D cases; used only to put the benchmark in context.")
S("14. Census Bureau, P60-269, Custodial Mothers and Fathers and Their Child Support: 2017 (May 2020). "
  "https://www.census.gov/content/dam/Census/library/publications/2020/demo/p60-269.pdf")

m.h1("C. Congressional Research Service and drafting references")
S("15. CRS, Child Support Enforcement: Program Basics, RS22380 (updated Jan. 12, 2026). "
  "https://crsreports.congress.gov/product/pdf/RS/RS22380")
S("16. CRS, Child Support Enforcement Program Incentive Payments: Background and Policy Issues, RL34203 (May 2, 2013). "
  "https://crsreports.congress.gov/product/pdf/RL/RL34203 — History of the pre-1998 incentives (6 to 10 percent of "
  "collections under Pub. L. 98-378). The copy reviewed was obtained from a public mirror because the CRS site returned "
  "an access error; it should be checked against the CRS original.")
S("17. House Office of the Legislative Counsel: Quick Guide to Legislative Drafting (rev. June 10, 2026); Introduction to "
  "Legislative Drafting (Jan. 13, 2025); Manual on Drafting Style (2022). https://legcounsel.house.gov/ — Used for "
  "the amendment format, “may not” usage, the omission of a purposes section, and the effective-date form.")
S("18. Government Publishing Office, H.R. 2000 (118th Cong.), introduced print, BILLS-118hr2000ih. "
  "https://www.govinfo.gov/content/pkg/BILLS-118hr2000ih/pdf/BILLS-118hr2000ih.pdf — Typography reference for the "
  "bill: Century-style serif type, line numbers, US Letter.")

m.h1("D. Method notes")
m.bullet("Simulation: the current formula under section 458(b), including the improvement rules, was applied to all 54 "
         "jurisdictions using FY2023 preliminary data. Compared with actual FY2023 payments, the median absolute error is "
         "8.8 percent and the maximum is 28.5 percent. Ohio’s error is 1.5 percent. HHS uses audited data and adjustments "
         "that the published tables do not show.")
m.bullet("Case-months proxy: 12 × (line 2 − line 2e). This overstates the count for cases open part of the year and "
         "includes orders for no cash support (line 2c, unpublished).")
m.bullet("Scripts and outputs: working/scripts (simulate.py, analyze.py, model.py), working/sim_fy2023.json, and "
         "working/analysis_results.txt.")

m.h1("E. Uncertain or unverified matters")
for t in ("Whether the federal incentive affects court order amounts, custody, or parenting time. No causal evidence was "
          "identified, and the package makes no such claim.",
          "Final (audited) data after FY2020, and actual incentive payments for FY2024 and FY2025, are not published.",
          "The budget-justification incentive line (e.g., $740.751 million for FY2026) differs from the DCL pool "
          "($755.389 million). The reason is not explained in the documents reviewed.",
          "Line 24 counts voluntary payments as amounts due when no order exists. Regulations must align this with the "
          "bill’s “owed” standard.",
          "How interstate cases appear in both States’ counts under the new base.",
          "Whether section 455(a)(4)(C)(iii) (disbursement-unit penalty) still operates in practice. The conforming change "
          "preserves its effect either way.",
          "GAO report HEHS/GGD-97-14 on the pre-1998 incentive system was identified but not reviewed. No CBO estimate "
          "exists for this proposal."):
    m.bullet(t)

m.h1("F. Corrections to the preliminary drafts")
for t in ("The preliminary bill amended “section 458A”; the section has been numbered 458 since 1998.",
          "Striking paragraphs (3) through (6) would have removed the data-reliability rule (paragraph (5)(B)) and broken "
          "the cross-reference in section 455(a)(4)(C)(iii). The revised draft amends only the collections base and the "
          "cost-effectiveness measure.",
          "A benchmark set by HHS at the 90th percentile of obligations would require case-level data that HHS does not "
          "collect. The revised draft uses a statutory, CPI-indexed amount.",
          "The purposes section and freestanding reporting section were removed (Legislative Counsel guidance), and "
          "publication was moved into section 458.",
          "The literal dollar-for-dollar reading is retained only as an analyzed alternative (about $60.5 billion a year "
          "at a $1,000 benchmark)."):
    m.bullet(t)

m.save(OUT)
print("saved", OUT)
