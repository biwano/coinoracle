from datetime import date
import click
import keras
from build_tests import build_one_test
import numpy


@click.command()
def predict():
    model = keras.saving.load_model("../data/model.keras", custom_objects=None, compile=True, safe_mode=True)
    data = [build_one_test(date.today(), withPrediction=False)]
    data = numpy.asarray(data, dtype=int)
    print(data.shape)

    data = data.reshape((data.shape[0], data.shape[1], 1))
    print(data.shape)

    res = model.predict(data)

    print(res)

