import tkinter
import matplotlib.pyplot as plt
from pip import main
import numpy as np

main_window = tkinter.Tk()

# Virtual plant frame size
frame = tkinter.Canvas(main_window, bg="white", height=600, width=1000)



frame.pack()
main_window.title('Virtual Plant DTS Kominfo 2022')
main_window.mainloop()
