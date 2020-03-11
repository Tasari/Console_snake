import random
import time
import sys
import msvcrt


def inputter(direction, time_limit):
    """
    Takes the actual direction 
    and time limit to change it,
    and returns the inputted letter 
    """
    temp_direction = direction
    start_time = time.time()
    while 1:
        if msvcrt.kbhit():
            temp_direction = chr(ord(msvcrt.getche()))
            if temp_direction in ["w", "a", "s", "d", "q"]:
                return temp_direction
        if time.time() - start_time > time_limit:
            return direction


def direction_change(parameters_object):
    """
    Changes the direction, 
    if random move is active it changes randomly, 
    if move blocking fruit is active it doesn't change,
    else takes the input from user
    """
    if parameters_object.random_move_flag == True:
        directions = ["w", "a", "s", "d"]
        temp_direction = directions[random.randrange(0, 3)]
    elif parameters_object.move_blocking_fruit_flag == True:
        temp_direction = parameters_object.direction
    else:
        temp_direction = inputter(parameters_object.direction, parameters_object.speed)
    direction_valid(parameters_object, temp_direction)


def direction_valid(parameters_object, temp_direction):
    """
    Assures that player's move is valid
    """
    if temp_direction == "w" and parameters_object.direction != "s":
        parameters_object.direction = temp_direction
    elif temp_direction == "a" and parameters_object.direction != "d":
        parameters_object.direction = temp_direction
    elif temp_direction == "s" and parameters_object.direction != "w":
        parameters_object.direction = temp_direction
    elif temp_direction == "d" and parameters_object.direction != "a":
        parameters_object.direction = temp_direction


def val2key(dictionary, value):
    """
    Gives the key in the dictionary 
    which returns the given value 
    """
    for key, val in dictionary.items():
        if val == value:
            return key


def game_over(score):
    """
    Ends the game
    """
    print("You lose")
    print("Your final score is " + str(score))
    time.sleep(5)
    sys.exit(0)
