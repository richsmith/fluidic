import model.environment
import parser, builder
import access

import apps.unknown
import apps.grid, apps.table
import apps.ls, apps.go, apps.properties, apps.recurse
import apps.sort, apps.reverse, apps.keep, apps.drop
import apps.history, apps.version, apps.show
import apps.error, apps.ext, apps.exit
import apps.read, apps.text, apps.html
import apps.ol
import apps.null, apps.file
import apps.clear
import apps.about, apps.suggest

#debugging
import apps.pipeline
import traceback

global environment
environment = model.environment.Environment()
environment.history = access.read_history()

def enter(string):
    assert string != None
    record_command_if_needed(environment, string)
    return process(string)

def process(string):
    try:
        commands = parser.parse(string)
        pipeline = builder.create_pipeline(commands)
        output = pipeline.execute(environment)
    except Exception as error:
        message = str(error)
        output = apps.error.execute(None, [message], None)
        traceback.print_exc()
    return output


def record_command_if_needed(environment, command):
    history = environment.history
    if (should_record_comand(history, command)):
        record_command(history, command)

def should_record_comand(history, command):
    return not is_command_repeat(history, command) and command != ""
        
def is_command_repeat(history, command):
    return len(history) > 0 and history[-1] == command

def record_command(history, command):
    max_history = 50 # TODO put this somewhere appropriate
    while len(history) >= max_history:
        del history[0]
    history.append(command)
    access.write_history(history)

