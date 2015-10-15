#!/usr/bin/env python
#encoding:utf-8
import pygtk
import sys
import re
import urllib
# from io import StringIO,BytesIO

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

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getMain(html):
    #reg = r'src="(.+?\.jpg)" pic_ext'
    
    #reg     =   r'<h1 class="refname">(.*)<\/h1>'
    reg     =   r'<span class="refname">.*</span> &mdash; <span class="dc-title">(.*)</span>'

    rege = re.compile(reg)
    result = re.findall(rege,html)
    for title in result:
        if title!=None:
            return title
        else:
            return 'error'
def getDescripiton(html):
    #reg = r'src="(.+?\.jpg)" pic_ext'
    
    #reg     =   r'<h1 class="refname">(.*)<\/h1>'
    reg     =   r'<div class="methodsynopsis dc-description">\n   <span class="type">(.*)</span> <span class="methodname"><strong>(.*)</strong></span>\n    \(([\s\S]*)\)'
    sys.stdout.write('sssss')
    rege = re.compile(reg)
    result = re.findall(rege,html)
    for description in result:
        if description!=None:
            for xx in description:
              print(xx)
            
        else:
            sys.stdout.write('error')

    
    # for imgurl in imglist:
    #     sys.stdout.write(imgurl,'%s.jpg' % x)
    
    #return imglist   

def notfound(html):
    reg     =   r'<h1>(.*)<\/h1>'

    rege = re.compile(reg)
    result = re.findall(rege,html)
    for con in result:
        if con=='Not Found':
            sys.stdout.write('not found')
            return 1
        else:
            return 0


 #  <div class="methodsynopsis dc-description">
 #   <span class="type">int</span> <span class="methodname"><strong>print</strong></span>
 #    ( <span class="methodparam"><span class="type">string</span> <code class="parameter">$arg</code></span>
 #   )</div>

 #  <p class="para rdfs-comment">

 #  </p>
 #  <p class="para">

 # </div>



if __name__ == "__main__":
    for line in sys.stdin:
        #sys.stdout.write(line)
        str     =   line.strip()
    #sys.stdout.write(str)
    url     =      'http://php.net/manual/zh/function.'+str+'.php'
    
    html    =   getHtml(url)
    ifNotFound  =notfound(html)
    if(ifNotFound):
        sys.stdout.write('stop')
        exit()
    else:
        title=getMain(html)
    if title!='error':
        sys.stdout.write(title)
    else:
        exit()
    getDescripiton(html)
    #sys.stdout.write(html)
    #echo 

    txt = SimpleTextInput()
    
    txt.main()
