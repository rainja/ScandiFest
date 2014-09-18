'''
Created on Sep 15, 2014
Updated on Sep 18, 2014

@author: Paul Reesman
'''

from Tkinter import *
from ttk import Style, Notebook
from main import Logic, Splash

database = Logic.Logic("/SQLite/BoothTool.db")
Splash.splash()
root = Tk()

class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        
        #self.notebook() <-- Should be it's own class, probably
        
        self.initUI()
        self.centerWindow()
    
    def initUI(self):
        self.parent.title("BoothTool")
        self.pack(fill=BOTH, expand=1)
        self.style = Style()
        self.style.configure("TFrame", foreground="black", background="white")
        
        self.parent.config(menu=Menubar(self.parent))
        #self.filebar.pack(side=TOP, expand=True, fill=X)
        #self.filebar.grid()
        
        self.labelList = []
        for index in xrange(0, len(database.pieNames)):
            self.labelList.append(Label(self.parent, text=str(database.pieNames[index])))
            self.labelList[index].pack(expand=True, side=TOP, fill=BOTH)
        
    
    def centerWindow(self):
        windowWidth = self.parent.winfo_screenwidth()
        windowHeight = self.parent.winfo_screenheight()
        
        width = .75 * windowWidth
        height = .75 * windowHeight
        x = (windowWidth - width) / 2
        y = (windowHeight - height) / 2
        
        self.parent.geometry("%dx%d+%d+%d" % (width, height, x, y))
    
    def notebook(self):
        tabFrame = Notebook(self.parent)



class Menubar(Menu):
    def __init__(self, root):
        Menu.__init__(self)
        
        self.filemenu = Menu(self, tearoff=0)
        self.filemenu.add_command(label="Logout")
        self.filemenu.add_command(label="print")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="exit", command=close)
        
        self.add_cascade(label="File", menu=self.filemenu)
        
        self.adminmenu = Menu(self, tearoff=0)
        self.adminmenu.add_command(label="Database...")
        self.adminmenu.add_command(label="Users...")
        
        self.add_cascade(label="Admin", menu=self.adminmenu)
        
        self.helpmenu = Menu(self, tearoff=0)
        self.helpmenu.add_command(label="About")
        self.helpmenu.add_command(label="Help")
        
        self.add_cascade(label="Help", menu=self.helpmenu)
        #Button(self, text="File").pack(side=LEFT)
        #Button(self, text="Admin").pack(side=LEFT)
        #Button(self, text="Help").pack(side=LEFT)


def main():
    GUI(root)
    root.protocol("WM_DELETE_WINDOW", close())
    root.mainloop()

def close():
    database.close()
    root.destroy




if __name__ == '__main__':
    main()
