#!/usr/bin/env python

# (C) Rich Smith 2014
# rls@hwyl.org

import os
from view import ui
from control import access, output, processor

name = "Fluidic"
version = "0.4.0"

if __name__ == '__main__':

    path = access.interpret_path("~")
    os.chdir(path)

    output.clear()
    output.welcome()

    ls_output = processor.process('ls');
    output.print_outputs(ls_output)
    

    ui.setup()





