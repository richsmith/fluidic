import glob

from model.app import app
from control import access, recognise_file
from model import iotypes
from util import globbing


@app(name = "file",
     input = (iotypes.Nothing, iotypes.File),
     output = iotypes.File,
     autoserial = None,
     preferred_renderer = 'show')
def execute(input, options, environment):

    files = []

    if (input != None and len(input) > 0):
        # check input is all files?
        files = input

    assert len(options) == 1    
    path = access.interpret_path(options[0])

    if globbing.is_glob_command(path):
        paths = expand_globs(path)
    else:
        paths = [path]

    for path in paths:
        files.append(recognise_file.create_file(path))

    return files


def expand_globs(path):
    return glob.iglob(path)
