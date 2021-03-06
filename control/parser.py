import os

from model import iotypes, pipeline, registry
from util import html, globbing
import processor, access, new_lexer


def parse(string):

    commands = []

    structured_tokens = new_lexer.lex(string)

    for token in structured_tokens:
        command_str, options = token
        command = get_command(command_str, options)
        commands.append(command)

    return commands


def get_command(command_str, options):
    assert command_str != None and options != None
    interpreters = \
        [check_for_null,
         check_for_text,
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
        return create_command('null', options)


def check_for_text(command_str, options):
    if command_str.startswith('"') and command_str.endswith('"'):
        options = [command_str[1:-1]]
        return create_command('literal', options)


def check_for_app(command_str, options):
    app = registry.get_app(command_str)
    if app:
        return pipeline.Command(app, options)


def check_for_external(command_str, options):
    if access.is_a_program(command_str):
        options.insert(0, command_str)
        return create_command('ext', options)


def check_for_file(command_str, options):
    path = access.interpret_path(command_str)
    
    if globbing.is_glob_command(path) or access.is_valid_path(path):
        assert options == [] # are we ever going to have options for a file?
        options = [path]
        return create_command('file', options)


def check_for_unknown(command_str, options):
    # if we get to this point we don't know what the user is requesting
    app = registry.get_app('unknown')
    options = [command_str]
    if app == None:
        raise Exception('App "Unknown" is missing')
    return pipeline.Command(app, options)

def create_command(app_name, options):
    app = registry.get_app(app_name)
    command = pipeline.Command(app, options)
    return command

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


