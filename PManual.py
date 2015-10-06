import sublime
import sublime_plugin
import subprocess
import os
import sys



class PManualCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        sel = self.view.sel()
        selected = None
        text_output = None
        args = []
        
        if len(sel) == 0:
            return;
        for region in sel:
                if region.size()!= 0:
                    word    =   self.view.substr(region)


        if sublime.platform() == 'linux':

            location = os.path.join(sublime.packages_path(), 'PManual', 'lib', 'info.py')
            args = [location]
           

            child = subprocess.Popen(args, stdin=subprocess.PIPE,stdout=subprocess.PIPE)
            #child.stdin.write() 
            text_returned = child.communicate()[0].strip()
           
               
            # print(buffer.get_text())

             

