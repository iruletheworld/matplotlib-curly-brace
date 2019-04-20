# -*- coding: utf-8 -*- 

'''
# epllise
# https://stackoverflow.com/questions/10952060/plot-ellipse-with-matplotlib-pyplot-python
'''

import matplotlib.pyplot as plt
import numpy as np
from curbrac import curbrac

# figure size and dpi
dbl_width   = 1000.0
dbl_height  = 720.0
dbl_dpi     = 100.0

# line width and colour for the epllise
lw = 2
color='royalblue'

u = 0.0  # x-position of the centre
v = 0.0  # y-position of the centre
a1 = 2.0  # radius on the x-axis for epllise 1
b1 = 1.5  # radius on the y-axis for epllise 1
a2 = 7.0  # radius on the x-axis for epllise 2
b2 = 5.5  # radius on the y-axis for epllise 2

theta = np.linspace(0, 2.0 * np.pi, 101)

x1 = u + a1 * np.cos(theta)
y1 = v + b1 * np.sin(theta)
x2 = u + a2 * np.cos(theta)
y2 = v + b2 * np.sin(theta)

fig, axes = plt.subplots(2, 1, figsize=(dbl_width / dbl_dpi, dbl_width / dbl_dpi), dpi=dbl_dpi)

# fontdict for axis titles
font = {'family': 'Arial',
        'color':  'k',
        'weight': 'bold',
        'style': 'normal',
        'size': 12,
        }

str_title1 = 'Example: Anti-Clockwise for a a pair of concentrate epllise'
str_title2 = 'Example: Clockwise for a a pair of concentrate epllise'

axes[0].plot(x1, y1, lw=lw, color=color)
axes[0].plot(x2, y2, lw=lw, color=color)
axes[1].plot(x1, y1, lw=lw, color=color)
axes[1].plot(x2, y2, lw=lw, color=color)

axes[0].set_aspect('equal', 'box')
axes[0].grid(color='lightgray', linestyle='--')
axes[0].set_title(str_title2, fontdict=font)
axes[1].set_aspect('equal', 'box')
axes[1].grid(color='lightgray', linestyle='--')
axes[1].set_title(str_title2, fontdict=font)

# bracket coefficient
k_r = 0.1

# points for the brackets
phi = np.linspace(0, 2.0 * np.pi, 13)

x1 = u + a1 * np.cos(phi)
y1 = v + b1 * np.sin(phi)
x2 = u + a2 * np.cos(phi)
y2 = v + b2 * np.sin(phi)

# fontdict for the brackets
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'style': 'normal',
        'size': 8,
        }

# bracket line width and colour
lw = 3
color = 'r'

for i in range(0, len(x1)):

    p1 = [x1[i], y1[i]]
    p2 = [x2[i], y2[i]]

    str_text = 'Epllise\nanti-clockwise'

    theta, pt = curbrac(axes[0], p1, p2, k_r, str_text=str_text, color=color, lw=lw, int_line_num=3, fontdict=font)

for i in range(0, len(x1)):

    p1 = [x2[i], y2[i]]
    p2 = [x1[i], y1[i]]

    str_text = 'Epllise\nclockwise'

    theta, pt = curbrac(axes[1], p1, p2, k_r, str_text=str_text, color=color, lw=lw, int_line_num=3, fontdict=font)

plt.show()