'''
'''

import matplotlib.pyplot as plt
import numpy as np
from curbrac import curbrac

dbl_width   = 1000.0
dbl_height  = 720.0
dbl_dpi     = 100.0

lw = 2
color='royalblue'

k_r1 = 0.02

c = np.linspace(0, 2.0 * np.pi, 101)

x = c
y = np.sin(c)

fig, axes = plt.subplots(1, 1 , figsize=(dbl_width / dbl_dpi, dbl_width / dbl_dpi), dpi=dbl_dpi)

font = {'family': 'Arial',
        'color':  'k',
        'weight': 'bold',
        'style': 'normal',
        'size': 20,
        }

str_title = 'Example: Annotating a Sine wave'

axes.set_title(str_title, fontdict=font)

axes.plot(x, y, lw=lw, color=color)
axes.set_aspect('equal', 'box')
axes.grid(color='lightgray', linestyle='--')
axes.set_xlim(xmin=0.0, xmax=2.0*np.pi)

p1 = [0.0, 0.0]
p2 = [np.pi, 0.0]

font = {'family': 'serif',
        'color':  'k',
        'weight': 'bold',
        'style': 'italic',
        'size': 20,
        }

str_text = '$\pi$\n'

curbrac(axes, p2, p1, k_r1, str_text=str_text, int_line_num=2, fontdict=font)

k_r2 = 0.1

p1 = [np.pi, 0.0]
p2 = [2.0 * np.pi, 0.0]

str_text = '\n$2\pi$'

curbrac(axes, p1, p2, k_r2, str_text=str_text, color='darkorange', int_line_num=2, fontdict=font)

plt.show()