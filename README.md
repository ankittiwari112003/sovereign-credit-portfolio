# sovereign-credit-portfolio

This is a personal project exploring sovereign creditworthiness in 16 emerging economies across 2008 and 2022. The aim is to simulate lending portfolio allocations based on a custom **Lending Attractiveness Index (LAI)** and average credit rating scores.

### Tools Used
- **Excel**: for initial data cleanup and exploration  
- **Python**: to calculate the LAI, simulate capital allocation, and filter based on corruption/credit metrics  
- **Power BI**: for final data visualization (portfolio distribution, credit scores, country-level comparisons)

### Lending Attractiveness Index (LAI)
The LAI was created by combining key variables:
- Credit Score
- SWF (Sovereign Wealth Fund) Size
- Whether or not a country received SWF loans
- Official Credit Rating (converted numerically)

Some countries were excluded from the index where key data was unavailable (e.g. no credit score, missing SWF data, or unrated).

---

### Key Visualizations
- **Portfolio Distribution (2008 vs 2022)**: Pie charts showing how capital would be allocated if invested purely based on LAI  
- **Credit Rating Comparison**: Bar charts showing average sovereign credit scores by country and year

---

### Model Output
In the Python model, a total capital pool of $10 billion was hypothetically allocated to the top 5 countries in 2022 based on their LAI. Allocation was proportional to each country's share of the total LAI. Expected annual income was estimated using each country's lending rate.

Note: This simulation filters out countries with high corruption (above 40) and low credit scores (below 5) in 2022 to reflect conservative risk preferences.

---

### File Overview
- `sovereign_lending_clean.xlsx`: cleaned dataset used in modeling and visualizations  
- `sovereign_lending_model.py`: Python script to calculate LAI, filter data, and simulate portfolio returns  
- `sovereign_credit_portfolio_analysis.pbix`: Power BI file containing final visualizations

---

### Limitations
- LAI is a simple proxy and does not reflect real-world geopolitical or market risk factors.
- Some countries (e.g. Angola, Kenya, Bangladesh in 2008) were excluded due to incomplete or inconsistent data.
- Lending rates and SWF data are based on estimates or assumptions where direct data was unavailable.

---

### Next Steps
Possible future improvements include:
- Extending the dataset to include more years or countries
- Incorporating macroeconomic indicators (GDP growth, inflation, reserves)
- Adding a risk-adjusted return framework

---

Created and maintained by [@ankittiwari112003](https://github.com/ankittiwari112003)
