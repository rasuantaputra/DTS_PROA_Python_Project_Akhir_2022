import tkinter
from venv import create
import matplotlib.pyplot as plt
import numpy as np

main_window = tkinter.Tk()

# Virtual plant frame size
frame = tkinter.Canvas(main_window, bg="white", height=600, width=1000)

# Insert tank image
img = tkinter.PhotoImage(file="img\Tank.png")
frame.create_image(320,360, image=img)

# Make linquid inside tank
# liquid = (level - x)/level
def liquid(level=310):
    # frame.create_rectangle(411, 600, 203, 300, fill="blue", outline = 'blue')
    # (x1, y1, x2, y2)
    frame.create_rectangle(174, level, 383, 518, fill="blue", outline = 'blue')

liquid()

frame.pack()
main_window.title('Tugas DTS Kominfo 2022')
main_window.mainloop()
