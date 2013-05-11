from model.app import app
from model import iotypes
from control import access

import pygments
from pygments import lexers
from pygments import formatters

#style = 'vs'
style = 'default'

@app(name = "highlight",
     input = iotypes.File,
     output = iotypes.Html)
def execute(input, options, environment):

    lexer = None
    #try :
    #lexer = lexers.get_lexer_for_mimetype(options[0])
    lexer = lexers.get_lexer_for_filename(input.name)
    # print "lexer is " + str(lexer)
    #except:
        #lexer = lexers.guess_lexer(input)

    #print "lexer is " + str(lexer)


    text = access.read_file(input.path)

    return highlight(lexer, text)


def highlight(lexer, text):
    formatter = formatters.HtmlFormatter(style=style)
    formatter.noclasses = True # generate styles inline (for now at least)

    return pygments.highlight(text, lexer, formatter)
