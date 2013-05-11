from model.app import app
from model import iotypes

from util import html

@app(name = 'ol',
     input = iotypes.Any,
     output = iotypes.Html,
     autoserial = False)
def execute(input, options, environment):

    assert isinstance(input, list)

    output = ""
    for item in input:
        output += html.li(item) + "\n"
    output = html.ol(output)
    return [output]
