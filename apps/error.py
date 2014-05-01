from model.app import app
from model import iotypes

@app(name = "error",
     input = iotypes.Nothing,
     output = iotypes.Html)
def execute(input, options, environment):
    # return '<div class="error">' + options[0] + '</div>'

    from control import output
    output.print_misc(options[0], 'error')
    return []
