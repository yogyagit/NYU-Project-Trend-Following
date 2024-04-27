# Trend Following Analysis on EUR/USD (Prof. Carlos De. Oliveira)

This repository contains the Jupyter Notebook for a trend-following analysis and backtesting project on the EUR/USD currency pair. Developed as part of a project at NYU, this notebook implements various trend-following strategies to analyze and predict the currency movements of the Euro against the US Dollar.

## Project Overview

The project aims to apply quantitative methods and financial theories to the forex market, specifically through trend-following strategies. By backtesting these strategies on historical EUR/USD data, we assess their potential profitability and viability.

## Repository Structure

- `EURUSD_TrendAnalysis_Backtest.ipynb`: Main Jupyter notebook containing all the code, visualizations, and analysis for the trend-following strategies.

## Getting Started

To get started with this project, you will need to have a Python environment capable of running Jupyter notebooks. Below are the steps to set up your environment and run the notebook.

### Prerequisites

- Python 3.8+
- Jupyter Notebook or JupyterLab
- Required Python libraries: pandas, numpy, matplotlib, seaborn, scipy

### Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/yogyagit/NYU-Project-Trend-Following.git
``` 

2. Navigate to the cloned repository:
```bash
cd NYU-Project-Trend-Following
```

3. Install the required Python libraries:
```bash
pip install pandas numpy matplotlib seaborn scipy
```

4. Open the Jupyter Notebook:
```bash
jupyter notebook EURUSD_TrendAnalysis_Backtest.ipynb
```
## Data Integration and Storage

This project leverages real-time and historical currency exchange rate data via the Polygon API and stores the data in MongoDB for subsequent analysis. Below are the key components and steps involved in the data integration process:

### MongoDB Setup

- **Database**: `Project_TrendFollowing`
- **Collection**: `eurusdRates_2y`

We use MongoDB to store and manage the historical data of EUR/USD currency pair rates. This allows for efficient retrieval and manipulation of data during the trend analysis process.

### Polygon API

Data is fetched from the Polygon API, which provides comprehensive historical and real-time forex data. The following process is automated in the project:

1. **Data Fetching**: The script fetches daily aggregates for the EUR/USD ticker, covering specified date ranges.
2. **Data Transformation**: Each record is formatted with relevant fields such as open, high, low, close prices, and volume.
3. **Data Insertion**: The transformed data is then inserted into the MongoDB collection for persistence.

### Automation Script

The script `fetch_and_insert_data.py` is scheduled to run at regular intervals to update the dataset with the latest available data. It handles:
- Establishing a connection to MongoDB.
- Fetching new data from the Polygon API.
- Inserting the fetched data into MongoDB after processing.
- Closing the database connection once the operation is completed.

### Prerequisites for Data Script

Ensure you have the following installed:
- `pymongo` - MongoDB Python Driver
- `polygon-api-client` - Official Python client for the Polygon API

```bash
pip install pymongo polygon-api-client
```

### Running the Data Script
To fetch and store new data, run the script with the necessary API key and date ranges:

```bash
python fetch_and_insert_data.py
```

Please replace "your-api-key" with your actual Polygon API key in the script before running.

### Usage
Once you have the notebook open, you can run the cells sequentially to see the analysis and results of the trend-following strategies on the EUR/USD currency pair.

## Contributing
Contributions are welcome. If you have suggestions to improve this analysis or additional strategies to test, please fork this repository and submit a pull request.


