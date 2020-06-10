# Modified from code at:
#http://antoniocangiano.com/2009/01/01/monte-carlo-simulation-of-the-monty-hall-problem-in-ruby-and-python/
#
#http://en.wikipedia.org/wiki/Monty_Hall_problem.

import sys
from random import randint, shuffle, choice

doors = ['fabulous riches', 'junk', 'junk']

def randomly_pick_door():
    return randint(0,2)

#Return the index of the door opened by the host - must be
#neither the door hiding the riches nor the player's chosen door.
def host_reveal_door(player_pick):
    all_doors = set([0, 1, 2])
    unavailable_doors = set([doors.index('fabulous riches'), player_pick])
    available_doors = list(all_doors - unavailable_doors)
    return choice(available_doors)

def other_door(player_pick, revealed_door):
    setDiff = set([0, 1, 2]) - set([player_pick, revealed_door])
    return list(setDiff)[0]

def simulateMontyHall(iterations, printInfo = False):
  
    wins_by_switching = 0
    wins_by_staying = 0
    
    for picknum in range(iterations):
        shuffle(doors)
        door_picked_by_player = randomly_pick_door()
        door_revealed_by_host = host_reveal_door(door_picked_by_player)
        remaining_door = other_door(door_picked_by_player, door_revealed_by_host)

        if printInfo:
            print("Prize is behind: {}, player picked: {}, host revealed: {}".format(
                  doors.index('fabulous riches'),
                  door_picked_by_player,
                  door_revealed_by_host))
            
        if doors[door_picked_by_player] == 'fabulous riches':
            wins_by_staying += 1

        if doors[remaining_door] == 'fabulous riches':
            wins_by_switching += 1

    staying_success_rate = (float(wins_by_staying) / iterations) * 100
    switching_success_rate = (float(wins_by_switching) / iterations) * 100

    print ("Success rate for staying: %f%%" % staying_success_rate )
    print ( "Success rate for switching: %f%%" % switching_success_rate )



