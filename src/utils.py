
import numpy
import os
import click

FOLDER = "../data"

data_cache = {}

TIMESTAMP = 0
CLOSE = 1
VOLUME = 1

def load_data(date):
    slug = f"{date.year:04}-{date.month:02}-{date.day:02}"
    filename = f"{FOLDER}/{slug}.csv"
    if slug in data_cache:
        return data_cache[slug]
    
    click.echo(f"Reading {filename} {date}")
    
    if os.path.isfile(filename):
        data = numpy.loadtxt(filename, delimiter="\t")
        data_cache[slug] = data
        return data


def save_data(date, raw_data):
    filename = f"{FOLDER}/{date.year:04}-{date.month:02}-{date.day:02}.csv"
    data = numpy.asarray(raw_data)
    numpy.savetxt(filename, data, delimiter="\t")
    return data

def read_data(date, hour):
    data = load_data(date)
    return data[hour]