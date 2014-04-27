import os
from control import access
from util import html, describe
import time

class Input(object):
    pass
        

class Any(object):
    def __str__(self):
        return "Type " + self.__class__.__name__

class Html(Any):
    pass

class Text(Any):
    pass

class Nothing(Any):
    pass



from control import mime
import magic
class File(Any):

    def __init__(self, path):
        if not access.is_valid_path(path):
            message = "File at " + html.strong(path) + " is not accessible"
            raise Exception(message)
        self.path = path

    def get_name(self):
        base, name = os.path.split(self.path)
        return name
    name = property(get_name)

    def get_extension(self):
        name_part, extension = os.path.splitext(self.name)
        return extension
    extension = property(get_extension)

    def get_size(self):
        size = os.path.getsize(self.path)
        return size
    size = property(get_size)

    def get_created(self):
        created = os.path.getctime(self.path)
        return created
    created = property(get_created)

    def get_accessed(self):
        accessed = os.path.getatime(self.path)
        return accessed
    accessed = property(get_accessed)

    def get_modified(self):
        modified = os.path.getmtime(self.path)
        return modified
    modified = property(get_modified)

    def get_mime_type(self):
        mime_type = mime.get_mime_type(self.path)
        return mime_type
    mime = property(get_mime_type)

    def get_tooltip(self):
        return self.get_name() + "\n" + self.describe_size()

    def describe_size(self):
        return str(describe.describe_file_size(self.get_size()))

    def describe_type(self):
        return "File"        

    def get_type_description(self):
        ms = magic.open(magic.MAGIC_NONE)
        ms.load()
        type = ms.file(self.path)

        return type

    def describe_modified(self):
        return self.describe_time(self.modified)

    def describe_accessed(self):
        return self.describe_time(self.accessed)
        
    def describe_time(self, time_property):
        local_time = (time.localtime(time_property))
        return time.strftime('%a %d %b %Y %H:%M:%S %Z', local_time)



        

    def get_details(self):
        size_str = self.describe_size()
        modified_str = self.describe_modified()
        accessed_str = self.describe_accessed()
        details = {"Size" : size_str, \
                   "Accessed" : accessed_str, \
                   "Modified" : modified_str}
        return [details]

    def __str__(self):
        # return '[File ' + self.name + ']'
        return self.name

from PIL import Image
class ImageFile(File):
    def get_details(self):
        image = Image.open(self.path)
        width, height = image.size
        details = {"width" : width, "height" : height}
        detail_list = File.get_details(self)
        detail_list.append(details)
        return detail_list

class TextFile(File):
    def get_details(self):
        details = {"lines" : 10, "words" : 30, "characters" : 5}
        return File.get_details(self).append(details)

class CodeFile(TextFile):
    pass


class Directory(File):
    def describe_size(self):
        num_files = len(os.listdir(self.path)) 
        return str(num_files) + ' ' + describe.pluralise('item', num_files)
    def describe_type(self):
        return "Folder"
    def __str__(self):
        # return '[Dir  ' + self.name + ']'
        return self.name
