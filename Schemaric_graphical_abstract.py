"""
Schematic: circular rebound effect (CRE) against value retention.

Model relationship (see Methods/Equation in the manuscript):

  Zero-burden allocation:
      CRE_ZBA = CFM / IF * 100
      The reused product carries no production burden, so avoided emissions
      equal the full new-product footprint. CRE does NOT depend on value
      retention -> a flat line.

  Economic allocation:
      CRE_EAA = CFM / ((1 - VR) * IF) * 100 = CRE_ZBA / (1 - VR)
      A share of the production burden proportional to retained value is
      reassigned to the second life, so avoided emissions scale with
      (1 - value retention). As value retention (VR) rises, the denominator
      shrinks and CRE rises, crossing the 100% backfire threshold.

This is an illustrative schematic. CRE0 sets the common starting level at
VR = 0 (where both rules coincide); pick it to suit the figure.
"""

import numpy as np
import matplotlib.pyplot as plt
import os


# ensure output directory exists
os.makedirs("schematic_graphical_abstract", exist_ok=True)


# ---------------------------------------------------------------- parameters
CRE0 = 70.0        # zero-burden CRE level (%), the value at VR = 0
VR_MAX = 0.70      # largest value retention shown (fraction, 0-1)
Y_MAX = 250.0      # top of the y-axis (%)
BACKFIRE = 100.0   # backfire threshold (%)

BLUE = "#1f4e79"   # zero-burden
RED = "#b22222"    # economic allocation
GREY = "#666666"

# ----------------------------------------------------------------- the curves
vr = np.linspace(0.0, VR_MAX, 300)        # value retention as a fraction
cre_eaa = CRE0 / (1.0 - vr)               # economic allocation: rises with VR
cre_zba = np.full_like(vr, CRE0)          # zero-burden: invariant to VR

# ------------------------------------------------------------------- plotting
fig, ax = plt.subplots(figsize=(6.2, 5.0))

# shade and mark the backfire region (CRE > 100%)
ax.axhspan(BACKFIRE, Y_MAX, color=RED, alpha=0.06, zorder=0)
ax.axhline(BACKFIRE, ls="--", lw=1.3, color=GREY, zorder=2)

# the two allocation rules
ax.plot(vr, cre_zba, color=BLUE, lw=2.6, zorder=3)
ax.plot(vr, cre_eaa, color=RED, lw=2.6, zorder=3)

# axes
ax.set_xlim(0.0, VR_MAX)
ax.set_ylim(40.0, Y_MAX)
ax.set_xticks([0.0, 0.2, 0.4, 0.6])
ax.set_xticklabels(["0", "20", "40", "60"], fontsize=20)
ax.set_yticks([BACKFIRE])
ax.set_yticklabels(["100"], fontsize=20)
ax.set_xlabel("Value retention (%)", fontsize=20)
ax.set_ylabel("Circular rebound effect (%)", fontsize=20)

# labels
ax.text(0.02, BACKFIRE + 35, "Backfire \n(CRE > 100%)",
        ha="left", va="top", fontsize=20, color=RED)
ax.text(VR_MAX - 0.01, CRE0 - 7, "Zero-burden: invariant",
        ha="right", va="top", fontsize=20, color=BLUE)
ax.annotate("Economic allocation:\nrises with value retention",
            xy=(0.585, CRE0 / (1.0 - 0.585)), xytext=(0.085, 200),
            fontsize=20, color=RED,
            arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))

for side in ("top", "right"):
    ax.spines[side].set_visible(False)
ax.tick_params(length=3)

fig.tight_layout()
fig.savefig("schematic_graphical_abstract/cre_vs_value_retention_schematic.pdf")
fig.savefig("schematic_graphical_abstract/cre_vs_value_retention_schematic.png", dpi=300)
plt.show()