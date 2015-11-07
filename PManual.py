import sublime
import sublime_plugin
import subprocess
import os
import sys
#from subprocess import Popen, PIPE, STDOUT
import subprocess


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
                else:
                    return
        word=word.encode(encoding="utf-8")

        if sublime.platform() == 'linux':

            location = os.path.join(sublime.packages_path(), 'PManual', 'lib', 'info.py')
            args = [location]
           
            # p = subprocess.Popen(args,stdout=subprocess.PIPE,stdin=subprocess.PIPE)
            # p.stdin.write('one\ntwo\nthree\nfour\nfive\nsix\n')
            # p.communicate()[0]

            from subprocess import Popen, PIPE, STDOUT

            p = Popen(args, stdout=PIPE, stdin=PIPE, stderr=STDOUT)    

            p.communicate(input=word)[0]
            #print(grep_stdout.decode())
            #print('xxx')

            # pipe = os.popen(args, 'w', bufsize)
  
            #pipe = Popen(args, shell=True, bufsize=bufsize, stdin=PIPE).stdin
          #  child = subprocess.Popen(args, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
            #child = subprocess.Popen(args, stdin=subprocess.PIPE,stdout=subprocess.PIPE)
         #  child.communicate(input=b'one\ntwo\nthree\nfour\nfive\nsix\n')[0]
            #child.stdin.write() 
           # text_returned = child.communicate()[0].strip()
           
               
            # print(buffer.get_text())

             

