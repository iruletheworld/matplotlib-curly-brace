"""Simple example of curlyBrace with automatic colors.

Author: Markus Reinert
Last Modified: 2022-03-23
"""

import matplotlib.pyplot as plt

from curlyBrace import curlyBrace


save_figure = False


fig, ax = plt.subplots()
ax.set_ylim(2, 12)
ax.set_xlim(-1, 1)
for i in range(12):
    # The color of the curlyBrace is not given explicitly,
    # but determined automatically by matplotlib's color rotation
    curlyBrace(fig, ax, (-1, i), (1, i))

if save_figure:
    import os
    fig.savefig(os.path.basename(__file__).replace(".py", ".png"))

plt.show()
