import os

from model.app import app
from model import iotypes

@app(name = "error",
     input = None,
     output = iotypes.Html)
def execute(input, options, environment):
    return '<div class="error">' + options[0] + '</div>'
