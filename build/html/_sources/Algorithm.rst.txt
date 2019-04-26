The Algorithm
======================================

This section describes the algorithm.

A curly bracket can be divided into 6 parts: 4 arcs and 2 straight lines.

For easy reference, name the 4 arcs from left to right (assuming the bracket is pointing up) as: arc1, arc2, arc3 and arc4. Also, name the two lines as line1 and line2. If all the points of all the arcs are known, then, by connecting the last point of arc1 and the first point of arc2, line1 can be formed. Similarly, line2 can also be formed once all the points of arc3 and arc4 are known. Therefore, the crucial thing here is to get all the points of all the arcs.

The angle of the straight line formed by the starting point and the end point can be calculated by an atan method that considers quadrants. The radius of the arcs, assuming they are quater circles, can be set as proportional to the lenght of the aforementioned straight line. Let the user decide the proportion. 

The centre of arc1 is on the aforementioned straight line and distances from the starting point by the length of the radius. All the points of arc1 can then calculated. The detailed method is in the source code. Similarly, all the points of arc4 can be calculated.

The centre of arc2 has a perpendicular ditance to the aforementioned straight line of twice the radius. It also distances from the midpoint of the straight line of one radius (along the direction of the straight line). By accounting the angle rotation of the arc, all the points of arc2 can be calculated (see source code for details). Similarly, all the points of arc3 can be calculated.

This algorithm has a lot to do with playing with geometry. You can also play with Sigmoid function to make curly brackets (but I like this one here).

For the text annotation, it is actually quite simple. Just use standard matplotlib text should be suffice. The only thing need to take into account is how far the text should be from the summit of bracket. This can be achieved by allow line breaks to be pad to the text. But whether to pad the lines before or after the text depends on where the bracket is, since the summit can be pointing up or down depending on the quadrants.

The catch is that the axes coordinates need to transformed into screen coordinates to calculate the pixels and the transform back. Otherwise the bracket may appear as just a straight line.

Log scale can be dealt with just by logging the axis/axes limits and then expoential the arcs' points back. 

The real difficult thing is the symlog scale since it is part log, part linear and this breaks the transformation and makes the bracket looks funny.