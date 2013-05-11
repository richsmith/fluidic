#!/usr/bin/env python

# p = re.compile('\S+\s*(\(.*?\)){0,1}')
# m = p.match('foo (a b) bar')

import re

def new_lexer(string):
    # one day we may need a proper grammar

    check_brackets(string)

    regex = """
        (?P<command>\w+)        # command; any contiguous non-whitespace
        \s*                     # optional whitespace
        (\((?P<options>.*?)\))? # options delimited by () may be present
        \s*                     # optional whitespace
    """

    pattern = re.compile(regex, re.VERBOSE)

    text = 'foo(a b) bar'
    #matches = pattern.findall()

    commands = []

    for match in re.finditer(pattern, text):
        #match.group(0) # gives foo (a b)
        command = match.group('command')
        print "command_str = " + str(match.group('command'))
        option_str = match.group('options')
        options = option_str.split() if option_str else []
        print "options are " + str(options)
        chunk = command, options
        commands.append(chunk)

    print str(commands)

def check_brackets(string):
    open_bracket = False
    for char in string:
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

        
    

def create_command(string):
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
