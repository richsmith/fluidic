import os
from model.app import app
from model import iotypes

from util.html import *

import grid

# Renderer that describes a list of files as an html table view

@app(name = "table",
     input = iotypes.File,
     output = iotypes.Html,
     autoserial = False)
def execute(files, options, environment):

    # check input is a list of files

    output = thead(th('') + th('Name') + th('Size') + \
                   th('Type') + th('Modified'))
    for file in files:
        output += describe_file(file)

    return table(output)

def describe_file(file):
    description = td(grid.get_icon_html(file))
    description += td(file.name)
    description += td(file.describe_size())
    description += td(file.describe_type())
    description += td(file.describe_modified())
    return tr(description)

def table(string):
    return tag('table', string)

def td(string):
    return tag('td', string)

def tr(string):
    return tag('tr', string)

def tag(name, string):
    return "<" + name + ">" + string + "</" + name + ">"



