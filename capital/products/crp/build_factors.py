"""Build factors.csv (one row per year and activity) from the UK Government GHG conversion factor flat files.

Usage: python3 build_factors.py DIR_WITH_YEAR_FOLDERS [--debug]
  DIR/2018/flat.xlsx ... DIR/2026/flat.xlsx   (download URLs and checksums are in factor_sources.csv;
  2018, 2019, 2021 and 2022 are published as .xls: convert with `soffice --headless --convert-to xlsx flat.xls`)
Writes factors.csv next to this script. Only total kg CO2e rows are used (not the per-gas rows).
The flat files are Crown copyright, Open Government Licence v3.0.

Each activity is matched on Level 1-3, optional extra words (Level 4 / Column Text) and the unit.
Category names changed between years, so each activity lists the alternatives seen. A year is left out for an
activity when no row matches exactly once: the generator then refuses that activity for that year rather than guess.
"""
import csv
import os
import re
import sys

import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
YEARS = range(2018, 2027)
HGV_ALL = ("HGV (all diesel)", "HGV (non-refrigerated, all diesel)")
HGV_REF = ("HGV refrigerated (all diesel)", "HGV (refrigerated, all diesel)")
CI = "Commercial and industrial waste"
FOOD = ("Organic: food and drink waste",)
BURN = ("Combustion",)
BURN_2025 = ("Incineration with Energy Recovery",)  # 2025 file's name for the same disposal route


# Refrigerants: from 2022 each gas has three rows (Kyoto only / non-Kyoto only / total); earlier files have one.
def RB(gas): return ("Refrigerant & other", ("Blends",), (gas,), ("only Kyoto",), "kg")
def RB_OLD(gas): return ("Refrigerant & other", ("Kyoto protocol- blends",), (gas,), (), "kg")
def RK(gas): return ("Refrigerant & other", ("Kyoto protocol products",), (gas,), ("only Kyoto",), "kg")
def RK_OLD(gas): return ("Refrigerant & other", ("Kyoto protocol - standard",), (gas,), (), "kg")
def WASTE(l2, l3, route): return ("Waste disposal", (l2,), (l3,), (route,), "tonnes")

