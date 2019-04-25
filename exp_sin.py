# -*- coding: utf-8 -*- 

'''
Author : 高斯羽 博士 (Dr. GAO, Siyu)

Version : 1.0.0

Last Modified : 2019-04-22

This script is an example to demonstration how to use the "curlyBrace" module to plot curly brackets using matplotlib.

This example demonstrate annotating two sine waves with the auto scale on and off.
'''

import matplotlib.pyplot as plt
import numpy as np
from curlyBrace import curlyBrace
import os

# save fig control
bool_savefig = False

# figure size and dpi
dbl_width   = 800.0
dbl_height  = 800.0
dbl_dpi     = 100.0

# line width and colour for the sine wave
lw = 2
color='royalblue'

# plot the sine wave
theta = np.linspace(0.0, 2.0 * np.pi, 101)

x = theta
y = np.sin(theta) * 8.0

fig, axes = plt.subplots(2, 1 , figsize=(dbl_width / dbl_dpi, dbl_width / dbl_dpi), dpi=dbl_dpi)

# fontdict for axis title
font = {'family': 'Arial',
        'color':  'k',
        'weight': 'bold',
        'style': 'normal',
        'size': 20,
        }

# aixs title string
str_title = [None, None]

str_title[0] = 'Example: Different axes scales, auto scale on'
str_title[1] = 'Example: Different axes scales, auto scale off'

axes[0].set_title(str_title[0], fontdict=font)
axes[0].plot(x, y, lw=lw, color=color)
axes[0].grid(linestyle='--')
axes[0].set_xlim(xmin=0.0, xmax=2.0*np.pi)

axes[1].set_title(str_title[1], fontdict=font)
axes[1].plot(x, y, lw=lw, color=color)
axes[1].grid(linestyle='--')
axes[1].set_xlim(xmin=0.0, xmax=2.0*np.pi)

# curly bracket 1 start point and end point
p1 = [0.0, 0.0]
p2 = [np.pi, 0.0]

# curly bracket 2 start point and end point
p3 = [np.pi, 0.0]
p4 = [2.0 * np.pi, 0.0]

# fontdict for curly bracket 1 text
font = {'family': 'serif',
        'color':  'k',
        'weight': 'bold',
        'style': 'italic',
        'size': 20,
        }

# curly brack text
str_text = '$\pi$'

# coefficient for curly bracket 1
k_r1 = 0.05

# coefficient for curly bracket 2
k_r2 = 0.1

# clockwise, need to swap the start point and end point
curlyBrace(fig, axes[0], p2, p1, k_r1, bool_auto=True, str_text=str_text, color='r', lw=2, int_line_num=1, fontdict=font)

# anti-clockwise, no need to swap the start point and end point
curlyBrace(fig, axes[0], p3, p4, k_r2, bool_auto=True, str_text=str_text, color='darkorange', lw=3, int_line_num=1, fontdict=font)

# clockwise, need to swap the start point and end point
curlyBrace(fig, axes[1], p2, p1, k_r1, bool_auto=False, str_text=str_text, color='m', lw=2, int_line_num=1, fontdict=font)

# anti-clockwise, no need to swap the start point and end point
curlyBrace(fig, axes[1], p3, p4, k_r2, bool_auto=False, str_text=str_text, color='darkgreen', lw=3, int_line_num=1, fontdict=font)

# save fig
if bool_savefig:

    str_filename = os.path.basename(__file__)[:-3] + '.png'

    str_filename = os.path.join(os.getcwd(), str_filename)

    fig.savefig(str_filename, bbox_inches='tight', dpi=300)

else:

    pass

plt.show()