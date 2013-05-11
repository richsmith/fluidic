import magic

def get_mime_type(path):

    # This is horrible
    # There has to be a better way of doing this...
    
    m = magic.open(magic.MAGIC_MIME)
    m.load()

    string = m.file(path)

    parts = string.split(';')
    mime_type = parts[0]

    return mime_type

def get_major_mime_part(mime_type):
    parts = mime_type.split('/')
    return parts[0]

def get_minor_mime_part(mime_type):
    parts = mime_type.split('/')
    return parts[-1]
