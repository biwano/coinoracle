
import click
from datetime import date, timedelta
from utils import read_data, CLOSE
import numpy

FEATURES = 2
FOLDER = "../data"

def build_one_test(test_date):
    bases = []
    features_data = []
    def add_features_data(row):
        for i in range(FEATURES):
            value = ((row[i + 1] - bases[i]) * 100) / bases[i]
            features_data[i].append(value)

    # init
    row = read_data(test_date, 23)
    for i in range(FEATURES):
        bases.append(row[i + 1])
        features_data.append([])

    result_date = test_date + timedelta(days=1)
    tomorrow_row = read_data(result_date, 23)
    diff = ((tomorrow_row[CLOSE] - row[CLOSE]) * 100) / row[CLOSE]
    prediction = 1 if diff > 1 else -1 if diff < -1 else 0

    # current day
    for i in range(23):
        add_features_data(read_data(test_date, 22 - i))

    res = [prediction]
    for i in range(FEATURES):
        res = res + features_data[i]

    return res

def build(name, start_date, end_date):
    raw_data = []
    test_date = end_date
    while test_date > start_date:
        try:
            raw_data.append(build_one_test(test_date))
        except: 
            click.echo(f"Invalid date data {test_date}")
            pass
        test_date = test_date - timedelta(days=2)

    filename = f"{FOLDER}/{name}.csv"
    data = numpy.asarray(raw_data)
    numpy.savetxt(filename, data, delimiter="\t")
    return data

@click.command()
def build_tests():
    build("train", date(year=2017, month=8, day=18), date(year=2022, month=1, day=8))
    build("test", date(year=2023, month=3, day=24), date(year=2025, month=1, day=2))



            