from Options import size_x, size_y, fruits
from Other import direction_change
from Map import Map_obj
from Fruits import trigger
from Snake import Snake
from Parametres import Parameters
import time
import sys
import os

# Set default variables in Parameters object
params = Parameters()
# Creating the map
game_map = Map_obj(size_x, size_y)
# Creating Snake on map
player = Snake(game_map)
game_map.spawn_snake(player)
# Spawn fruits symbols on map
[game_map.spawn_fruit(z) for z in fruits.keys()]
# Draws the map on screen
game_map.draw(params.score)
os.system("cls")
print("Loading")
# Loop going till game over function is called
while 1:
    direction_change(params)
    player.move(params)
    if sys.platform == "linux":
        os.system("clear")
    else:
        os.system("cls")
    game_map.draw(params.score)
