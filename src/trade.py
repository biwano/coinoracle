import click
from fetch import fetch_
from predict import predict_
import requests

@click.command()
def trade():
    import numpy
    fetch_()
    prediction = predict_()
    max_index = numpy.array(prediction).argmax()
    direction = max_index.item() - 1
    direction = -1

    res = requests.post("http://ftxbot.ilponse.com/api/bots/btc/trade", json={
        "command": "apply_desired_direction",
        "desired_direction": direction
    })
    click.echo(res.json())

