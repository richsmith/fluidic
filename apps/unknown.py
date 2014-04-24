import os

from model.app import app
from model import iotypes

@app(name = "unknown",
     input = iotypes.Any,
     output = iotypes.Text)
def execute(input, options, environment):
    if len(options) == 1:
        raise Exception('Unknown command "' + options[0] + '"')
    else:
        raise Exception('Problem calling error reporting app "Unknown"')
