iimport time
from datetime import datetime
from pymongo import MongoClient
from polygon import RESTClient

# MongoDB client
client = MongoClient('localhost', 27017)
db = client['Project_TrendFollowing']
collection = db['eurusdRates_2y']  # Changed collection name

# Polygon REST client
polygon_client = RESTClient("your-api-key")

def fetch_and_insert_data(start_date: datetime, end_date: datetime):
    print("Fetching data from Polygon API...")

    # Fetching aggregates with hourly granularity
    aggregates = polygon_client.get_aggs(
        ticker="C:EURUSD",
        multiplier=1,
        timespan="day", 
        from_=start_date,
        to=end_date,
        adjusted=True
    )

    print("Data received from Polygon API.")
    print(f"Aggregates: {aggregates}")

    if aggregates:
        print(f"Number of results: {len(aggregates)}")

        # Inserting the fetched data into MongoDB
        for agg in aggregates:
            data = {
                'date': datetime.utcfromtimestamp(agg.timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S'),
                'open': agg.open,
                'high': agg.high,
                'low': agg.low,
                'close': agg.close,
                'volume': agg.volume,
                'volume_weighted': agg.vwap,
                'transactions': agg.transactions
            }
            print(f"Inserting data into MongoDB: {data}")
            collection.insert_one(data)

        print("Data insertion into MongoDB completed.")
    else:
        print("No results found in the aggregates.")

# Define start and end dates
start_date = datetime(2022, 3, 23)
end_date = datetime(2024, 3, 22)

# Fetch and insert data into MongoDB
fetch_and_insert_data(start_date, end_date)

# Close MongoDB client
client.close()
