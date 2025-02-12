import click
import requests
import math
from datetime import datetime, timezone
from utils import save_data, load_data

FOLDER = "../data"

def ts(time: datetime):
    return math.floor(time.timestamp()) * 1000

def fetch_one(startTime: datetime) -> list:
    data = load_data(startTime)
    
    if data is None:
        click.echo(f"Cache failure. Fetching")
        endTime = datetime(day=startTime.day, month=startTime.month, year=startTime.year, 
                        hour=23, minute=59, second=59,tzinfo=timezone.utc)
        
        x = requests.get("https://api.binance.com/api/v3/klines",
                        params={ "symbol": "BTCUSDT",
                                "interval": "1h" ,
                                "startTime": ts(startTime),
                                "endTime": ts(endTime)
                                    })
        # timestamp, close, volume
        raw_data = [ [ float(d[0]), float(d[4]), float(d[5]) ] for d in x.json()]
        data = save_data(startTime, raw_data)

    return data
    

def fetch_():
    t = datetime.now()
    startTime = datetime(day=t.day-1, month=t.month, year=t.year, tzinfo=timezone.utc)
    data = fetch_one(startTime)

    while len(data) == 24:
        startTime = datetime.fromtimestamp(startTime.timestamp() - 24 * 60 * 60)
        data = fetch_one(startTime)


@click.command()
def fetch():
    return fetch_()
    

    