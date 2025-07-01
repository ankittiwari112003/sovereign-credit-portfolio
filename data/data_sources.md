# Data Sources – Sovereign Credit Portfolio Project

This project draws on publicly available data across key macroeconomic and risk indicators for emerging markets. Data was compiled manually for 2008 and 2022 across the following categories:

---

## 📊 Datasets & Sources

| Metric                         | Description                                                                 | Source                                                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| **GDP (US$ Billion)**         | Country-level nominal GDP, 2008 & 2022                                      | [World Bank Open Data](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)                           |
| **Lending Rate (%)**          | Lending interest rates or sovereign yield proxies                           | [World Bank Lending Rates](https://data.worldbank.org/indicator/FR.INR.LEND)                          |
| **Credit Ratings**            | Sovereign ratings (S&P format) for default risk assessment                  | [Trading Economics](https://tradingeconomics.com/country-list/rating)                                 |
| **Corruption Index (CPI)**    | Transparency International's Corruption Perception Index                    | [Transparency International](https://www.transparency.org/en/cpi)                                     |
| **SWF Size (US$ Billion)**    | Sovereign wealth fund asset size (if applicable)                            | [SWFI – Sovereign Wealth Fund Institute](https://www.swfinstitute.org/fund-rankings/sovereign-wealth-fund) |
| **IMF Lending Status**        | Whether the country had a lending arrangement with the IMF in the given year| [IMF Lending Tracker](https://www.imf.org/en/Topics/imf-and-covid19/COVID-Lending-Tracker)            |

---

## 🧹 Notes on Usage
- Missing data points (e.g. credit ratings for some frontier markets in 2008) were excluded from the LAI calculation.
- All numerical values were rounded or approximated to reflect reported macroeconomic data as of 2008 and 2022.
- The compiled and cleaned dataset used for modeling is saved in:  
  `data/sovereign_lending_clean.xlsx`
