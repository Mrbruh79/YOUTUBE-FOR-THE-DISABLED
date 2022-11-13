import mysql.connector
import matplotlib.pyplot as plt  
from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import tkinter as tk
import matplotlib
import pandas as pd
matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database = "Analytics"
)
a = ""
print(mydb)
cursor = mydb.cursor()

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Matplotlib Demo')
        
        
        
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

        daterange = pd.DataFrame(columns=["Time" , "Watching"])
        for x in range(0,len(startt)):
           a = pd.date_range(startt[x][0],endd[x][0],freq='T').to_series()
           for y in a:
               daterange = daterange.append({"Time" : y , "Watching": 1 } , ignore_index= True)
           if(x != len(startt)-1):
               a = pd.date_range(endd[x][0],startt[x+1][0],freq='T').to_series()
               for y in a:
                   daterange = daterange.append({"Time" : y , "Watching": 0 } , ignore_index= True)
               
        print(daterange)

        
        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, self)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, self)

        # create axes
        axes = figure.add_subplot()
        EMOTION = []
        duration = []

        for i in cursor:
        	EMOTION.append(i[0])
        	duration.append(i[1])

        # create the barchart
        axes.scatter(daterange["Time"], daterange["Watching"])
        axes.set_title('Mood analytics')
        axes.set_ylabel('Watching')
        axes.set_xlabel('Time')
        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


if __name__ == '__main__':
    app = App()
    app.mainloop()
