import pandas as pd
import numpy as np
import pycountry

# Get list of countries
countries = [country.name for country in pycountry.countries]

years = range(2019, 2024)

data = []

for country in countries:
    base_throughput = np.random.randint(50, 1000)
    base_lpi = np.random.uniform(2.0, 4.5)
    
    for year in years:
        throughput = base_throughput + np.random.randint(-100, 100)
        lpi_score = round(base_lpi + np.random.uniform(-0.3, 0.3), 2)
        storm_count = np.random.poisson(lam=5)
        
        data.append([
            country,
            year,
            max(throughput, 10),
            lpi_score,
            storm_count
        ])

df = pd.DataFrame(data, columns=[
    "country",
    "year",
    "throughput",
    "lpi_score",
    "storm_count"
])

df.to_csv("synthetic_supply_chain_data.csv", index=False)

print("Synthetic dataset created successfully.")
