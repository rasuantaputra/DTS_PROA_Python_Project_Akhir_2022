import tkinter
from venv import create

main_window = tkinter.Tk()

# Virtual plant frame size
frame = tkinter.Canvas(main_window, bg="white", height=600, width=1000)
# take Tank.png image
img = tkinter.PhotoImage(file="img\Tank.png")

# mose motion function for definding coordinate
def mouse_motion_coordinate(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

def tank_image():
    # Insert tank image
    frame.create_image(320,360, image=img)
    # valve 1 (x1, y1, x2, y2, x3, y3, x4, y4, x5, y5)
    # frame.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5)
    # valve 2 (x1, y1, x2, y2, x3, y3, x4, y4, x5, y5)
    # frame.create_polygon()
    
# liquid = (level - x)/level
def liquid(level=310):
    # Make linquid inside tank
    frame.create_rectangle(174, level, 383, 518, fill="blue", outline = 'blue')

# =========try block========
tank_image()
liquid()
# ==========================
frame.pack()

# Activate mouse corrdinate
main_window.bind('<Motion>', mouse_motion_coordinate)
main_window.title('Tugas DTS Kominfo 2022')
main_window.mainloop()
