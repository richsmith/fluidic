import os

from model.app import app
from model import iotypes
from control import access

@app(name = "read",
     input = iotypes.File,
     output = iotypes.Text)
def execute(input, options, environment):

    return access.read_file(input.path)
