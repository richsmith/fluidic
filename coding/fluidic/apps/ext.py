import os
import subprocess

from model.app import app
from model import iotypes

@app(name = "ext",
     input = iotypes.Text,
     output = iotypes.Text)
def execute(input, options, environment):

    assert len(options) >= 1
    command = options[0]

    options = options[1:]
    option_str = ""
    for option in options:
        option_str = option_str + " " + str(option)

    if options:
        proc = subprocess.Popen([command, option_str], stdout=subprocess.PIPE)
    else:
        proc = subprocess.Popen([command], stdout=subprocess.PIPE)

    stdout_value = proc.communicate()[0]
    #print "out: ", repr(stdout_value)

    return stdout_value
