# Ideal Mathematical Model
import math 
import matplotlib.pyplot as plt

# Since compiler (a program that translates the code into 
# binary numbers in order for the processor to generate an output)
# can't convert angles into binary value;
# Python uses radians instead of degrees
# (radians represent the length of the arc,
# or a part of a circle made by a given angle);
# For this reason, we need a function that converts
# degrees into radians; and we will call it: Deg2Rad.
# Since radius (the length from the center of a circle to its edge) * 3.14159.... (pi) draws a half circle (180 degrees), then:
# 180 deg = pi radians, and
# any other deg = ? radians;
# We use proportions to solve for ?:
# ? = deg * pi / 180
def Deg2Rad(x): return (x*math.pi/180)
 
