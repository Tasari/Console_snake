import random
import time
import sys
import msvcrt

# Player score increaser
def score_up(x, score):
    score += x


def inputter(direction, time_limit):
    temp_direction = direction
    start_time = time.time()
    while 1:
        if msvcrt.kbhit():
            temp_direction = chr(ord(msvcrt.getche()))
            if temp_direction != direction:
                return temp_direction
        if time.time() - start_time > time_limit:
            return direction


def direction_change(drunk_fruit_flag, boring_fruit_flag, direction, speed):
    if drunk_fruit_flag == True:
        directions = ["w", "a", "s", "d"]
        temp_direction = directions[random.randrange(0, 3)]
    elif boring_fruit_flag == True:
        temp_direction = direction
    else:
        temp_direction = inputter(direction, speed)
    # assure that player won't be able to go turn 180°
    if temp_direction == "w" and direction != "s":
        direction = temp_direction
    elif temp_direction == "a" and direction != "d":
        direction = temp_direction
    elif temp_direction == "s" and direction != "w":
        direction = temp_direction
    elif temp_direction == "d" and direction != "a":
        direction = temp_direction
    return direction


def val2key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key


# function called after moving into impassable tile
def game_over(score):
    print("You lose")
    print("Your final score is " + str(score))
    time.sleep(5)
    sys.exit(0)
