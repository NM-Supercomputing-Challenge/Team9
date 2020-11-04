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
 
# IdealModel is the 'best case' result from PV.
# The formula used in this function refers to a shadow
# produced by the PV panel - the larger the shadow the more
# light falls on it; and it's calculated by multiplying a sine of an
# angle, at which the sunlight falls on the panel, by 100%.
# The sine function is the ratio of the side opposite a given
# angle (in a right triangle) to the hypotenuse.
# Assuming that we will use 1 as the length of the hypotenuse,
# which represents the PV panel, and that the side opposite the angle
# represents the percentage of the shadow, the formula of the sine will be:
# sin(angle in radians) = shadow / length of PV panel; and:
# shadow in % = length of PV panel (= 1) * sin(angle in radians) * 100:
def IdealModel(x): return round(math.sin(Deg2Rad(x))*100, 1)
# round(num1, num2) rounds num1 to num2 precision
#===================================================
Angle = [i * 5.0 for i in range(0,37)]
# Angle is a list created using a list comprehension method;
# this is a list of values from 0 to 37, each multiplied by 5.0,
# since 37 * 5 = 185,so this list has the following values:
# [0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, .... 180,0], see:
print(Angle)
# We then send each of these angles to our IdealModel() function above:
IdealSampled = [IdealModel(i) for i in Angle]

# plot Ideal Model
plt.plot(Angle,IdealSampled,label="Ideal PV Panel Model", color='red',linestyle='dashed',marker='o',markerfacecolor='red',markersize=4)
#Labels for x and y axis:
plt.xlabel('Degrees')
plt.ylabel('Percent')
plt.grid()
plt.legend()
#Title of the graph:
plt.title('Ideal Model of PV Panel')
plt.show()
