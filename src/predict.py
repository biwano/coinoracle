import click

def predict_():
    from datetime import date
    import keras
    from build_tests import build_one_test
    import numpy

    model = keras.saving.load_model("../data/model.keras", custom_objects=None, compile=True, safe_mode=True)
    data = [build_one_test(date.today(), withPrediction=False)]
    data = numpy.asarray(data, dtype=int)
    data = data.reshape((data.shape[0], data.shape[1], 1))
    res = model.predict(data)

    click.echo(res)
   
    return res

@click.command()
def predict():
    return predict_()
    

