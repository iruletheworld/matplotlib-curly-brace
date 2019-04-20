# -*- coding: utf-8 -*- 

'''
'''

import matplotlib.pyplot as plt
import numpy as np
from curbrac import curbrac

# figure size and dpi
dbl_width   = 1000.0
dbl_height  = 1080.0
dbl_dpi     = 100.0

# line width and colour for the circles
lw = 2
color='royalblue'

# plot the two concentrate circles
theta = np.linspace(0, 2.0 * np.pi, 101)

# the radius for the circles
r1 = 5.0
r2 = 15.0

# the points of the circles
x1 = r1 * np.cos(theta)
y1 = r1 * np.sin(theta)

x2 = r2 * np.cos(theta)
y2 = r2 * np.sin(theta)

# fig1, axes1 = plt.subplots(1, 1, figsize=(dbl_width / dbl_dpi, dbl_height / dbl_dpi), dpi=dbl_dpi)
fig, axes = plt.subplots(2, 1, figsize=(dbl_width / dbl_dpi, dbl_height / dbl_dpi), dpi=dbl_dpi)
# fig2, axes2 = plt.subplots(1, 1, figsize=(dbl_width / dbl_dpi, dbl_height / dbl_dpi), dpi=dbl_dpi)

# fontdict for axis titles
font = {'family': 'Arial',
        'color':  'k',
        'weight': 'bold',
        'style': 'normal',
        'size': 12,
        }

str_title1 = 'Example: Anti-Clockwise for a a pair of concentrate circles'
str_title2 = 'Example: Clockwise for a a pair of concentrate circles'

axes[0].plot(x1, y1, lw=lw, color=color)
axes[0].plot(x2, y2, lw=lw, color=color)
axes[1].plot(x1, y1, lw=lw, color=color)
axes[1].plot(x2, y2, lw=lw, color=color)

axes[0].set_aspect('equal', 'box')
axes[0].grid(color='lightgray', linestyle='--')
axes[0].set_title(str_title1, fontdict=font)
axes[1].set_aspect('equal', 'box')
axes[1].grid(color='lightgray', linestyle='--')
axes[1].set_title(str_title2, fontdict=font)

# bracket coefficient
k_r = 0.1

# points for the brackets
phi = np.linspace(0, 2.0 * np.pi, 13)

x1 = r1 * np.cos(phi)
y1 = r1 * np.sin(phi)

x2 = r2 * np.cos(phi)
y2 = r2 * np.sin(phi)

# fontdict for the brackets
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'style': 'normal',
        'size': 9,
        }

lw = 3

for i in range(0, len(x1)):

    p1 = [x1[i], y1[i]]
    p2 = [x2[i], y2[i]]

    str_text = 'Circle\nanti-clockwise'

    theta, pt = curbrac(axes[0], p1, p2, k_r, str_text=str_text, color='r', lw=lw, int_line_num=2, fontdict=font)

for i in range(0, len(x1)):

    p1 = [x2[i], y2[i]]
    p2 = [x1[i], y1[i]]

    str_text = 'Circle\nclockwise'

    theta, pt = curbrac(axes[1], p1, p2, k_r, str_text=str_text, color='r', lw=lw, int_line_num=2, fontdict=font)

plt.show()