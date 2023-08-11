import numpy as np
import pandas as pd  # think this would be used if I were to read data in from a csv or xcel file. Making a 'dataframe'
import matplotlib.pyplot as plt  # pyplot is a specific (function?) "module" of matplotlib that works like MATlab stuff.

""" Test plot section. Test

#Data for plotting
t = np.arange(0.01,1.00,.01)  #time range, 0 to 1 second, .01 sec intervals
s = 1+ np.sin(2*np.pi*t)    #simple sine wave graph. 

fig, ax = plt.subplots()
ax.plot(t, s)               # x axis, y axis.

ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='Sinwave Test Graph')
ax.grid()

fig.savefig("Graphs & Plots/test.png")    #save plot as a png file somewhere.
plt.show()
"""

# Impact Analysis

# Time
t = np.arange(0.01, 1.50, .01)    # Also the impact duration, technically. Seconds.

# Constants and Assumptions
Yw = 64             # Specific Weight of Water,     lbf/ft^3
a_g = 32.2          # Acceleration due to gravity,  ft/s^2

# Panel Properties
Hp = 3.94                       # Height of Panel,              ft
Wp = 6.89                       # Width of Panel,               ft, verify this with shop dwgs.
SigmaMax = 6.54                 # [] of Plywood,   Ksi
C_d = 2.0                       # Coefficient of Drag,          --
Ply_th = .069                   # Plywood Thickness             ft
H_s1 = 2.1                      # Height of first strut row, from bottom up. ft
# H_s2 = x

# Stuff that varies (find better name), also things to make into a range at some point.
Hw = Hp                         # Height of Water,                      ft, set to be same as Hw for now.
Vw = 5                          # Velocity of Water,                    ft/s
Vi = Vw                         # Object Impact Velocity, = Vw for now. ft/s
W_o = 1000                      # Impact Object weight                  lbf
SM_p = (Wp * (Ply_th ** 2)) / 6  # Section Modulus of Plywood,           ft^3

# Pressures & Forces on panel
Dh = (C_d * (Vw ** 2)) / (2 * a_g)

P_dyn = Dh * Yw                 # Dynamic Pressure,                     lbf/ft^2
Qx_w = P_dyn * Wp               # Dynamic Force, per unit width         lbf/ft

Ps_max = Yw * Hw                # Maximum Static Pressure               lbf/ft^2
Wx_w = Ps_max * Wp              # Static Force, per unit width          lbf/ft^2

F_s = ((Ps_max * Hw) / 2) * Wp  # Static Force on panel                 lbf
F_d = P_dyn * Hw * Wp           # Dynamic Force on panel                lbf

# May need to make into a loop, or some type of data frame.
F_i = (W_o * Vi) / (a_g * t)    # Force of Impact, as a func of time    lbf
B_y = ((Wx_w * ((Hw ** 2) / 6)) + (Qx_w * ((Hw ** 2) / 2)) + ((F_i * Hw) / H_s1))   # Reaction force at point B
A_y = ((Wx_w * (Hw ** 2)) + (Qx_w * Hw) + (F_i) - (B_y))                            # Reaction force at point A

#Moments and Bending Stress

d = np.arange(0.0, Hp, .01)         # Distance along vertical panel component,    ft
w_x = (Ps_max - (Yw * d)) * Wp      # Static Force, along panel height          lbf/ft
#Moment
M_x_a =
M_x_b =
M_x = # two diff components. Before and after strut.                            lbf*ft


# plotting
fig, ax = plt.subplots()
ax.plot(t, F_i, label='Impact Force')
ax.plot(t, B_y, label='Reaction at B')               # x axis, y axis.
ax.plot(t, A_y, label='Reaction at A')

ax.set(xlabel='Impact Duration (s)', ylabel='Force, (lbf)', title='Reaction forces vs. Impact Duration')
ax.grid()
ax.legend(loc='upper right')

fig.savefig("Graphs & Plots/Forces_1.png")    #save plot as a png file somewhere.
plt.show()