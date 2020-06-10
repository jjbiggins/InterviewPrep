#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1
# File              : hw1.py
# Author            : Joe Biggins <jjbiggins@joebiggins.io>
# Date              : 10.06.2020
# Last Modified Date: 10.06.2020
# Last Modified By  : Joe Biggins <jjbiggins@joebiggins.io>

import math


def tripCost(distance, vehSpeed, vehMPG, gasCostPerGallon, hotelCostPerNight):
	maxHrsPerDay = 8
	
	totalHrsDriving = distance / vehSpeed
	numberNights = totalHrsDriving / maxHrsPerDay
	totalHotelCost = numberNights * hotelCostPerNight
	
	gallonsNeeded = (1 / vehMPG) * distance
	totalGasCost = gasCostPerGallon * gallonsNeeded
	
	totalCost = totalGasCost + totalHotelCost
	
	return totalCost


def chooseVehicleForTrip(distance: float, veh1Name: str, veh1Speed: float, veh1MPG: float, veh2Name: str, veh2Speed: float, veh2MPG: float, gasCostPerGallon: float,
                         hotelCostPerNight: float) -> float:
	veh1Cost = tripCost (distance, veh1Speed, veh1MPG, gasCostPerGallon, hotelCostPerNight)
	veh2Cost = tripCost (distance, veh2Speed, veh2MPG, gasCostPerGallon, hotelCostPerNight)
	
	if veh1Cost > veh2Cost:
		return veh2Name, veh2Cost
	elif veh1Cost < veh2Cost:
		print("name: " + str(veh1Name) + ", cost: " + str(veh1Cost))
	else:
		return "vehicles are the same"


def testQ1():
	print (tripCost (1.0, 1.0, 1.0, 1.0, 1.0))
	print (tripCost (5.0, 1.0, 1.0, 1.0, 1.0))
	print (tripCost (10.0, 1.0, 3.0, 5.0, 70.0))
	print (tripCost (100.0, 10.0, 3.0, 5.0, 70.0))
	print (tripCost (8.0, 1.0, 1.0, 1.50, 1000.0))
	print (tripCost (16.0, 1.0, 1.0, 1.50, 1000.0))
	print (tripCost (24.0, 1.0, 1.0, 1.50, 1000.0))
	print (tripCost (96.0, 1.0, 1.0, 1.50, 1000.0))


def testQ2():
	chooseVehicleForTrip (100.0, 'V1', 10.0, 1.0, 'V2', 100.0, 10.0, 5.0, 1000.0)
	chooseVehicleForTrip (100.0, 'V1', 10.0, 1.0, 'V2', 1.0, 10.0, 10.0, 0.01)
	chooseVehicleForTrip (1231.5, 'V1', 10.0, 1.0, 'V2', 1.0, 10.0, 10.0, 50.0)
	chooseVehicleForTrip (1231.5, 'V1', 33.0, 2.0, 'V2', 1.0, 10.0, 10.0, 50.0)
	chooseVehicleForTrip (1231.5, 'V1', 33.0, 111.0, 'V2', 1.0, 10.0, 10.0, 50.0)
	chooseVehicleForTrip (1231.5, 'V1', 33.0, 111.0, 'V2', 1.0, 10.0, 0.0, 50.0)
	chooseVehicleForTrip (1231.5, 'V1', 33.0, 111.0, 'V2', 1.0, 10.0, 10.0, 0.0)
	chooseVehicleForTrip (240.0, 'Slow', 20.0, 60.0, 'Fast', 40.0, 40.0, 10.0,
	                      20.0)
	chooseVehicleForTrip (1231.5, 'V1', 33.0, 111.0, 'V2', 1.0, 10.0, 0.0, 0.0)
	chooseVehicleForTrip (24.0, 'V1', 3.0, 10.0, 'V2', 1.0, 10.0, 500.0, 5000.0)
