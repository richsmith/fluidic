import os

from model.app import app
from model import iotypes

@app(name = "null",
     input = iotypes.Any,
     output = None)
def execute(input, options, environment):
    return 




