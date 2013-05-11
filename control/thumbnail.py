import gnome.ui
import gnomevfs

def get_thumbnail_path(file):
    uri = gnomevfs.get_uri_from_local_path(file.path)
    factory = gnome.ui.ThumbnailFactory(gnome.ui.THUMBNAIL_SIZE_NORMAL)

    lookup = factory.lookup(uri, 0)

    if lookup != None:
        return lookup
    else:
        return generate_thumbnail(factory, uri)
    

def generate_thumbnail(factory, uri):

    mime = gnomevfs.get_mime_type(uri)

    if factory.can_thumbnail(uri, mime, 0):
        thumbnail = factory.generate_thumbnail(uri, mime)
        if thumbnail != None:
            factory.save_thumbnail(thumbnail, uri, 0) 
            return thumbnail
    
    return None
