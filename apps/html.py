import os

from model.app import app
from model import iotypes

# converts text to HTML

@app(name = 'html',
     input = iotypes.Text,
     output = iotypes.Html)
def execute(input, options, environment):

    output = None

    if input != None and input != '':
        output = "<pre>" + input + "</pre>"

    return output
        

