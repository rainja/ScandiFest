# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:36:20 2015

@author: Paul
"""

from Tkinter import Menu

class Menubar(Menu):
    def __init__(self, root, gui):
        Menu.__init__(self)
        
        self.filemenu = Menu(self, tearoff=0)
        self.filemenu.add_command(label="Logout")
        self.filemenu.add_command(label="Print...")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=root.destroy)
        
        self.add_cascade(label="File", menu=self.filemenu)
        
        self.adminmenu = Menu(self, tearoff=0)
        self.adminmenu.add_command(label="Database")
        self.adminmenu.add_command(label="Users")
        
        self.add_cascade(label="Admin", menu=self.adminmenu)
        
        self.helpmenu = Menu(self, tearoff=0)
        self.helpmenu.add_command(label="About")
        self.helpmenu.add_command(label="Help")
        
        self.add_cascade(label="Help", menu=self.helpmenu)