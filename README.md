# Lighter Protocol Data Analysis

A modular Python project designed for robust, modular interaction with the zkLighter API and direct EVM block data. The project enables retrieval, analysis, and visualization of cryptocurrency market data—including candlesticks, funding rates, open interest, and liquidity provider metrics—as well as on-chain analytics for protocol valuation, asset flow tracking, and comprehensive wallet/user segmentation.

## Protocol Information

Lighter is a decentralized trading platform focused on delivering unmatched security and scalability. It features verifiable matching and liquidations, operating with performance comparable to leading traditional exchanges.

## Overview

This project provides key capabilities which includes:

- Retrieving account and market data from the zkLighter API
- Analyzing candlestick data across multiple markets
- Tracking and visualizing perpetuals trading volume
- Tracking and visualizing funding rates
- Monitoring current open interest
- Evaluating Lighter Liquidity Provider (LLP) performance
- Parsing EVM block data (transfers and logs) to analyze asset flows and total value locked (TVL)
- Assessing deposit and withdrawal activity, profiling user wallet behavior, and segmenting wallets by size and activity

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd lighter-analysis
```

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the project root:
```bash
MY_L1_ADDRESS=your_ethereum_address_here
ALCHEMY_API_KEY=your_alchemy_api_key_here
```

## Project Structure

```
lighter-analysis/
├── lighter_api.py              # API client with all endpoint functions
├── process.py                  # Data processing utilities
├── lighter.ipynb               # Main analysis notebook
├── evm.ipynb                   # Web3 integration and blockchain data analysis
├── data/                       # CSV data files
│   ├── usdc_logs_deposits.csv
│   ├── usdc_transfer_deposits.csv
│   └── usdc_transfer_withdrawals.csv
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (create this)
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

## Features & Data Analysis

This project provides a comprehensive suite of tools for cryptocurrency market and on-chain protocol analysis, organized into interactive Jupyter notebooks:

- **Market Data Analysis (`lighter.ipynb`):**
  - **Volume Analysis:**  
    - Visualize trading volumes across all markets
    - Identify top 5 markets by volume
    - Analyze historical volume trends and total market volume over time
  - **Funding Rate Analysis:**  
    - Track funding rates with heatmap visualizations
    - Explore historical funding rate trends
    - Calculate direction-aware funding (long/short)
  - **Open Interest Tracking:**  
    - Monitor current open interest by market
    - Correlate trading activity with open interest
    - Highlight top markets by open interest (OI)
  - **LLP (Lighter Liquidity Provider) Performance:**  
    - Track Total Value Locked (TVL)
    - Calculate Annual Percentage Yield (APY)
    - Analyze share price history and daily returns

- **On-Chain Analytics (`evm.ipynb`):**
  - **Total Value Locked (TVL) Analysis:**  
    - Monitor contract balances
    - Analyze deposits and withdrawals
    - Visualize daily, weekly, and monthly asset flows
  - **User Wallet Segmentation:**  
    - Parse transaction logs for unique wallet deposit activity
    - Segment user profiles by deposit size and frequency
    - Group users based on activity and wallet characteristics

Both notebooks leverage robust data processing and visualization to deliver actionable insights into protocol health, user behavior, and market dynamics.

## Configuration

### Environment Variables (`.env` file)

Set the following variables in your `.env` file to configure the project:

- `MY_L1_ADDRESS` - (required) Your Ethereum L1 address.
- `ALCHEMY_API_KEY` - (required) Your Alchemy API key for Ethereum node access.

## Dependencies

- `requests` - HTTP client for API calls
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computing
- `matplotlib` - Plotting and visualization
- `seaborn` - Statistical data visualization
- `python-dotenv` - Environment variable management
- `ipython` - Interactive Python shell
- `jupyter` - Jupyter notebook support
- `web3` - Ethereum blockchain interaction

## References

- [Lighter API Documentation](https://apidocs.lighter.xyz/)  
  Comprehensive guide to Lighter protocol endpoints and integration.
- [Lighter on DefiLlama](https://defillama.com/protocol/tvl/lighter)  
  Aggregated data on TVL and protocol metrics.
- [Lighter User and Flow Analytics (Dune Dashboard)](https://dune.com/tervelix/lighter-user-and-flow-analytics)  
  Detailed analytics on user activity and asset movements.
