import math
import matplotlib.pyplot as plt
avgDailyUsage = float(input("Your average usage per day from your Utility bill: "))
avgDailyCost = float(input("Your average electricity cost per day: "))
print()
print("Your annual electricity usage is about {:,.0f} kWh.".format(avgDailyUsage*365))   #curly brackets indicate the placeholder for variable, comma is used to indicate the thousands place and .0 means that there will be no decimal values, and f means that this variable uses float as a data type 
print("Your annual electricity cost is about ${:,.0f}.".format(avgDailyCost*365))


#Use PVWatts Calculator to get annual production made by 1 - 10 kW DC(direct current) Systems:
if avgDailyUsage*365 <= 1800:        #max 1 kW DC System outpt
  print("SIZE: 1 kW DC System;")
  print()
  print("RECOMMENDED TYPE: Fixed (roof mount);")
  print()
  print("ANNUAL PRODUCTION: about 1,745 kWh of AC")
  production = [122, 125, 156, 165, 179, 170, 157, 155, 146, 136, 121, 113]
  pricePayoff(1000)
  