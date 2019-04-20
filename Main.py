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
#Symbols have to be 2 characters
border_symbol = colorama.Fore.WHITE + '#' * 2 + colorama.Style.RESET_ALL
classic_fruit_symbol = colorama.Fore.RED + '░' * 2 + colorama.Style.RESET_ALL
speed_fruit_symbol = colorama.Fore.BLUE + '░' * 2 + colorama.Style.RESET_ALL
boring_fruit_symbol = colorama.Fore.YELLOW + '░' * 2 + colorama.Style.RESET_ALL
drunk_fruit_symbol = colorama.Fore.MAGENTA + '░' * 2 + colorama.Style.RESET_ALL
death_fruit_symbol = colorama.Fore.WHITE + '░' * 2 + colorama.Style.RESET_ALL
multiply_fruit_symbol = colorama.Fore.CYAN + '░' * 2 + colorama.Style.RESET_ALL
snake_symbol = colorama.Fore.GREEN + '█' * 2 + colorama.Style.RESET_ALL
blank_spot = colorama.Fore.BLACK + colorama.Back.BLACK + ' ' * 2 + colorama.Style.RESET_ALL
left_border = colorama.Fore.WHITE + ' #' + colorama.Style.RESET_ALL
right_border = colorama.Fore.WHITE + '# ' + colorama.Style.RESET_ALL
#The less speed you have here, the faster you go
speed = 0.1
#Direction of the beggining
direction = None
#Starting lenght
snek_lenght = 4
#DO NOT TOUCH
score = 0
moves = []
move_x = None
del_x = None
boring_fruit_flag = False
drunk_fruit_flag = False
fruits = [multiply_fruit_symbol, boring_fruit_symbol, classic_fruit_symbol, death_fruit_symbol, drunk_fruit_symbol, speed_fruit_symbol]
impassable_symbols = [border_symbol, snake_symbol, left_border, right_border]
pyautogui.PAUSE = 0.02

#Player score increaser
def score_up(x):
    global score
    score += x

#function used in direction_change to do input without stopping program
def inputter():
    global temp_direction
    input_direction = input()
    if input_direction != direction:
        temp_direction = input_direction

#function used to change direction of snake
def direction_change():
    global temp_direction
    if drunk_fruit_flag == True:
        directions = ['w', 'a', 's', 'd']
        temp_direction = directions[random.randrange(0,3)]
    else:
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

#Effect of eating boring fruit - You are unable to change direction
def boring_fruit_effect():
    global boring_fruit_flag
    boring_fruit_flag = True
    time.sleep(speed*(size_x+size_y)/4)
    boring_fruit_flag = False
#Effect of eating drunk fruit - Your direction is changed randomly
def drunk_fruit_effect():
    global drunk_fruit_flag
    drunk_fruit_flag = True
    time.sleep(speed*(size_x+size_y)/15)
    drunk_fruit_flag = False

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

