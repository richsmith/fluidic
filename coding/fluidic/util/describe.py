_kb = 1024.0
_mb = _kb * _kb
_gb = _mb * _kb
_tb = _gb * _kb
def describe_file_size(bytes):
    if bytes < _kb:
        return "%d bytes" % (bytes,)
    elif bytes < _mb:
        return "%.1f KB" % (bytes/_kb,)
    elif bytes < _gb:
        return "%.1f MB" % (bytes/_mb,)
    elif bytes < _tb:
        return "%.1f GB" % (bytes/_gb,)
    else:
        return "%.1f TB" % (bytes/_tb,)



def pluralise(noun, num_items):
    plural = noun
    if not noun.endswith('s') and num_items != 1:
        plural += 's'
    return plural
        
def dict_to_string(dict):
    string = 'dict: ['
    for key in dict:
        string += str(key) + '=' + str(dict[key]) + ', '
    string += ']'
