import os
import shutil

from model.app import app
from model import iotypes

@app(name = 'move',
     aliases = ['mv', '->'],
     input = iotypes.File,
     output = None)
def execute(input, options, environment):

    source = input.path
    destination = get_destination(options)

    os.rename(source, destination)


def get_destination(options):
    num_options = len(options)
    if (num_options == 0):
        raise Exception('No destination supplied for requested move')
    elif (num_options > 1):
        raise Exception('Too many arguments for move command')
    else:
        return options[0]
