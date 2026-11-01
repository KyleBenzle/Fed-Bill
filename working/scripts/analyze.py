"""Derived results from sim_fy2023.json (all illustrative; FY2023 preliminary data; proxy case-months)."""
import json, sys
d = json.load(open(sys.argv[1])); S = d["states"]; P = d["pool"]
def alloc(states, B, key="M_new"):
    iba = {n: max(0.0, B*s["case_months"]-s["D"])*s[key] for n, s in states.items()}
    T = sum(iba.values()); return {n: P*v/T for n, v in iba.items()}
B = 1000.0
cur = {n: s["sim_current"] for n, s in S.items()}
new = alloc(S, B)
ch = sorted(((new[n]-cur[n])/cur[n], n) for n in S)
print("vs simulated current law, B=1000: median %.1f%%" % (ch[len(ch)//2][0]*100))
print(" n gaining:", sum(1 for c,_ in ch if c>0), "n losing:", sum(1 for c,_ in ch if c<0))
print(" largest losses:", [(n, round(c*100,1)) for c,n in ch[:5]])
print(" largest gains:", [(n, round(c*100,1)) for c,n in ch[-5:]])
o = S["OHIO"]
print("OHIO sim current %.2fM new %.2fM change %.1f%%" % (cur["OHIO"]/1e6, new["OHIO"]/1e6, (new["OHIO"]/cur["OHIO"]-1)*100))
print("OHIO avg owed per case-month %.2f; national %.2f" % (o["D"]/o["case_months"], sum(s["D"] for s in S.values())/sum(s["case_months"] for s in S.values())))
# Ohio sensitivity
for pct in (-0.10, 0.10):
    S2 = json.loads(json.dumps(S)); S2["OHIO"]["D"] *= 1+pct
    n2 = alloc(S2, B)
    print("OHIO owed %+d%% (%+.1fM owed): payment %.2fM (%+.2fM), cents per $ %.2f" % (pct*100, o["D"]*pct/1e6, n2["OHIO"]/1e6, (n2["OHIO"]-new["OHIO"])/1e6, (n2["OHIO"]-new["OHIO"])/(o["D"]*pct)*100))
# All states +10%
S3 = {n: dict(s, D=s["D"]*1.1) for n, s in S.items()}; n3 = alloc(S3, B)
print("ALL +10%%: OHIO %.2fM; national total unchanged %.0f" % (n3["OHIO"]/1e6, sum(n3.values())))
# Ohio: one additional case-month at $0, $275, $1000 order
T = sum(max(0.0,B*s["case_months"]-s["D"])*s["M_new"] for s in S.values())
for O in (0, 275, 500, 1000):
    print("value to Ohio of one added case-month with order $%d: $%.2f" % (O, P*o["M_new"]*(B-O)/T*(1-new["OHIO"]/P)))
# Dollar-for-dollar alternative
dd = {n: max(0.0, B*s["case_months"]-s["D"]) for n, s in S.items()}
print("Dollar-for-dollar at B=1000: national $%.1fB vs pool $%.0fM (x%.0f); Ohio $%.2fB" % (sum(dd.values())/1e9, P/1e6, sum(dd.values())/P, dd["OHIO"]/1e9))
# B that makes dollar-for-dollar total equal pool
lo, hi = 0.0, 1000.0
for _ in range(60):
    mid=(lo+hi)/2; t=sum(max(0.0,mid*s["case_months"]-s["D"]) for s in S.values())
    lo,hi=(mid,hi) if t<P else (lo,mid)
z = sum(1 for s in S.values() if mid*s["case_months"]-s["D"]<=0)
print("Dollar-for-dollar budget-neutral B=%.2f; states receiving zero: %d of %d; Ohio $%.1fM" % (mid, z, len(S), max(0,mid*o["case_months"]-o["D"])/1e6))
# Sensitivity of Ohio to B
for b in d["B_list"]:
    print("B=%d Ohio new %.2fM marg %.2f c/$" % (b, S["OHIO"]["new_%d"%b]/1e6, S["OHIO"]["marg_%d"%b]*100))
# national marginal range
m = sorted((s["marg_1000"]*100, n) for n, s in S.items())
print("marg c/$ range:", m[0], m[-1])
