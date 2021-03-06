# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 20:38:36 2015

@author: Paul
"""

from Tkinter import Frame, Label, Entry, Button, Toplevel, TOP
import title


class newUserPage(Frame):
    def __init__(self, root, gui):
        Frame.__init__(self, root)
        self.gui = gui
        self.root = root
        
        self.config(background="gainsboro")
        Label(self, text="Create A New User", background="gainsboro", height=20, width=root.winfo_width()).pack(side=TOP)
        Label(self, text="First Name:", background="gainsboro", font=("Times", "20")).pack()
        text1 = Entry(self, font=("Times", "16"))
        text1.pack()
        Label(self, text="Last Name:", background="gainsboro", font=("Times", "20")).pack()
        text2 = Entry(self, font=("Times", "16"))
        text2.pack()
        Label(self, text="Username:", background="gainsboro", font=("Times", "20")).pack()
        text3 = Entry(self, font=("Times", "16"))
        text3.pack()
        Label(self, text="Password:", background="gainsboro", font=("Times", "20")).pack()
        text4 = Entry(self, show="*", font=("Times", "16"))
        text4.pack()
        Button(self, text="Create User", font=("Times", "20"), command=lambda: self.createUser(text3.get(), text4.get(), text1.get(), text2.get())).pack()
    
    def createUser(self, username, password, fname, lname):
        if self.gui.btd.database.newUser(username, password, fname, lname):
            popup = Toplevel()
            popup.title("Account created!")
            
            windowWidth = popup.winfo_screenwidth()
            windowHeight = popup.winfo_screenheight()
            
            width = .25 * windowWidth
            height = .1 * windowHeight
            x = (windowWidth - width) / 2
            y = (windowHeight - height) / 2
            
            popup.geometry("%dx%d+%d+%d" % (width, height, x, y))
            popup.update()
            
            Label(popup, text="Your new account has been successfully created!").pack()
            Button(popup, text="Dismiss", command=popup.destroy).pack()
            
            self.gui.screenChange(title.titlePage(self.root, self.gui))
        else:
            popup = Toplevel()
            popup.title("Username Exists!")
            
            windowWidth = popup.winfo_screenwidth()
            windowHeight = popup.winfo_screenheight()
            
            width = .25 * windowWidth
            height = .1 * windowHeight
            x = (windowWidth - width) / 2
            y = (windowHeight - height) / 2
            
            popup.geometry("%dx%d+%d+%d" % (width, height, x, y))
            popup.update()
            
            Label(popup, text="A user account with that username already exists!").pack()
            Button(popup, text="Dismiss", command=popup.destroy).pack()