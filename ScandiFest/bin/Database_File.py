'''
Created on Sep 15, 2014
updated on Sep 26, 2014

@author: Paul Reesman
'''

import sqlite3 as lite

class Database():
    foodItems = []
    
    def __init__(self, DB, IP='local host'):
        try:
            self.conn = lite.connect(DB)
        except:
            print "Could not connect to the database!\nPlease enter a valid path!"
            
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cursor = self.conn.cursor()
        
        self.conn.execute("CREATE TABLE if not EXISTS users (username TEXT PRIMARY KEY, password TEXT, fname TEXT, lname TEXT)")
        #self.cursor.execute("SELECT name FROM Freezer")
        #pieNames = self.cursor.fetchall()
        #for member in self.cursor.execute("SELECT name FROM Freezer"):
        #    self.pieNames.append(member)
        #print self.pieNames
    
    def login(self, username, password):
        self.cursor.execute("SELECT EXISTS(SELECT * FROM users WHERE username=?)", (username,))
        if int(self.cursor.fetchone()[0]):
            self.cursor.execute("SELECT password FROM users WHERE username=?", (username,))
            if password == self.cursor.fetchone()[0]:
                return True
        return False
    
    def newUser(self, username, password, fname, lname):
        self.cursor.execute("SELECT EXISTS(SELECT * FROM users WHERE username=?)", (username,))
        if int(self.cursor.fetchone()[0]):
            return False
        self.cursor.execute("INSERT INTO users(username, password, fname, lname) VALUES(?, ?, ?, ?)", (username, password, fname, lname))
        self.conn.commit()
        return True
    
    def close(self):
        self.conn.close()
