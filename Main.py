from Options import size_x, size_y, speed, lenght, fruits
from Other import direction_change
from Map import Map_obj
from Fruits import trigger
from Snake import Snake
import time
import sys
import os

# Set start variables
score = 0
move_x = None
del_x = None
boring_fruit_flag = False
drunk_fruit_flag = False
direction = None
drunk_counter = 0
boring_counter = 0
# Creating the map
game_map = Map_obj(size_x, size_y)
# Creating Snake on map
player = Snake(game_map)
game_map.spawn_snake(lenght, player.moves)
# Spawn fruits symbols on map
[game_map.spawn_fruit(z) for z in fruits.keys()]
# Draws the map on screen
game_map.draw(score)
os.system("cls")
print("Loading")
# Loop going till game over function is called
while 1:
    direction = direction_change(drunk_fruit_flag, boring_fruit_flag, direction, speed)
    (
        score,
        speed,
        drunk_fruit_flag,
        boring_fruit_flag,
        drunk_counter,
        boring_counter,
    ) = player.move(
        direction,
        score,
        speed,
        drunk_fruit_flag,
        boring_fruit_flag,
        drunk_counter,
        boring_counter,
    )
    if sys.platform == "linux":
        os.system("clear")
    else:
        os.system("cls")
    game_map.draw(score)
