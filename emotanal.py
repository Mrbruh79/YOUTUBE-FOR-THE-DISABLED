import mysql.connector
import matplotlib.pyplot as plt  
from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import tkinter as tk
import matplotlib

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
  database = "emot"
)
a = ""
print(mydb)
cursor = mydb.cursor()


cursor.execute("select EMOTION, duration from emot")
result = cursor.fetchall

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Matplotlib Demo')

        
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
        axes.bar(EMOTION, duration)
        axes.set_title('Mood analytics')
        axes.set_ylabel('duration')
        axes.set_xlabel('EMOTION')
        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


if __name__ == '__main__':
    app = App()
    app.mainloop()