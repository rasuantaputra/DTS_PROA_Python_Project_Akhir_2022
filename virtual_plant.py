import tkinter

from pip import main
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


main_window = tkinter.Tk()
main_window.title('Tugas DTS Kominfo 2022')

# Virtual plant frame size
frame = tkinter.Canvas(main_window, bg="white", height=700, width=1365)
# take Tank.png image
img = tkinter.PhotoImage(file="img\Tank.png")

# mose motion function for definding coordinate
def mouse_motion_coordinate(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

def tank(level=310):
    x = 320
    y = 360
    # Insert tank image
    frame.create_image(x,y, image=img)
    # valve 1 (x1, y1, x2, y2, x3, y3, x4, y4, x5, y5)
    frame.create_polygon(x-207, y-90, x-207, y-140, x-121, y-90, x-121, y-140, fill='lime')
    # valve 2 (x1, y1, x2, y2, x3, y3, x4, y4, x5, y5)
    frame.create_polygon(x+151, y+155, x+151, y+95, x+237, y+155, x+237, y+95, fill='lime')
    # Make linquid inside tank
    # liquid = (level - x)/level
    # frame.create_rectangle(174, level, 383, 518, fill="blue", outline = 'blue')
    frame.create_rectangle(x-146, level, x+63, y+158, fill="blue", outline = 'blue')
    

def graph():
    # Figure size
    figure = Figure()
    plot1 = figure.add_subplot(111)
    # Plot graph
    plot1.grid(True)
    plot1.set_title('Response Graph')
    plot1.set_xlabel('time (sec)')
    plot1.set_ylabel('Process Value (PV)')
    plot1.plot([1, 2, 3, 4], [5, 6, 7, 9])
    # Embedding in canvas or frame
    canvas_graph = tkinter.Canvas(main_window, bg='white')
    # frame_graph.place(relx=0.4,rely=0.2,relwidth=0.4,relheight=0.6,anchor='e')
    canvas_graph.place(x=0,y=0, width=400, height=200)

    canvasGrafik = FigureCanvasTkAgg(figure, canvas_graph)
    canvasGrafik.get_tk_widget().place(relheight=1,relwidth=1)
    canvasGrafik.draw()


# =========try block========
tank()
graph()
# ==========================
frame.pack()

# Activate mouse corrdinate
main_window.bind('<Motion>', mouse_motion_coordinate)
main_window.mainloop()
