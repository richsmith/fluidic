import traceback

import model.environment
import parser, builder, access
import apps


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

