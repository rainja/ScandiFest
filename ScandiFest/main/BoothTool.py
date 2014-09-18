'''
Created on Sep 15, 2014
Updated on Sep 17, 2014

@author: Paul Reesman
'''

from Tkinter import Tk, Label, BOTH, TOP
from ttk import Frame, Style, Notebook
from main import Logic, Splash

class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        
        self.initUI()
        self.notebook()
        self.centerWindow()
    
    def initUI(self):
        self.parent.title("BoothTool")
        self.pack(fill=BOTH, expand=1)
        self.style = Style()
        self.style.configure("TFrame", foreground="black", background="white")
        
        self.labelList = []
        for index in xrange(0, len(database.pieNames)):
            self.labelList.append(Label(self.parent, text=str(database.pieNames[index])))
            #self.labelList[index].pack(expand=True, side=TOP, fill=BOTH)
        
    
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



def main():
    Splash.splash()
    root = Tk()
    GUI(root)
    root.protocol("WM_DELETE_WINDOW", close(root))
    root.mainloop()

def close(root):
    database.close()
    root.destroy



database = Logic.Logic("/SQLite/BoothTool.db")

if __name__ == '__main__':
    main()
