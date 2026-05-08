#!/usr/bin/env python3
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

SAMPLES = ["Control", "P1 – LoF only", "P1 – LoF+benign", "P2 – LoF only", "P2 – LoF+benign"]
VARIANTS = ["KAT6B_LOF\n(C>A, nonsense)", "P2_KAT6B_LOF_FS\n(C>CC, frameshift)", "BENIGN1\n(G>A, benign)"]
MATRIX = [
    [0, 0, 1],
    [1, 0, 0],
    [1, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
]
C_KAT6B  = "#01696f"
C_BENIGN = "#bb653b"
C_ABSENT = "#f0efeb"

fig1, ax1 = plt.subplots(figsize=(9, 5))
fig1.patch.set_facecolor("white")
ax1.set_facecolor("white")
for i, row in enumerate(MATRIX):
    for j, val in enumerate(row):
        color  = (C_KAT6B if j < 2 else C_BENIGN) if val else C_ABSENT
        tcolor = "white" if val else "#9a9994"
        rect = mpatches.FancyBboxPatch((j+0.05, i+0.08), 0.88, 0.82,
            boxstyle="round,pad=0.04", linewidth=0, facecolor=color)
        ax1.add_patch(rect)
        ax1.text(j+0.49, i+0.49, "Present" if val else "Absent",
            ha="center", va="center", fontsize=11,
            fontweight="bold" if val else "normal", color=tcolor)
ax1.set_xlim(0, 3); ax1.set_ylim(0, 5)
ax1.set_xticks([x+0.49 for x in range(3)])
ax1.set_xticklabels(VARIANTS, fontsize=10)
ax1.set_yticks([y+0.49 for y in range(5)])
ax1.set_yticklabels(SAMPLES, fontsize=11)
ax1.tick_params(length=0)
for s in ax1.spines.values(): s.set_visible(False)
ax1.legend(handles=[
    mpatches.Patch(color=C_KAT6B,  label="KAT6B LoF present"),
    mpatches.Patch(color=C_BENIGN, label="Benign variant present"),
    mpatches.Patch(color=C_ABSENT, label="Absent", ec="#ccc"),
], loc="lower center", bbox_to_anchor=(0.5, -0.18), ncol=3, frameon=False, fontsize=10)
ax1.set_title("Variant Presence Across Synthetic KAT6B Samples", fontsize=13, fontweight="bold", pad=12)
fig1.tight_layout()
fig1.savefig("variant_heatmap.png", dpi=180, bbox_inches="tight", facecolor="white")
print("Saved: variant_heatmap.png")

CHR10 = 133_797_422
fig2, ax2 = plt.subplots(figsize=(11, 4))
fig2.patch.set_facecolor("white")
ax2.set_facecolor("#fafaf8")
ax2.fill_between([0, CHR10], [-0.15], [0.15], color="#e8e6e1", zorder=1)
ax2.text(CHR10/2, -0.32, "chr10 hg38 (133.8 Mb)", ha="center", fontsize=9, color="#7a7974")
ax2.axvspan(74_800_000, 75_200_000, alpha=0.12, color=C_KAT6B, zorder=2)
ax2.text(75_000_000, 0.58, "KAT6B (10q22)", ha="center", fontsize=9, color=C_KAT6B, fontweight="bold")
for pos, label, color, y in [
    (74_975_481, "P1: KAT6B_LOF\nC>A nonsense",   C_KAT6B,  0.65),
    (75_028_821, "P2: KAT6B_LOF_FS\nC>CC frameshift", C_BENIGN, -0.7),
    (101_000_000,"BENIGN1\nG>A",                  "#7a7974", 0.65),
]:
    ax2.scatter(pos, 0, color=color, s=90, zorder=5)
    ax2.annotate(label, xy=(pos, 0), xytext=(pos, y), fontsize=8.5,
        ha="center", color=color, fontweight="bold",
        arrowprops=dict(arrowstyle="-", color=color, lw=1.1))
ax2.set_xlim(-3e6, CHR10+3e6); ax2.set_ylim(-1.1, 1.1)
ax2.set_yticks([])
xticks = [0, 25e6, 50e6, 75e6, 100e6, 125e6, CHR10]
ax2.set_xticks(xticks)
ax2.set_xticklabels([f"{int(x/1e6)}Mb" for x in xticks], fontsize=9)
for s in ["top","right","left"]: ax2.spines[s].set_visible(False)
ax2.spines["bottom"].set_color("#ccc")
ax2.set_title("Synthetic Variant Positions on chr10 (hg38)", fontsize=13, fontweight="bold", pad=12)
fig2.tight_layout()
fig2.savefig("chr10_variant_positions.png", dpi=180, bbox_inches="tight", facecolor="white")
print("Saved: chr10_variant_positions.png")
print("Done!")
