import os

from model.app import app
from model import iotypes
from control import access
from util import html

@app(name = 'go',
     aliases = ['cd'],
     input = iotypes.Directory,
     output = iotypes.Nothing)
def execute(input, options, environment):

    assert len(options) == 0 or len(options) == 1

    if input != None:

        assert isinstance(input, iotypes.Directory)
        path = input.path
    elif len(options) != 0:
        path = access.interpret_path(options[0])
    else:
        path = access.interpret_path("~")
        
    if not os.path.exists(path):
        raise IOError(html.strong(path) + ' is not accessible')
    elif not os.path.isdir(path):
        raise IOError(html.strong(path) + ' is not a directory')
    else:
        try:
            os.chdir(path)
        except Exception as error:
            raise IOError("Can't move to " + html.strong(path) + \
                "; error is:" + html.br() + str(error))




