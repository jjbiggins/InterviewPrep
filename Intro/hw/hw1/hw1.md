 CS1210 Homework 1 **Homework 1**
CS1210 Computer Science 1
Due Sunday, January 29, by 11:59pm
10 points

**1.** Write a Python function, tripCost(distance, vehSpeed, vehMPG, gasCostPerGallon, hotelCostPerNight) that returns the cost of a trip of based on several parameters The function's parameters are:

*   distance: the trip's distance in miles (type: float)
*   vehSpeed: the speed of the vehicle used for the trip, in miles per hour (type: float)
*   vehMPG: the vehicle fuel efficiency in miles per gallon (type: float)
*   gasCostPerGallon: the price of one gallon of gas in dollars (type: float)
*   hotelCostPerNight: the cost of one night in a hotel in dollars (type: float)

Presume that you can only drive 8 hours per day. So, if a trip requires 15.25 hours, it will require a one-night hotel stay at an additional cost (beyond gas costs) equal to hotelCostPerNight.

Note: If a trip requires 8.0 hours, it does _not_ require a hotel stay. Similarly, a trip of 16.0 hours requires _one_ night of hotel, not two.

**2.** Write a Python function, chooseVehicleForTrip(distance, veh1Name, veh1Speed, veh1MPG, veh2Name, veh2Speed, veh2MPG, gasCostPerGallon, hotelCostPerNight) that computes the cost of a trip for two different vehicles, _prints_ information about the cost, and _prints_ a recommendation which vehicle should be used to save money (note: if trip cost is the same for both vehicles, say something appropriate).

The function's parameters are:

*   distance: the trip's distance in miles (type: float)
*   veh1Name: a string representing the first vehicle (e.g. "Tesla")
*   veh1Speed: vehicle 1's speed in miles per hour (type: float)
*   veh1MPG: vehicle 1's fuel efficiency in miles per gallon (type: float)
*   veh2Name: a string representing the second vehicle (e.g. "Dongfeng")
*   veh2Speed: vehicle 2's speed in miles per hour (type: float)
*   veh2MPG: vehicle 2's fuel efficiency in miles per gallon (type: float)
*   gasCostPerGallon: the price of one gallon of gas in dollars (type: float)
*   hotelCostPerNight: the cost of one night in a hotel in dollars (type: float)

For full credit, chooseVehicleForTrip must use/call tripCost, the function you write for Q1.

Note: Your function should not _return_ anything. Instead it should _print_ information about the cost of the trip for both vehicle 1 and vehicle 2 and should recommend choosing the vehicle that yields the less expensive trip.

For example,

\>>> chooseVehicleForTrip(1000.0, "Bugatti", 100.0, 1.0, "Vespa", 30.0, 100.0, 2.10, 55.0)
1000.0 miles in vehicle 'Bugatti' will take 1.25 days (1 night) and cost $2155.00.
1000.0 miles in vehicle 'Vespa' will take 4.17 days (4 nights) and cost $241.00.
To save money, use 'Vespa'
>>>

_Note:_ It is _not required_ that you print the days and nights information in your output. Printing only the cost information is sufficient. If you want to print the days and nights information, that is good, and there are a few possible ways to do it. The tripCost function needs to compute the days and nights function, and it's not good programming practice to recompute that information in chooseVehicleForTrip. One solution (that has not yet been taught in class) is to modify tripCost to return three values instead of one. That is instead of returning just the cost, it can return the cost, the number of days, and the number of nights. To return multiple values, you can use a line like:

          return cost, numDays, numNights

and to "receive" or save multiple values from a function call, you can use a line like:

          veh1TripCost, veh1TripDays, veh1TripNights = tripCost(...)

Again, this is optional; it is not required for HW1.

* * *

Submit to ICON one python file containing both function definitions (using **def**). The file must not include any code that is not part of a function definition.

Make sure your functions are named _exactly_ (including upper/lower case usage) as in the specification, with the same set of parameters.

You may (but are not required to) add additional functions as helpers or testers of your the specified functions. In general, it is excellent practice to include a function that tests your other code. For example, you might write a function, "def testChooseVehicleForTrip(): ..." that makes several calls to chooseVehicleForTrip using a variety of input values. In future homeworks assignments, we will often require inclusion of such test functions.
