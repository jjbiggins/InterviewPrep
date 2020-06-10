# CS1210 Spring 2017Homework 1 solution
#
import math

# tripCost(distance, vehSpeed, vehMPG, gasCostPerGallon, hotelCostPerNight):
#
# returns the cost of a trip of based on parameters:
#    distance: the trip's distance in miles (type: float)
#    vehSpeed: the speed of the vehicle used for the trip, in miles per hour (type: float)
#    vehMPG: the vehicle fuel efficiency in miles per gallon (type: float)
#    gasCostPerGallon: the price of one gallon of gas in dollars (type: float)
#    hotelCostPerNight: the cost of one night in a hotel in dollars (type: float)
#
def tripCost(distance, vehSpeed, vehMPG, gasCostPerGallon, hotelCostPerNight):
    vehTime = distance/vehSpeed
    vehGallons = distance/vehMPG
    vehDays = vehTime/8.0
    vehNights = math.ceil(vehDays)-1
    hotelCost = vehNights * hotelCostPerNight    
    totalCost = (gasCostPerGallon * vehGallons) + hotelCost
    return totalCost

# chooseVehicleForTrip(distance,
#                                     veh1Name, veh1Speed, veh1MPG,
#                                     veh2Name, veh2Speed, veh2MPG,
#                                     gasCostPerGallon, hotelCostPerNight)
#
# computes (using the tripCost function above)  the cost of a trip for two different vehicles,
# prints information about the cost, and prints a recommendation for which vehicle should
# be used to save money.
#
# The parameters are:
#    distance: the trip's distance in miles (type: float)
#    veh1Name: a string representing the first vehicle (e.g. "Tesla")
#    veh1Speed: vehicle 1's speed in miles per hour (type: float)
#    veh1MPG: vehicle 1's fuel efficiency in miles per gallon (type: float)
#    veh2Name: a string representing the second vehicle (e.g. "Dongfend")
#    veh2Speed: vehicle 2's speed in miles per hour (type: float)
#    veh2MPG: vehicle 2's fuel efficiency in miles per gallon (type: float)
#    gasCostPerGallon: the price of one gallon of gas in dollars (type: float)
#    hotelCostPerNight: the cost of one night in a hotel in dollars (type: float)
#
# Presume that you can only drive 8 hours per day. So, if a trip requires 15.25 hours,
# it will require a one-night hotel stay at an additional cost (beyond gas costs) equal to
# nightlyHotelCost. (Note: an exact 8-hour trip does not require a hotel stay, and a
# 16-hour trip requires just one night of hotel.)
#
def chooseVehicleForTrip(distance, veh1Name, veh1Speed, veh1MPG, veh2Name, veh2Speed, veh2MPG, gasCostPerGallon, hotelCostPerNight):
    veh1Cost = tripCost(distance, veh1Speed, veh1MPG, gasCostPerGallon, hotelCostPerNight)
    veh2Cost = tripCost(distance, veh2Speed, veh2MPG, gasCostPerGallon, hotelCostPerNight)

    print("{} miles in vehicle '{}' will cost ${:.2f}.".format(distance, veh1Name, veh1Cost))
    print("{} miles in vehicle '{}' will cost ${:.2f}.".format(distance, veh2Name, veh2Cost))

    if veh1Cost < veh2Cost:
        print("To save money, use '{}'".format(veh1Name))
    elif veh2Cost < veh1Cost:
        print("To save money, use '{}'".format(veh2Name))
    else:
        print("Trip cost is the same in both vehicles. Choose your favorite.")

def testQ1():
    print(tripCost(1.0, 1.0, 1.0, 1.0, 1.0))
    print(tripCost(5.0, 1.0, 1.0, 1.0, 1.0))
    print(tripCost(10.0, 1.0, 3.0, 5.0, 70.0))
    print(tripCost(100.0, 10.0, 3.0, 5.0, 70.0))
    print(tripCost(8.0, 1.0, 1.0, 1.50, 1000.0))
    print(tripCost(16.0, 1.0, 1.0, 1.50, 1000.0))
    print(tripCost(24.0, 1.0, 1.0, 1.50, 1000.0))
    print(tripCost(96.0, 1.0, 1.0, 1.50, 1000.0))
   
def testQ2():
    chooseVehicleForTrip(100.0, 'V1', 10.0, 1.0, 'V2', 100.0, 10.0, 5.0, 1000.0)
    chooseVehicleForTrip(100.0, 'V1', 10.0, 1.0, 'V2', 1.0, 10.0, 10.0, 0.01)
    chooseVehicleForTrip(1231.5, 'V1', 10.0, 1.0, 'V2', 1.0, 10.0, 10.0, 50.0)
    chooseVehicleForTrip(1231.5, 'V1', 33.0, 2.0, 'V2', 1.0, 10.0, 10.0, 50.0)
    chooseVehicleForTrip(1231.5, 'V1', 33.0, 111.0, 'V2', 1.0, 10.0, 10.0, 50.0)
    chooseVehicleForTrip(1231.5, 'V1', 33.0, 111.0, 'V2', 1.0, 10.0, 0.0, 50.0)
    chooseVehicleForTrip(1231.5, 'V1', 33.0, 111.0, 'V2', 1.0, 10.0, 10.0, 0.0)
    chooseVehicleForTrip(240.0, 'Slow', 20.0, 60.0, 'Fast', 40.0, 40.0, 10.0, 20.0)
    chooseVehicleForTrip(1231.5, 'V1', 33.0, 111.0, 'V2', 1.0, 10.0, 0.0, 0.0)
    chooseVehicleForTrip(24.0, 'V1', 3.0, 10.0, 'V2', 1.0, 10.0, 500.0, 5000.0)
    
