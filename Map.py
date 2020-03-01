from Options import fruits, impassable_symbols, blank_spot
import random
class Map_obj():
    def __init__(self, map_x, map_y):
        self.map_x = map_x
        self.map_y = map_y
        self.board = [[ x for x in range(self.map_x+1)] for y in range(self.map_y)]
        self.change_map_tiles()
        self.add_instruction()


    def draw(self, score):
        visible_map = ''
        for x in range(self.map_x):
            visible_row = ''
            for y in range(self.map_y):
                visible_row += self.board[y][x]
            visible_map += visible_row
            visible_map += '\n'
        print(visible_map)
        print('Your acutal score is ' + str(score)) 

    def change_map_tiles(self):
        #Make all of them blank
        for y in range(self.map_y):
            for x in range(self.map_x):
                self.board[y][x]= blank_spot
        #Add some other shapes to create border
        for x in range(self.map_x-1):
            self.board[x][0] = impassable_symbols['border_symbol']#upper side
            self.board[x][self.map_y-1] = impassable_symbols['border_symbol']#lower side
        for y in range(self.map_y):
            self.board[0][y] = impassable_symbols['left_border']#left side
            self.board[self.map_x-2][y] = impassable_symbols['right_border']#right side

    def add_instruction(self):
        self.board[self.map_x-1][1] = fruits['classic_fruit_symbol'] + ' - Classic Fruit' 
        self.board[self.map_x-1][2] = 'Just points (250 points)'
        self.board[self.map_x-1][4] = fruits['speed_fruit_symbol'] + ' - Speed Fruit' 
        self.board[self.map_x-1][5] = 'Increase your speed (500 points)'
        self.board[self.map_x-1][7] = fruits['boring_fruit_symbol'] + ' - Boring Fruit'  
        self.board[self.map_x-1][8] = 'Lose ability to change'
        self.board[self.map_x-1][9] = 'direction for 5 moves (750 points)'
        self.board[self.map_x-1][11] = fruits['drunk_fruit_symbol'] + ' - Drunk Fruit'
        self.board[self.map_x-1][12] = 'Randomly change directions'
        self.board[self.map_x-1][13] = 'for 3 moves (1500 points)'
        self.board[self.map_x-1][15] = fruits['multiply_fruit_symbol'] + ' - Multiply Fruit'
        self.board[self.map_x-1][16] = 'More fruits on board = more fun (2500 points)'
        self.board[self.map_x-1][18] = fruits['death_fruit_symbol'] + ' - Death Fruit' 
        self.board[self.map_x-1][19] = 'You collect it, you die, simple and fun,'
        self.board[self.map_x-1][20] = 'you also get your final score multiplied by 2'
    
    def spawn_fruit(self, fruit_symbol):
        x = random.randint(1, self.map_x-2)
        y = random.randint(1, self.map_y-1)
        while self.board[x][y] != blank_spot:
            x = random.randint(1, self.map_x-2)
            y = random.randint(1, self.map_y-1)
        self.board[x][y] = fruits[fruit_symbol]

    def spawn_snake(self, lenght, moves):
        x = int(self.map_x/2)
        y = int(self.map_y/2)
        for i in range(lenght):
            self.board[x][y] = impassable_symbols['snake_symbol']
            y += 1
            moves.append('w')