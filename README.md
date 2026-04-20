# 🔐 Cryptographic Network Security Auditor
### Final Project — Milestone 2: The "Wrangling" Sprint

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Dataset](https://img.shields.io/badge/Data-CoinGecko%20%7C%20Bitcoin-green)
![Status](https://img.shields.io/badge/Milestone-2%20Complete-brightgreen)

---

## 📌 Project Overview

This project audits the **Bitcoin (BTC) blockchain network** using historical market data sourced from **CoinGecko**. By applying data wrangling and statistical analysis, we identify anomalous network activity that could signal security-relevant events such as coordinated trading, network stress, pump-and-dump schemes, or crash cascades.

---

## 🎯 Milestone 2 Objective

> Transform messy, raw data into a structured, high-integrity format ready for visualization.

| Task | Status |
|------|--------|
| Environment Setup | ✅ Done |
| Load & Inspect (`df.info`, `df.describe`) | ✅ Done |
| DateTime Conversion | ✅ Done |
| Handle Missing Values (Linear Interpolation) | ✅ Done |
| Feature Engineering (Anomaly Score, Volume Spikes, Volatility) | ✅ Done |
| 15 Exploratory Charts | ✅ Done |
| Correlation Heatmap (seaborn) | ✅ Done |
| Export Cleaned Dataset | ✅ Done |

---

## 📁 Repository Structure

```
crypto-security-auditor/
│
├── Milestone2_CryptoSecurityAuditor_BTC.ipynb   # Main Jupyter Notebook
├── bitcoin.csv                                   # Raw dataset (CoinGecko)
├── bitcoin_cleaned.csv                          # Cleaned & enriched dataset (generated)
└── README.md                                     # This file
```

---

## 📊 Dataset

- **Source:** CoinGecko API
- **Coin:** Bitcoin (BTC)
- **Period:** January 1, 2015 → March 27, 2024
- **Rows:** 3,373 daily records
- **Columns:** `date`, `price`, `total_volume`, `market_cap`, `coin_name`
- **Missing Values:** 1 (market_cap — handled via linear interpolation)

---

## 🔧 Feature Engineering

New columns created during wrangling:

| Feature | Description |
|---------|-------------|
| `price_return_pct` | Daily percentage price change |
| `price_ma30` | 30-day rolling average price |
| `anomaly_score` | Price deviation from MA30 in standard deviations (σ) — our "Delay Delta" |
| `volume_ma30` | 30-day rolling average volume |
| `volume_spike` | Boolean flag: True if volume > 2× MA30 |
| `market_cap_growth_pct` | Daily market cap % change |
| `rolling_volatility` | 30-day rolling std dev of daily returns |

---

## 📈 Exploratory Charts (15 Total)

| # | Chart |
|---|-------|
| 1 | BTC Price Over Time with 30-Day MA |
| 2 | Daily Trading Volume Over Time |
| 3 | Anomaly Score Over Time (±2σ zones) |
| 4 | Market Capitalization Over Time |
| 5 | Distribution of Daily Price Returns |
| 6 | Volume Spikes Overlaid on Price |
| 7 | Price vs. Volume Scatter (colored by year) |
| 8 | Average BTC Price by Year (bar chart) |
| 9 | Distribution of Anomaly Scores |
| 10 | Monthly Volume Heatmap by Year |
| 11 | **Correlation Heatmap** (seaborn) |
| 12 | Top 20 Highest Anomaly Score Days |
| 13 | Rolling 30-Day Volatility |
| 14 | Price Return Boxplot by Year |
| 15 | Full Anomaly Timeline (Pump & Crash Signals) |

---

## 🧠 Key Findings

- **Anomaly Score** captures real Bitcoin events: 2017 bubble, 2020 halving rally, 2021 ATH, May 2022 Terra Luna collapse, November 2022 FTX crash, and 2024 ETF surge.
- **Volume spikes** frequently precede anomaly score extremes — a key network stress signal.
- **2022** was the most security-critical year with two major crash events.
- **2023–2024** shows recovery and stabilization.

---

## 🚀 How to Run

### Option A — Google Colab (Recommended)
1. Open [Google Colab](https://colab.research.google.com)
2. Upload `Milestone2_CryptoSecurityAuditor_BTC.ipynb`
3. Upload `bitcoin.csv` via the Files panel (📁)
4. Click **Runtime → Run All**

### Option B — Local Jupyter
```bash
pip install pandas numpy matplotlib seaborn scipy
jupyter notebook Milestone2_CryptoSecurityAuditor_BTC.ipynb
```

---

*Dataset provided by CoinGecko. Analysis performed using Python (pandas, seaborn, matplotlib, scipy).*
