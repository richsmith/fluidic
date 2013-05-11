import os

from model.app import app
from model import iotypes
from control import output

@app(name = "clear",
     input = iotypes.Nothing,
     output = iotypes.Nothing)
def execute(input, options, environment):

    assert len(options) == 0

    output.clear()

    