#function called after moving into impassable tile
def game_over():
    global score
    print('You lose')
    print('Your final score is ' + str(score))
    sys.exit(0)

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
            for x in range(self.map_x + 1):
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
        for x in range(size_x-1):
            list[x][0] = border_symbol#upper side
            list[x][size_y-1] = border_symbol#lower side
        for y in range(size_y):
            list[0][y] = left_border#left side
            list[size_x-2][y] = right_border#right side
        list[int(size_x/2)][int(size_y/2)] = snake_symbol
        list[size_x-1][1] = classic_fruit_symbol + ' - Classic Fruit' 
        list[size_x-1][2] = 'Just points (250 points)'
        list[size_x-1][4] = speed_fruit_symbol + ' - Speed Fruit' 
        list[size_x-1][5] = 'Increase your speed (500 points)'
        list[size_x-1][7] = boring_fruit_symbol + ' - Boring Fruit'  
        list[size_x-1][8] = 'Lose ability to change'
        list[size_x-1][9] = 'direction for {} moves (750 points)'.format(int((size_x+size_y)/4))
        list[size_x-1][11] = drunk_fruit_symbol + ' - Drunk Fruit'
        list[size_x-1][12] = 'Randomly change directions'
        list[size_x-1][13] = 'for {} moves (1500 points)'.format(int((size_x+size_y)/20))
        list[size_x-1][18] = death_fruit_symbol + ' - Death Fruit' 
        list[size_x-1][19] = 'You collect it, you die, simple and fun,'
        list[size_x-1][20] = 'you also get your final score multiplied'
        list[size_x-1][15] = multiply_fruit_symbol + ' - Multiply Fruit'
        list[size_x-1][16] = 'More fruits on board = more fun (2500 points)'
    #Add function to draw a map from coords in form of string
    def map_drawer(self, list):
        visual_map = ''
        for x in range(size_x):
            visual_row = ''
            for y in range(size_y):
                visual_row += str(list[y][x])
            visual_map += visual_row
            visual_map = visual_map + '\n'
        print(visual_map)
        print('Your actual score is ' + str(score))

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
        if boring_fruit_flag == False:
            direction_change()
        #up
        if direction == 'w':
            move = list[move_x][move_y-1]
            if move in impassable_symbols:
                game_over()
            elif move in fruits:
                if move == classic_fruit_symbol:
                    fruit_obj = classic_fruit_obj
                elif move == death_fruit_symbol:
                    fruit_obj = death_fruit_obj
                elif move == speed_fruit_symbol:
                    fruit_obj = speed_fruit_obj
                elif move == drunk_fruit_symbol:
                    fruit_obj = drunk_fruit_obj
                elif move == boring_fruit_symbol:
                    fruit_obj = boring_fruit_obj
                elif move == multiply_fruit_symbol:
                    fruit_obj = multiply_fruit_obj
                fruit_obj.effect()
                fruit_obj.fruit_spawn(coords)
                list[move_x][move_y-1] = snake_symbol
                move_y -= 1
            elif move == blank_spot:
                list[move_x][move_y-1] = snake_symbol
                move_y -= 1
                del_x, del_y = snek_del(list, moves)
                list[del_x][del_y] = blank_spot
            moves.append('w')
        #left
        elif direction == 'a':
            move = list[move_x-1][move_y]
            if move in impassable_symbols:
                game_over()
            elif move in fruits:
                if move == classic_fruit_symbol:
                    fruit_obj = classic_fruit_obj
                elif move == death_fruit_symbol:
                    fruit_obj = death_fruit_obj
                elif move == speed_fruit_symbol:
                    fruit_obj = speed_fruit_obj
                elif move == drunk_fruit_symbol:
                    fruit_obj = drunk_fruit_obj
                elif move == boring_fruit_symbol:
                    fruit_obj = boring_fruit_obj
                elif move == multiply_fruit_symbol:
                    fruit_obj = multiply_fruit_obj                    
                fruit_obj.effect()
                fruit_obj.fruit_spawn(coords)
                list[move_x-1][move_y] = snake_symbol
                move_x -= 1
            elif move == blank_spot:
                list[move_x-1][move_y] = snake_symbol
                move_x -= 1
                del_x, del_y = snek_del(list, moves)
                list[del_x][del_y] = blank_spot
            moves.append('a')
        #down
        elif direction == 's':
            move = list[move_x][move_y+1]
            if move in impassable_symbols:
                game_over()
            elif move in fruits:
                if move == classic_fruit_symbol:
                    fruit_obj = classic_fruit_obj
                elif move == death_fruit_symbol:
                    fruit_obj = death_fruit_obj
                elif move == speed_fruit_symbol:
                    fruit_obj = speed_fruit_obj
                elif move == drunk_fruit_symbol:
                    fruit_obj = drunk_fruit_obj
                elif move == boring_fruit_symbol:
                    fruit_obj = boring_fruit_obj
                elif move == multiply_fruit_symbol:
                    fruit_obj = multiply_fruit_obj
                fruit_obj.effect()
                fruit_obj.fruit_spawn(coords)
                list[move_x][move_y+1] = snake_symbol
                move_y += 1
            elif move == blank_spot:
                list[move_x][move_y+1] = snake_symbol
                move_y += 1
                del_x, del_y = snek_del(list, moves)
                list[del_x][del_y] = blank_spot
            moves.append('s')
        #right
        elif direction == 'd':
            move = list[move_x+1][move_y]
            if move in impassable_symbols:
                game_over()
            elif move in fruits:
                if move == classic_fruit_symbol:
                    fruit_obj = classic_fruit_obj
                elif move == death_fruit_symbol:
                    fruit_obj = death_fruit_obj
                elif move == speed_fruit_symbol:
                    fruit_obj = speed_fruit_obj
                elif move == drunk_fruit_symbol:
                    fruit_obj = drunk_fruit_obj
                elif move == boring_fruit_symbol:
                    fruit_obj = boring_fruit_obj
                elif move == multiply_fruit_symbol:
                    fruit_obj = multiply_fruit_obj
                fruit_obj.effect()
                fruit_obj.fruit_spawn(coords)
                list[move_x+1][move_y] = snake_symbol
                move_x += 1
            elif move == blank_spot:
                list[move_x+1][move_y] = snake_symbol
                move_x += 1
                del_x, del_y = snek_del(list, moves)
                list[del_x][del_y] = blank_spot
            moves.append('d')

