import os
import shutil

from control import access
from model.app import app
from model import iotypes

@app(name = 'copy',
     aliases = ['cp', '+>'],
     input = iotypes.File,
     output = iotypes.Nothing)
def execute(input, options, environment):

    source = get_source(input)
    destination = get_destination(options)

    fn = None

    if isinstance(input, iotypes.Directory):
        fn = shutil.copytree
    elif isinstance(input, iotypes.File):
        fn = shutil.copy2
    else:
        raise Exception("Attempted to copy an invalid object (not a file?)")

    fn(source, destination)

def get_source(input):
    source = input.path
    if not access.is_valid_path(source):
        raise Exception("Attempted to copy from an invalid path")
    return source


def get_destination(options):
    num_options = len(options)
    if (num_options == 0):
        raise Exception('No destination supplied for requested copy')
    elif (num_options > 1):
        raise Exception('Too many arguments for copy command')
    else:
        return options[0]
