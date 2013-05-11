glob_chars = set(["*", "?"])

def is_glob_command(string):
    return set(string).intersection(glob_chars) != set([])
