import os

from model.app import app
from model import iotypes
from control import output

@app(name = "version",
     input = iotypes.Nothing,
     output = iotypes.Html)
def execute(input, options, environment):
    import fluidic # FIXME put at top without breaking
    version = fluidic.version
    name = fluidic.name
    banner = '<div class="banner"> ' + name + ' v' + version + '</div>'
    output.print_misc(banner, 'banner')
