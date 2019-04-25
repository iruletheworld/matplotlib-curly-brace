Example Codes
======================================

The following are some examples showing what this module is capable of.

Annotating a sine wave
--------------------------------------------------

In this example, since the axes are not "equal", the auto scale should be on.

.. figure:: ../build/html/_sources/img/exp_sin.png
    :alt: Sine wave example
    :scale: 25%

.. literalinclude:: ../exp_sin.py
   :language: python
   :linenos:

Annotating two circles
--------------------------------------------------

The annotation text follows an "aniti-clockwise" convention for its location. To flip it, swap the start point and the end point. Also, since the axes are "equal" in this example, auto scale should be off.

.. figure:: ../build/html/_sources/img/exp_circle.png
    :alt: Cirle example
    :scale: 25%

.. literalinclude:: ../exp_circle.py
   :language: python
   :linenos:

Annotating two ellipses
--------------------------------------------------

Similar to the circle example, but this time demonstrates not "equal" axes and "equal" axes. You should be able to that see the summits of the brackets in the second subplot are kinda warpped.

.. figure:: ../build/html/_sources/img/exp_ellipse.png
    :alt: Ellipse example
    :scale: 25%

.. literalinclude:: ../exp_ellipse.py
   :language: python
   :linenos:

Annotating two astroids
--------------------------------------------------

Similar to the ellipse example, but this time demonstrates what would happen when the axes are "equal" but auto scale is on.

.. figure:: ../build/html/_sources/img/exp_astroid.png
    :alt: Astroid example
    :scale: 25%

.. literalinclude:: ../exp_astroid.py
   :language: python
   :linenos:

Annotating linear axes with log axes
--------------------------------------------------

This example shows that this module also works with log scale. The starting point and the end point are the same in the two subplots.

P.S. The really difficult thing to work around is the "symlog" scale. Not because it could have negative log, but because part of it is log while part of it is linear. This breaks the transformation. I hope you don't need to use curly brackets on symlog. If you have a good solution, please let me know.

.. figure:: ../build/html/_sources/img/exp_log.png
    :alt: Log example
    :scale: 25%

.. literalinclude:: ../exp_log.py
   :language: python
   :linenos: