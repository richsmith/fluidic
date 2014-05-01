import os
from model import pipeline, iotypes, registry
import access, parser

def create_pipeline(commands):
    
    new_pipeline = pipeline.Pipeline()

    for command in commands:
         new_pipeline.add(command)

    apply_special_pipeline_rules(new_pipeline)
    ensure_pipeline_starts(new_pipeline)
    ensure_pipeline_terminates(new_pipeline)

    return new_pipeline


def apply_special_pipeline_rules(pipeline):
    check_for_navigation(pipeline)


def check_for_navigation(pipeline):
    if pipeline.output == iotypes.File and len(pipeline.commands) == 1\
            and command_refers_to_dir(pipeline.commands[0]):
        go_command = parser.get_command('go', [])
        pipeline.add(go_command) 
        ls_command = parser.get_command('ls', [])
        pipeline.add(ls_command) 


def command_refers_to_dir(command):
    options = command.options
    if len(options) == 1:
        option = options[0]
        path = access.interpret_path(option)
        if access.is_accessible_directory(path):
            return True
    return False
        

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
        print new_pipeline.describe()
        raise Exception(
            "Not sure how to wire up an input of type " + 
            str(new_pipeline.input.__name__))
