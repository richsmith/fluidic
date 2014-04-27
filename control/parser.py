import os

from model import iotypes, pipeline, registry
from util import html, globbing
import processor, access, new_lexer


def create_pipeline(string):
    
    new_pipeline = pipeline.Pipeline()

    structured_tokens = new_lexer.lex(string)

    for token in structured_tokens:
        command_str, options = token
        command = get_command(command_str, options)
        new_pipeline.add(command)

    # print new_pipeline.describe()
    ensure_pipeline_starts(new_pipeline)
    ensure_pipeline_terminates(new_pipeline)

    return new_pipeline


def ensure_pipeline_starts(pipeline):
    if not starts_with_valid_command(pipeline):
        intelligently_add_start(pipeline)


def ensure_pipeline_terminates(pipeline):
    if not ends_in_valid_renderer(pipeline):
        intelligently_add_renderer(pipeline)


def starts_with_valid_command(pipeline):
    first_app = pipeline.commands[0].app
    return first_app.can_take(iotypes.Nothing)


def ends_in_valid_renderer(pipeline):
    return pipeline.output in [None, iotypes.Nothing, iotypes.Html]


def get_command(command_str, options):
    assert command_str != None and options != None
    interpreters = \
        [check_for_null,
         check_for_app,
         check_for_external,
         check_for_file,
         check_for_unknown]
    
    for interpreter in interpreters:
        command = interpreter(command_str, options)
        if command:
            return command

    # shouldn't get here
    raise Error(command_str + " not found")
    

def check_for_null(command_str, options):
    if command_str == '':
        assert options == []
        app = registry.get_app("null")
        return pipeline.Command(app, options)

def check_for_app(command_str, options):
    app = registry.get_app(command_str)
    if app:
        return pipeline.Command(app, options)

def check_for_external(command_str, options):
    if access.is_a_program(command_str):
        app = registry.get_app("ext")
        options.insert(0, command_str)
        return pipeline.Command(app, options)

def check_for_file(command_str, options):
    path = access.interpret_path(command_str)
    
    if globbing.is_glob_command(path) or access.is_valid_path(path):
        assert options == [] # are we ever going to have options for a file?
        app = registry.get_app("file")
        options = [path]
        return pipeline.Command(app, options)

def check_for_unknown(command_str, options):
    # if we get to this point we don't know what the user is requesting
    app = registry.get_app("unknown")
    options = [command_str]
    if app == None:
        raise Exception('App "Unknown" is missing')
    return pipeline.Command(app, options)


def intelligently_add_renderer(new_pipeline):

    # if pipeline.output == iotypes.Directory:
    #     app = registry.get_app('go')
    if new_pipeline.preferred_renderer != None:
        app = registry.get_app(new_pipeline.preferred_renderer)
        if app == None:
            raise Exception('Preferred renderer ' + \
                            str(new_pipeline.preferred_renderer) + ' not found')
    elif new_pipeline.output == iotypes.Text:
        app = registry.get_app('html')
    elif new_pipeline.output == iotypes.File:
        app = registry.get_app('grid')
    else:
        raise Exception("Unexpected typing error; please check the code")

    renderer = pipeline.Command(app, [None])
    new_pipeline.add(renderer)


def intelligently_add_start(new_pipeline):

    if new_pipeline.input == iotypes.File:
        app = registry.get_app('file')
        command = pipeline.Command(app, [os.getcwd()])
        new_pipeline.add_to_start(command)
    else:
        raise Exception(
            "Not sure how to wire up an input of " + str(new_pipeline.input))


def parse_command(string):
    string = string.strip()
    words = string.split()
    
    if len(words) == 0:
        command = ''
    else:
        command = words[0]

    if len(words) > 1:
        args = words[1:]
    else:
        args = []

    return command, args


