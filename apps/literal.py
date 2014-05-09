from model.app import app
from model import iotypes

@app(name = "literal",
     input = iotypes.Nothing,
     output = iotypes.Text)
def execute(input, options, environment):

    assert len(options) == 1
    return str(options[0])
