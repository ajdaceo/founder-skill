"""Second check before a plan is released: re-add the calculation record and compare it with the figures printed in the plan.
Usage: python3 verify_outputs.py out_dir      (exit 0 = consistent, 1 = mismatch)
Independent of build_crp.py's own totals: it reads only the two documents the client receives."""
import os
import re
import sys


def parse_calc(text):
    """{'Baseline': {1: t, 2: t, 3: t}, 'Current': {...}} recomputed from quantity x factor / 1000 on each line."""
    out, part = {}, None
    for line in text.splitlines():
        m = re.match(r"## (Baseline|Current):", line)
        if m:
            part = m.group(1)
            out[part] = {1: 0.0, 2: 0.0, 3: 0.0}
            continue
        cells = [c.strip() for c in line.split("|")]
        if part and len(cells) > 8 and re.fullmatch(r"[123]", cells[5]):
            qty, factor = float(cells[2].replace(",", "")), float(cells[4])
            printed = float(cells[7].replace(",", ""))
            if abs(qty * factor / 1000 - printed) > 0.0006:
                raise ValueError(f"{part}: line '{cells[1]}' prints {printed} but {qty} x {factor} / 1000 = {qty * factor / 1000:.4f}")
            out[part][int(cells[5])] += qty * factor / 1000
    return out


def parse_plan(text):
    out = {}
    for name, heading in (("Baseline", "## Baseline emissions footprint"), ("Current", "## Current emissions reporting")):
        sec = text.split(heading, 1)[1].split("\n## ", 1)[0]
        vals = {}
        for label, key in (("Scope 1", 1), ("Scope 2", 2), ("Scope 3 (included sources)", 3), ("**Total emissions**", "total")):
            m = re.search(r"\|\s*" + re.escape(label) + r"\s*\|\s*\**([\d,]+\.\d\d)\**\s*\|", sec)
            if not m:
                raise ValueError(f"{name}: '{label}' row not found in plan")
            vals[key] = float(m.group(1).replace(",", ""))
        out[name] = vals
    return out


def verify(out_dir):
    calc = parse_calc(open(os.path.join(out_dir, "calculation.md")).read())
    plan = parse_plan(open(os.path.join(out_dir, "plan.md")).read())
    problems = []
    for part in ("Baseline", "Current"):
        for scope in (1, 2, 3):
            if abs(calc[part][scope] - plan[part][scope]) > 0.0051:
                problems.append(f"{part} Scope {scope}: record adds to {calc[part][scope]:.3f}, plan prints {plan[part][scope]:.2f}")
        total = sum(calc[part].values())
        if abs(total - plan[part]["total"]) > 0.0051:
            problems.append(f"{part} total: record adds to {total:.3f}, plan prints {plan[part]['total']:.2f}")
    return problems


if __name__ == "__main__":
    try:
        problems = verify(sys.argv[1])
    except (ValueError, OSError, IndexError) as e:
        problems = [str(e)]
    print("consistent" if not problems else "MISMATCH:\n  " + "\n  ".join(problems))
    sys.exit(1 if problems else 0)
