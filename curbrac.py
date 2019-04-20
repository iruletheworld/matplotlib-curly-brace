# -*- coding: utf-8 -*- 

'''
'''

# https://stackoverflow.com/questions/1289681/drawing-braces-with-pyx/1290110#1290110
# https://uk.mathworks.com/matlabcentral/fileexchange/38716-curly-brace-annotation

import matplotlib.pyplot as plt
import numpy as np

def curbrac(ax, p1, p2, k_r=0.1, str_text='', int_line_num=2, fontdict={}, **kwargs):
    '''
    '''

    # calculate the angle
    theta = np.arctan2(p2[1] - p1[1], p2[0] - p1[0])

    # calculate the radius of the arcs
    r = np.hypot(p2[0] - p1[0], p2[1] - p1[1]) * k_r

    # arc1 centre
    x11 = p1[0] + r * np.cos(theta)
    y11 = p1[1] + r * np.sin(theta)

    # arc2 centre
    x22 = (p2[0] + p1[0]) / 2.0 - 2.0 * r * np.sin(theta) - r * np.cos(theta)
    y22 = (p2[1] + p1[1]) / 2.0 + 2.0 * r * np.cos(theta) - r * np.sin(theta)

    # arc3 centre
    x33 = (p2[0] + p1[0]) / 2.0 - 2.0 * r * np.sin(theta) + r * np.cos(theta)
    y33 = (p2[1] + p1[1]) / 2.0 + 2.0 * r * np.cos(theta) + r * np.sin(theta)

    # arc4 centre
    x44 = p2[0] - r * np.cos(theta)
    y44 = p2[1] - r * np.sin(theta)

    # prepare the rotated
    q = np.linspace(theta, theta + np.pi/2.0, 50)

    # reverse q
    t = np.flip(q)

    # arc coordinates
    arc1x = r * np.cos(t + np.pi/2.0) + x11
    arc1y = r * np.sin(t + np.pi/2.0) + y11

    arc2x = r * np.cos(q - np.pi/2.0) + x22
    arc2y = r * np.sin(q - np.pi/2.0) + y22

    arc3x = r * np.cos(q + np.pi) + x33
    arc3y = r * np.sin(q + np.pi) + y33

    arc4x = r * np.cos(t) + x44
    arc4y = r * np.sin(t) + y44

    # plot arcs
    ax.plot(arc1x, arc1y, **kwargs)
    ax.plot(arc2x, arc2y, **kwargs)
    ax.plot(arc3x, arc3y, **kwargs)
    ax.plot(arc4x, arc4y, **kwargs)

    # plot lines
    ax.plot([arc1x[-1], arc2x[1]], [arc1y[-1], arc2y[1]], **kwargs)
    ax.plot([arc3x[-1], arc4x[1]], [arc3y[-1], arc4y[1]], **kwargs)

    summit = [arc2x[-1], arc2y[-1]]

    if str_text:

        int_line_num = int(int_line_num)

        str_temp = '\n' * int_line_num
        
        # conver radians to degree and within 0 to 360
        ang = np.degrees(theta) % 360.0

        if (ang >= 0.0) and (ang <= 90.0):

            rotation = ang

            str_text = str_text + str_temp

        if (ang > 90.0) and (ang < 270.0):

            rotation = ang + 180.0

            str_text = str_temp + str_text

        elif (ang >= 270.0) and (ang <= 360.0):

            rotation = ang

            str_text = str_text + str_temp

        ax.axes.text(arc2x[-1], arc2y[-1], str_text, ha='center', va='center', rotation=rotation, fontdict=fontdict)

    else:

        pass

    return theta, summit