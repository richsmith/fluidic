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
        files.append(file)
        root_path = file.path
        if isinstance(file, iotypes.Directory):
            to_add = get_files_in(file.path)
            for sub_file in to_add:
                files.append(sub_file)

    return files


def get_files_in(root_path):
    files = []
    for root, sub_dirs, filenames in os.walk(root_path):
        for filename in filenames:
            path = os.path.join(root, filename)
            #yield iotypes.File()
            file_object = file.execute(None, [path], None)[0]
            files.append(file_object)

    return files
