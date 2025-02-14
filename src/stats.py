import click
import requests

@click.command()
def stats():
    res = requests.get("http://ftxbot.ilponse.com/api/bots/btc/stats")
    try:
        data = res.json()["result"]["btc"]
        click.echo(f"|\tdirection\t|\tprice\t|")
        click.echo(f"|\t{round(data['direction'])}\t\t|\t{round(data['price'])}\t|")
    except:
        click.echo(f"Error status: {res.status_code}")


