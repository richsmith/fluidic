def render(files):

    # check input is a list of files

    details = get_details(files)

    output = two_d_list_into_table(details)

    return output


def get_details(files):
    
    details = []
    for file in files:
        details.append(get_details_for_file(file))

    return details

def get_details_for_file(file):
    import stat
    details = []
    details.append(file.name)
    details.append(os.path.getsize(file))
    file_stats = os.stat(file.name)
    details.append(file_stats[stat.ST_MTIME])
    return details


def two_d_list_into_table(list):
    output = "<table>"
    for row in list:
        output += "<tr>"
        for col in row:
            output += "<td>" + col + "</td>"
    output += "</table>"
    return output
