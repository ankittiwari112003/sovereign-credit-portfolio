import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# import excel dataset
df = pd.read_excel("sovereign_lending_clean.xlsx")


# convert credit ratings to scores
rating_map = {
    "AAA": 20, "AA+": 19, "AA": 18, "AA-": 17,
    "A+": 16, "A": 15, "A-": 14,
    "BBB+": 13, "BBB": 12, "BBB-": 11,
    "BB+": 10, "BB": 9, "BB-": 8,
    "B+": 7, "B": 6, "B-": 5,
    "CCC+": 4, "CCC": 3, "CC": 2, "C": 1,
    "SD": 0, "D": 0, "NR": np.nan
}
df["Credit_Score"] = df["Credit_Rating"].map(rating_map)

# establish lending attractiveness index (LAI)
df["LAI"] = (
    (df["GDP_Billion_USD"] / df["GDP_Billion_USD"].max()) * 0.3 +
    (df["Credit_Score"] / 20) * 0.3 +
    ((100 - df["Corruption_Index"]) / 100) * 0.2 +
    (df["SWF_Size_Billion_USD"] / df["SWF_Size_Billion_USD"].max()) * 0.2
)

# portfolio simulation: allocation of $10B to top 5 by LAI (2022)
total_capital = 10_000  # $10B

# filter for 2022 only and drop NA
df_2022 = df[(df["Year"] == 2022) & (df["Credit_Score"] >= 5) & (df["Corruption_Index"] <= 40)].copy()
top5 = df_2022.sort_values(by="LAI", ascending=False).head(5)
top5["Capital_Allocated"] = (top5["LAI"] / top5["LAI"].sum()) * total_capital
top5["Expected_Annual_Income"] = top5["Capital_Allocated"] * (top5["Lending_Rate_%"] / 100)

# visualization of portfolio allocation
# =============================
plt.figure(figsize=(10, 6))
plt.pie(top5["Capital_Allocated"], labels=top5["Country"], autopct="%1.1f%%", startangle=140)
plt.title("SWF Infrastructure Portfolio Allocation (Top 5 Countries, 2022)")
plt.tight_layout()
plt.show()

# show allocation table
print(top5[["Country", "LAI", "Capital_Allocated", "Lending_Rate_%", "Expected_Annual_Income"]])
df.to_excel("sovereign_lending_clean.xlsx", index=False)

