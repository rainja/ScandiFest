'''
Created on Sep 15, 2014
Updated on Sep 26, 2014

@author: Paul Reesman
'''

import tkFileDialog
from Tkinter import Tk
from Database_File import Database
from Splash import splash
from pages.gui import GUI


class boothTool():
    def __init__(self):
        location = tkFileDialog.askopenfilename(title="Choose Database", initialdir="db")
        self.database = Database(location)
        #database = None


def main():
    #splash()
    root = Tk()
    GUI(root, boothTool())
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()
