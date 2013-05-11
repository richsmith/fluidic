import os

from model.app import app
from model import iotypes
from control import access

@app(name = "reverse",
     input = iotypes.File, #or anything
     output = iotypes.File, #or same (specify?)
     autoserial = False) 
def execute(input, options, environment):
    output = input # need to make defensive copy?
    output.reverse()
    return output
