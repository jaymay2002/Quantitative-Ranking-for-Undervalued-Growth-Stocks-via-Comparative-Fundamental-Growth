# Stock Selection Algorithm

## Important Files
- **ETFSCREENER_SLOPE.ipynb**: This notebook contains stock selection criteria using moving averages, historical performance, and technical indicators.
- **GridSearch.ipynb**: This notebook contains the basis for stock fundamental data analysis using weighted growth metrics of key indicators.
- **FINALCOMBINEDFUNDAMENTALETFS.ipynb**: This notebook combines all previous methodologies to dynamically select and rank prime stock candidates based on technical and fundamental indicators.

This project implements an algorithmic strategy to identify optimal stocks through a blend of technical and fundamental analysis. The primary goal is to pinpoint fundamentally strong, undervalued stocks with high growth potential by leveraging quantitative analysis of key market and company indicators. The project includes a backtesting framework to optimize stock selection parameters and refine results.

## Project Overview

### 1. Stock Screening and Selection
- The algorithm scans **2,500 stocks** daily across multiple indices and sectors.
- Stocks are selected based on **fundamental** and **technical stock analysis**, including:
  - Growth of **key fundamental indicators** such as:
    - **Earnings per share (EPS)**
    - **Free cash flow (FCF)**
    - **Net income**
  - **Technical indicators** such as:
    - **Moving averages** (e.g., 50-day and 200-day MA crossovers)
    - **Momentum and strength indicators**
    - **Historical performance trends**
- The goal is to identify **high-potential stocks** with strong fundamental growth and positive technical signals.

### 2. Comparative Analysis and Ranking
- Stocks are evaluated on a **relative basis** to assess **comparative growth** across key fundamental indicators.
- Technical trends are combined with these growth metrics to rank stocks based on **overall potential** and **undervaluation**.
- The goal is to build a ranking of stocks that exhibit both **robust growth fundamentals** and **strong technical indicators**.

### 3. Backtesting and Optimization
- **Backtesting** is utilized to fine-tune parameters, identifying optimal combinations of technical and fundamental indicators.
- The framework adjusts the weighting of various growth and technical metrics to enhance the selection process and improve portfolio performance.
- The objective is to continually optimize the model’s stock selection criteria based on historical performance.

## Key Features

- **Dynamic Stock Screening**: Daily screening of 2,500 stocks based on technical and fundamental growth metrics.
- **In-depth Comparative Analysis**: Selection of stocks through a quantitative ranking system using relative growth and technical indicators.
- **Backtesting and Parameter Optimization**: Backtesting strategies to refine stock selection criteria and optimize indicator weightings.

## Project Workflow

1. **Data Collection**: Gather daily technical and fundamental data for a universe of 2,500 stocks.
2. **ETF Screener**: Apply technical criteria like moving averages and performance metrics to rank stocks.
3. **Stock Screener**: Perform growth-based fundamental analysis and narrow down stock selections based on technical indicators.
4. **Backtesting**: Test various selection parameters to find the best-performing strategy.

## Future Enhancements

- **Real-time data integration** for live stock screening.
- **Expansion of stock universe** to incorporate additional sectors.
- **Incorporation of machine learning models** for predictive stock selection and enhanced analysis.
