from concurrent.futures import process
import tkinter
from tkinter.messagebox import YESNOCANCEL
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

from pip import main
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.animation import FuncAnimation
from tkinter import ttk

def start():
    # make variable being globaly
    global frame, img, main_window

    main_window = tkinter.Tk()
    main_window.title('Tugas DTS Kominfo 2022')
    main_window.resizable(0,0)

    # Virtual plant frame size
    frame = tkinter.Canvas(main_window, bg='#2596be', height=680, width=1000)
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
    frame.create_rectangle(358, 348, 150, level, fill="blue", outline = 'blue')

def graph(time, pv):
    global line, ani, fig
    
    # array/list for plot
    time_x = time
    processValue_y = pv

    # Figure size
    fig = plt.Figure()

    # Embedding in canvas
    canvas_graph = tkinter.Canvas(main_window, bg='white')
    canvas_graph.place(x=580,y=1, width=450, height=400)

    canvasGrafik = FigureCanvasTkAgg(fig, canvas_graph)
    canvasGrafik.get_tk_widget().place(relheight=1,relwidth=1)
    canvasGrafik.draw()

    plot1 = fig.add_subplot(111)
    # Plot graph
    plot1.grid(True)
    plot1.set_title('Response Graph')
    plot1.set_xlabel('time (Sec)')
    plot1.set_ylabel('Process Value (PV)')
    plot1.plot(time_x, processValue_y, color='blue')
    # ani = FuncAnimation(fig, animation_function_name, np.arange(1, 2000000), interval=10)


def control_panel():
    frame.create_rectangle(0, 401, 1009, 680 , fill='#074447', outline = '#074447')

def debit_input():
    # Make entry debit
    debit = tkinter.Label(bg='#074447', text='Debit Input      :', fg='white', font='sans 16 bold')
    debit.place(x=320,y=404)
    val = tkinter.StringVar(main_window, value=0.5)
    debit = tkinter.Entry(main_window,textvariable=val)
    debit.pack()
    debit.place(x=479 , y=411)

    return debit

def maximum_liquid_lvl_input():
    # Make entry maximum lvl
    maximum_liquid_lvl = tkinter.Label(bg='#074447', text='Max Liquid lvl :', fg='white', font='sans 16 bold')
    maximum_liquid_lvl.place(x=320,y=438)
    val = tkinter.StringVar(main_window, value=1)
    maximum_liquid_lvl = tkinter.Entry(main_window,textvariable=val)
    maximum_liquid_lvl.pack()
    maximum_liquid_lvl.place(x=479 , y=445)

    return maximum_liquid_lvl

def gravitation_input():
    # Make entry gravitation
    gravitation = tkinter.Label(bg='#074447', text='Gravitation     :', fg='white', font='sans 16 bold')
    gravitation.place(x=320,y=472)
    val = tkinter.StringVar(main_window, value=9.78)
    gravitation = tkinter.Entry(main_window,textvariable=val)
    gravitation.pack()
    gravitation.place(x=479 , y=479)

    return gravitation

def valve1_area_input():
    # Make entry q1 valve diameter
    valve1_area = tkinter.Label(bg='#074447', text='Valve 1 D        :', fg='white', font='sans 16 bold')
    valve1_area.place(x=320,y=506)
    val = tkinter.StringVar(main_window, value=50)
    valve1_area = tkinter.Spinbox(main_window,textvariable=val, from_=0, to=100, increment=10, width=18)
    valve1_area.pack()
    valve1_area.place(x=479 , y=513)

    return valve1_area

def pipe1_area_input():
    # Make entry q1 pipe diameter
    pipe1_area = tkinter.Label(bg='#074447', text='Pipe 1 D          :', fg='white', font='sans 16 bold')
    pipe1_area.place(x=320,y=540)
    val = tkinter.StringVar(main_window, value=0.02)
    pipe1_area = tkinter.Entry(main_window,textvariable=val)
    pipe1_area.pack()
    pipe1_area.place(x=479 , y=547)

    return pipe1_area

def pipe2_area_input():
    # Make entry q2 pipe diameter
    pipe2_area = tkinter.Label(bg='#074447', text='Pipe 2 D          :', fg='white', font='sans 16 bold')
    pipe2_area.place(x=320,y=574)
    val = tkinter.StringVar(main_window, value=0.02)
    pipe2_area = tkinter.Entry(main_window,textvariable=val)
    pipe2_area.pack()
    pipe2_area.place(x=479 , y=581)

    return pipe2_area

