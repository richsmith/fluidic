import os
from model import registry
from control import access

def get_all_completions(fragment):

    all_app_names = [app.name for app in registry.get_all_apps()]
    app_completions = filter(lambda c: c.startswith(fragment), all_app_names)

    file_completions = get_file_superstrings(fragment)

    completions = app_completions + file_completions

    return completions



def get_file_superstrings(substring):

    quoted_directory, fragment = os.path.split(substring)
    absolute_directory = access.interpret_path(quoted_directory) 

    superstrings = []

    for filename in os.listdir(absolute_directory):
        if filename.startswith(fragment):
            candidate = os.path.join(absolute_directory, filename)
            if os.path.isdir(candidate):
                filename += os.sep # add separator to directories
            superstrings.append(os.path.join(quoted_directory, filename))

    #superstrings = filter(lambda f:f.startswith(fragment), filenames)
    return superstrings



