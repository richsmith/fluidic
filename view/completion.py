from control import parser, ui_interface

def get_super_commands(string):
    # all_commands = parser.get_all_available_commands()
    all_commands = ui_interface.get_all_completions(string)
    #print "all commands are " + str(all_commands) + " str is " + str(string)
    matching = filter(lambda c: c.startswith(string), all_commands)
    return matching

def complete(string):
    commands = get_super_commands(string)
    if len(commands) == 1:
        return commands[0]
    else:
        return get_longest_common_substring(commands)

def get_longest_common_substring(commands):
    substring = None

    for command in commands:
        if substring == None: # first command
            substring = command
        else:
            last_index = -1
            for i in range(min(len(substring), len(command))):
                if substring[i] == command[i]:
                    last_index = i
                else:
                    break
            
            if last_index == -1: # no common substring, so might as well bail
                return ''
            else:
                substring = substring[:last_index + 1]

    return substring
            
