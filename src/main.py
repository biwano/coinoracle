import click
from fetch import fetch 

@click.group()
def cli():
    pass

cli.add_command(fetch)

if __name__ == '__main__':
    cli()