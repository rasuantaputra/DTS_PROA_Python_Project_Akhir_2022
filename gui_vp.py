import tkinter

from pip import main
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

def start():
    # make variable being globaly
    global frame, img, main_window

    main_window = tkinter.Tk()
    main_window.title('Tugas DTS Kominfo 2022')
    main_window.resizable(0,0)

    # Virtual plant frame size
    frame = tkinter.Canvas(main_window, bg='#2596be', height=600, width=1000)
    # take Tank.png image
    img = tkinter.PhotoImage(file="img\Tank.png")

# mose motion function for definding coordinate
def mouse_motion_coordinate(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

def tank(level=141):
    # Tank coordinate
    x = 295
    y = 190
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
    plot1.set_xlabel('time (Sec)')
    plot1.set_ylabel('Process Value (PV)')
    plot1.plot([1, 2, 3, 4], [5, 6, 7, 9])
    # Embedding in canvas
    canvas_graph = tkinter.Canvas(main_window, bg='white')
    # frame_graph.place(relx=0.4,rely=0.2,relwidth=0.4,relheight=0.6,anchor='e')
    canvas_graph.place(x=580,y=1, width=450, height=400)

    canvasGrafik = FigureCanvasTkAgg(figure, canvas_graph)
    canvasGrafik.get_tk_widget().place(relheight=1,relwidth=1)
    canvasGrafik.draw()

def control_panel():
    frame.create_rectangle(0, 401, 1009, 603 , fill='#074447', outline = '#074447')

    # Make entry debit
    debit = tkinter.Label(bg='#074447', text='Debit Input      :', fg='white', font='sans 16 bold')
    debit.place(x=320,y=404)
    debit = tkinter.Entry(main_window)
    debit.place(x=479 , y=411)
    debit.insert(0,69)

    # Make entry maximum lvl
    maximum_liquid_lvl = tkinter.Label(bg='#074447', text='Max Liquid lvl :', fg='white', font='sans 16 bold')
    maximum_liquid_lvl.place(x=320,y=438)
    maximum_liquid_lvl = tkinter.Entry(main_window)
    maximum_liquid_lvl.place(x=479 , y=445)
    maximum_liquid_lvl.insert(0,69)

    # Make entry gravitation
    gravitation = tkinter.Label(bg='#074447', text='Gravitation     :', fg='white', font='sans 16 bold')
    gravitation.place(x=320,y=472)
    gravitation = tkinter.Entry(main_window)
    gravitation.place(x=479 , y=479)
    gravitation.insert(0,69)

    # Make entry q1 pipe diameter
    valve1_area = tkinter.Label(bg='#074447', text='Valve 1 D        :', fg='white', font='sans 16 bold')
    valve1_area.place(x=320,y=506)
    valve1_area = tkinter.Entry(main_window)
    valve1_area = tkinter.Spinbox(main_window, values=(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))
    valve1_area.place(x=479 , y=513)

    # Make tank area diameter
    tank_area = tkinter.Label(bg='#074447', text='Tank Area      :', fg='white', font='sans 16 bold')
    tank_area.place(x=320,y=540)
    tank_area = tkinter.Entry(main_window)
    tank_area.place(x=479 , y=547)
    tank_area.insert(0,69)

    # Make start button
    start_button = tkinter.Button(main_window, text='Start', font='sans 16 bold')
    start_button.place(x=163 , y=408,relwidth=0.3,relheight=0.1,anchor='n')

    # Make pause button
    pause_button = tkinter.Button(main_window, text='Pause', font='sans 16 bold')
    pause_button.place(x=163 , y=473,relwidth=0.3,relheight=0.1,anchor='n')

    # Make reset button
    reset_button = tkinter.Button(main_window, text='Reset', font='sans 16 bold')
    reset_button.place(x=163 , y=538,relwidth=0.3,relheight=0.1,anchor='n')

def activate():
    frame.pack()
    # Activate mouse corrdinate
    main_window.bind('<Motion>', mouse_motion_coordinate)
    main_window.mainloop()


# =========try block========
start()
tank()
graph()
control_panel()
activate()
# ==========================