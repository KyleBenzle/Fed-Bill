import sys
from docbase import Memo

OUT = sys.argv[1]
m = Memo("Fiscal and Policy Analysis", "Fiscal and Policy Analysis — Discussion Draft of November 1, 2026")
m.title("Families First Act of 2027",
        "Fiscal and Policy Analysis of Discussion Draft",
        "November 1, 2026")

m.para(("Status of figures. ", "b"),
       "Confirmed facts are drawn from statute and from data of the HHS Office of Child Support Enforcement (OCSE; some recent documents use the name OCSS); FY2022–FY2025 "
       "program data are preliminary. Simulations are illustrative: they use FY2023 data and a proxy for case-months, and "
       "they are not a cost estimate. The Congressional Budget Office has not reviewed or estimated this proposal.",
       align="j")

# 1
m.h1("1. Existing incentive funding")
m.para("Section 458 of the Social Security Act (42 U.S.C. 658a) sets a national incentive pool and divides it among States. "
       "The pool was set in statute through FY2008 and has been indexed to the CPI since. It was $678.8 million in FY2023 "
       "(the amount actually paid), $735.5 million in FY2025, and $755.4 million in FY2026 (Dear Colleague Letter ACF-OCSS-DCL-"
       "25-12). States must reinvest incentives in the program (section 458(f)) and may not use them as the State share for "
       "federal matching funds (section 455(a)(1), as amended in 2006). Incentives are separate from, and much smaller than, "
       "federal reimbursement of 66 percent of State administrative costs, which was $4.22 billion in FY2025 (preliminary).",
       align="j")
m.para("Each State’s share equals its “incentive base amount” divided by the sum for all States. The base amount "
       "is the State collections base (total IV-D collections, with collections in current and former public-assistance "
       "cases counted twice) multiplied by the sum of five performance percentages: paternity establishment, cases with "
       "orders, current collections rate, arrearage cases paying, and cost-effectiveness (the last two capped at 75 percent "
       "of the base). Because the pool is fixed, an additional dollar collected raises a State’s payment by only a few "
       "cents. Our reproduction of the FY2023 formula estimates the marginal value to Ohio at about 2.0 cents per "
       "additional dollar of collections base.", align="j")
m.para("The current formula rewards collections. Collections generally rise with order amounts, but higher orders can also "
       "lower a State’s current-collections rate. The available evidence shows that the financial link exists. It does not "
       "show that the link changes how courts decide order amounts, custody, or parenting time, and this analysis does not "
       "assume that it does.", align="j")

# 2
m.h1("2. Proposed formula")
m.para("The bill replaces the collections base with an order-adjusted base and drops the cost-effectiveness measure:",
       align="j", keep=True)
m.formula("Order-adjusted baseₛ = max(0, B × CMₛ − Dₛ)")
m.formula("IBAₛ = order-adjusted baseₛ × Mₛ")
m.formula("Mₛ = PEP% + Orders% + Current% + 0.75 × Arrears%")
m.formula("Paymentₛ = Pool × IBAₛ ÷ Σ;   Σ = sum of IBA for all States")
m.para("Here IBA is the incentive base amount, M is the performance multiplier (applicable percentages as fractions; at most 3.75), B is the benchmark (bracketed at $1,000 per case-month), CM is the number of case-months with current support "
       "owed, and D is total current support owed for the year (OCSE-157 line 24). Each case-month contributes B minus "
       "the amount owed for that month: $1,000 for a $0 order, $750 for $250, $500 for $500, zero for $1,000, and "
       "−$500 for $1,500. These are weights, not dollars. Because the pool is fixed, a one-dollar reduction in "
       "weight moves the State’s payment by the State’s marginal share of the pool, not by one dollar:", align="j")
m.formula("∂Paymentₛ/∂Dₛ = −Pool × Mₛ × (Σ − IBAₛ) ÷ Σ²")
m.para("Cases without current support owed (no order, or arrears only) add nothing to the base. A State therefore gains "
       "nothing by keeping such cases open, and the retained order-establishment measure continues to reward "
       "establishing orders.", align="j")

