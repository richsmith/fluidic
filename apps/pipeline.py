import os

from model.app import app
from model import iotypes
from control import access, parser, builder

@app(name = "pipeline",
     input = iotypes.Nothing,
     output = iotypes.Text,
     preferred_renderer = 'ol')
def execute(input, options, environment):
    # Shouldn't the input be a string of the command instead of the data
    # being passed as an option?

    command_str = " ".join(options)

    commands = parser.parse(command_str)
    pipeline = builder.create_pipeline(commands)

    output = []
    for command in pipeline.commands:
        output.append(describe(command))

    return output

def describe(command):
    description = command.app.name
    description += ' '
    description += str(command.options)
    return description
