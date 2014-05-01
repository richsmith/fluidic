from model.app import app
from model import iotypes

import properties
from control import access, mime, icon
from util import html
import highlight

@app(name = "show",
     input = iotypes.File,
     output = iotypes.Html)
def execute(input, options, environment):

    def interpret(input):
        if isinstance(input, iotypes.File):
            return input
        else:
            return iotypes.File(input)
        
    if input:
        #assert len(options) == 0
        file = interpret(input)
    else:
        #assert len(options) == 1
        file = interpret(options[0])

    if isinstance(file, iotypes.Directory):
        return show_directory(file)
    elif icon.is_thumbnailable(file):
        output = show_image(file)
    elif isinstance(file, iotypes.CodeFile):
        output = html.div(get_highlight(file), clazz='text')
    else: # else assume text file for now
        output = html.div(show_text(file), clazz='text')

    return html.div(output, clazz='show')

def show_image(file):
    url = access.path_to_url(file.path)
    return html.img(src=url)


def show_text(file):
    content = access.read_file(file.path)
    content = content.replace('\n', '<br />')
    return content

def show_code(file):
    #return html.div(access.read_file(file), clazz='show')
    return hilight(file)

def show_directory(file):
    return properties.execute(file, [], None)


def get_highlight(file):
    #return highlight.execute(access.read_file(file), [file.mime], None)
    return highlight.execute(file, [], None)
