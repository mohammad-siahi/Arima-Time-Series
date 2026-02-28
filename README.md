# ARIMA Time Series Analysis – ENEL.MI

This project applies ARIMA modeling to monthly log returns of ENEL (ENEL.MI) stock using Yahoo Finance data.

## Method
- Convert daily prices to monthly data  
- Compute log returns (%)  
- Test stationarity (ADF test)  
- Fit ARIMA model using `auto.arima()`  
- Perform residual diagnostics  
- Forecast 12 months ahead  

## Result
Selected model: **ARIMA(0,0,0) with mean**  
Monthly returns behave approximately as white noise with a constant mean.

Note: The model forecasts **returns**, not prices.

---

## How to Run

1. Install R and RStudio (if not already installed).

2. Download or clone this repository.

3. Open the file `enel_arima.Rmd` in RStudio.

4. Click the **Knit** button (top of the editor) and choose **Knit to HTML**.

The analysis will run automatically and generate the HTML report.
