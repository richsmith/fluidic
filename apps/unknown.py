import os

from model.app import app
from model import iotypes

@app(name = "unknown",
     input = iotypes.Any,
     output = iotypes.Text)
def execute(input, options, environment):
    raise Error("Unknown command")
