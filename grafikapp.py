from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

root = Tk()
root.title("Aplikasi Grafik Trigonometri")
root.resizable(width=False,height=False)

WIDTH = 1200
HEIGHT = 700
canvas = Canvas(root, width=WIDTH,height=HEIGHT, bg='lightblue')
canvas.pack()

def bikingrafik():
    a = int(aInput.get())
    b = int(bInput.get())
    c = int(cInput.get())
    xmin = int(xminInput.get())
    xmax = int(xmaxInput.get())

    x = np.linspace(np.pi * xmin, np.pi * xmax, 1000)

    if yInput.get()==yvalues[0]:
        y = c + a*(np.sin(x)**b)
        ax.plot(x, y)
    if yInput.get()==yvalues[1]:
        y = c + a*(np.cos(x)**b)
        ax.plot(x, y)
    if yInput.get()==yvalues[2]:
        y = c + a*(np.tan(x)**b)
        ax.plot(x, y)

    canvasGrafik.draw()


def resetgrafik():
    global ax

    ax.clear()
    ax.set_title('Grafik Trigonometri')
    ax.set_xlabel('x dalam satuan pi')
    ax.set_ylabel('y')
    ax.grid(True)

    canvasGrafik.draw()


frameInput = Frame(root, bg='#074447')
frameInput.place(relx=0.025,rely=0.5,relwidth=0.25,relheight=0.7,anchor='w')

yvalues = ("c + a sin(x)^b",
           "c + a cos(x)^b",
           "c + a tan(x)^b")

ylabel = Label(frameInput, bg='#074447', text='y', fg='white')
ylabel.place(relx=0.1,rely=0,relwidth=0.2,relheight=0.125,anchor='n')
yInput = Spinbox(frameInput, values=yvalues)
yInput.place(relx=0.5,rely=0.025,relwidth=0.6,relheight=0.08,anchor='n')

alabel = Label(frameInput, bg='#074447', text='a', fg='white')
alabel.place(relx=0.1,rely=0.125,relwidth=0.2,relheight=0.125,anchor='n')
aInput = Entry(frameInput)
aInput.place(relx=0.5,rely=0.15,relwidth=0.6,relheight=0.08,anchor='n')
aInput.insert(0,1)

blabel = Label(frameInput, bg='#074447', text='b', fg='white')
blabel.place(relx=0.1,rely=0.25,relwidth=0.2,relheight=0.125,anchor='n')
bInput = Entry(frameInput)
bInput.place(relx=0.5,rely=0.275,relwidth=0.6,relheight=0.08,anchor='n')
bInput.insert(0,1)

clabel = Label(frameInput, bg='#074447', text='c', fg='white')
clabel.place(relx=0.1,rely=0.375,relwidth=0.2,relheight=0.125,anchor='n')
cInput = Entry(frameInput)
cInput.place(relx=0.5,rely=0.4,relwidth=0.6,relheight=0.08,anchor='n')
cInput.insert(0,0)

xlabel = Label(frameInput, bg='#074447', text='x', fg='white')
xlabel.place(relx=0.1,rely=0.5,relwidth=0.2,relheight=0.125,anchor='n')
xfromlabel = Label(frameInput,text='from',bg='#074447',fg='white')
xfromlabel.place(relx=0.2,rely=0.525,relwidth=0.1,relheight=0.08,anchor='n')
xminInput = Entry(frameInput)
xminInput.place(relx=0.35,rely=0.525,relwidth=0.15,relheight=0.08,anchor='n')
xminInput.insert(0,-2)
xtolabel = Label(frameInput,text='pi to',bg='#074447',fg='white')
xtolabel.place(relx=0.5,rely=0.525,relwidth=0.1,relheight=0.08,anchor='n')
xmaxInput = Entry(frameInput)
xmaxInput.place(relx=0.65,rely=0.525,relwidth=0.15,relheight=0.08,anchor='n')
xmaxInput.insert(0,2)
xpilabel = Label(frameInput,text='pi',bg='#074447',fg='white')
xpilabel.place(relx=0.8,rely=0.525,relwidth=0.1,relheight=0.08,anchor='n')

enter_button = Button(frameInput, text='Enter', command=bikingrafik)
enter_button.place(relx=0.5,rely=0.7,relwidth=0.3,relheight=0.1,anchor='n')

reset_button = Button(frameInput, text='Reset', command=resetgrafik)
reset_button.place(relx=0.5,rely=0.85,relwidth=0.3,relheight=0.1,anchor='n')

frameGrafik = Frame(root, bg='white')
frameGrafik.place(relx=1,rely=0.5,relwidth=0.7,relheight=1,anchor='e')

f = Figure()
ax = f.add_subplot(111)

ax.set_title('Grafik Trigonometri')
ax.set_xlabel('x dalam satuan pi')
ax.set_ylabel('y')
ax.grid(True)

canvasGrafik = FigureCanvasTkAgg(f, frameGrafik)
canvasGrafik.get_tk_widget().place(relheight=1,relwidth=1)
canvasGrafik.draw()











root.mainloop()