"""Simple example of curlyBrace in a figure with inverted y-axis.

Author: Markus Reinert
Last Modified: 2022-03-23
"""

import matplotlib.pyplot as plt

from curlyBrace import curlyBrace


save_figure = False


fig, axs = plt.subplots(ncols=2, figsize=(8, 4))

axs[0].set_title("vertical axis normal")
axs[0].set_ylim(-2, +2)
axs[0].scatter([0, 1], [-0.5, 0.5])
curlyBrace(fig, axs[0], (1, 0.5), (0, -0.5), str_text="Hello curly brace!", color="black")

axs[1].set_title("vertical axis increasing downwards")
axs[1].set_ylim(+2, -2)
axs[1].scatter([0, 1], [-0.5, 0.5])
curlyBrace(fig, axs[1], (1, 0.5), (0, -0.5), str_text="Hello curly brace!", color="black")

if save_figure:
    import os
    fig.savefig(os.path.basename(__file__).replace(".py", ".png"))

plt.show()
