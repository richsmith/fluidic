import os

from model.app import app
from model import iotypes
from apps import file

@app(name = "recurse",
     input = iotypes.File,
     output = iotypes.File,
     autoserial = False)
def execute(input, options, environment):

    files = []

    for file in input:
        path = file.path
        to_add = get_files_in(path)
        for new_file in to_add:
            files.append(new_file)

    return files


def get_files_in(root_path):

    files = []

    def add_file(path):
        file_object = get_file(path)
        files.append(file_object)

    add_file(root_path)

    for root, dirs, filenames in os.walk(root_path):

        for dir in dirs:
            path = os.path.join(root, dir)
            add_file(path)

        for filename in filenames:
            path = os.path.join(root, filename)
            add_file(path)

    return files


def get_file(path):
    return file.execute(None, [path], None)[0]
