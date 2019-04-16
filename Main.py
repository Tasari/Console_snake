#!python3
#snake.py - snake game in console
import random
import threading
import time
import pyautogui
import sys
import os

#Global options
max_x = 50
max_y = 50
size_x = 25
size_y = 25
border_symbol = '#'
fruit_symbol = '░'
snake_symbol = '█'
blank_spot = ' '
speed = 1
impassable_symbols = ['##', '██', '# ', ' #']
a = None
direction = 'a'

#function used in direction_change to do input without stopping program
def inputter():
    global temp_direction
    input_direction = input()
    if input_direction != direction:
        temp_direction = input_direction
    return temp_direction

#function used in direction_change to end threaded input without user needing to press enter
def finisher():
    time.sleep(0.5)
    pyautogui.press('enter')

#function used to change direction of snake
def direction_change():
    global temp_direction
    temp_direction = threading.Thread(target=inputter)
    temp_direction.start()#create input tread without stopping program
    threading.Thread(target=finisher).start()#end input thread
    global direction
    time.sleep(0.6)
    #assure that player won't be able to go turn 180°
    if temp_direction == 'w' and direction != 's':
        direction = temp_direction
    elif temp_direction == 'a' and direction != 'd':
        direction = temp_direction
    elif temp_direction == 's' and direction != 'w':
        direction = temp_direction
    elif temp_direction == 'd' and direction != 'a':
        direction = temp_direction

def game_over():
    print('Przegrałeś')
    input()
    sys.exit(1)

#Create Map() class to work on our map of snake
class Map():
    def __init__(self, map_x, map_y):
        self.map_x = map_x
        self.map_y = map_y

    #Create map coordinates to make the movement through map easy
    def create_2d_table(self):
        board = []
        for y in range(self.map_y):
            y_table = []
            for x in range(self.map_x):
                y_table.append(x)
            board.append(y_table)
        return board  

    #Change the coords to make create appearance of tiles       
    def change_map_tiles(self, list, bordersymbol=border_symbol):
        #Make all of them blank
        for y in range(size_y):
            for x in range(size_x):
                list[y][x]= '  '
        #Add some other shapes to create border
        for y in range(size_y):
            list[0][y] = bordersymbol + ' '#left side
            list[size_x-1][y] = ' ' + bordersymbol#right side
        for x in range(size_x):
            list[x][0] = bordersymbol*2#upper side
            list[x][size_y-1] = bordersymbol*2#lower side

    #Add function to draw a map from coords in form of string
    def map_drawer(self, list):
        for x in range(size_x):
            visual_map = ''
            for y in range(size_y):
                visual_map += str(list[y][x])
            print(visual_map.center(75))

    #Spawn point creating device with random spawn on board
    def fruit_spawn(self, list, fruitsymbol = fruit_symbol):
        while 1:
            y = random.randint(1, size_y-2)
            x = random.randint(1, size_x-2) 
            if(list[x][y]== '  '):#Assure our fruits won't spawn on occupied tiles
                list[x][y] = fruitsymbol*2
                break
            else:#In case it wants to spawn where snake actually is
                continue

    #Create Player's snake
    def snek_spawn(self, list):
        y = int(size_y/2)
        x = int(size_x/2)
        snek_lenght = 5
        for part in range(snek_lenght):
            list[x][y] = snake_symbol*2
            y += 1

    #Create snake movement
    def snek_move(self, list, direction):
        #starting point
        global a, b
        if a == None:
            a = int(size_y/2)
            b = int(size_x/2)
        #góra
        if direction == 'w':
            if list[a][b-1] in impassable_symbols:
                game_over()
            elif list[a][b-1] == fruit_symbol*2:
                list[a][b-1] = snake_symbol*2
                b -= 1
            elif list[a][b-1] == '  ':
                list[a][b-1] = snake_symbol*2
                b -= 1
        #lewo
        elif direction == 'a':
            if list[a-1][b] in impassable_symbols:
                game_over()
            elif list[a-1][b] == fruit_symbol*2:
                list[a-1][b] = snake_symbol*2
                a -= 1
            elif list[a-1][b] == '  ':
                list[a-1][b] = snake_symbol*2
                a -= 1
        #dół
        elif direction == 's':
            if list[a][b+1] in impassable_symbols:
                game_over()
            elif list[a][b+1] == fruit_symbol*2:
                list[a][b+1] = snake_symbol*2
                b += 1
            elif list[a][b+1] == '  ':
                list[a][b+1] = snake_symbol*2
                b += 1
        #prawo
        elif direction == 'd':
            if list[a+1][b] in impassable_symbols:
                game_over()
            elif list[a+1][b] == fruit_symbol*2:
                list[a+1][b] = snake_symbol*2
                a += 1
            elif list[a+1][b] == '  ':
                list[a+1][b] = snake_symbol*2
                a += 1
        direction_change()
        time.sleep(0.5)

        


table = Map(size_x, size_y)
coords = table.create_2d_table()
table.change_map_tiles(coords)
table.snek_spawn(coords)
while 1:
    table.snek_move(coords, direction)
    time.sleep(speed)
    os.system('clear')
    table.map_drawer(coords)