import sys
from model.app import app

@app(name = "exit",
     input = None,
     output = None)
def execute(files, options, environment):
    sys.exit(0)




