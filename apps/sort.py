import os

from model.app import app
from model import iotypes
from control import access
import operator

@app(name = "sort",
     input = iotypes.File,
     output = iotypes.File,
     autoserial = False)
def execute(input, options, environment):

    if (len(options) == 0):
        raise Exception("Need at least one field to sort on")
    if (len(options) > 1):
        raise Exception("Can't sort on more than field yet")

    field_str = options[0]

    output = sorted(input, key=lambda item: getattr(item, field_str))

    return output
