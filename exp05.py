# -*- coding: utf-8 -*- 

'''
Author : 高斯羽 博士 (Dr. GAO, Siyu)

Version : 1.0.0

Last Modified : 2019-04-22

This script is an example to demonstration how to use the "curlyBrace" module to 
plot curly brackets using matplotlib.

This example demonstrate the function works on log scale as well.

But the result on "symlog" is not satisfactory.
'''

import numpy as np
import matplotlib.pyplot as plt
from curlyBrace import curlyBrace

# figure size and dpi
dbl_width   = 800.0
dbl_height  = 800.0
dbl_dpi     = 100.0
lw = 3

# make data
x = np.linspace(-100, 100, 201)
y = 2.0 * x

# points
p1 = [-67.87, -50]
p2 = [75.12, 151.6]

p3 = [20.0, 27.58]
p4 = [87.8, 115.95]

# fontdict for axis title
font = {'family': 'Arial',
        'color':  'k',
        'weight': 'bold',
        'style': 'normal',
        'size': 14
        }

fig, axes = plt.subplots(2, 1, figsize=(dbl_width / dbl_dpi, dbl_width / dbl_dpi), dpi=dbl_dpi)

# linear
axes[0].plot(x,y, lw=lw)
axes[0].set_title('Linear Scale', fontdict=font)
axes[0].grid(True)

curlyBrace(fig, axes[0], p1, p2, k_r=0.1, str_text='Linear', int_line_num=2, color='r', lw=2)

# log
axes[1].plot(x,y, lw=lw)
axes[1].set_title('Log Scale', fontdict=font)
axes[1].set_yscale('log')
axes[1].grid(True)

curlyBrace(fig, axes[1], p4, p3, k_r=0.1, str_text='Log', int_line_num=2, color='r', lw=2)

fig.suptitle('Example: Different axes scale', fontweight='bold', fontsize=20)

plt.show()