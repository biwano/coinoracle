import click

from utils import DATA_FOLDER


@click.command()
def test():
    import numpy as np
    import keras


    def readucr(filename):
        data = np.loadtxt(filename, delimiter="\t")
        y = data[:, 0]
        x = data[:, 1:]
        return x, y.astype(int)

    x_test, y_test = readucr(f"{DATA_FOLDER}/test.csv")
    x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], 1))

    model = keras.saving.load_model(f"{DATA_FOLDER}/model.keras")
    model.evaluate(x_test, y_test, verbose=1)

