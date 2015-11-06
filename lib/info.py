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

    def __init__(self,title,param):
        # create a new window
        self.print_text_flag = False
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_DIALOG)
        window.set_title("PHP Manual")
        window.set_default_size(300, 360)
        window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        window.connect("destroy", self.destroy)
        window.set_border_width(5)

        # self.textInput = gtk.Entry()
        # self.textInput.set_text(title)
        # #echo
        # self.textInput.set_max_length(20)
      
        #self.textInput.connect("key_press_event", self.on_key_press)
        # window.add(self.textInput)

        self.text = gtk.Entry()
        self.text.set_text(param)
        self.text.connect("key_press_event", self.on_key_press)
        #echo
        self.text.set_max_length(50)
        window.add(self.text)


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
    reg     =   r'<div class="methodsynopsis dc-description">\n   <span class="type">(.*)</span> <span class="methodname"><strong>(.*)</strong></span>\n    \(([\s\S]*)\)</div>'
   #sys.stdout.write('sssss')
    rege = re.compile(reg)
    result = re.findall(rege,html)
    count  =    0
    count1 =   0
    param  = []
    param_type=[]
    for description in result:
        if description!=None:
            for xx in description:
                count+=1;
                
                if count ==1 :
                    #print(xx);
                    reg1    =   r'<span class="type .*">(.*)</span>'
                    rege = re.compile(reg1)
                    result = rege.search(xx)
                    if result:
                        returnvalue    =    result.group(1);
                        param.append(returnvalue)
                        #sys.stdout.write(returnvalue);
                if count ==2 :
                    #sys.stdout.write(xx);
                    name =xx;

                if count ==3 :
                    #print(xx);
                    musreg  =   r'<span class="methodparam">.*\n   \['
                    rege = re.compile(musreg)
                    result = rege.search(xx)
                    if result:
                        musp    =   result.group(0)
                        
                        
                        #echo


                   ##得到必须参数
                    reg1    =   r'(?:<span class="methodparam"><span class="type">(.*)</span> <code class="parameter">(.*)</code></span>\n)*'
                    rege = re.compile(reg1)
                    result = re.findall(rege,musp)

                    
                    for value in result:
                        #count1+=1;
                       
                        
                        if value!=None:
                            param.append(value[0])
                            param.append(value[1])
                            # sys.stdout.write(value[0]);
                            # sys.stdout.write(value[1])

                    ##得到可选参数
                    nomusreg    =   r'\[.*\n  \]'
                    
                    rege = re.compile(nomusreg)
                    result = rege.search(xx)
                    if result:
                        nomusp    =   result.group(0)
                        
                        
                        #echo


                   ##得到必须参数
                    reg1    =   r'(?:<span class="methodparam"><span class="type">(.*)</span> <code class="parameter">(.*)</code></span>\n)*'
                    rege = re.compile(reg1)
                    result = re.findall(rege,nomusp)
                    param.append('line')
                    for value in result:
                        #count1+=1;
                       
                        
                        if value!=None:
                            param.append(value[0])
                            param.append(value[1])

            return param
                           
                # if count ==4 :
                #     print('ss');
                    # reg1    =   r'<span class="type .*">(.*)</span>'
                    # rege = re.compile(reg1)
                    # result = rege.search(xx)
                    # if result:
                    #     returnvalue    =    result.group(1);
                    #     #sys.stdout.write(returnvalue);

                    #echo

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
    string =''
    count =0;
    param   =   getDescripiton(html)
    length  =   len(param)
    num2    =0
    for test in reversed(param):
        num2+=1
        if test !='':
            break;
    #print(num2)
    length=length-num2-1


    for value in param:
        # num2+=1
        if value=='':
            count+=1
            continue
        if value=='line':
            string+= '['
            count-=1
        elif count==0:

            string += 'void  ('

        elif count%2==0:
            # print(num2)
            if count==length:
                string +=' '+value+' '
            else:
                string +=' '+value+','
        else:
            string +=' '+value+' '
        count +=1
        # sys.stdout.write('1')
    #echo 
    string+=' ])'
    # sys.stdout.write(string)


    txt = SimpleTextInput(title,string)
    
    txt.main()
