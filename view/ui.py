import os, gtk, webkit
from control import processor
from control import output
from control import ui_interface
import window, completion

#global history_index
history_index = 0

def setup():
    window.create_window()
    window.input_area.connect("key-press-event", handle_key_press)
    window.input_area.grab_focus()

    # Turn over control to the GTK+ main loop
    gtk.main()


def handle_key_press(widget, event):
    keyname = gtk.gdk.keyval_name(event.keyval)
    if keyname == 'Return':
        text = window.get_input() 
        if text == None:
            text = ''
        output.print_input(text)
        window.clear_input()

        global history_index
        history_index = 0

        if text != '':
            result = ui_interface.enter(text)
        #assert result != None
            if result != []:
                if isinstance(result, list):
                    output.print_outputs(result)
                else:
                    output.print_output(result)

        window.refresh()

    elif keyname == 'F5':
        window.refresh()

    elif keyname == 'Up':
        new_command_str = previous_command(processor.environment.history)
        window.set_input(new_command_str)
        window.cursor_to_end()
        # return True to stop default action of switching widget focus
        return True

    elif keyname == 'Down':
        new_command_str = next_command(processor.environment.history)
        window.set_input(new_command_str)
        window.cursor_to_end()
        # return True to stop default action of switching widget focus
        return True

    elif keyname == 'Tab':
        input = window.get_input();
        completed = completion.complete(input)
        if completed:
            window.set_input(completed)
            window.cursor_to_end()
        return True


def previous_command(history):
    global history_index
    global active_command

    # if we're going into history from an active state, store the current input
    if history_index == 0:
        active_command = window.get_input()
    # if we're not at the earliest command, step back
    if abs(history_index) != len(history):
        history_index -= 1

    return get_current_command(history)


def next_command(history):
    global history_index
    global active_command

    if history_index == 0:
        active_command = window.get_input()
    else:
        history_index += 1

    return get_current_command(history)

def get_current_command(history):
    if history_index == 0:
        return active_command
    else:
        return history[history_index]
