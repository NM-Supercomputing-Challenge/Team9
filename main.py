import math
import matplotlib.pyplot as plt
avgDailyUsage = float(input("Your average usage per day from your Utility bill: "))
avgDailyCost = float(input("Your average electricity cost per day: "))
print()
print("Your annual electricity usage is about {:,.0f} kWh.".format(avgDailyUsage*365))   #curly brackets indicate the placeholder for variable, comma is used to indicate the thousands place and .0 means that there will be no decimal values, and f means that this variable uses float as a data type 
print("Your annual electricity cost is about ${:,.0f}.".format(avgDailyCost*365))
