import os

from model.app import app
from model import iotypes

# converts text to Html

@app(name = "html",
     input = iotypes.Text,
     output = iotypes.Html)
def execute(input, options, environment):
    output = "<pre>"
    for line in input:
        output = output + line
    output = output + "</pre>"
    print "output = " + str(output)
    return output
        

