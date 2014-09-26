'''
Created on Sep 15, 2014
Updated on Sep 26, 2014

@author: Paul Reesman
'''

from Tkinter import *
from ttk import Notebook
from Logic import Logic
from Splash import splash

database = Logic("/SQLite/BoothTool.db")

class GUI(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        
        #self.notebook() <-- Should be it's own class, probably
        
        self.centerWindow()
        self.initUI()
        
    
    def initUI(self):
        self.root.title("BoothTool")
        self.root.config(menu=Menubar(self.root, self))
        
        self.widget = Frame(self.root)
        
        self.widget = titlePage(self.root, self)
        self.widget.pack(expand=True, fill=BOTH, side=TOP)
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
        self.widget.pack_forget()
        self.widget = newScreen
        self.widget.pack(expand=True, fill=BOTH, side=TOP)
    
    def notebook(self):
        tabFrame = Notebook(self.root)



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



class titlePage(Frame):
    def __init__(self, root, gui):
        Frame.__init__(self, root)
        
        self.config(background="blue")
        Label(self, text="BoothTool.py\nVersion A.01", background="blue", height=20, width=root.winfo_width()).pack(side=TOP)
        Button(self, text="Login", font=("Times", "24"), command=lambda: gui.screenChange(loginPage(root, gui))).pack(side=TOP)
        Button(self, text="New User?", font=("Times", "24"), command=lambda: gui.screenChange(newUserPage(root, gui))).pack(side=TOP)



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
        if database.login(username, password):
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



class welcomePage(Frame):
    def __init__(self, root, gui):
        Frame.__init__(self, root)



class newUserPage(Frame):
    def __init__(self, root, gui):
        Frame.__init__(self, root)
        self.gui = gui
        
        self.config(background="blue")
        Label(self, text="Create A New User", background="blue", height=20, width=root.winfo_width()).pack(side=TOP)
        Label(self, text="First Name:", background="blue", font=("Times", "20")).pack()
        text1 = Entry(self, font=("Times", "16"))
        text1.pack()
        Label(self, text="Last Name:", background="blue", font=("Times", "20")).pack()
        text2 = Entry(self, font=("Times", "16"))
        text2.pack()
        Label(self, text="Username:", background="blue", font=("Times", "20")).pack()
        text3 = Entry(self, font=("Times", "16"))
        text3.pack()
        Label(self, text="Password:", background="blue", font=("Times", "20")).pack()
        text4 = Entry(self, show="*", font=("Times", "16"))
        text4.pack()
        Button(self, text="Create User", font=("Times", "20"), command=lambda: self.createUser(text3.get(), text4.get(), text1.get(), text2.get())).pack()
    
    def createUser(self, username, password, fname, lname):
        if database.newUser(username, password, fname, lname):
            self.gui.screenChange(welcomePage(self.root, self.gui))
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



def main():
    splash()
    root = Tk()
    GUI(root)
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()



if __name__ == '__main__':
    main()
