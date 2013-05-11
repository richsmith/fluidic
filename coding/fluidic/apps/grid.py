import os
from model.app import app
from model import iotypes

from control import icon
from util import html
# Renderer that describes a list of files as an html grid view

@app(name = "grid",
     input = iotypes.File,
     output = iotypes.Html,
     autoserial = False)
def execute(files, options, environment):
    output = ""
    for file in files:
        output += describe_file(file)

    return [output]

def describe_file(file):
    content = get_icon_html(file) + ' ' + file.name
    output = html.span(content, clazz="fileBox", title=file.get_tooltip())
    return output

def get_icon_html(file):
    return html.img(src='file://' + icon.get_icon_path_for_file(file))

