# sovereign-credit-portfolio

This is a personal project exploring sovereign creditworthiness in 16 economies in 2008 and 2022. The aim is to simulate lending portfolio allocations based on a custom **Lending Attractiveness Index (LAI)** and average credit rating scores.

### Tools Used
- **Excel**: for initial data cleanup and exploration  
- **Python**: to calculate the LAI, simulate capital allocation, and filter based on corruption/credit metrics  
- **Power BI**: for final data visualization (portfolio distribution, credit scores, country-level comparisons)

---

### Lending Attractiveness Index (LAI)
The LAI was created by combining key variables:
- Credit Score
- SWF (Sovereign Wealth Fund) Size
- Whether or not a country received SWF loans
- Official Credit Rating (converted numerically)

The goal was to estimate relative lending attractiveness across sovereigns by normalizing and aggregating these variables. Countries with insufficient data (e.g. missing SWF amounts, unrated debt, or no credit score) were excluded from the LAI.

---

### Key Visualizations
- **Portfolio Distribution (2008 vs 2022)**  
  Pie charts showing how capital would be allocated if invested purely based on LAI weights.  
  Each slice reflects the share of hypothetical portfolio value allocated to that country based on its LAI.

- **Credit Rating Comparison (2008 vs 2022)**  
  Bar charts comparing average sovereign credit scores by country and year.  
  ⚠️ **Lower bars = stronger creditworthiness.**  
  ⚠️ **Higher bars = weaker credit profiles.**  

---

### Model Output
In the Python model, a total capital pool of $10 billion was hypothetically allocated to the top 5 countries in 2022 based on their LAI scores. Allocation was proportional to each country's share of the total LAI. Expected annual income was then estimated using each country's sovereign lending rate.

The model also applies filtering:
- Countries with **corruption scores over 40** were excluded (i.e. too corrupt to lend to)
- Countries with **credit scores under 5** were excluded (i.e. too risky to lend to)

This reflects a conservative lender’s profile — prioritizing creditworthy, transparent sovereigns.

---

### File Overview
- `data/sovereign_lending_clean.xlsx`: Cleaned dataset used for modeling and visualizations  
- `scripts/sovereign_lending_model.py`: Python script to calculate LAI, apply filters, and simulate allocation/returns  
- `visualizations/sovereign_credit_portfolio_analysis.pbix`: Power BI dashboard with visual outputs  
- `data/data_sources.md`: Breakdown of original source links and methodology

---

### Limitations
- LAI is a simplified index and does not account for real-world political/macroeconomic risk, external debt, or currency volatility  
- Countries with incomplete data (e.g. Angola 2008, Kenya 2008, Bangladesh 2008) were excluded from LAI calculations  
- Lending rates were estimated where official data was missing  
- Credit ratings in visuals follow **inverted scoring** for chart clarity

---

### Next Steps
- Expand dataset to more countries or years  
- Add macroeconomic fundamentals (GDP growth, inflation, external reserves)  
- Build a formal risk-return framework or Monte Carlo simulations for lending outcomes  
- Explore different allocation strategies (e.g. equal weight, risk parity)

---

Created and maintained by [@ankittiwari112003](https://github.com/ankittiwari112003)
