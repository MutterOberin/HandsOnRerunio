# Imports for rerun and numpy

import rerun as rr
import numpy as np

rr.init("SimpleDots", spawn = True)

pointCount = 100
pointFraction = 1.0 / pointCount

# Create a 2D array

function = np.zeros((pointCount, 3))

# First column contains x values from 0 to 2pi
# Second column contains sin(x) values

for i in range(pointCount):
    function[i, 0] = i / (pointCount / 2) * np.pi
    function[i, 1] = np.sin(function[i, 0])
    function[i, 2] = 0

# Create a 2D array with pointCount color values
colors = np.zeros((pointCount, 3))

for i in range(pointCount):
    colors[i, 0] = 0.0 + pointFraction * i
    colors[i, 1] = 1.0 - pointFraction * i
    colors[i, 2] = 0.1 + 0.0 * i

rr.log("function", rr.Points3D(function, colors = colors, radii = 0.02))



