import os

from model.app import app
from model import iotypes
from control import output, html

# takes a directory(? or files??) and outputs files (filtered)

@app(name = "welcome",
     input = iotypes.Nothing,
     output = iotypes.Html)
def execute(input, options, environment):

    output.print_misc(get_message(), 'command')


def get_message():
    return '<h1>Fluidic</h1><h2>Rethinking the Shell</h2>'


