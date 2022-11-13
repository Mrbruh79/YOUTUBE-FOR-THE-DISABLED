# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 14:16:09 2022

@author: Restandsleep
"""

import mysql.connector
import tkinter  as tk 
from tkinter import * 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database = "Playlists"
)
a = ""
print(mydb)
cursor = mydb.cursor()
table = ""
def create(name ):
    x = "CREATE TABLE {pname} (name VARCHAR(255), url TEXT);".format(pname = name)
    cursor.execute(x)
    mydb.commit()

def save(table ,name , url ):
    cursor.execute("""SELECT name FROM {playlist} WHERE url = "{surl}";""".format(playlist = table ,surl = url))
    x = cursor.fetchall()
    a = ""
    if not(len(x) == 0):
        print("Song already exists with name {sname}".format(sname = x[3:len(x) - 4]))
        a = "Song already exists with name {sname}".format(sname = x[3:len(x) - 4])
        return a
    cursor.execute("""SELECT * FROM {playlist} WHERE name = "{sname}";""".format(playlist = table ,sname = name))
    x = cursor.fetchall()
    
    if len(x)==0:
        
        cursor.execute("""insert into {playlist}(name,url) VALUES ('{sname}' , "{surl}");""".format(playlist = table ,sname = name , surl = url))
        mydb.commit()
    else:
        print("Another song already saved under name")
        a = "Another song already saved under name"
    return a
        
        
def remove(table,name):
    cursor.execute("""SELECT * FROM {playlist} WHERE name = "{sname}";""".format(playlist = table ,sname = name))
    x = cursor.fetchall()
    a = ""
    if not(len(x)==0):
        
        cursor.execute("""DELETE FROM {playlist} WHERE name = "{sname}";""".format(playlist = table ,sname = name))
        mydb.commit()
    else:
        print("Song dosent exist")
        a =  "Song dosent exist"
    return a
        
def geturl(table , name ):
    cursor.execute("""SELECT * FROM {playlist} WHERE name = "{sname}";""".format(playlist = table ,sname = name))
    x = cursor.fetchall()
    a = ""
    if not(len(x)==0):
        cursor.execute("""SELECT url FROM {playlist} WHERE name = "{sname}";""".format(playlist = table ,sname = name))
        x = str(cursor.fetchall())
        y = x[3:len(x) - 4]
        return y
    else:
        print("Song dosent exist")
        a =  "Song dosent exist"
        return a
        

def show(table):
    my_w = tk.Tk()
    my_w.geometry("400x250") 
    cursor.execute("SELECT * FROM {playlist}".format(playlist = table))
    e=Label(my_w,width=10,text='Song name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(my_w,width=10,text='URL',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)


    i=1
    for student in cursor: 
        for j in range(len(student)):
            e = Entry(my_w, width=10, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, student[j])
        i=i+1
    
    my_w.update()
    return my_w
def close(my_w ):
    my_w.destroy()
    
