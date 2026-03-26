import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler

# Page Configuration

st.set_page_config(
    page_title="Global Supply Chain Risk Dashboard",
    layout="wide"
)

# Title

st.title("🌍 Global Supply Chain Risk Dashboard (2020–2024)")
st.write("Analyze global shipment delays and supply chain risks.")

# Load Dataset

df = pd.read_csv("global_supply_chain_risk_dataset_2020_2024.csv")

# Risk Score Calculation

scaler = MinMaxScaler()

df["congestion_score"] = scaler.fit_transform(df[["Shipments"]])
df["delay_score"] = scaler.fit_transform(df[["Average_Delay_Hours"]])

df["risk_score"] = (
    df["congestion_score"] * 0.5 +
    df["delay_score"] * 0.5
)

# SIDEBAR FILTERS

st.sidebar.header("🔍 Filters")

# Year filter
selected_year = st.sidebar.selectbox(
    "Select Year",
    sorted(df["Year"].unique())
)

# Country filter
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    sorted(df["Country"].unique()),
    default=df["Country"].unique()[:5]
)

# Apply filters
filtered_df = df[
    (df["Year"] == selected_year) &
    (df["Country"].isin(selected_countries))
]

# KPI Metrics

st.header("📊 KPI Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Shipments", int(filtered_df["Shipments"].sum()))
col2.metric("Average Delay (Hours)", round(filtered_df["Average_Delay_Hours"].mean(), 2))
col3.metric("Average Risk Score", round(filtered_df["risk_score"].mean(), 2))

# Global Risk Map

st.header("🌍 Global Risk Map")

country_delay = filtered_df.groupby("Country")["Average_Delay_Hours"].mean().reset_index()

fig_map = px.choropleth(
    country_delay,
    locations="Country",
    locationmode="country names",
    color="Average_Delay_Hours",
    hover_name="Country",
    title="Average Shipment Delay by Country",
    color_continuous_scale="Reds"
)

st.plotly_chart(fig_map, use_container_width=True)

# Shipment Trend

st.header("📈 Shipment Trend Over Time")

trend_df = df[df["Country"].isin(selected_countries)]

yearly_shipments = trend_df.groupby("Year")["Shipments"].sum().reset_index()

fig_trend = px.line(
    yearly_shipments,
    x="Year",
    y="Shipments",
    markers=True,
    title="Global Shipments Trend"
)

st.plotly_chart(fig_trend, use_container_width=True)

# Delay Analysis

st.header("📊 Average Delay by Country")

delay_country = filtered_df.groupby("Country")["Average_Delay_Hours"].mean().reset_index()

fig_bar = px.bar(
    delay_country,
    x="Country",
    y="Average_Delay_Hours",
    color="Average_Delay_Hours",
    title="Average Shipment Delay by Country"
)

st.plotly_chart(fig_bar, use_container_width=True)

# Weather Impact

st.header("🌦 Weather Impact on Delays")

weather_delay = filtered_df.groupby("Weather")["Average_Delay_Hours"].mean().reset_index()

fig_weather = px.bar(
    weather_delay,
    x="Weather",
    y="Average_Delay_Hours",
    color="Weather",
    title="Weather Impact on Shipment Delay"
)

st.plotly_chart(fig_weather, use_container_width=True)

# Top Risk Countries

st.header("🚨 Top 10 High Risk Countries")

top_risk = filtered_df.groupby("Country")["risk_score"].mean().reset_index()
top_risk = top_risk.sort_values(by="risk_score", ascending=False).head(10)

fig_top = px.bar(
    top_risk,
    x="Country",
    y="risk_score",
    color="risk_score",
    title="Top 10 Countries with Highest Supply Chain Risk"
)

st.plotly_chart(fig_top, use_container_width=True)

# Data Preview

st.header("📄 Filtered Data")

st.dataframe(filtered_df)

# Save processed dataset

filtered_df.to_csv("final_risk_data.csv", index=False)