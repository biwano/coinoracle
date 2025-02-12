import click
from datetime import datetime, timedelta, date
import kagglehub
import csv
import pytz
from utils import save_data

FILE = "/home/biwano/.cache/kagglehub/datasets/oscardavidperilla/historical-bitcoin-prices-btc/versions/1/BTCUSDT_1h.csv"
@click.command()
def kaggle_fetch():
    path = kagglehub.dataset_download("oscardavidperilla/historical-bitcoin-prices-btc")

    print("Path to dataset files:", path)
    

@click.command()
def kaggle_transform():
    with open(FILE, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        current_date = False
        data = []
        i = 0
        for row in csvreader:
            if i > 0:
                try: 
                    new_datetime = datetime.strptime(f"{row[5]}-0500", "%Y-%m-%d %H:%M:%S.%f-05:00%z")
                except:
                    new_datetime = datetime.strptime(f"{row[5]}-0500", "%Y-%m-%d %H:%M:%S-05:00%z")
                utc_new_datetime = new_datetime.astimezone(pytz.utc) + timedelta(seconds=1)
                new_date = date(year=utc_new_datetime.year, month=utc_new_datetime.month, day=utc_new_datetime.day)

                if new_date != current_date:
                    if current_date:
                        print(utc_new_datetime.timestamp())
                        save_data(new_date, data)
                    current_date = new_date
                    data = []

                data.append([utc_new_datetime.timestamp() * 1000, float(row[3]), float(row[4])])
            i = i +1
            
            
