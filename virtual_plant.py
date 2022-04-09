from email.mime import image
import tkinter
from venv import create
import matplotlib.pyplot as plt
import numpy as np

main_window = tkinter.Tk()

# Virtual plant frame size
frame = tkinter.Canvas(main_window, bg="white", height=600, width=1000)

# Insert tank image
img = tkinter.PhotoImage(file="img\Tank.png")
frame.create_image(300,300, image=img)

# Make linquid inside tank
# liquid = (430 - x)/430
def liquid(level=225):
    # frame.create_rectangle(411, 600, 203, 300, fill="blue", outline = 'blue')
    # (x1, y1, x2, y2)
    frame.create_rectangle(204, level, 411, 432, fill="blue", outline = 'blue')

liquid(430)

frame.pack()
main_window.title('Tugas DTS Kominfo 2022')
main_window.mainloop()
