#!/usr/bin/env python3
"""
vcf_compare.py
Parses all patient/control VCF files and produces a comparison table.
"""

import os
import glob

VCF_FILES = {
    "control":                  "vcf/control/synthetic_control_chr10_benign_only.vcf",
    "patient1_lof_only":        "vcf/patients/synthetic_patient1_kat6b_lof_only.vcf",
    "patient1_lof_plus_benign": "vcf/patients/synthetic_patient1_kat6b_lof_plus_benign.vcf",
    "patient2_lof_only":        "vcf/patients/synthetic_patient2_kat6b_lof_only.vcf",
    "patient2_lof_plus_benign": "vcf/patients/synthetic_patient2_kat6b_lof_plus_benign.vcf",
}

def parse_vcf(filepath):
    variants = []
    with open(filepath) as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            fields = line.strip().split("\t")
            if len(fields) < 8:
                continue
            variants.append({
                "CHROM":  fields[0],
                "POS":    int(fields[1]),
                "ID":     fields[2],
                "REF":    fields[3],
                "ALT":    fields[4],
                "QUAL":   fields[5],
                "FILTER": fields[6],
                "INFO":   fields[7],
            })
    return variants

def main():
    all_data = {}
    all_variant_ids = set()

    for sample, path in VCF_FILES.items():
        variants = parse_vcf(path)
        all_data[sample] = {v["ID"]: v for v in variants}
        all_variant_ids.update(v["ID"] for v in variants)

    # Print header
    samples = list(VCF_FILES.keys())
    col_w = 28
    header = f"{'Variant ID':<28} {'POS':<12} {'REF>ALT':<10} " + \
             "  ".join(f"{s:<22}" for s in samples)
    print(header)
    print("-" * len(header))

    for vid in sorted(all_variant_ids, key=lambda x: (
        next((v["POS"] for s in all_data.values() for k, v in s.items() if k == x), 0)
    )):
        # Get POS and REF>ALT from first sample that has it
        pos, ref_alt = "?", "?"
        for s in all_data.values():
            if vid in s:
                v = s[vid]
                pos = str(v["POS"])
                ref_alt = f"{v['REF']}>{v['ALT']}"
                break
        presence = []
        for s in samples:
            presence.append("PRESENT" if vid in all_data[s] else "absent")
        row = f"{vid:<28} {pos:<12} {ref_alt:<10} " + \
              "  ".join(f"{p:<22}" for p in presence)
        print(row)

    print("\n--- Summary ---")
    for sample in samples:
        n = len(all_data[sample])
        ids = ", ".join(all_data[sample].keys())
        print(f"{sample:<30}: {n} variant(s)  [{ids}]")

if __name__ == "__main__":
    main()
