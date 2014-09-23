'''
Created on Sep 15, 2014
updated on Sep 22, 2014

@author: Paul Reesman
'''

import sqlite3 as lite

class Logic():
    pieNames = []
    
    def __init__(self, DB, IP='local host'):
        try:
            self.conn = lite.connect(DB)
            self.cursor = self.conn.cursor()
            
            #self.cursor.execute("SELECT name FROM Freezer")
            #pieNames = self.cursor.fetchall()
            for member in self.cursor.execute("SELECT name FROM Freezer"):
                self.pieNames.append(member)
            print self.pieNames
        
        except:
            self.exit()
    
    def login(self, username, password):
        if self.cursor.execute("SELECT EXISTS(SELECT * FROM users WHERE username=?)", username):
            if password == self.execute("SELECT password FROM users WHERE username=?", username):
                return True
        return False
    
    def newUser(self, username, password):
        if self.cursor.execute("SELECT EXISTS(SELECT * FROM users WHERE username=?)", username):
            return False
        self.cursor.execute("INSERT INTO users(username, password) VALUES(?, ?)", (username, password))
        return True
    
    def close(self):
        self.conn.close()