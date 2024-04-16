import time
from datetime import datetime, timedelta
from pymongo import MongoClient
from polygon import RESTClient
import pytz

# MongoDB client
client = MongoClient('localhost', 27017)
db = client['Project_TrendFollowing']

# Function to delete and recreate collection
def recreate_collection():
    if 'eurusdRates_2y_hourly' in db.list_collection_names():
        db.drop_collection('eurusdRates_2y_hourly')
    return db['eurusdRates_2y_hourly']

# Polygon REST client
polygon_client = RESTClient("oDq8WeCSpxtCj3NnFp561nDjAo4asq5V")

def fetch_and_insert_data(start_date: datetime, end_date: datetime, collection):
    print("Fetching data from Polygon API...")
    print(f"Requesting data from {start_date} to {end_date}")

    # Convert start_date and end_date to UTC timezone
    utc_timezone = pytz.timezone('UTC')
    start_date_utc = utc_timezone.localize(start_date)
    end_date_utc = utc_timezone.localize(end_date)

    # Fetching aggregates with hourly granularity
    aggregates = polygon_client.get_aggs(
        ticker="C:EURUSD",
        multiplier=1,
        timespan="hour",
        from_=start_date_utc,
        to=end_date_utc,
        adjusted=True,
        sort = 'asc'
    )
    print("Data received from Polygon API.")
    print(f"Aggregates: {aggregates}")

    if aggregates:
        print(f"Number of results: {len(aggregates)}")
        last_timestamp = None

        # Inserting the fetched data into MongoDB
        for agg in aggregates:
            timestamp_dt = datetime.fromtimestamp(agg.timestamp / 1000)
            timestamp_est = timestamp_dt.astimezone(pytz.timezone('America/New_York'))
            data = {
                'date': timestamp_est.strftime('%Y-%m-%d %H:%M:%S'),
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
            last_timestamp = timestamp_dt

        print("Data insertion into MongoDB completed.")
        print(f"Last timestamp: {last_timestamp}")
        return last_timestamp
    else:
        print("No results found in the aggregates.")
        return None

# Initial start and end dates in UTC timezone
# Initial start and end dates in UTC timezone
start_date = datetime(2022, 3, 26)
end_date = datetime(2024, 3, 24, 23, 0, 0)

# Convert start_date and end_date to UTC timezone

# Delete and recreate collection
collection = recreate_collection()

while start_date_utc < end_date_utc:
    last_timestamp = fetch_and_insert_data(start_date_utc, min(end_date_utc, start_date_utc + timedelta(days=3)), collection)

    if last_timestamp:
        start_date_utc = last_timestamp + timedelta(hours=1)
    else:
        break

    # Wait for 12 seconds before the next API call
    time.sleep(12)

# Close MongoDB client
client.close()

