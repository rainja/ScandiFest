# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:27:44 2015

@author: Paul
"""


from Tkinter import Frame, Label, Entry, Button, Toplevel, BOTH, TOP
from welcome import welcomePage


class loginPage(Frame):
    def __init__(self, root, gui):
        Frame.__init__(self, root)
        self.gui = gui
        self.root = root
        
        #self.config(background="blue")
        #background_image = "images/rosemaling.gif"
        #self.image = PhotoImage(file=background_image)
        background_label = Label(self, background="gainsboro").pack(expand=1, fill=BOTH)
        
        Label(background_label, text="BoothTool.py\nVersion A.01", background="gainsboro", height=20, width=root.winfo_width()).pack(side=TOP)
        Label(background_label, text="Username:", background="gainsboro", font=("Times", "20")).pack()
        
        text1 = Entry(background_label, font=("Times", "16"), background="gainsboro")
        text1.pack()
        
        Label(background_label, text="Password:",background="gainsboro", font=("Times", "20")).pack()
        
        text2 = Entry(background_label, show="*", font=("Times", "16"), background="gainsboro")
        text2.pack()
        
        Button(background_label, text="Login...", font=("Times", "20"), background="gainsboro", command=lambda: self.loginCommand(text1.get(), text2.get())).pack()
    
    def loginCommand(self, username, password):
        if self.gui.btd.database.login(username, password):
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