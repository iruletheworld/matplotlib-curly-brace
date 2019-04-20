# -*- coding: utf-8 -*- 

'''
'''

import matplotlib.pyplot as plt
import numpy as np
from curbrac import curbrac

# figure size and dpi
dbl_width   = 1000.0
dbl_height  = 720.0
dbl_dpi     = 100.0

# line width and colour for the sine wave
lw = 2
color='royalblue'

# plot the sine wave
theta = np.linspace(0.0, 2.0 * np.pi, 101)

x = theta
y = np.sin(theta)

fig, axes = plt.subplots(1, 1 , figsize=(dbl_width / dbl_dpi, dbl_width / dbl_dpi), dpi=dbl_dpi)

# fontdict for axis title
font = {'family': 'Arial',
        'color':  'k',
        'weight': 'bold',
        'style': 'normal',
        'size': 20,
        }

# aixs title string
str_title = 'Example: Annotating a sine wave'

axes.set_title(str_title, fontdict=font)

axes.plot(x, y, lw=lw, color=color)
axes.set_aspect('equal', 'box')
axes.grid(color='lightgray', linestyle='--')
axes.set_xlim(xmin=0.0, xmax=2.0*np.pi)

# curly bracket 1 start point and end point
p1 = [0.0, 0.0]
p2 = [np.pi, 0.0]

# fontdict for curly bracket 1 text
font = {'family': 'serif',
        'color':  'k',
        'weight': 'bold',
        'style': 'italic',
        'size': 20,
        }

# curly brack 1 text
str_text = '$\pi$'

# coefficient for curly bracket 1
k_r1 = 0.02

# clockwise, need to swap the start point and end point
curbrac(axes, p2, p1, k_r1, str_text=str_text, color='r', lw=2, linestyle='dashed', int_line_num=1, fontdict=font)

# coefficient for curly bracket 2
k_r2 = 0.1

# curly bracket 2 start point and end point
p1 = [np.pi, 0.0]
p2 = [2.0 * np.pi, 0.0]

str_text = '$\pi$'

# anti-clockwise, no need to swap the start point and end point
curbrac(axes, p1, p2, k_r2, str_text=str_text, color='darkorange', lw=3, int_line_num=1, fontdict=font)

plt.show()