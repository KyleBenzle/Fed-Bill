"""State-by-state simulation, FY2023 (preliminary OCSS data).

1. Reproduces the CURRENT-LAW formula (42 U.S.C. 658a(b)) from published data and compares
   with actual FY2023 incentive payments (Table P-38) to validate the method.
2. Computes the PROPOSED formula (bill sec. 2) with benchmark B per case-month.

Proxy (assumption): case-months = 12 x (Line 2 - Line 2e) [cases with orders at year end,
minus arrears-only cases]. This includes orders with no cash amount (Line 2c, unpublished)
and ignores partial-year cases. Actual case-months are not reported to HHS today.

Run with: /tmp/lv/bin/python -I simulate.py <acf_dir> <out_json>
"""
import json
import sys

import openpyxl

ACF, OUT = sys.argv[1], sys.argv[2]
POOL_FY23 = 678_795_663  # FY2025 Preliminary Report, Table F; equals national total in Table P-38


def table(path, sheet):
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    rows = list(wb[sheet].iter_rows(values_only=True))
    hdr = rows[2]
    out = {}
    for r in rows[3:]:
        if not r[0] or str(r[0]).startswith(("Source", "Line", "1/", "NA", "FY", "The ")):
            continue
        name = str(r[0]).strip().upper()
        out[name] = dict(zip(hdr, r))
    return out


def num(v):
    if v is None or v == "NA":
        return None
    if isinstance(v, str):
        v = v.replace("%", "").replace(",", "").strip()
        if not v or v == "NA":
            return None
    return float(v)


f23 = f"{ACF}/fy_2023_preliminary_data_tables.xlsx"
f22 = f"{ACF}/fy_2022_preliminary_data_tables.xlsx"
f25 = f"{ACF}/FY_2025_Preliminary_data_tables.xlsx"
P4, P6, P7 = table(f23, "P-4"), table(f23, "P-6"), table(f23, "P-7")
P39, P39p = table(f23, "P-39"), table(f22, "P-39")
P42, P83, P38 = table(f23, "P-42"), table(f23, "P-83"), table(f25, "P-38")
k42_2, k42_2e = "Cases Open with Support Orders Established in 2023", None
for k in next(iter(P42.values())).keys():
    if k and "Arrears-Only" in str(k) and "2023" in str(k):
        k42_2e = k
assert k42_2e, "Line 2e 2023 column not found"


def pct_ladder(level, floor):
    """Applicable percentage under 658a(b)(6)(A)-(D)."""
    if level >= 80:
        return 100.0
    if level < floor:
        return 0.0
    # 50-80 for PEP/orders, 40-80 for current/arrears
    b = int(level)
    if b >= 70:
        return 80 + (b - 70) * 2.0
    return 60.0 + (b - 50)  # [50,51)->60 ... [69,70)->79; for current/arrears [40,41)->50


def ce_pct(r):
    for lo, p in ((5.0, 100), (4.5, 90), (4.0, 80), (3.5, 70), (3.0, 60), (2.5, 50), (2.0, 40)):
        if r >= lo:
            return p
    return 0.0


def applicable(level, prior, floor, improve):
    p = pct_ladder(level, floor)
    if p == 0 and prior is not None and level - prior >= improve:
        p = 50.0
    return p


def pep(row):
    vals = [num(row.get("IV-D PEP")), num(row.get("Statewide PEP"))]
    vals = [v for v in vals if v is not None]
    return max(vals) if vals else None


