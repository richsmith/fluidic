import os, gtk, webkit
import buffer
from control import icon
from control import access

def create_window():
    # Create a GTK+ window
    global window
    window = gtk.Window()
    window.set_position(gtk.WIN_POS_CENTER)

    #window.set_icon_from_file(icon.get_icon_path('folder'))
    base_path = access.get_abs_base_dir_path()
    icon_path = base_path + 'resources/icons/main.png'
    window.set_icon_from_file(icon_path)

    # Terminate the program when the window is closed
    window.connect("destroy", gtk.main_quit)
    # Instantiate the WebKit renderer
    global web_view
    web_view = webkit.WebView()
    # web_view.set_editable(True) <- hmm, look into this!

    # disable right-click
    web_view.props.settings.props.enable_default_context_menu = False


    web_view.connect('size-allocate', autoscroll_view) # auto scroll to bottom

    global input_area
    input_area = gtk.Entry(max=0)
    input_area.set_has_frame(False)

    scrolled_window = gtk.ScrolledWindow(hadjustment=None, vadjustment=None)
    scrolled_window.set_policy(hscrollbar_policy=gtk.POLICY_NEVER, 
                               vscrollbar_policy=gtk.POLICY_ALWAYS)
    scrolled_window.add_with_viewport(web_view)

    box = gtk.VBox(homogeneous=False, spacing=0)
    box.pack_start(scrolled_window, expand=True, fill=True, padding=0)
    box.pack_end(input_area, expand=False, fill=False, padding=0)
    window.add(box)

    # Load an HTML string into the renderer
    refresh()


    # Add the renderer to the window
    #window.add(web_view)
    window.resize(width=800, height=600)
    window.show_all()


def clear_input():
    input_area.set_text('')

def set_input(text):
    input_area.set_text(text)

def get_input():
    return input_area.get_text()

def cursor_to_end():
    input_area.set_position(len(get_input()))


# bollocks to make window scroll to bottom
def autoscroll_view(view, allocation):
    #parent is the gtk.ScrolledWindow that needs updating
    parent = view.get_parent()
    adj = parent.get_vadjustment()
    adj.value = adj.upper - adj.page_size
    #parent.set_vadjsutment(adj)

    

def refresh():
    #web_view.open("file:///home/rls/coding/fluidic/view/output.html")
    
    #web_view.loadString(buffer.get_buffer())

    #html = "<html><body><h1>hi world</h1></body></html>"
    #web_view.load_string(, "text/html")

    #web_view.load_string(html, "text/html", "utf-8", '')

    web_view.load_string(get_view_html(), "text/html", "utf-8", 'file://')

    window.set_title(os.getcwd() + " | Fluidic")

def get_view_html():
    #template = get_template()
    output = None
    with open('/home/rls/coding/fluidic/view/output.html', 'r') as file:
        output = file.read()


    from string import Template
    template = Template(get_template())
    html = template.substitute(content=output)

    return str(html)


def get_template():
    #global template
    #if template == None:
    template = load_template()
    return template
        

def load_template():
    template_path = '/home/rls/coding/fluidic/view/template.html'
    template = None
    with open(template_path, "r") as file:
        template = file.read()
    return template
