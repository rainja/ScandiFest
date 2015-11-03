# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:34:51 2015

@author: Paul
"""

from Tkinter import Frame, Label, Button, TOP
from login import loginPage
from newUser import newUserPage

class titlePage(Frame):
    def __init__(self, root, gui):
        Frame.__init__(self, root)
        
        self.config(background="gainsboro")
        Label(self, text="BoothTool.py\nVersion A.01", font=("Times", 24, "bold"), background="gainsboro", height=20, width=root.winfo_width()).pack(side=TOP)
        Button(self, text="Login", font=("Times", "24"), command=lambda: gui.screenChange(loginPage(root, gui))).pack(side=TOP)
        Button(self, text="New User?", font=("Times", "24"), command=lambda: gui.screenChange(newUserPage(root, gui))).pack(side=TOP)
