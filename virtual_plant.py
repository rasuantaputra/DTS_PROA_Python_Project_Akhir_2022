import tkinter
import matplotlib.pyplot as plt
from pip import main
import numpy as np

main_window = tkinter.Tk()

# Besar frame untuk virtual plant
frame = tkinter.Canvas(main_window, bg="white", height=600, width=1000)

# Membuat air dalam tank
frame.create_water_tank(50, 50, 20, 100, fill="blue", outline = 'blue')

frame.pack()
main_window.mainloop()
