'''
Created on Sep 15, 2014
updated on Sep 23, 2014

@author: Paul Reesman
'''

import sqlite3 as lite

class Logic():
    pieNames = []
    
    def __init__(self, DB, IP='local host'):
        self.conn = lite.connect(DB)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cursor = self.conn.cursor()
        
        #self.cursor.execute("SELECT name FROM Freezer")
        #pieNames = self.cursor.fetchall()
        #for member in self.cursor.execute("SELECT name FROM Freezer"):
        #    self.pieNames.append(member)
        #print self.pieNames
    
    def login(self, username, password):
        self.cursor.execute("SELECT EXISTS(SELECT * FROM users WHERE username=?)", (username,))
        if self.cursor.fetchone():
            self.cursor.execute("SELECT password FROM users WHERE username=?", (username,))
            if password == self.cursor.fetchone():
                return True
        return False
    
    def newUser(self, username, password, fname, lname):
        self.cursor.execute("SELECT EXISTS(SELECT * FROM users WHERE username=?)", (username,))
        if self.cursor.fetchone():
            return False
        self.cursor.execute("INSERT INTO users(username, password, fname, lname) VALUES(?, ?, ?, ?)", (username, password, fname, lname))
        self.conn.commit()
        return True
    
    def close(self):
        self.conn.close()