from model.app import app
from model import iotypes
from control import output, access

@app(name = "welcome",
     input = iotypes.Nothing,
     output = iotypes.Html)
def execute(input, options, environment):

    output.print_misc(get_message(), 'banner')


def get_message():
    return access.read_resource('welcome')


