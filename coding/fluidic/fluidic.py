#!/usr/bin/env python

# (C) Rich Smith 2012
# rls@hwyl.org

import os
from view import ui
from control import access, output
import apps

name = "Fluidic"
version = "0.4.0"

if __name__ == '__main__':
    path = access.interpret_path("~")
    os.chdir(path)

    output.clear()
    output.welcome()

    apps.ls.execute(None, None, None)

    ui.setup()


