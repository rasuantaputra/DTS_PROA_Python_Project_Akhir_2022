from asyncio import constants
from cProfile import run
from cmath import inf, pi, tan
from itertools import count
from pdb import line_prefix
from queue import LifoQueue
from re import A
from time import process_time
from timeit import repeat
from wsgiref import handlers
from gui_vp import *
import csv

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
dt = 0

set_point = 0

kp = 0
ki = 0
kd = 0
controll_output = 0
# ==================================================
# ====================state=========================
h = 0
t = 0
# ====================graph plot====================
time = []
pv = []
sp = []
# ===================================================
# ====================runge kutta 45=================
dt = 0.1

# ===============PID Controll======================

def pid_controller(sp, kp, ki, kd):
    global controll_output, h

    error = h - sp
    error_integral = 0
    eint = error_integral
    error_previous = 0

    derivative = (error - error_previous)/dt
    eint = eint + error * dt

    error_previous = error
    error_integral = eint
    controll_output = (kp * error) + (ki * eint) + (kd * derivative)
# ==================================================
# ===================Model==========================

def dh_dt(q1, q2, area):
    return (q1 - q2)/area

def count():
    global h, t, valve1, test_valve, pipe1, pipe2, tank_area, h0
    
    q1 = (valve1/100) * pipe1 * debit
    q2 = controll_output * pipe2 * np.sqrt(2 * gravitation) * math.sqrt(h)

    k1 = dt * dh_dt(q1, q2, tank_area)
    k2 = dt * dh_dt(q1 + dt/4, q2 + k1/4, tank_area)
    k3 = dt * dh_dt(q1 + (3/8 * dt), q2 + (3/32 * k1) + (9/32 * k2), tank_area)
    k4 = dt * dh_dt(q1 + (12/13 * dt), q2 + (1932/2197 * k1) - (7200/2197 * k2) + (7296/2197 * k3), tank_area)
    k5 = dt * dh_dt(q1 + dt, q2 + (439/216 * k1) - (8 * k2) + (3680/513 * k3) - (845/4104 * k4), tank_area)
    k6 = dt * dh_dt(q1 + (dt/2), q2 - (8/27 * k1) + (2 * k2) - (3544/2565 * k3) + (1859/4104 * k4) - (11/40 * k5), tank_area)

    h = h + (16/135 * k1) + (6656/12825 * k3) + (28561/56430 * k4) + (9/50 * k5) + (2/55 * k6)
    # h = h + dh_dt(q1, q2, tank_area) * dt
    t = t + dt

    if h >= 1:
        h = 1
    elif h <= 0:
        h = 0
    
    pv.append(h)
    time.append(t)

    print('set poin = ', set_point)
    print('valve1 = ', valve1, 'controller = ', controll_output)
    print('q1 = ', q1, 'q2 = ', q2)
    print('pv = ',h, 'time =', t)

# ============Tunning button event=================
def on_tuning():
    global debit, liquid, gravitation, valve1, test_valve, tank_area, set_point, proportional, integral, derivative, pipe1, pipe2, dt, set_point, kp, ki, kd

    debit = float(constants[0].get())
    liquid = float(constants[1].get())
    gravitation = float(constants[2].get())
    valve1 = float(constants[3].get())
    pipe1 = float(constants[4].get())
    pipe2 = float(constants[5].get())
    dt = float(constants[6].get())
    tank_area = float(constants[7].get())

    set_point = float(pid_control[0].get())
    kp = float(pid_control[1].get())
    ki = float(pid_control[2].get())
    kd = float(pid_control[3].get())

tunning_button(on_tuning)
# =============================
# =======Liquid Animation=========
# nomor = 1
# ukuran = 335

# def awal():
#     global nomor, ukuran

#     if nomor < 3000:
#         tank(ukuran)
#         nomor +=1
#         ukuran -= 5
#         x.append(nomor)
#         y.append(np.sin(nomor))
#     # frame.after(10, awal)

# liquid_animation = 344 * (1 - h)

def tank_animation():
    global h
    liquid_animation = 344 - (185 * h)
    tank(liquid_animation)
    # frame.after(10, awal)

# =============================
# ====start, paused, reset, save=====
running = False
flag = True

def start_app():
   global h
   if running:
      pid_controller(set_point, kp, ki, kd)
      count()
      tank_animation()
      graph(time, pv)
    
  
   frame.after(200, start_app)

if flag:    
    pid_controller(set_point, kp, ki, kd)
    count()
    tank_animation()
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
    filename = asksaveasfilename(filetype=[('CSV files', '*.csv')])
    if filename:
        data = {'Time': time, 'PV': pv}

        df = pd.DataFrame(data)
        #df.to_csv(filename, header=False, index=False)
        df.to_csv(filename, index=False)


start_button(on_start)
pause_button(on_stop)
reset_button(on_reset)
save_button(on_save)

control_panel()
activate()