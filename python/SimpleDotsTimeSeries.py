# Imports for rerun and numpy

import rerun as rr
import numpy as np

rr.init("SimpleDotsTimeSeries", spawn = True)

sampleCount = 500
pointCount = 100
pointFraction = 1.0 / pointCount

# Create a 2D array

function = np.zeros((pointCount, 3))
baseline = np.zeros((pointCount, 3))

# First column contains x values from 0 to 2pi
# Second column contains sin(x) values

for i in range(pointCount):
    function[i, 0] = i / (pointCount / 2) * np.pi
    function[i, 1] = np.sin(function[i, 0])
    function[i, 2] = 0

    baseline[i, 0] = i / (pointCount / 2) * np.pi

# Create a 2D array with pointCount color values
colors = np.zeros((pointCount, 3))

for i in range(pointCount):
    colors[i, 0] = 0.0 + pointFraction * i
    colors[i, 1] = 1.0 - pointFraction * i
    colors[i, 2] = 0.1 + 0.0 * i

# Create a time series of the points
# The function will be shifted such that a complete cycle is shown

for t in range(sampleCount):

    rr.set_time_seconds("time_stamp", t / 50.0)

    # Draw lines from base to function at each point
    rr.log("lines", rr.LineStrips3D(np.stack((baseline, function), axis=1), colors = 0.5 * colors, radii = 0.005))

    rr.log("function", rr.Points3D(function, colors = colors, radii = 0.02))

    # Shift the function
    for i in range(pointCount):
        function[i, 1] = np.sin(function[i, 0] + (t / 100) * 2 * np.pi)
    