# key: (scope, PPN 006 Scope 3 category or "", unit, [alternatives]); alternative = (L1, L2 options, L3 options, extra words, UOM)
SPEC = {
    # Scope 1: fuels burned and vehicles the organisation owns or controls
    "natural_gas_kwh": (1, "", "kWh", [("Fuels", ("Gaseous fuels",), ("Natural gas",), (), "kWh (Gross CV)")]),
    "lpg_litre": (1, "", "litre", [("Fuels", ("Gaseous fuels",), ("LPG",), (), "litres")]),
    "burning_oil_litre": (1, "", "litre", [("Fuels", ("Liquid fuels",), ("Burning oil",), (), "litres")]),
    "gas_oil_litre": (1, "", "litre", [("Fuels", ("Liquid fuels",), ("Gas oil",), (), "litres")]),
    "diesel_litre": (1, "", "litre", [("Fuels", ("Liquid fuels",), ("Diesel (average biofuel blend)",), (), "litres")]),
    "petrol_litre": (1, "", "litre", [("Fuels", ("Liquid fuels",), ("Petrol (average biofuel blend)",), (), "litres")]),
    "own_car_km": (1, "", "km", [("Passenger vehicles", ("Cars (by size)",), ("Average car",), ("Unknown",), "km")]),
    "own_car_diesel_km": (1, "", "km", [("Passenger vehicles", ("Cars (by size)",), ("Average car",), ("Diesel",), "km")]),
    "own_car_petrol_km": (1, "", "km", [("Passenger vehicles", ("Cars (by size)",), ("Average car",), ("Petrol",), "km")]),
    "own_van_diesel_km": (1, "", "km", [("Delivery vehicles", ("Vans",), ("Average (up to 3.5 tonnes)",), ("Diesel",), "km")]),
    "refrigerant_r404a_kg": (1, "", "kg", [RB("R404A"), RB_OLD("R404A")]),
    "refrigerant_r410a_kg": (1, "", "kg", [RB("R410A"), RB_OLD("R410A")]),
    "refrigerant_r407c_kg": (1, "", "kg", [RB("R407C"), RB_OLD("R407C")]),
    "refrigerant_r134a_kg": (1, "", "kg", [RK("HFC-134a"), RK_OLD("HFC-134a")]),
    "refrigerant_r32_kg": (1, "", "kg", [RK("HFC-32"), RK_OLD("HFC-32")]),
    # Scope 2: purchased electricity, location-based (UK grid average)
    "electricity_kwh": (2, "", "kWh", [("UK electricity", ("Electricity generated",), ("Electricity: UK",), (), "kWh")]),
    # Scope 3, category 4 and 9: transport and distribution by third parties
    "van_diesel_km": (3, "4/9", "km", [("Freighting goods", ("Vans",), ("Average (up to 3.5 tonnes)",), ("Diesel",), "km")]),
    "van_diesel_tonne_km": (3, "4/9", "tonne.km", [("Freighting goods", ("Vans",), ("Average (up to 3.5 tonnes)",), ("Diesel",), "tonne.km")]),
    "hgv_rigid_km": (3, "4/9", "km", [("Freighting goods", HGV_ALL, ("All rigids", "Average non-refrigerated rigids"), ("Average laden",), "km")]),
    "hgv_artic_km": (3, "4/9", "km", [("Freighting goods", HGV_ALL, ("All artics", "Average non-refrigerated artics"), ("Average laden",), "km")]),
    "hgv_tonne_km": (3, "4/9", "tonne.km", [("Freighting goods", HGV_ALL, ("All HGVs", "Average non-refrigerated HGVs"), ("Average laden",), "tonne.km")]),
    "hgv_refrigerated_km": (3, "4/9", "km", [("Freighting goods", HGV_REF, ("All HGVs", "Average refrigerated HGVs"), ("Average laden",), "km")]),
    "hgv_refrigerated_tonne_km": (3, "4/9", "tonne.km", [("Freighting goods", HGV_REF, ("All HGVs", "Average refrigerated HGVs"), ("Average laden",), "tonne.km")]),
    # Scope 3, category 5: waste generated in operations
    "waste_landfill_tonne": (3, "5", "tonne", [("Waste disposal", ("Refuse",), (CI,), ("Landfill",), "tonnes")]),
    "waste_combustion_tonne": (3, "5", "tonne", [("Waste disposal", ("Refuse",), (CI,), BURN, "tonnes"), ("Waste disposal", ("Refuse",), (CI,), BURN_2025, "tonnes")]),
    "waste_recycled_tonne": (3, "5", "tonne", [("Waste disposal", ("Refuse",), (CI,), ("Closed-loop",), "tonnes")]),
    "recycling_paper_card_tonne": (3, "5", "tonne", [WASTE("Paper", "Paper and board: mixed", "Closed-loop")]),
    "recycling_plastics_tonne": (3, "5", "tonne", [WASTE("Plastic", "Plastics: average plastics", "Closed-loop")]),
    "recycling_glass_tonne": (3, "5", "tonne", [WASTE("Other", "Glass", "Closed-loop")]),
    "recycling_metal_tonne": (3, "5", "tonne", [WASTE("Metal", "Metal: mixed cans", "Closed-loop")]),
    "food_waste_ad_tonne": (3, "5", "tonne", [("Waste disposal", ("Refuse",), FOOD, ("Anaerobic digestion",), "tonnes")]),
    "food_waste_compost_tonne": (3, "5", "tonne", [("Waste disposal", ("Refuse",), FOOD, ("Composting",), "tonnes")]),
    "food_waste_landfill_tonne": (3, "5", "tonne", [("Waste disposal", ("Refuse",), FOOD, ("Landfill",), "tonnes")]),
    "water_treatment_m3": (3, "5", "cubic metre", [("Water treatment", ("Water treatment",), ("Water treatment",), (), "cubic metres")]),
    # Scope 3, category 6: business travel
    "car_km": (3, "6", "km", [("Business travel- land", ("Cars (by size)",), ("Average car",), ("Unknown",), "km")]),
    "car_diesel_km": (3, "6", "km", [("Business travel- land", ("Cars (by size)",), ("Average car",), ("Diesel",), "km")]),
    "car_petrol_km": (3, "6", "km", [("Business travel- land", ("Cars (by size)",), ("Average car",), ("Petrol",), "km")]),
    "rail_km": (3, "6", "passenger.km", [("Business travel- land", ("Rail",), ("National rail",), (), "passenger.km")]),
    "bus_km": (3, "6", "passenger.km", [("Business travel- land", ("Bus",), ("Average local bus",), (), "passenger.km")]),
    "taxi_km": (3, "6", "passenger.km", [("Business travel- land", ("Taxis",), ("Regular taxi",), (), "passenger.km")]),
    "flight_domestic_km": (3, "6", "passenger.km", [("Business travel- air", ("Flights",), ("Domestic, to/from UK",), ("Average passenger", "With RF"), "passenger.km")]),
    "flight_short_haul_km": (3, "6", "passenger.km", [("Business travel- air", ("Flights",), ("Short-haul, to/from UK",), ("Average passenger", "With RF"), "passenger.km")]),
    "flight_long_haul_km": (3, "6", "passenger.km", [("Business travel- air", ("Flights",), ("Long-haul, to/from UK",), ("Average passenger", "With RF"), "passenger.km")]),
    "hotel_night_uk": (3, "6", "room night", [("Hotel stay", ("Hotel stay",), ("UK",), (), "Room per night")]),
    # Scope 3, category 7: employee commuting (same published factors as business travel)
    "commute_km": (3, "7", "km", [("Business travel- land", ("Cars (by size)",), ("Average car",), ("Unknown",), "km")]),
    "commute_rail_km": (3, "7", "passenger.km", [("Business travel- land", ("Rail",), ("National rail",), (), "passenger.km")]),
    "commute_bus_km": (3, "7", "passenger.km", [("Business travel- land", ("Bus",), ("Average local bus",), (), "passenger.km")]),
    "commute_motorbike_km": (3, "7", "km", [("Business travel- land", ("Motorbike",), ("Average",), (), "km")]),
}