B_LIST = (750.0, 1000.0, 1500.0)
states = {}
for name, r in P39.items():
    if name in ("NATIONAL", "TOTALS") or name not in P83:
        continue
    pr = P39p.get(name, {})
    lv = {"pep": pep(r), "ord": num(r["Percent of Cases with Orders"]),
          "cur": num(r["Percent of Current Collections"]), "arr": num(r["Percent of Arrearage Cases"]),
          "ce": num(r["Cost Effectiveness Ratio"])}
    pv = {"pep": pep(pr) if pr else None, "ord": num(pr.get("Percent of Cases with Orders")) if pr else None,
          "cur": num(pr.get("Percent of Current Collections")) if pr else None,
          "arr": num(pr.get("Percent of Arrearage Cases")) if pr else None}
    if None in lv.values():
        print("skip (missing measure)", name, lv)
        continue
    ap = {"pep": applicable(lv["pep"], pv["pep"], 50, 10), "ord": applicable(lv["ord"], pv["ord"], 50, 5),
          "cur": applicable(lv["cur"], pv["cur"], 40, 5), "arr": applicable(lv["arr"], pv["arr"], 40, 5),
          "ce": ce_pct(lv["ce"])}
    coll = num(P4[name]["2023"]); ca = num(P6[name]["2023"]) or 0; fa = num(P7[name]["2023"]) or 0
    cbase = 2 * (ca + fa) + (coll - ca - fa)
    m_cur = (ap["pep"] + ap["ord"] + ap["cur"]) / 100 + 0.75 * (ap["arr"] + ap["ce"]) / 100
    m_new = (ap["pep"] + ap["ord"] + ap["cur"]) / 100 + 0.75 * ap["arr"] / 100
    cases = num(P42[name][k42_2]) - num(P42[name][k42_2e])
    states[name] = {"levels": lv, "applicable": ap, "collections_base": cbase, "M_current": m_cur, "M_new": m_new,
                    "cases_current": cases, "case_months": 12 * cases, "D": num(P83[name]["2023"]),
                    "actual": num(P38[name]["2023"]) if name in P38 else None}

# current law
S = sum(s["collections_base"] * s["M_current"] for s in states.values())
for s in states.values():
    s["sim_current"] = POOL_FY23 * s["collections_base"] * s["M_current"] / S
# proposed
res = {}
for B in B_LIST:
    iba = {n: max(0.0, B * s["case_months"] - s["D"]) * s["M_new"] for n, s in states.items()}
    T = sum(iba.values())
    for n, s in states.items():
        s[f"new_{int(B)}"] = POOL_FY23 * iba[n] / T
        s[f"marg_{int(B)}"] = -POOL_FY23 * s["M_new"] * (T - iba[n]) / T ** 2  # $ change per $1 owed
    res[B] = T

tot_act = sum(s["actual"] for s in states.values() if s["actual"])
err = [abs(s["sim_current"] - s["actual"]) / s["actual"] for s in states.values() if s["actual"]]
print(f"States simulated: {len(states)}; pool ${POOL_FY23:,}; sum of actuals ${tot_act:,.0f}")
print(f"Current-law reproduction: median abs error {sorted(err)[len(err)//2]*100:.1f}%, max {max(err)*100:.1f}%")
nat_cm = sum(s["case_months"] for s in states.values()); nat_D = sum(s["D"] for s in states.values())
print(f"National proxy case-months {nat_cm:,.0f}; D ${nat_D:,.0f}; avg owed per case-month ${nat_D/nat_cm:,.2f}")
avgs = sorted((s["D"] / s["case_months"], n) for n, s in states.items())
print("lowest avg:", [(n, round(a)) for a, n in avgs[:3]], "highest avg:", [(n, round(a)) for a, n in avgs[-4:]])
o = states["OHIO"]
print("OHIO", json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in o.items()}, indent=1))
for B in B_LIST:
    ch = sorted(((s[f"new_{int(B)}"] - s["actual"]) / s["actual"], n) for n, s in states.items() if s["actual"])
    print(f"B={B}: change vs actual median {ch[len(ch)//2][0]*100:.1f}%  min {ch[0]} max {ch[-1]}")
json.dump({"pool": POOL_FY23, "states": states, "B_list": B_LIST}, open(OUT, "w"), indent=1)
