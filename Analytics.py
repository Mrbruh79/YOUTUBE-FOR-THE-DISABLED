import mysql.connector
import tkinter  as tk 
from tkinter import * 
import sv_ttk
import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt
import os
import datetime
import scatanal
import emotanal



my_w = tk.Tk()
sv_ttk.use_dark_theme()
my_w.geometry("400x250") 


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database = "Analytics"
)
print(mydb)
cursor = mydb.cursor()



cursor.execute("SELECT * FROM analytics")
e=Label(my_w,width=10,text='Searchword',font=("Franklin Gothic Demi",10),borderwidth=2, relief='ridge',anchor='w',bg='grey')
e.grid(row=0,column=0)
e=Label(my_w,width=10,text='EMOTION',borderwidth=2,font=("Franklin Gothic Demi",10), relief='ridge',anchor='w',bg='grey')
e.grid(row=0,column=1)
e=Label(my_w,width=10,text='starttime',borderwidth=2,font=("Franklin Gothic Demi",10), relief='ridge',anchor='w',bg='grey')
e.grid(row=0,column=2)
e=Label(my_w,width=10,text='endtime',borderwidth=2,font=("Franklin Gothic Demi",10), relief='ridge',anchor='w',bg='grey')
e.grid(row=0,column=3)
e=Label(my_w,width=10,text='analytics',borderwidth=2,font=("Franklin Gothic Demi",10), relief='ridge',anchor='w',bg='grey')
e.grid(row=0,column=4)


i=1
for student in cursor: 
    for j in range(len(student)):
        e = Entry(my_w, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, student[j])
    i=i+1
my_w.update()
query = "SELECT Searchword, EMOTION , starttime , endtime , duration FROM analytics"
cursor.execute(query)
to_plot = cursor.fetchall()

to_plot = pd.DataFrame(to_plot, columns=['Searchword' , 'EMOTION' , 'starttime','endtime' ,  'duration']) #set_index('starttime')


query = "SELECT starttime FROM analytics"
cursor.execute(query)
startt = cursor.fetchall()
query = "SELECT endtime FROM analytics"
cursor.execute(query)
endd = cursor.fetchall()

# daterange = pd.DataFrame(columns=["Time" , "Watching"])
# for x in range(0,len(startt)):
#    a = pd.date_range(startt[x][0],endd[x][0],freq='T').to_series()
#    for y in a:
#        daterange = daterange.append({"Time" : y , "Watching": 1 } , ignore_index= True)
#    if(x != len(startt)-1):
#        a = pd.date_range(endd[x][0],startt[x+1][0],freq='T').to_series()
#        for y in a:
#            daterange = daterange.append({"Time" : y , "Watching": 0 } , ignore_index= True)
       
# print(daterange)


# fig, ax = plt.subplots()

# ax.plot(to_plot['daterange'], 'blue' , label = 'duration' )
# for tick in ax.get_xticklabels():
#     tick.set_rotation(45)
# ax.legend()
# plt.show()
# import mysql.connector
# import matplotlib.pyplot as plt  
# from tkinter import * 
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
# NavigationToolbar2Tk)
# import tkinter as tk
# import matplotlib

# matplotlib.use('TkAgg')

# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import (
#     FigureCanvasTkAgg,
#     NavigationToolbar2Tk
# )

appa = scatanal.anal()
appe = emotanal.eanal()

while(True):
    appa.update()
    appe.update()

