from asyncio import constants
from cProfile import run
from cmath import inf, tan
from itertools import count
from pdb import line_prefix
from queue import LifoQueue
from re import A
from time import process_time
from timeit import repeat
from gui_vp import *

# =======tuning=========
# gravitation = tkinter.Entry(main_window)
# gravitation.pack()
# gravitation.place(x=479 , y=479)

constants = (    
    debit_input(),
    maximum_liquid_lvl_input(),
    gravitation_input(),
    valve1_area_input(),
    pipe1_area_input(),
    pipe2_area_input(),
    sampling_time_input(),
    tank_area_input()
)

pid_control = (
    set_point_input(),
    proportional_input(),
    integral_input(),
    derivative_input()
)
# ==================== Variabel ====================
debit = 0
liquid = 0
gravitation = 0
valve1 = 0
test_valve = 0
tank_area = 0.7
pipe1 = 0
pipe2 = 0

set_point = 0

proportional = 0
integral = 0
derivative = 0
# ==================================================
# ====================state=========================
h = 0.5
t = 0
# ====================graph plot====================
time = []
pv = []
# ===================================================
# ====================runge kutta 45=================
dt = 0.1

# q1 = (valve1/10) * debit
# if test_valve == 0:
#     q2 = 0
# else:
#     q2 = (test_valve/10) * np.sqt(2 * gravitation) * np.sqrt(h) 


def dh_dt(q1, q2):
    return (q1 - q2)/tank_area

def count():
    global h, t, valve1, test_valve

    if test_valve == 0:
        q2 = 0
        q1 = 0
    else:
        q1 = (valve1/10) * debit
        q2 = (test_valve/10) * np.sqrt(2 * gravitation) * np.sqrt(h)

    k1 = dt * dh_dt(q1, q2)
    k2 = dt * dh_dt(q1 + dt/4, q2 + k1/4)
    k3 = dt * dh_dt(q1 + (3/8 * dt), q2 + (3/32 * k1) + (9/32 * k2))
    k4 = dt * dh_dt(q1 + (12/13 * dt), q2 + (1932/2197 * k1) - (7200/2197 * k2) + (7296/2197 * k3))
    k5 = dt * dh_dt(q1 + dt, q2 + (439/216 * k1) - (8 * k2) + (3680/513 * k3) - (845/4104 * k4))
    k6 = dt * dh_dt(q1 + (dt/2), q2 - (8/27 * k1) + (2 * k2) - (3544/2565 * k3) + (1859/4104 * k4) - (11/40 * k5))

    h = h + (16/135 * k1) + (6656/12825 * k3) + (28561/56430 * k4) + (9/50 * k5) + (2/55 * k6)
    t = t + dt

    pv.append(h)
    time.append(t)
    print('valve1 = ', (valve1/10), 'valve2 = ', (test_valve/10))
    print('pv = ',h, 'time =', t)








# ============Tunning button event=================
# val = tkinter.StringVar(main_window, value=1)
# valve2 = tkinter.Entry(main_window,textvariable=val)
# valve2.pack()

def on_tuning():
    global debit, liquid, gravitation, valve1, test_valve, tank_area, set_point, proportional, integral, derivative

    debit = float(constants[0].get())
    liquid = float(constants[1].get())
    gravitation = float(constants[2].get())
    valve1 = float(constants[3].get())
    tank_area = float(constants[4].get())
    # test_valve = float(valve2.get())

tunning_button(on_tuning)
# =============================
# =======Liquid Animation=========
nomor = 1
ukuran = 335


def awal():
    global nomor, ukuran

    if nomor < 3000:
        tank(ukuran)
        nomor +=1
        ukuran -= 5
        x.append(nomor)
        y.append(np.sin(nomor))
    # frame.after(10, awal)
# =============================
# =========Graph animation==========
x = []
y = []


# =============================
# ====start, paused, reset=====
running = False
flag = True

def start_app():
   if running:
      awal()
      count()
    #   graph(x, y)
      graph(time, pv)
  
   frame.after(200, start_app)

if flag:
    awal()
    graph(time, pv)

def on_start():
   global running, flag
   running = True
   flag = False

def on_stop():
   global running, flag
   running = False
   flag = True

frame.after(0, start_app)

def on_reset():
    global running
    running = False
    time.clear()
    pv.clear()

def on_save():
    return None
start_button(on_start)
pause_button(on_stop)
reset_button(on_reset)
save_button()

control_panel()
activate()