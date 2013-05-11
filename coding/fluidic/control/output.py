import apps
from util import html

##### stuff to write to html; to be done properly

output_file = "/home/rls/coding/fluidic/view/output.html"

def print_input(input):
    add_output(input, "command")

def print_outputs(outputs):
    print_output('\n\n'.join(outputs))

def print_output(output):
    add_output(output, "output")

def print_misc(text, clazz):
    add_output(text, clazz)

    
def add_output(text, elementName):
    element = '\n\n' + html.div(text, clazz=elementName)

    with open(output_file, "a") as file:
        file.write(element)


def add_output_nicer(text, elementName):

    dom = parse("output.html")

    body = dom.getElementsByTagName("body")[0]
    node = dom.createElement("div")
    node.setAttribute("class", elementName)
    node.appendChild(dom.createTextNode(text))
    body.appendChild(node)

    f = open("output.html", 'w')
    dom.writexml(f)
    f.close()
    #print dom.toxml()

def clear():
    with open(output_file, "w") as file:
        file.write('')

def welcome():
    apps.about.execute(None, None, None)
