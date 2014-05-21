from model.app import app
from model import iotypes

from control import icon
from util import html

@app(name = "properties",
     input = iotypes.File,
     output = iotypes.Html,
     format_class = 'properties')
def execute(input, options, environment):

    file = input
    title_html = get_title(file)
    type_html = html.p(html.em(file.get_type_description()))
    details_html = details_table_to_html(file.get_details())

    html_str = title_html + type_html + details_html

    return html.div(html_str, clazz='properties')
    


def get_title(file):
    return  html.h2(get_icon(file) + " " + file.name)

def get_icon(file):
    icon_path = icon.get_icon_path_for_file(file)
    icon_html = html.img(src=icon_path)
    return icon_html

def details_table_to_html(details):
    table = ""
    for detail_chunk in details:
        for detail in detail_chunk:
            table += html.tr(html.td(detail) + html.td(detail_chunk[detail]))
    
    return html.table(table)



