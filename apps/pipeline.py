import os

from model.app import app
from model import iotypes
from control import access, parser

@app(name = "pipeline",
     input = None,
     output = iotypes.Text,
     preferred_renderer = 'ol')
def execute(input, options, environment):

    command_str = " ".join(options)
    pipeline = parser.create_pipeline(command_str)

    output = []
    for command in pipeline.commands:
        output.append(describe(command))

    return output
    #return "This command disabled until the new syntax is worked out"

def describe(command):
    description = command.app.name
    description += ' '
    description += str(command.options)
    return description
