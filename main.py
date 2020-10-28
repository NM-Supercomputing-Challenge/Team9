import math
import matplotlib.pyplot as plt
print()
#The max daily usage: 50!
#Small house uses about 8-10 kWh at the cost of $1-2 per day
#Large household uses about 35-50 kWh at the cost of $5.5 - 7 per day
avgDailyUsage = float(input("Your average usage per day from your Utility bill: "))
avgDailyCost = float(input("Your average electricity cost per day: "))
print()
print("Your annual electricity usage is about {:,.0f} kWh.".format(avgDailyUsage*365))   #curly brackets indicate the placeholder for variable, comma is used to indicate the thousands place and .0 means that there will be no decimal values, and f means that this variable uses float as a data type 
print("Your annual electricity cost is about ${:,.0f}.".format(avgDailyCost*365))

def pricePayoff(size): 
  print()
  panels = math.ceil(size/275) #275 watts is produced by a standard polycrystaline solar panel 
  print("Approximate NUMBER of PANELS: "+str(panels)+';')
  print()  #2.91 is the average cost of 1 watt produced by a PV system
  print("TOTAL COST: about ${:,.0f};".format(size*2.91)) 
  print()
  netCost = size*2.91 - size*2.91*36/100  #26% is federal income tax credit and 10% is state, all = 36%
  print("NET COST (after deducting 36% federal & state tax credits): ${:,.0f};".format(netCost))
  print()
  print("PAYOFF: It will take about {:.1f} years to pay off such system".format(netCost/(avgDailyCost*365)))
  print("from what you will save on your utility bills each year.")
  print()
  months = ['Jan:', 'Feb:', 'Mar:', 'Apr:', 'May:', 'Jun:', 'Jul:', 'Aug:', 'Sep:', 'Oct:','Nov:', 'Dec:']
  print("Such PV System will produce the following amount of AC energy each month:")
  for i in range(len(prod)):
    print(months[i],prod[i])
  print("Total:",sum(prod),'kWh')

print()
print("Specifications of the PV System for area code = 87507:")
print("*"*54)
print()
#Use PVWatts Calculator to get annual production made by 1 - 10 kW DC(direct current) PV Systems:
if avgDailyUsage*365 <= 1800:        #max 1 kW DC System outpt
  print("SIZE: 1 kW DC System;")
  print()
  print("RECOMMENDED TYPE: Fixed (roof mount);")
  print()
  print("ANNUAL PRODUCTION: about 1,745 kWh of AC")
  production = [122, 125, 156, 165, 179, 170, 157, 155, 146, 136, 121, 113]
  pricePayoff(1000, production)
elif avgDailyUsage*365 > 1800 and  avgDailyUsage*365 <= 2700:   #max 1.5 kW DC System output
  print("SIZE: 1.5 kW DC System;")
  print()
  print("RECOMMENDED TYPE: Fixed (roof mount);")
  print()
  print("ANNUAL PRODUCTION: about 2,619 kWh of AC;")
  production = [183, 188, 233, 248, 269, 256, 235, 232, 219, 205, 182, 169]
  pricePayoff(1500, production)
elif avgDailyUsage*365 > 2700 and avgDailyUsage*365 <= 3500:
    print("SIZE: 2 kW DC System;")
    print()
    print("RECOMMENDED TYPE: Fixed (roof mount);")
    print()
    print("ANNUAL PRODUCTION: about 3,492 kWh of AC;")
    production = [244, 251, 311, 330, 359, 341, 313, 310, 292, 273, 242, 226]
    pricePayoff(2000, production)
elif avgDailyUsage*365 > 3500 and avgDailyUsage*365 <= 4500:
    print("SIZE: 2.5 kW DC System;")
    print()
    print("RECOMMENDED TYPE: Fixed (roof mount);")
    print()
    print("ANNUAL PRODUCTION: about 4,365 kWh of AC;")
    production = [305, 314, 389, 413, 448, 426, 391, 387, 365, 341, 303, 282]
    pricePayoff(2500, production)
elif avgDailyUsage*365 > 4500 and avgDailyUsage*365 <= 5400:
    print("SIZE: 3 kW DC System;")
    print()
    print("RECOMMENDED TYPE: Fixed (roof mount);")
    print()
    print("ANNUAL PRODUCTION: about 5,238 kWh of AC;")
    production = [367, 376, 467, 495, 538, 511, 470, 465, 438, 409, 363, 339]
    pricePayoff(3000, production)
