import os
import subprocess

from model.app import app
from model import iotypes

@app(name = "ext",
     input = [iotypes.Nothing, iotypes.Text],
     output = iotypes.Text)
def execute(input, options, environment):

    assert len(options) >= 1
    command = options[0]

    options = options[1:]

    option_str = " ".join(options)

    if options:
        proc = subprocess.Popen([command, option_str], 
            stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    else:
        proc = subprocess.Popen([command], 
            stdout=subprocess.PIPE, stderr = subprocess.PIPE)

    stdout_value, stderr_value = proc.communicate()

    if stderr_value != '':
        raise Exception(stderr_value)


    return stdout_value
