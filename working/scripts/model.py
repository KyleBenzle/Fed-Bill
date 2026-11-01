"""Mathematical model of the proposed incentive formula.

Proposed (bill, sec. 2):
  base_s  = max(0, B * CM_s - D_s)            B: benchmark $/case-month; CM: case-months; D: annual current support owed
  IBA_s   = base_s * M_s                       M_s = sum of applicable percentages (paternity + order + current
                                               + 0.75 * arrears), max 3.75 after cost-effectiveness is struck
  pay_s   = Pool * IBA_s / sum_k IBA_k

Marginal effect of one more dollar of annual current support owed in State s (CM fixed):
  d pay_s / d D_s = -Pool * M_s * (S - IBA_s) / S**2,   S = sum_k IBA_k
"""
import json
import sys


def allocate(states, B, pool):
    out = {}
    iba = {}
    for n, s in states.items():
        base = max(0.0, B * s["cm"] - s["D"])
        iba[n] = base * s["M"]
        out[n] = {"base": base}
    S = sum(iba.values())
    for n, s in states.items():
        out[n]["iba"] = iba[n]
        out[n]["share"] = iba[n] / S if S else float("nan")
        out[n]["pay"] = pool * out[n]["share"] if S else float("nan")
        out[n]["marg"] = -pool * s["M"] * (S - iba[n]) / S ** 2 if (S and out[n]["base"] > 0) else 0.0
    return out


def hypothetical():
    """Three hypothetical States, identical performance (M = 3.75), pool $100 million, B = $1,000."""
    B, pool = 1000.0, 100e6
    st = {
        "A (100,000 cases, avg $300)": {"cm": 1.2e6, "D": 1.2e6 * 300, "M": 3.75},
        "B (100,000 cases, avg $450)": {"cm": 1.2e6, "D": 1.2e6 * 450, "M": 3.75},
        "C (300,000 cases, avg $400)": {"cm": 3.6e6, "D": 3.6e6 * 400, "M": 3.75},
    }
    r0 = allocate(st, B, pool)
    st2 = json.loads(json.dumps(st))
    st2["B (100,000 cases, avg $450)"]["D"] = 1.2e6 * 500  # State B average rises $50/month
    r1 = allocate(st2, B, pool)
    # all States +10% orders
    st3 = {k: dict(v, D=v["D"] * 1.10) for k, v in st.items()}
    r2 = allocate(st3, B, pool)
    # State over benchmark
    st4 = json.loads(json.dumps(st)); st4["B (100,000 cases, avg $450)"]["D"] = 1.2e6 * 1100
    r3 = allocate(st4, B, pool)
    return {"base": r0, "B_up50": r1, "all_up10": r2, "B_over": r3}


def per_case_weights(B=1000.0):
    return [(o, B - o) for o in (0, 250, 450, 1000, 1500)]


if __name__ == "__main__":
    for o, w in per_case_weights():
        print(f"order {o:>5}: weight {w:>6}")
    res = hypothetical()
    for k, r in res.items():
        print("==", k)
        for n, v in r.items():
            print(f"  {n:32s} base {v['base']/1e6:9.1f}M  share {v['share']*100:6.2f}%  pay ${v['pay']/1e6:7.2f}M  marg/$ {v['marg']*100:6.2f}c")
