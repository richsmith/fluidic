import os
import shutil

from control import access
from model.app import app
from model import iotypes

@app(name = 'remove',
     aliases = ['rm'],
     input = iotypes.File,
     output = iotypes.Nothing)
def execute(input, options, environment):

    source = get_source(input)

    fn = None

    if isinstance(input, iotypes.Directory):
        fn = shutil.rmtree
    elif isinstance(input, iotypes.File):
        fn = os.remove
    else:
        raise Exception("Attempted to delete an invalid object (not a file?)")

    fn(input.path)



def get_source(input):
    source = input.path
    if not access.is_valid_path(source):
        raise Exception("Attempted to delete an invalid path")
    return source
