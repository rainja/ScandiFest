'''
Created on Sep 15, 2014
updated on Sep 16, 2014

@author: Paul Reesman
'''

import sqlite3 as lite

class Logic():
    pieNames = []
    
    def __init__(self, IP='local host', DB):
        try:
            self.conn = lite.connect(DB)
            self.cursor = self.conn.cursor()
            
            self.cursor.execute("SELECT name FROM Freezer")
            pieNames = self.cursor.fetchone()
        
        except:
            self.exit()