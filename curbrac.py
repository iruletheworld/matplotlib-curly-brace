# -*- coding: utf-8 -*- 

# https://stackoverflow.com/questions/1289681/drawing-braces-with-pyx/1290110#1290110
# https://uk.mathworks.com/matlabcentral/fileexchange/38716-curly-brace-annotation

import matplotlib.pyplot as plt
import numpy as np
# import math






def curbrac(ax, p1, p2, k_r, lw=2, color='r'):

    # theta = np.arctan2(y_end-y_start, x_end-x_start)
    theta = np.arctan2(p2[1] - p1[1], p2[0] - p1[0])

    r = np.hypot(p2[0] - p1[0], p2[1] - p1[1]) * k_r

    x_brace1 = p1[0] + r * (np.cos(theta) - np.sin(theta))
    y_brace1 = p1[1] + r * (np.sin(theta) + np.cos(theta))

    x_brace2 = p2[0] - r * (np.cos(theta) + np.sin(theta))
    y_brace2 = p2[1] - r * (np.sin(theta) - np.cos(theta))

    x11 = p1[0] + r * np.cos(theta)
    y11 = p1[1] + r * np.sin(theta)

    x22 = (p2[0] + p1[0]) / 2.0 - 2.0 * r * np.sin(theta) - r * np.cos(theta)
    y22 = (p2[1] + p1[1]) / 2.0 + 2.0 * r * np.cos(theta) - r * np.sin(theta)

    x33 = (p2[0] + p1[0]) / 2.0 - 2.0 * r * np.sin(theta) + r * np.cos(theta)
    y33 = (p2[1] + p1[1]) / 2.0 + 2.0 * r * np.cos(theta) + r * np.sin(theta)

    x44 = p2[0] - r * np.cos(theta)
    y44 = p2[1] - r * np.sin(theta)

    q = np.linspace(theta, theta + np.pi/2.0, 50)

    t = q[::-1]

    arc1x = r * np.cos(t + np.pi/2.0) + x11
    arc1y = r * np.sin(t + np.pi/2.0) + y11

    arc2x = r * np.cos(q - np.pi/2.0) + x22
    arc2y = r * np.sin(q - np.pi/2.0) + y22

    arc3x = r * np.cos(q + np.pi) + x33
    arc3y = r * np.sin(q + np.pi) + y33

    arc4x = r * np.cos(t) + x44
    arc4y = r * np.sin(t) + y44


    axes.plot([x_brace1, arc2x[0]], [y_brace1, arc2y[0]], lw=2, color='k')
    axes.plot([x_brace2, arc3x[-1]], [y_brace2, arc3y[-1]], lw=2, color='k')

    axes.plot(arc1x, arc1y, lw=2, color='k')
    axes.plot(arc2x, arc2y, lw=2, color='k')
    axes.plot(arc3x, arc3y, lw=2, color='k')
    axes.plot(arc4x, arc4y, lw=2, color='k')

    # plt.show()


c = np.linspace(0, 2.0 * np.pi, 101)

ang = 0.0

l = 10.0

x = l * np.cos(c)
y = l * np.sin(c)

fig, axes = plt.subplots(1, 1)

axes.plot(x, y)
axes.set_aspect('equal', 'box')

axes.grid()

k_r = 0.1
# k_d = 0.5

# x_start = 1.0
# y_start = 2.0

# x_end = 2.15
# y_end = -5.0

p1 = [1.0, 2.0]
p2 = [2.7, 5.0]

curbrac(axes, p1, p2, k_r)

plt.show()