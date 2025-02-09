import click
from fetch import fetch 
from kaggle import kaggle_fetch, kaggle_transform
from build_tests import build_tests

@click.group()
def cli():
    pass

cli.add_command(fetch)
cli.add_command(kaggle_fetch)
cli.add_command(kaggle_transform)
cli.add_command(build_tests)

if __name__ == '__main__':
    cli()