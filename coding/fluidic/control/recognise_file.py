from control import access, mime
from model import iotypes

def create_file(path):
    # fixme
    # this will need a better system for instantiating file types
    # perhaps do this polymorphically?
    # probably want to use python magic

    file = iotypes.File(path) # default: everything's a file

    if (is_directory(file)):
        file = iotypes.Directory(file.path)
    elif (is_code_file(file)):
        file = iotypes.CodeFile(file.path)
    elif (is_image_file(file)):
        file = iotypes.ImageFile(file.path)

    return file

def is_directory(file):
    return access.is_accessible_directory(file.path)

def is_code_file(file):
    minor = mime.get_minor_mime_part(file.mime)

    # a bit horrible so far...
    return minor in ['x-python', 'x-java'] \
        or file.extension in ['.java', '.py', '.lisp', '.c', '.html', '.xml']
    # (files with markup are essentially code files for our purposes)


def is_image_file(file):
    major = mime.get_major_mime_part(file.mime)
    return major == 'image'