m.h2("Worked example (hypothetical)")
m.para("Three States with identical performance (multiplier 3.75), a $100 million pool, and B = $1,000:", keep=True)
m.table(["State", "Cases", "Avg. monthly order", "Order-adjusted base", "Share", "Payment"],
        [["A", "100,000", "$300", "$840 million", "22.95%", "$22.95 million"],
         ["B", "100,000", "$450", "$660 million", "18.03%", "$18.03 million"],
         ["C", "300,000", "$400", "$2,160 million", "59.02%", "$59.02 million"]],
        [0.6, 0.85, 1.25, 1.45, 0.75, 1.3], ["l", "r", "r", "r", "r", "r"],
        note="If State B’s average order rises by $50 (+$60 million owed per year), its payment falls to $16.67 million "
             "(−$1.36 million, or about 2.3 cents per added dollar owed); A and C gain. If every State’s orders rise 10 "
             "percent, total payments are unchanged and the lowest-order State gains share. If B’s average exceeded $1,000, "
             "its base and payment would be zero.")

# 3
m.h1("3. National fiscal implications")
m.para(("Direct federal cost. ", "b"),
       "The bill does not change the pool or its CPI indexing, so direct federal spending on incentives is unchanged. "
       "Changing reporting systems would increase administrative costs, which the federal government reimburses at 66 percent; "
       "this cost has not been estimated.", align="j")
m.para(("Distribution among States. ", "b"),
       "Using FY2023 preliminary data and B = $1,000, the proposal is redistributive. Of 54 jurisdictions, 27 gain and 27 "
       "lose relative to the current formula simulated the same way. States with higher average orders lose share: New "
       "Jersey (average $614 per case-month in the proxy) loses 63 percent, and North Dakota, Maine, Massachusetts, and "
       "Alaska each lose about 40 percent. Delaware, the District of Columbia, Mississippi, Kentucky, and the Virgin Islands "
       "gain the most. Order levels largely reflect incomes and living costs, so these shifts partly penalize "
       "higher-income States regardless of program practice.", align="j")
m.para(("Indirect effects. ", "b"),
       "If orders fall, collections retained to repay public assistance would fall as well. The federal share of such "
       "collections was $543 million in FY2023 and $406 million in FY2025. Program interactions (for example, child support "
       "counted as income in SNAP and Medicaid) would also change. These effects depend on behavioral responses that "
       "cannot be estimated from available data.", align="j")
m.para(("Dollar-for-dollar alternative. ", "b"),
       "The original concept could also be read as paying each State B minus the amount ordered, in actual dollars, per case. "
       "At B = $1,000, that would cost about $60.5 billion a year, roughly 89 times the FY2023 pool. A benchmark that keeps "
       "the cost at the FY2023 pool level would be about $280 a month, and 40 of 54 jurisdictions would then receive nothing. "
       "The draft therefore keeps the fixed pool with relative weights. A dollar-for-dollar version remains available as a "
       "policy alternative, but only with a new appropriation and an explicit cap.", align="j")

# 4
m.h1("4. Ohio example (FY2023, preliminary data)")
m.table(["Item", "Value", "Source / method"],
        [["Actual incentive payment", "$37,367,485", "OCSE Table P-38"],
         ["Current formula, simulated", "$36.79 million", "Reproduction; 1.5% below actual"],
         ["Proposed formula (B = $1,000)", "$46.48 million", "+26% vs. simulated current law"],
         ["Current support owed (line 24)", "$1,534,485,919", "OCSE Table P-83"],
         ["Cases with current orders (proxy)", "465,519", "Line 2 − line 2e (Table P-42)"],
         ["Average owed per case-month", "$275 (national $339)", "Line 24 ÷ (12 × proxy cases)"],
         ["Performance multiplier", "4.12 now; 3.37 proposed", "Applicable % from Table P-39 measures"],
         ["Effect of +$1 owed", "−1.07 cents", "Marginal formula above"],
         ["Owed ±10% (±$153 million)", "\u2212/+$1.64 million", "Re-run of simulation"],
         ["Payment at B = $750 / $1,500", "$48.98 / $44.71 million", "Benchmark sensitivity"]],
        [2.3, 1.75, 2.45], ["l", "r", "l"],
        note="Ohio gains under the proposal mainly because its average amount owed per case is below the national average. "
             "Adding one case-month with a $0 order would raise Ohio’s payment by about $10.69; adding one with a $500 "
             "order, by about $5.34.")

