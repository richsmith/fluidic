import os

from model.app import app
from model import iotypes
from control import access

@app(name = "text",
     input = iotypes.Any,
     output = iotypes.Text,
     autoserial = False)
def execute(input, options, environment):

    assert isinstance(input, list)

    output = ""
    for item in input:
        output += str(item) + "\n"
    return [output]
