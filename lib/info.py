#!/usr/bin/env python
import pygtk
import sys

pygtk.require('2.0')
import gtk

class SimpleTextInput:
    def print_text(self):
        buffer = self.textInput.get_buffer()


    def destroy(self, widget, data=None):
        if self.print_text_flag == False:
            self.print_text()
        gtk.main_quit()

    def __init__(self):
        # create a new window
        self.print_text_flag = False
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_DIALOG)
        window.set_title("PHP Manual")
        window.set_default_size(300, 360)
        window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        window.connect("destroy", self.destroy)
        window.set_border_width(5)
        self.textInput = gtk.Entry()
        self.textInput.set_max_length(5)
        self.textInput.connect("key_press_event", self.on_key_press)
        window.add(self.textInput)

        window.show_all()
    def on_key_press(self, widget, event):
        keyname = gtk.gdk.keyval_name(event.keyval)
        if event.state & gtk.gdk.CONTROL_MASK and keyname == 'Return' or keyname == 'Return':
            self.print_text()
            self.print_text_flag = True
            self.destroy(self, widget)  
        if keyname == 'Escape':  
            gtk.main_quit()

    def main(self):
        gtk.main()


if __name__ == "__main__":
    sys.stdout.write(argv[0]+"222\n")
    txt = SimpleTextInput()
    txt.main()
