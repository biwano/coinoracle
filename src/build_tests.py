
import click
from datetime import date, timedelta
from utils import DATA_FOLDER, read_data, CLOSE


FEATURES = 1
THRESHOLD = 0.97
FEATURES_SCALE = [100, 1]

def build_one_test(test_date, withPrediction = True):
    bases = []
    features_data = []

    def add_features_data(row):
        for i in range(FEATURES):
            value = ((row[i + 1] - bases[i]) * FEATURES_SCALE[i]) / bases[i]
            features_data[i].append(value)

    # init
    date_pointer = test_date - timedelta(days=1)
    row = read_data(date_pointer, 24)
    for i in range(FEATURES):
        bases.append(row[i + 1])
        features_data.append([])

    res = []
    if withPrediction:
        prediction_date = test_date
        prediction_row = read_data(prediction_date, 24)
        diff = ((prediction_row[CLOSE] - row[CLOSE]) * 100) / row[CLOSE]
        prediction = 2 if diff > THRESHOLD else 0 if diff < -THRESHOLD else 1
        res = [prediction]

    # current day
    for i in range(23):
        add_features_data(read_data(test_date, 23 - i))

    # last 16 days     
    """
    for i in range(14):
        date_pointer = date_pointer - timedelta(days=1)
        add_features_data(read_data(date_pointer, 24))

    # last 3 weeks        
    for i in range(14):
        date_pointer = date_pointer - timedelta(weeks=1)
        add_features_data(read_data(date_pointer, 24))

    # last 1 months        
    for i in range(6):
        date_pointer = date_pointer - timedelta(days=30)
        add_features_data(read_data(date_pointer, 24))
    """   

    
    for i in range(FEATURES):
        res = res + features_data[i]


    return res

def build(name, start_date, end_date):
    import numpy
    raw_data = []
    test_date = end_date
    categories = [0,0,0]
    while test_date >= start_date:
        try:
            res = build_one_test(test_date)
            prediction = res[0]
            raw_data.append(res)
            categories[prediction] = categories[prediction] + 1
        except Exception as e:  
            click.echo(f"Invalid date data {test_date}")
            print(e)
            pass
        test_date = test_date - timedelta(days=2)

    print(categories)
    filename = f"{DATA_FOLDER}/{name}.csv"
    data = numpy.asarray(raw_data)
    numpy.savetxt(filename, data, delimiter="\t")
    return data

@click.command()
def build_tests():
    build("train", date(year=2017, month=8, day=19), date(year=2022, month=1, day=9))
    build("test", date(year=2023, month=3, day=25), date(year=2025, month=1, day=3))



            