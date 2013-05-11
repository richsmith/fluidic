import os
import model.iotypes

def interpret_path(path):
    """Transforms a user-supplied path into a form Fluidic can work with."""
    path = os.path.expanduser(path)
    path = os.path.abspath(path)
    return path

def is_valid_path(path):
    return os.path.exists(path)
    

def path_to_url(path):
    return "file://" + path

def is_accessible_directory(path):
    return os.path.isdir(path) and os.path.exists(path)


def is_a_program(command):

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(command)
    if fpath:
        if is_exe(command):
            return True
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, command)
            if is_exe(exe_file):
                return True

    return False



def write_history(history):
    history_text = '\n'.join(history)
    write_config_file('history', history_text)

def read_history():
    try:
        history_text = read_config_file('history')
        return history_text.split('\n')
    except:
        return []

def read_file(path):
    contents = ''
    with open(path, 'r') as f:
        contents = f.read()
    return contents

def write_file(path, text):
    with open(path, 'w') as f:
        f.writelines(text)


def write_config_file(name, text):
    path = get_config_path(name)
    write_file(path, text)

def read_config_file(name):
    path = get_config_path(name)
    return read_file(path)

def get_config_path(name):
    path = os.path.join(get_config_directory(), name)
    return path

def get_config_directory():
    home = os.path.expanduser("~")
    
    candidate = os.path.join(home, '.config', 'fluidic')
    if is_accessible_directory(candidate):
        return candidate
    else:
        os.makedirs(candidate)
        return candidate



def read_resource(name):
    path = get_resource_path(name)
    return read_file(path)

def get_resource_path(name):
    return os.path.join(get_abs_base_dir_path(), 'resources', name)


def get_abs_base_dir_path():
    return '/home/rls/coding/fluidic/'
