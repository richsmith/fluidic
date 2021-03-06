def h2(content, **attributes):
    return element('h2', content, **attributes)

def p(content, **attributes):
    return element('p', content, **attributes)

def span(content, **attributes):
    return element('span', content, **attributes)

def div(content, **attributes):
    return element('div', content, **attributes)

def img(**attributes):
    assert 'src' in attributes
    return void_element('img', **attributes)


def thead(content, **attributes):
    return element('thead', content, **attributes)

def th(content, **attributes):
    return element('th', content, **attributes)

def table(content, **attributes):
    return element('table', content, **attributes)

def td(content, **attributes):
    return element('td', content, **attributes)

def tr(content, **attributes):
    return element('tr', content, **attributes)

def strong(content, **attributes):
    return element('strong', content, **attributes)

def em(content, **attributes):
    return element('em', content, **attributes)

def br():
    return void_element('br')

def li(content, **attributes):
    return element('li', content, **attributes)

def ol(content, **attributes):
    return element('ol', content, **attributes)




def void_element(name, **attributes):
    return '<' + name + process_attributes(**attributes) + '/>'

def element(name, content, **attributes):
    return '<' + name + process_attributes(**attributes) + '>' + \
        str(content) + \
        '</' + name + '>'

def process_attributes(**attributes):
    string = ''
    for attribute in attributes:
        name = 'class' if attribute == 'clazz' else attribute
        string += ' ' + name + ' = "' + attributes[attribute] + '"'

    return string
