# ==========================================================
# ARIMA Time Series Analysis – ENEL.MI
# ==========================================================
# This script performs ARIMA modeling on monthly log returns
# of ENEL (ENEL.MI) stock using Yahoo Finance data.
#
# For the rendered report with outputs and plots,
# see the file: index.html
# ==========================================================


# =========================
# 1. Load Libraries
# =========================

library(quantmod)
library(forecast)
library(tseries)


# =========================
# 2. Download Data
# =========================

ticker <- "ENEL.MI"

data <- getSymbols(ticker, src = "yahoo", auto.assign = FALSE)

# Use Adjusted Close prices (safer than column index)
price <- Ad(data)

cat("First observations of price data:\n")
print(head(price))


# =========================
# 3. Compute Monthly Log Returns
# =========================

monthly_price <- to.monthly(price, indexAt = "lastof", drop.time = TRUE)
monthly_close <- monthly_price[,4]

returns <- diff(log(monthly_close)) * 100
returns <- na.omit(returns)

cat("\nFirst observations of monthly returns:\n")
print(head(returns))

y <- ts(as.numeric(returns), frequency = 12)


# =========================
# 4. Plot Monthly Returns
# =========================

plot(y,
     main = "Monthly Log Returns",
     ylab = "Return (%)",
     col = "steelblue")


# =========================
# 5. Descriptive Statistics
# =========================

cat("\nDescriptive Statistics:\n")
cat("Mean:", mean(y), "\n")
cat("Standard Deviation:", sd(y), "\n")
cat("Variance:", var(y), "\n")


# =========================
# 6. T-Test for Zero Mean
# =========================

cat("\nOne-sample t-test:\n")
print(t.test(y))


# =========================
# 7. Stationarity Test (ADF)
# =========================

cat("\nAugmented Dickey-Fuller Test:\n")
print(adf.test(y))


# =========================
# 8. Fit ARIMA Model
# =========================

fit <- auto.arima(y, seasonal = FALSE)

cat("\nSelected ARIMA Model:\n")
print(summary(fit))


# =========================
# 9. Residual Diagnostics
# =========================

checkresiduals(fit)


# =========================
# 10. Forecast 12 Months Ahead
# =========================

fc <- forecast(fit, h = 12)

plot(fc,
     main = "ARIMA Forecast")


# =========================
# 11. Forecast Accuracy
# =========================

cat("\nForecast Accuracy:\n")
print(accuracy(fc))


# =========================
# End of Script
# =========================
