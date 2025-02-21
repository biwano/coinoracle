import click
from fetch import fetch 
from kaggle import kaggle_fetch, kaggle_transform
from build_tests import build_tests
from train import train
from predict import predict
from trade import trade
from stats import stats
from test import test

@click.group()
def cli():
    pass

cli.add_command(fetch)
cli.add_command(kaggle_fetch)
cli.add_command(kaggle_transform)
cli.add_command(build_tests)
cli.add_command(train)
cli.add_command(predict)
cli.add_command(trade)
cli.add_command(stats)
cli.add_command(test)

if __name__ == '__main__':
    cli()
    