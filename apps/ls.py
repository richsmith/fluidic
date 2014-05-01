import os

from model.app import app
from model import iotypes
from apps import sort

@app(name = "ls",
     input = iotypes.File, # eventually, files or dir
     output = iotypes.File, # outputs filtered files
     preferred_renderer = 'grid')
def execute(input, options, environment):

    if input == None:
        input = os.getcwd()
        filenames = os.listdir(input)
    else:
        filenames = os.listdir(input.path)

    filenames = get_visible_files(filenames)

    files = []
    for filename in filenames:

        path = os.path.abspath(filename)
        if os.path.isdir(filename):
            files.append(iotypes.Directory(path))
        else:
            files.append(iotypes.File(path))

    files = default_sort(files)

    return files


def get_visible_files(filenames):
    return filter(is_visible, filenames)

def is_visible(name):
    return not (is_hidden(name) or is_archive(name))

def is_hidden(name):
    return name.startswith('.')

def is_archive(name):
    return name.endswith('~')

def default_sort(files):
    return sort.execute(files, ['name'], None)
