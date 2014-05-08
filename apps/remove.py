import os
import shutil

from model.app import app
from model import iotypes

@app(name = 'remove',
     aliases = ['rm'],
     input = iotypes.File,
     output = None)
def execute(input, options, environment):

    print "Would have deleted " + str(input.path)

    # os.remove(input.path)
    # os.removedirs(input.path)
