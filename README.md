# ETF and Stock Selection Algorithm

This project implements an algorithmic strategy for selecting optimal ETFs and stocks, combining both technical and fundamental analysis. The primary goal is to identify attractive ETFs and then select the best-performing stocks within those ETFs based on key market and financial indicators. Additionally, the project includes a backtesting framework to fine-tune selection parameters and optimize results.

## Project Overview

### 1. ETF Screening and Selection
- The algorithm scans **2,000 of the largest ETFs** daily.
- ETFs are selected based on **technical criteria**, including:
  - **Moving averages** (e.g., 50-day and 200-day MA crossovers)
  - **Recent and historical performance**
  - **Undervaluation indicators**
  - **Momentum and strength indicators**
- The aim is to identify **optimal ETFs** across different sectors by analyzing technical data and focusing on ETFs with strong potential.

### 2. Stock Screening within Optimal ETFs
- The algorithm identifies **optimal stocks** from the **S&P 500** and **NASDAQ 100** indices.
- Stocks are selected based on **fundamental** and **technical stock analysis**, including:
  - Growth of **key fundamental indicators** such as:
    - **Earnings per share (EPS)**
    - **Free cash flow (FCF)**
    - **Net income**
  - Combining ETF sector strength with the stock’s performance.
- The goal is to find stocks within ETFs that are ranked highly based on both **fundamental growth** and **technical indicators**.

### 3. Backtesting and Optimization
- **Backtesting** is performed to find the optimal parameters for selecting ETFs and stocks.
- The backtesting framework is used to determine which selection criteria (e.g., moving averages, earnings growth) provide the best results.
- The model **adjusts weightings** of various indicators to improve decision-making and portfolio performance.

## Key Features

- **Dynamic ETF Selection**: Daily screening of ETFs based on market conditions and technical criteria.
- **Comprehensive Stock Analysis**: Screening stocks based on fundamental growth and technical indicators within selected ETFs.
- **Backtesting and Optimization**: Backtesting strategies to identify optimal selection criteria and refining weightings for various indicators.

## Project Workflow

1. **Data Collection**: Gather daily technical data for **2,000 ETFs** and fundamental data for **S&P 500** and **NASDAQ 100** stocks.
2. **ETF Screener**: Apply technical criteria like moving averages and performance metrics to rank ETFs.
3. **Stock Screener**: Perform growth-based fundamental analysis and narrow down stock selections based on ETF strength.
4. **Backtesting**: Test various selection parameters to find the best-performing strategy.
5. **Optimization**: Adjust indicator weightings to maximize portfolio returns and minimize risk.

## Future Enhancements

- **Real-time data integration** for live ETF and stock screening.
- **Expanding the stock universe** beyond the S&P 500 and NASDAQ 100.
- **Incorporation of machine learning models** for predictive stock and ETF selection.
