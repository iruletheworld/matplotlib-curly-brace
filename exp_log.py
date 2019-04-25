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
import os

# fig save control
bool_savefig = False

# figure size and dpi
dbl_width   = 800.0
dbl_height  = 800.0
dbl_dpi     = 100.0
lw = 3

# make data
x = np.linspace(0.1, 100, 200)
y = 2.0 * x

# points
p1 = [20, 10.69]
p2 = [80, 151.6]

# p3 = [20.0, 27.58]
# p4 = [87.8, 115.95]

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

curlyBrace(fig, axes[0], p2, p1, k_r=0.05, str_text='Linear', int_line_num=2, color='r', lw=2)

# log
axes[1].plot(x,y, lw=lw)
axes[1].set_title('Log Scale', fontdict=font)
axes[1].set_yscale('log')
axes[1].grid(True)

curlyBrace(fig, axes[1], p2, p1, k_r=0.05, str_text='Log', int_line_num=2, color='r', lw=2)

fig.suptitle('Example: Log scale', fontweight='bold', fontsize=20)

if bool_savefig:

    str_filename = os.path.basename(__file__)[:-3] + '.png'

    str_filename = os.path.join(os.getcwd(), str_filename)

    fig.savefig(str_filename, bbox_inches='tight', dpi=300)

else:

    pass

plt.show()