'''
Created on Sep 15, 2014
Updated on Sep 22, 2014

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



class newUserPage(Frame):
    def __init__(self, root, gui):
        Frame.__init__(self, root)



def main():
    splash()
    root = Tk()
    GUI(root)
    root.protocol("WM_DELETE_WINDOW", close(root))
    root.mainloop()


def close(root):
    database.close()
    root.destroy



if __name__ == '__main__':
    main()
