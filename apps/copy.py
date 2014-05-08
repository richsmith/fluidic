import os
import shutil

from model.app import app
from model import iotypes

@app(name = 'copy',
     aliases = ['cp', '+>'],
     input = iotypes.File,
     output = None)
def execute(input, options, environment):

    source = input.path
    destination = get_destination(options)

    shutil.copy2(source, destination)


def get_destination(options):
    num_options = len(options)
    if (num_options == 0):
        raise Exception('No destination supplied for requested copy')
    elif (num_options > 1):
        raise Exception('Too many arguments for copy command')
    else:
        return options[0]
