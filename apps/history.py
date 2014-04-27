import os

from model.app import app
from model import iotypes

@app(name = 'history',
     input = iotypes.Nothing,
     output = iotypes.Text,
     preferred_renderer = 'ol',
     autoserial = False)
def execute(input, options, environment):
    return environment.history

