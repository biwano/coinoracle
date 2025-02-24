import click

from utils import DATA_FOLDER

def predict_():
    from datetime import date
    import keras
    from build_tests import build_one_test
    import numpy

    model = keras.saving.load_model(f"{DATA_FOLDER}/model.keras", custom_objects=None, compile=True, safe_mode=True)
    data = [build_one_test(date.today(), withPrediction=False)]
    data = numpy.asarray(data, dtype=int)
    data = data.reshape((data.shape[0], data.shape[1], 1))
    res = model.predict(data, verbose=None)

    return res

@click.command()
def predict():
    res = predict_()
    click.echo(res)
    return res
    