def sampling_time_input():
    # Make entry sampling time
    sampling_time = tkinter.Label(bg='#074447', text='Sampling (t)    :', fg='white', font='sans 16 bold')
    sampling_time.place(x=320,y=608)
    val = tkinter.StringVar(main_window, value=0.1)
    sampling_time = tkinter.Entry(main_window,textvariable=val)
    sampling_time.pack()
    sampling_time.place(x=479 , y=615)

    return sampling_time

def tank_area_input():
    # Make tank area diameter
    tank_area = tkinter.Label(bg='#074447', text='Tank Area      :', fg='white', font='sans 16 bold')
    tank_area.place(x=320,y=642)
    val = tkinter.StringVar(main_window, value=2)
    tank_area = tkinter.Entry(main_window,textvariable=val)
    tank_area.pack()
    tank_area.place(x=479 , y=649)

    return tank_area

def set_point_input():
    # Make proportional controll input
    set_point = tkinter.Label(bg='#074447', text='Set Point (SP)    :', fg='white', font='sans 16 bold')
    set_point.place(x=650,y=404)
    val = tkinter.StringVar(main_window, value=0.7)
    set_point = tkinter.Entry(main_window,textvariable=val)
    set_point.pack()
    set_point.place(x=828 , y=411)

    return set_point

def proportional_input():
    # Make proportional controll input
    proportional = tkinter.Label(bg='#074447', text='Proportional (P) :', fg='white', font='sans 16 bold')
    proportional.place(x=650,y=434)
    val = tkinter.StringVar(main_window, value=0)
    proportional = tkinter.Entry(main_window,textvariable=val)
    proportional.pack()
    proportional.place(x=828 , y=441)

    return proportional

def integral_input():
    # Make integral controll input
    integral = tkinter.Label(bg='#074447', text='Integral (I)           :', fg='white', font='sans 16 bold')
    integral.place(x=650,y=468)
    val = tkinter.StringVar(main_window, value=0)
    integral = tkinter.Entry(main_window,textvariable=val)
    integral.pack()
    integral.place(x=828 , y=475)

    return integral

def derivative_input():
    # Make derivative controll input
    derivative = tkinter.Label(bg='#074447', text='Derivative (D)     :', fg='white', font='sans 16 bold')
    derivative.place(x=650,y=502)
    val = tkinter.StringVar(main_window, value=0)
    derivative = tkinter.Entry(main_window,textvariable=val)
    derivative.pack()
    derivative.place(x=828 , y=509)

    return derivative

def start_button(function):
    # Make start button
    start_button = tkinter.Button(main_window, text='Start', font='sans 16 bold', command=function)
    start_button.pack()
    start_button.place(x=163 , y=428,relwidth=0.3,relheight=0.1,anchor='n')
 

def pause_button(function):
    # Make pause button
    pause_button = tkinter.Button(main_window, text='Pause', font='sans 16 bold', command=function)
    pause_button.pack()
    pause_button.place(x=163 , y=500,relwidth=0.3,relheight=0.1,anchor='n')

def reset_button(function):
    # Make reset button
    reset_button = tkinter.Button(main_window, text='Reset', font='sans 16 bold', command=function)
    reset_button.pack()
    reset_button.place(x=163 , y=572,relwidth=0.3,relheight=0.1,anchor='n')

    return reset_button

def tunning_button(function):
    # Make tunnig button
    tunning_button = tkinter.Button(main_window, text='Tune', font='sans 16 bold', command=function)
    tunning_button.place(x=803 , y=535,relwidth=0.3,relheight=0.1,anchor='n')

    return tunning_button

def save_button(function):
    # Make tunnig button
    save_button = tkinter.Button(main_window, text='Save', font='sans 16 bold', command=function)
    save_button.place(x=803 , y=608,relwidth=0.3,relheight=0.1,anchor='n')

    return tunning_button




def activate():
    frame.pack()
    # Activate mouse corrdinate
    # main_window.bind('<Motion>', mouse_motion_coordinate)
    main_window.mainloop()


# =========try block========
start()
# tank()
# graph()
# control_panel()
# debit_input()
# maximum_liquid_lvl_input()
# gravitation_input()
# valve1_area_input()
# tank_area_input()
# start_button()
# pause_button()
# reset_button()
# activate()
# ==========================
