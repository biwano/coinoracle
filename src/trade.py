import click
import requests
from fetch import fetch_
from predict import predict_

@click.command()
def trade():
    import numpy
    fetch_()
    click.echo("\n------------")
    prediction = predict_()
    click.echo(f"Prediction: {prediction}")

    max_index = numpy.array(prediction).argmax()
    direction = max_index.item() - 1
    direction = -1
    click.echo(f"Direction: {direction}")


    res = requests.post("http://ftxbot.ilponse.com/api/bots/btc/trade", json={
        "command": "apply_desired_direction",
        "desired_direction": direction
    })
    click.echo(f"Trader: {res.json()}")
    click.echo("------------\n")

