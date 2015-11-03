# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:41:53 2015

@author: Paul
"""

from Tkinter import Frame, BOTH, TOP
from ttk import Notebook
from menubar import Menubar
from title import titlePage


class GUI(Frame):
    def __init__(self, root, boothToolDatabase):
        Frame.__init__(self, root)
        self.root = root
        self.btd = boothToolDatabase
        #self.notebook() <-- Should be it's own class, probably
        
        self.centerWindow()
        self.initUI()
        
    def initUI(self):
        self.root.title("BoothTool")
        self.root.config(menu=Menubar(self.root, self))
        
        self.widget = Frame(self.root)
        
        self.widget = titlePage(self.root, self)
        self.widget.pack(expand=True, fill=BOTH, side=TOP)
        #root.configure(image=PhotoImage(file="images/rosemaling.gif"))
        #self.labelList = []
        #for index in xrange(0, len(database.pieNames)):
            #self.labelList.append(Label(self.root, text=str(database.pieNames[index])))
            #self.labelList[index].pack(expand=True, side=TOP, fill=BOTH)
        
    def centerWindow(self):
        windowWidth = self.root.winfo_screenwidth()
        windowHeight = self.root.winfo_screenheight()
        
        width = .75 * windowWidth
        height = .75 * windowHeight
        x = (windowWidth - width) / 2
        y = (windowHeight - height) / 2
        
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.update()
    
    def screenChange(self, newScreen):
        self.widget.pack_forget()   ### Change implementation to grid - update to version A.02
        self.widget = newScreen
        self.widget.pack(expand=True, fill=BOTH, side=TOP)
    
    def notebook(self):
        tabFrame = Notebook(self.root)