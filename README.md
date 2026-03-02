# ARIMA Time Series Analysis – ENEL.MI

This project applies ARIMA modeling to monthly log returns of ENEL (ENEL.MI) stock using data from Yahoo Finance.

---

## 🔗 Live Report

👉 https://mohammad-siahi.github.io/Arima-Time-Series/

The full rendered analysis (including outputs and plots) is available at the link above.

---

## Methodology

- Conversion of daily prices to monthly data  
- Computation of log returns (%)  
- Augmented Dickey–Fuller (ADF) stationarity test  
- ARIMA model selection using `auto.arima()`  
- Residual diagnostics (Ljung–Box test)  
- 12-month ahead forecast  

The selected model for monthly returns is:

**ARIMA(0,0,0) with non-zero mean**

This suggests that monthly returns behave approximately as white noise with a constant mean.

---

## Project Structure

- `Analysis.R` → Full R script  
- `index.html` → Rendered HTML report (GitHub Pages)  
- `README.md` → Project documentation  

---

## How to Run Locally

Open `Analysis.R` in RStudio and run the script.

Required packages:

```r
install.packages(c("quantmod","forecast","tseries"))