# 5
m.h1("5. Administrative implementation")
m.para("States do not currently report case-months with current support owed. OCSE-157 line 2 counts cases with orders "
       "at year end, including arrears-only cases (line 2e) and orders for no cash support (line 2c, which is collected but "
       "not published). HHS would need to revise form OCSE-157 (OMB 0970-0177, which expires March 31, 2028) and amend 45 "
       "CFR 305.2 and 305.31. States would also need to extract a monthly count from their automated systems. Section "
       "454(15)(B) already requires States to transmit the data needed for section 458. Existing data-reliability audits "
       "would extend to the new data elements, and the bill makes unreliable data disqualifying.", align="j")

# 6
m.h1("6. Incentive effects and unintended consequences")
m.para("The marginal incentive is small: about 1 cent per dollar of support owed, similar in size to the existing "
       "incentive tied to collections. That limits both the intended effect and the risk of manipulation. Possible "
       "responses include:", align="j", keep=True)
for t in ("State guideline reviews under section 467 (at least every four years) could produce lower schedules, or "
          "agencies could favor more deviations or $0 orders. The rebuttable presumption and written-finding requirement "
          "in section 467(b)(2) still apply.",
          "Cases with low orders gain weight while cases with orders above B lose weight, which could influence "
          "case-closure and enrollment decisions. Federal case-closure criteria at 45 CFR 303.11 limit discretion.",
          "Reporting manipulation (undercounting the amount owed or overcounting case-months) is addressed by the "
          "existing audit and the bill’s zero-payment rule for unreliable data.",
          "A case covering several children usually carries a larger order, so States with larger families score lower. "
          "Interstate cases may be counted by both States, which is consistent with the existing collections rule in "
          "section 458(c) but should be confirmed in regulations.",
          "Collections in public-assistance cases are no longer double-weighted, which reduces the emphasis on "
          "recovering assistance costs. Dropping the cost-effectiveness measure removes the only measure tied to "
          "program spending."):
    m.bullet(t)

# 7
m.h1("7. Principal objections and possible responses")
m.lead("Lower orders harm children. ",
       "The bill does not alter guidelines or any order. It keeps the order-establishment and current-collections measures, "
       "and it adds GAO evaluation. Some downward pressure on orders is the intended policy, and its effect on children is "
       "not known.")
m.lead("No evidence that incentives affect custody. ",
       "Correct. The case for the bill rests on removing a federal financial stake in order amounts, not on a proven "
       "causal effect on custody.")
m.lead("Penalizes higher-income States. ",
       "One option is to scale B by State median income; this adds complexity and data needs. Another is a phase-in or "
       "transition floor.")
m.lead("Judicial independence and federalism. ",
       "The formula affects only federal payments to State agencies. Courts continue to set orders under State law.")

# 8
m.h1("8. Information needed for credible scoring")
for t in ("Actual case-months and monthly amounts owed by State (case-level distribution, including $0 orders).",
          "Final (audited) FY2023–FY2025 incentive and performance data; final reports after FY2020 are not yet published.",
          "Estimates of how State guideline reviews, deviation rates, and case management respond to small financial incentives.",
          "Effects on retained public-assistance collections and on means-tested programs that count child support as income.",
          "State and federal costs of systems and reporting changes."):
    m.bullet(t)

m.save(OUT)
print("saved", OUT)
