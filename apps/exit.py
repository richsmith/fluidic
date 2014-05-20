import sys
import control
from model import iotypes
from model.app import app


@app(name = "exit",
     input = iotypes.Nothing,
     output = iotypes.Nothing)
def execute(files, options, environment):
    control.output.clear()
    sys.exit(0)




