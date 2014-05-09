import os
import shutil

from model.app import app
from model import iotypes

@app(name = 'append',
     aliases = ['>>'],
     input = iotypes.Text,
     output = None)
def execute(input, options, environment):

    destination = options[0]

    with open(destination, 'a') as f:
        f.write(input)
        

