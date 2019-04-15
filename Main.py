#!python3
#snake.py - snake game in console
import random
import threading
#Global options

max_x = 50
max_y = 50
size_x = 25
size_y = 25
border_symbol = '#'
fruit_symbol = '░'

def direction_change():
    thread_input = threading.Thread(target= = input())
    thread_end = threading.Thread(target='\n')
    thread_input.start()
    time.sleep(0.1)
    thread_end.start()
#Create Map() class to work on our map of snake
class Map():
    def __init__(self, map_x, map_y):
        self.map_x = map_x
        self.map_y = map_y

    #Create map coordinates to make the movement through map easily
    def create_2d_table(self):
        board = []
        for y in range(self.map_y):
            y_table = []
            for x in range(self.map_x):
                y_table.append(x)
            board.append(y_table)
        return board  

    #Change the tiles to make create appearance of tiles       
    def change_map_tiles(self, list, bordersymbol=border_symbol):
        #Make all of them blank
        for y in range(size_y):
            for x in range(size_x):
                list[y][x]= '  '
        
        for y in range(size_y):
            list[0][y] = bordersymbol + ' '#left side
            list[size_x-1][y] = ' ' + bordersymbol#right side
        #Then add some other shapes to create border
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
        y = random.randint(1, size_y-2)
        x = random.randint(1, size_x-2) 
        if(list[y][x]== '  '):#Assure our fruits won't spawn on occupied tiles
            list[y][x] = fruitsymbol*2
        else:#In case it wants to spawn where snake actually is
            self.fruit_spawn(self, list)

    #Create Player's snake
    def snek_spawn(self, list):
        y = int(size_y/2)
        x = int(size_x/2)
        list[x][y] = '██'
        snek_lenght = 4
        for part in range(snek_lenght):
            x += 1
            list[x][y] = '██'




table = Map(size_x, size_y)
coords = table.create_2d_table()
table.change_map_tiles(coords)
table.fruit_spawn(coords)
table.snek_spawn(coords)
table.map_drawer(coords)