#Superclass of all fruits
class Fruit():
    def __init__(self, fruit_symbol):
        self.fruit_symbol = fruit_symbol

        #Creating fruit randomly on board
    def fruit_spawn(self, list):
        while 1:
            y = random.randint(1, size_y-2)
            x = random.randint(1, size_x-2) 
            if(list[x][y]== blank_spot):#Assure our fruits won't spawn on occupied tiles
                list[x][y] = self.fruit_symbol
                break
            else:#In case it wants to spawn where snake actually is
                continue

#Classic fruit - Just points
class Classic_Fruit(Fruit):
    def effect(self):
        score_up(250)

#Speed fruit - Move faster
class Speed_Fruit(Fruit):
    def effect(self):
        global speed
        score_up(500)
        speed /= 1.37

#Boring fruit - Unable to change direction
class Boring_Fruit(Fruit):
    def effect(self):
        score_up(750)
        threading.Thread(target = boring_fruit_effect).start()

#Drunk fruit - Get controled by rng god
class Drunk_Fruit(Fruit):
    def effect(self):
        score_up(1500)
        threading.Thread(target = drunk_fruit_effect).start()

#Death fruit - You eat, you die
class Death_Fruit(Fruit):
    def effect(self):
        score_up(score*3)
        game_over()
#Multiply Fruit - More Fruits
class Multiply_Fruit(Fruit):
    def effect(self):
        score_up(2500)
        classic_fruit_obj.fruit_spawn(coords)
        speed_fruit_obj.fruit_spawn(coords)
        boring_fruit_obj.fruit_spawn(coords)
        drunk_fruit_obj.fruit_spawn(coords)
        death_fruit_obj.fruit_spawn(coords)

#create map        
table = Map(size_x, size_y)
#create coords
coords = table.create_2d_table()
#create cooler tiles
table.change_map_tiles(coords)
#create snake
table.snek_spawn(coords, snek_lenght)
#create fruits
classic_fruit_obj = Classic_Fruit(classic_fruit_symbol)
classic_fruit_obj.fruit_spawn(coords)
speed_fruit_obj = Speed_Fruit(speed_fruit_symbol)
speed_fruit_obj.fruit_spawn(coords)
boring_fruit_obj = Boring_Fruit(boring_fruit_symbol)
boring_fruit_obj.fruit_spawn(coords)
drunk_fruit_obj = Drunk_Fruit(drunk_fruit_symbol)
drunk_fruit_obj.fruit_spawn(coords)
death_fruit_obj = Death_Fruit(death_fruit_symbol)
death_fruit_obj.fruit_spawn(coords)
multiply_fruit_obj = Multiply_Fruit(multiply_fruit_symbol)
multiply_fruit_obj.fruit_spawn(coords)
#move the snake    
while 1:
    table.snek_move(coords, direction)
    time.sleep(speed)
    if sys.platform == 'linux':
        os.system('clear')
    else:
        os.system('cls')
    table.map_drawer(coords)