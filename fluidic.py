#!/usr/bin/env python

# (C) Rich Smith 2012
# rls@hwyl.org

import os
from view import ui
from control import access, output, parser

name = "Fluidic"
version = "0.4.0"

def print_home():
    from apps import ls
    ls.execute(None, None, None)

if __name__ == '__main__':
    path = access.interpret_path("~")
    os.chdir(path)

    output.clear()
    output.welcome()

    print_home()
    ui.setup()




