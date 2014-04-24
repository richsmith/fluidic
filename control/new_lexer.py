#!/usr/bin/env python

import re

regex = """
        (?P<command>[\w\.]+)    # command; any contiguous alphanumeric or .
        \s*                     # optional whitespace
        (\((?P<options>.*?)\))? # options delimited by () may be present
        \s*                     # optional whitespace
    """
pattern = re.compile(regex, re.VERBOSE)

def lex(text):
    # one day we may need a proper grammar

    check_brackets(text)

    commands = []

    for match in re.finditer(pattern, text):
        command = match.group('command')
        # print "command_str = " + str(match.group('command'))
        option_str = match.group('options')
        options = option_str.split() if option_str else []
        # print "options are " + str(options)
        chunk = command, options
        commands.append(chunk)

    print str(commands)
    return commands

def check_brackets(text):
    open_bracket = False
    for char in text:
        if char == '(':
            if open_bracket:
                raise SyntaxError('open bracket found inside open bracket')
            else:
                open_bracket = True
        elif char == ')':
            if open_bracket:
                open_bracket = False
            else:
                raise SyntaxError('close bracket found without an open bracket')

    if open_bracket:
        raise SyntaxError('open bracket not closed')

    

if __name__ == '__main__':
    new_lexer("foo()()()")
