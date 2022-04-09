from email.mime import image
import tkinter
import matplotlib.pyplot as plt
import numpy as np

main_window = tkinter.Tk()

# Virtual plant frame size
frame = tkinter.Canvas(main_window, bg="white", height=600, width=1000)

img = tkinter.PhotoImage(file="img\Tank.png")
frame.create_image(300,300, image=img)




frame.pack()
main_window.title('Virtual Plant DTS Kominfo 2022')
main_window.mainloop()
