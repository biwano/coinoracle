
import numpy
import os
import click

FOLDER = "../data"

def load_data(date):
    filename = f"{FOLDER}/{date.year:04}-{date.month:02}-{date.day:02}.csv"
    click.echo(f"Reading {filename} {date}")
    
    if os.path.isfile(filename):
        data = numpy.loadtxt(filename, delimiter="\t")
        return data


def save_data(date, raw_data):
    filename = f"{FOLDER}/{date.year:04}-{date.month:02}-{date.day:02}.csv"
    data = numpy.asarray(raw_data)
    numpy.savetxt(filename, data, delimiter="\t")
    return data
