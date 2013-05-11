import os

from model.app import app
from model import iotypes
from control import access

@app(name = "read",
     input = iotypes.File,
     output = iotypes.Text)
def execute(input, options, environment):
    assert len(options) == 0

    path = access.interpret_path(options[0])
    if access.is_valid_path(path):
        url = access.path_to_url(path)
        print "url is " + url
        return '<div class="show"><img src="' + url + '"/></div>'
    else:
        raise RuntimeError("Not valid " + options[0])
