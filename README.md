# 🌍 Global Supply Chain Risk Dashboard

An interactive data analytics dashboard to analyze global shipment delays and supply chain risks from 2020 to 2024.

---

## 🚀 Live Demo

👉 *(Add your Streamlit link here after deployment)*

---

## 📊 Features

* 🌍 Global Choropleth Map (Risk by Country)
* 📈 Shipment Trend Analysis
* 📊 Delay Analysis by Country
* 🌦 Weather Impact on Delays
* 🚨 Top High-Risk Countries
* 📊 KPI Metrics (Shipments, Delay, Risk Score)
* 🎛 Interactive Filters (Year, Country)

---

## 🧠 Risk Score Model

The risk score is calculated using:

Risk Score =
0.5 × Congestion Score (Shipments) +
0.5 × Delay Score (Average Delay Hours)

---

## 🛠 Tech Stack

* Python
* Pandas
* Plotly
* Streamlit
* Scikit-learn

---

## 📁 Project Structure

```
global_supply_chain_dashboard/
│
├── dashboard.py
├── generate_dataset.py
├── risk_model.py
├── global_supply_chain_risk_dataset_2020_2024.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run Locally

1. Clone the repository:

```
git clone https://github.com/Piyush-Rajbanshi/Global-Supply-Chain-Dashboard.git
cd Global-Supply-Chain-Dashboard
```

2. Create virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the app:

```
streamlit run dashboard.py
```

---

## 📌 Key Insights

* Countries with high shipment volume tend to have higher delays
* Weather conditions significantly impact shipment delays
* Risk hotspots can be identified using combined metrics

---
