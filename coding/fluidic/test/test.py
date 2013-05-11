#!/usr/bin/env python

import magic
# m = magic.open(magic.MAGIC_MIME)
# m.load()
# print dir(m)
# print (m.file("test.py"))
#print (m.descriptor("test.py"))
print dir(magic.Magic)
foo = 1
mime = magic.Magic(True)
mime.from_file("test.py")
