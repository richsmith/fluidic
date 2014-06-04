import re

from model.app import app
from model import iotypes

@app(name = 'drop',
     aliases = ['-'],
     input = iotypes.File,
     output = iotypes.File,
     autoserial = False)
def execute(input, options, environment):
    to_keep = input
    for filter in options:
        to_keep = process_filter(filter, to_keep)
    return to_keep


def process_filter(filter, files):
    to_keep = []

    for file in files:
        print 'checking file ' + file.name
        if not matches(filter, file):
            print 'does not match'
            to_keep.append(file)

    return to_keep
        
    
def matches(filter, file):
    pattern = re.compile(filter, re.VERBOSE)
    return re.match(pattern, file.name)
        
        
