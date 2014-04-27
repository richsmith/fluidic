import os

from model.app import app
from model import iotypes

@app(name = "null",
     input = iotypes.Any,
     output = iotypes.Nothing)
def execute(input, options, environment):
    return 




