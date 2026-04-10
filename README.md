# The circularity paradox in secondhand markets

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)

Reproducibility package for:

> Laurenti, R. (2026). The circularity paradox in secondhand markets: value retention, allocation, and rebound effects. *Resources, Conservation & Recycling*, XX(X), XXXXXX. https://doi.org/XX.XXXX/XXXXXXX

## Overview

This repository contains the code and input files needed to reproduce the analysis presented in the paper. The Jupyter notebook implements a complete pipeline that (i) cleans and summarises listing-level price data from a major Swedish online secondhand marketplace, (ii) projects retail prices and value retention ratios from manually curated reference products, (iii) derives cradle-to-gate carbon footprints using EXIOBASE 3.8.2 multi-regional input–output (MRIO) multipliers, (iv) estimates potential avoided emissions under both zero-burden and economic allocation, (v) models potential increased emissions from buyer and seller re-spending using Swedish household expenditure profiles, (vi) computes the circular rebound effect (CRE) for 32 product categories, and (vii) runs sensitivity analyses on reference product selection.

## Repository structure

```
.
├── README.md
├── LICENSE
├── requirements.txt
├── environment.yml
├── notebooks/
│   └── CRE_analysis.ipynb
├── raw/                          # Large input data (not tracked by Git)
│   └── scraped_data.xlsx         # → download from Zenodo (see below)
├── factors/                      # Input files for IO-LCA modelling
│   ├── retail_prices_representative_products.yaml
│   ├── df_32cat_CFexio_RL.xlsx
│   ├── Exio_COICOP12.xlsx
│   └── EXIOBASE341f_CC500f.csv
├── processed/                    # Generated intermediate files (gitignored)
├── derived/                      # Generated derived tables (gitignored)
└── results/                      # Generated figures and tables (gitignored)
```

## Data availability

**Raw marketplace data.** The scraped listing dataset (`scraped_data.xlsx`, 239,643 listings) is archived on Zenodo:

> https://doi.org/10.5281/zenodo.19471590

Download the file and place it in the `raw/` directory before running the notebook.

**EXIOBASE 3.8.2.** The notebook reads the EXIOBASE product-by-product input–output table (`IOT_2022_pxp.zip`) to build household carbon footprint multipliers. Download the dataset from [Zenodo](https://doi.org/10.5281/zenodo.5589597) and update the path in Section 04 of the notebook (variable `exio_path`).

**Factor files.** The remaining input files in `factors/` are included in this repository:

| File | Description |
|---|---|
| `retail_prices_representative_products.yaml` | Manually curated retail prices and sources for the 32 reference products |
| `df_32cat_CFexio_RL.xlsx` | Mapping between 32 marketplace categories and EXIOBASE product sectors, with GHG emission intensities per M EUR |
| `Exio_COICOP12.xlsx` | Concordance matrix between EXIOBASE sectors and 12 COICOP household expenditure categories |
| `EXIOBASE341f_CC500f.csv` | Characterisation matrix for converting EXIOBASE environmental stressors into carbon footprint multipliers (kg CO₂-eq.) |

## System requirements

- Python 3.11
- Approximately 4 GB RAM (EXIOBASE parsing is memory-intensive)

### Installation

Using conda (recommended):

```bash
conda env create -f environment.yml
conda activate exiobase
```

Using pip:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Reproducing the analysis

1. Clone this repository.
2. Download `scraped_data.xlsx` from [Zenodo](https://doi.org/10.5281/zenodo.19471590) and place it in `raw/`.
3. Download `IOT_2022_pxp.zip` from [EXIOBASE on Zenodo](https://doi.org/10.5281/zenodo.5589597) and update the `exio_path` variable in Section 04 of the notebook.
4. Create the environment (see above).
5. Launch the notebook and run all cells sequentially:

```bash
jupyter lab notebooks/CRE_analysis.ipynb
```

The notebook creates three output directories (`processed/`, `derived/`, `results/`) and populates them as it runs. Key outputs include:

| Output | Location |
|---|---|
| Cleaned listing data | `processed/df_cleaned_en.parquet` |
| Household carbon footprint multipliers | `processed/Y_HH_COICOP_perc_CF_SE.parquet` |
| Economic and environmental benefits (Table 2) | `results/table2_econ_env_benefits.xlsx` |
| Normalised impact metrics figure | `results/normalized_impact_metrics_plot.png` |
| CRE heatmap figure | `results/fig_cre_heatmap.png` |
| Sensitivity analysis figure | `results/fig_sensitivity_cre.png` |
| Sensitivity tables (A, B, C) | `results/sensitivity_*.csv` |

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Citation

If you use this code or data, please cite the paper:

```bibtex
@article{laurenti2026circularity,
  title     = {The circularity paradox in secondhand markets: value retention, allocation, and rebound effects},
  author    = {Laurenti, Rafael},
  journal   = {Resources, Conservation & Recycling},
  year      = {2026},
  doi       = {XX.XXXX/XXXXXXX}
}
```
