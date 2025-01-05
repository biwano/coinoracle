import click
import requests
import math
from datetime import datetime, timezone
from pandas import DataFrame, read_csv
import os.path
import time

FOLDER = "../data"

def ts(time: datetime):
    return math.floor(time.timestamp()) * 1000

def fetch_one(startTime: datetime) -> list:
    filename = f"{FOLDER}/{startTime.year:04}-{startTime.month:02}-{startTime.day:02}.csv"
    click.echo(f"Reading {filename} {startTime}")
    
    if os.path.isfile(filename):
        df = read_csv(filename)
    
    else:
        click.echo(f"Cache failure. Fetching")
        endTime = datetime(day=startTime.day, month=startTime.month, year=startTime.year, 
                        hour=23, minute=59, second=59,tzinfo=timezone.utc)
        
        x = requests.get("https://api.binance.com/api/v3/klines",
                        params={ "symbol": "BTCUSDT",
                                "interval": "1h" ,
                                "startTime": ts(startTime),
                                "endTime": ts(endTime)
                                    })
        data = [ [d[0], d[4], d[5] ] for d in x.json()]
        df = DataFrame(data, columns=["time", "close", "volume"])
        df.to_csv(filename)
        time.sleep(0.1)

    return df
    

@click.command()
def fetch():
    t = datetime.now()
    startTime = datetime(day=t.day-1, month=t.month, year=t.year, tzinfo=timezone.utc)
    data = fetch_one(startTime)

    while len(data) == 24:
        startTime = datetime.fromtimestamp(startTime.timestamp() - 24 * 60 * 60)
        data = fetch_one(startTime)
    

    