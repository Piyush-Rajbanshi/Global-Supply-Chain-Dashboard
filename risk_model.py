import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("synthetic_supply_chain_data.csv")

scaler = MinMaxScaler()

df["congestion_score"] = scaler.fit_transform(df[["throughput"]])
df["weather_score"] = scaler.fit_transform(df[["storm_count"]])

df["risk_score"] = (
    df["congestion_score"] * 0.6 +
    df["weather_score"] * 0.4 -
    df["lpi_score"] * 0.1
)

df.to_csv("final_risk_data.csv", index=False)

print("Risk dataset created.")