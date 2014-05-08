import os
import shutil

from model.app import app
from model import iotypes

@app(name = 'write',
     aliases = ['>'],
     input = iotypes.Text,
     output = None)
def execute(input, options, environment):

    print "Would have written to " + options[0]



