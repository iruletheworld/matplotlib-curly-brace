# -*- coding: utf-8 -*- 

# https://stackoverflow.com/questions/1289681/drawing-braces-with-pyx/1290110#1290110
# https://uk.mathworks.com/matlabcentral/fileexchange/38716-curly-brace-annotation

import matplotlib.pyplot as plt
import numpy as np
import math


c = np.linspace(0, 2.0*math.pi, 101)

ang = 0.0

l = 10.0

x = l * np.cos(c)
y = l * np.sin(c)

fig, axes = plt.subplots(1, 1)

axes.plot(x, y)
axes.set_aspect('equal', 'box')

axes.grid()

k_r = 0.1
k_d = 0.25

x_start = 1.0
y_start = 2.0

x_end = 2.15 
y_end = -5.0 

theta = math.atan2(y_end-y_start, x_end-x_start)

r = math.hypot(x_end-x_start, y_end-y_start) * k_r

d = r * k_d

x_brace1 = x_start + r * (math.cos(theta) - math.sin(theta))
y_brace1 = y_start + r * (math.sin(theta) + math.cos(theta))

x_brace2 = x_end - r * (math.cos(theta) + math.sin(theta))
y_brace2 = y_end - r * (math.sin(theta) - math.cos(theta))

x_mid = (x_end + x_start) / 2.0 - (r + d) * math.sin(theta)
y_mid = (y_end + y_start) / 2.0 + (r + d) * math.cos(theta)

x_ang1 = (x_end + x_start) / 2.0 - r * math.sin(theta) - d * math.cos(theta)
y_ang1 = (y_end + y_start) / 2.0 + r * math.cos(theta) - d * math.sin(theta)

x_ang2 = (x_end + x_start) / 2.0 - r * math.sin(theta) + d * math.cos(theta)
y_ang2 = (y_end + y_start) / 2.0 + r * math.cos(theta) + d * math.sin(theta)

# axes.plot([x_start, x_end], [y_start, y_end], lw=2, color='r')
# axes.plot([x_start, x_brace1, x_brace2, x_end], [y_start, y_brace1, y_brace2, y_end], lw=2, color='k')


x11 = x_start + r * math.cos(theta)
y11 = y_start + r * math.sin(theta)

x22 = (x_end + x_start) / 2.0 - 2.0 * r * math.sin(theta) - r * math.cos(theta)
y22 = (y_end + y_start) / 2.0 + 2.0 * r * math.cos(theta) - r * math.sin(theta)

x33 = (x_end + x_start) / 2.0 - 2.0 * r * math.sin(theta) + r * math.cos(theta)
y33 = (y_end + y_start) / 2.0 + 2.0 * r * math.cos(theta) + r * math.sin(theta)

x44 = x_end - r * math.cos(theta)
y44 = y_end - r * math.sin(theta)

q = np.linspace(theta, theta + math.pi/2.0, 50)

t = q[::-1]

arc1x = r * np.cos(t+math.pi/2.0) + x11
arc1y = r * np.sin(t+math.pi/2.0) + y11

arc2x = r * np.cos(q-math.pi/2.0) + x22
arc2y = r * np.sin(q-math.pi/2.0) + y22

arc3x = r * np.cos(q+math.pi) + x33
arc3y = r * np.sin(q+math.pi) + y33

arc4x = r * np.cos(t) + x44
arc4y = r * np.sin(t) + y44


axes.plot([x_brace1, arc2x[0]], [y_brace1, arc2y[0]], lw=2, color='k')
axes.plot([x_brace2, arc3x[-1]], [y_brace2, arc3y[-1]], lw=2, color='k')

axes.plot(arc1x, arc1y, lw=2, color='k')
axes.plot(arc2x, arc2y, lw=2, color='k')
axes.plot(arc3x, arc3y, lw=2, color='k')
axes.plot(arc4x, arc4y, lw=2, color='k')

plt.show()
