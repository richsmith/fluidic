import os

from model.app import app
from model import iotypes
from control import access

@app(name = "pipeline",
     input = None,
     output = iotypes.Html)
def execute(input, options, environment):

    command_str = " ".join(options)
    return "This command disabled until the new syntax is worked out"
