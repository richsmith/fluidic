from model import iotypes, pipeline, registry
from util import html, globbing
import processor, access, new_lexer

# def old_get_pipeline(string):
    
#     new_pipeline = pipeline.Pipeline()

#     tokens = tokenise(string)

#     for token in tokens:
#         command = process_token(token)
#         new_pipeline.add(command)

#     ensure_pipeline_terminates(new_pipeline)
    
#     print new_pipeline.describe()

#     return new_pipeline



def create_pipeline(string):
    
    new_pipeline = pipeline.Pipeline()

    structured_tokens = new_lexer.lex(string)
    print 'structured tokens: ' + str(structured_tokens)

    for token in structured_tokens:
        print "handling token " + str(token)
        command_str, options = token
        command = get_command(command_str, options)
        print "about to add command " + str(command)
        new_pipeline.add(command)

    print new_pipeline.describe()

    ensure_pipeline_terminates(new_pipeline)

    return new_pipeline


def ensure_pipeline_terminates(pipeline):
    if not ends_in_valid_renderer(pipeline):
        intelligently_add_renderer(pipeline)

def ends_in_valid_renderer(pipeline):
    return pipeline.output in [None, iotypes.Nothing, iotypes.Html]

# def old_process_token(part):
#     command_str, args = parse_command(part)
#     assert command_str != None
#     assert args != None
#     command = get_command(command_str, args)
#     if not command:
#         message = "Command " + html.strong(str(command_str)) + \
#             " not understood"
#         raise Exception(message)

#     return command


def get_command(command_str, options):
    assert command_str != None and options != None
    interpreters = \
        [check_for_null,
         check_for_app,
         check_for_external,
         #check_for_directory,
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

# def check_for_directory(command_str, options):
#     # making this into a go command is a temporary hack;
#     # maybe we should probably go to a dir if it is output at the end?
#     if access.is_accessible_directory(command_str):
#         app = registry.get_app("go")
#         options = [command_str]
#         return pipeline.Command(app, options)
       
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
    # elif new_pipeline.output == iotypes.ListOfFiles:
    #     app = registry.get_app("grid")
    else:
        raise Exception("Unexpected typing error; please check the code")

    print "app is " + str(app)

    renderer = pipeline.Command(app, [None])
    new_pipeline.add(renderer)


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




def tokenise(string):
    string = string.strip()
    commands = string.split("|")
    return commands


