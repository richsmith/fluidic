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
    assert len(options) > 0

    #assume only sorting on one field for now
    assert len(options) == 1

    field_str = options[0]

    print "executing sort for input len " + str(len(input))

    input.sort(key=lambda item: getattr(item, field_str))

    print "input now len " + str(len(input))


    return input