def norm(v):
    return re.sub(r"\s+", " ", str(v if v is not None else "").replace("\xa0", " ")).strip().lower()


def load(path, year):
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = wb["Factors by Category"]
    it = ws.iter_rows(values_only=True)
    for row in it:
        cells = [norm(c) for c in row]
        if "scope" in cells and "level 1" in cells:
            col = {name: cells.index(name) for name in ("scope", "level 1", "level 2", "level 3", "level 4", "column text", "uom")}
            col["ghg"] = cells.index("ghg/unit") if "ghg/unit" in cells else cells.index("ghg")
            col["id"] = cells.index("id") if "id" in cells else None
            col["value"] = next(i for i, c in enumerate(cells) if c.startswith("ghg conversion factor"))
            break
    else:
        raise SystemExit(f"{year}: header row not found")
    rows = []
    for row in it:
        if len(row) <= col["value"] or norm(row[col["ghg"]]) != "kg co2e" or row[col["value"]] in (None, ""):
            continue
        try:
            value = float(row[col["value"]])
        except (TypeError, ValueError):
            continue
        rows.append({"scope": norm(row[col["scope"]]), "l1": norm(row[col["level 1"]]), "l2": norm(row[col["level 2"]]),
                     "l3": norm(row[col["level 3"]]), "extra": norm(row[col["level 4"]]) + " | " + norm(row[col["column text"]]),
                     "uom": norm(row[col["uom"]]), "value": value,
                     "id": str(row[col["id"]]) if col["id"] is not None else "",
                     "label": " > ".join(str(row[col[k]]) for k in ("level 1", "level 2", "level 3", "level 4", "column text", "uom")
                                         if row[col[k]] not in (None, ""))})
    return rows


def match(rows, alts):
    hits = []
    for l1, l2s, l3s, extras, uom in alts:
        for r in rows:
            if (r["l1"] == norm(l1) and r["l2"] in [norm(x) for x in l2s] and r["l3"] in [norm(x) for x in l3s]
                    and r["uom"] == norm(uom) and all(norm(e) in r["extra"] for e in extras)):
                hits.append(r)
    return hits


def main(root, debug=False):
    out, missing = [], []
    for year in YEARS:
        path = os.path.join(root, str(year), "flat.xlsx")
        if not os.path.exists(path):
            print(f"{year}: no file, skipped")
            continue
        rows = load(path, year)
        for key, (scope, cat, unit, alts) in SPEC.items():
            hits = match(rows, alts)
            values = {round(h["value"], 8) for h in hits}
            if len(values) != 1:
                missing.append((year, key, len(hits)))
                if debug:
                    l1 = norm(alts[0][0])
                    near = sorted({r["label"] for r in rows if r["l1"] == l1 and any(norm(x) in r["l3"] or r["l3"] in norm(x) for x in alts[0][2])})
                    print(f"  MISS {year} {key}: {len(hits)} hits; near: {near[:6]}")
                continue
            h = hits[0]
            if f"scope {scope}" != h["scope"]:
                raise SystemExit(f"{year} {key}: expected Scope {scope}, file says {h['scope']}")
            out.append({"year": year, "key": key, "unit": unit, "kgco2e_per_unit": repr(h["value"]) if h["value"] != int(h["value"]) else str(h["value"]),
                        "scope": scope, "ppn_scope3_category": cat,
                        "source": f"UK Government GHG conversion factors {year}: {h['label']}" + (f" [{h['id']}]" if h["id"] else "")})
    with open(os.path.join(HERE, "factors.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["year", "key", "unit", "kgco2e_per_unit", "scope", "ppn_scope3_category", "source"])
        w.writeheader()
        w.writerows(out)
    print(f"wrote {len(out)} factors for {len({r['year'] for r in out})} years and {len({r['key'] for r in out})} activities")
    for m in missing:
        print("  not available:", m)


if __name__ == "__main__":
    main(sys.argv[1], "--debug" in sys.argv)
