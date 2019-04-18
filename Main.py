#!python3
#snake.py - snake game in console
import random
import threading
import time
import pyautogui
import sys
import os
import colorama

#Global options
size_x = 30
size_y = 30
border_symbol = colorama.Fore.LIGHTBLACK_EX + '#' * 2 + colorama.Style.RESET_ALL
classic_fruit_symbol = colorama.Fore.MAGENTA + '░' * 2 + colorama.Style.RESET_ALL
snake_symbol = colorama.Fore.GREEN + '█' * 2 + colorama.Style.RESET_ALL
blank_spot = colorama.Fore.WHITE + ' ' * 2 + colorama.Style.RESET_ALL
left_border = colorama.Fore.LIGHTBLACK_EX + ' #' + colorama.Style.RESET_ALL
right_border = colorama.Fore.LIGHTBLACK_EX + '# ' + colorama.Style.RESET_ALL
speed = 0.01
impassable_symbols = [border_symbol, snake_symbol, left_border, right_border]
direction = 'w'
snek_lenght = 3
#DO NOT TOUCH
score = 0
moves = []
move_x = None
del_x = None
#function used in direction_change to do input without stopping program
def inputter():
    global temp_direction
    input_direction = input()
    if input_direction != direction:
        temp_direction = input_direction
#Player score
def score_up(x):
    global score
    score += x
#function used to change direction of snake
def direction_change():
    global temp_direction
    temp_direction = threading.Thread(target=inputter)
    temp_direction.start()#create input tread without stopping program
    pyautogui.press('enter')
    global direction
    #assure that player won't be able to go turn 180°
    if temp_direction == 'w' and direction != 's':
        direction = temp_direction
    elif temp_direction == 'a' and direction != 'd':
        direction = temp_direction
    elif temp_direction == 's' and direction != 'w':
        direction = temp_direction
    elif temp_direction == 'd' and direction != 'a':
        direction = temp_direction
#function called after moving into impassable tile
def game_over():
    print('Przegrałeś')
    input()
    sys.exit(0)

def fruit_collected(fruit_obj, list):
    fruit_obj.effect()
    fruit_obj.fruit_spawn(list)

    #Delete last tile of snake
def snek_del(list, moves):
    global del_x, del_y
    if del_x == None:
        del_x = int(size_x/2)
        del_y = int((size_y/2)+snek_lenght)
    else:
        del_direction = moves[0]
        moves.pop(0)
        if del_direction == 'w':
            del_y -= 1
        elif del_direction == 'a':
            del_x -= 1
        elif del_direction == 's':
            del_y += 1
        elif del_direction == 'd':
            del_x += 1
    return del_x, del_y

class Fruit():
    def __init__(self, fruit_symbol):
        self.fruit_symbol = fruit_symbol

        #Spawn point creating device with random spawn on board
    def fruit_spawn(self, list):
        while 1:
            y = random.randint(1, size_y-2)
            x = random.randint(1, size_x-2) 
            if(list[x][y]== blank_spot):#Assure our fruits won't spawn on occupied tiles
                list[x][y] = self.fruit_symbol
                break
            else:#In case it wants to spawn where snake actually is
                continue

class Classic_Fruit(Fruit):
    def effect(self):
        score_up(100)

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
    def change_map_tiles(self, list):
        #Make all of them blank
        for y in range(size_y):
            for x in range(size_x):
                list[y][x]= blank_spot
        #Add some other shapes to create border
        for x in range(size_x):
            list[x][0] = border_symbol#upper side
            list[x][size_y-1] = border_symbol#lower side
        for y in range(size_y):
            list[0][y] = left_border#left side
            list[size_x-1][y] = right_border#right side


    #Add function to draw a map from coords in form of string
    def map_drawer(self, list):
        for x in range(size_x):
            visual_map = ''
            for y in range(size_y):
                visual_map += str(list[y][x])
            print(visual_map.center(75))

    #Create Player's snake
    def snek_spawn(self, list, snek_lenght):
        y = int(size_y/2)
        x = int(size_x/2)
        for part in range(snek_lenght):
            list[x][y] = snake_symbol
            y += 1
            moves.append('w')

    #Create snake movement
    def snek_move(self, list, direction):
        #starting point
        global move_x, move_y
        if move_x == None:
            move_x = int(size_y/2)
            move_y = int(size_x/2)
        direction_change()
        #up
        if direction == 'w':
            #print(list[a][b-1])
            if list[move_x][move_y-1] in impassable_symbols:
                game_over()
            elif list[move_x][move_y-1] == classic_fruit_symbol:
                fruit_collected(classic_fruit_obj, coords)
                list[move_x][move_y-1] = snake_symbol
                move_y -= 1
            elif list[move_x][move_y-1] == blank_spot:
                list[move_x][move_y-1] = snake_symbol
                move_y -= 1
                del_x, del_y = snek_del(list, moves)
                list[del_x][del_y] = blank_spot
            moves.append('w')
        #left
        elif direction == 'a':
            #print(list[a-1][b])
            if list[move_x-1][move_y] in impassable_symbols:
                game_over()
            elif list[move_x-1][move_y] == classic_fruit_symbol:
                fruit_collected(classic_fruit_obj, coords)
                list[move_x-1][move_y] = snake_symbol
                move_x -= 1
            elif list[move_x-1][move_y] == blank_spot:
                list[move_x-1][move_y] = snake_symbol
                move_x -= 1
                del_x, del_y = snek_del(list, moves)
                list[del_x][del_y] = blank_spot
            moves.append('a')
        #down
        elif direction == 's':
            if list[move_x][move_y+1] in impassable_symbols:
                game_over()
            elif list[move_x][move_y+1] == classic_fruit_symbol:
                fruit_collected(classic_fruit_obj, coords)
                list[move_x][move_y+1] = snake_symbol
                move_y += 1
            elif list[move_x][move_y+1] == blank_spot:
                list[move_x][move_y+1] = snake_symbol
                move_y += 1
                del_x, del_y = snek_del(list, moves)
                list[del_x][del_y] = blank_spot
            moves.append('s')
        #right
        elif direction == 'd':
            if list[move_x+1][move_y] in impassable_symbols:
                game_over()
            elif list[move_x+1][move_y] == classic_fruit_symbol:
                fruit_collected(classic_fruit_obj, coords)
                list[move_x+1][move_y] = snake_symbol
                move_x += 1
            elif list[move_x+1][move_y] == blank_spot:
                list[move_x+1][move_y] = snake_symbol
                move_x += 1
                del_x, del_y = snek_del(list, moves)
                list[del_x][del_y] = blank_spot
            moves.append('d')
#create map        
table = Map(size_x, size_y)
#create coords
coords = table.create_2d_table()
#create cooler tiles
table.change_map_tiles(coords)
#create snake
table.snek_spawn(coords, snek_lenght)
#create fruit
classic_fruit_obj = Classic_Fruit(classic_fruit_symbol)
classic_fruit_obj.fruit_spawn(coords)
#move the snake
while 1:
    table.snek_move(coords, direction)
    time.sleep(speed)
    os.system('clear')
    table.map_drawer(coords)