# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:27:44 2015

@author: Paul
"""


from Tkinter import *
from welcome import welcomePage


class loginPage(Frame):
    def __init__(self, root, gui):
        Frame.__init__(self, root)
        self.gui = gui
        self.root = root
        
        self.config(background="blue")
        Label(self, text="BoothTool.py\nVersion A.01", background="blue", height=20, width=root.winfo_width()).pack(side=TOP)
        Label(self, text="Username:", background="blue", font=("Times", "20")).pack()
        text1 = Entry(self, font=("Times", "16"))
        text1.pack()
        Label(self, text="Password:", background="blue", font=("Times", "20")).pack()
        text2 = Entry(self, show="*", font=("Times", "16"))
        text2.pack()
        Button(self, text="Login...", font=("Times", "20"), command=lambda: self.loginCommand(text1.get(), text2.get())).pack()
    
    def loginCommand(self, username, password):
        if self.gui.btd.login(username, password):
            self.gui.screenChange(welcomePage(self.root, self.gui))
        else:
            popup = Toplevel()
            popup.title("Incorrect")
            
            windowWidth = popup.winfo_screenwidth()
            windowHeight = popup.winfo_screenheight()
            
            width = .25 * windowWidth
            height = .1 * windowHeight
            x = (windowWidth - width) / 2
            y = (windowHeight - height) / 2
            
            popup.geometry("%dx%d+%d+%d" % (width, height, x, y))
            popup.update()
            
            Label(popup, text="Incorrect username or password!").pack()
            Button(popup, text="Dismiss", command=popup.destroy).pack()