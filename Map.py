from Options import fruits, impassable_symbols, blank_spot, lenght
import random


class Map_obj:
    def __init__(self, map_x, map_y):
        """
        Creating the map with given height and width
        """
        self.map_x = map_x
        self.map_y = map_y
        # add one more x for instruction
        self.board = [[x for x in range(self.map_x + 1)] for y in range(self.map_y)]
        self.change_map_tiles()
        self.add_instruction()

    def draw(self, score):
        """
        Draws the map saved in board and the score
        """
        visible_map = ""
        for x in range(self.map_x):
            visible_row = ""
            for y in range(self.map_y):
                visible_row += self.board[y][x]
            visible_map += visible_row
            visible_map += "\n"
        print(visible_map)
        print("Your acutal score is " + str(score))

    def change_map_tiles(self):
        """
        Changes the initial map tiles, 
        giving blank symbol everywhere 
        and then creating border
        """
        for y in range(self.map_y):
            for x in range(self.map_x):
                self.board[y][x] = blank_spot
        self.create_borders()

    def create_borders(self):
        """
        Changes the border symbols of map, 
        used in change map tiles
        """
        for x in range(self.map_x - 1):
            self.board[x][0] = impassable_symbols["border_symbol"]
            self.board[x][self.map_y - 1] = impassable_symbols["border_symbol"]
        for y in range(self.map_y):
            self.board[0][y] = impassable_symbols["left_border"]
            self.board[self.map_x - 2][y] = impassable_symbols["right_border"]

    def add_instruction(self):
        """
        Adds instructions next to the map
        """
        self.board[self.map_x - 1][1] = (
            fruits["classic_fruit_symbol"] + " - Classic Fruit"
        )
        self.board[self.map_x - 1][2] = "Just points (250 points)"
        self.board[self.map_x - 1][4] = fruits["speed_fruit_symbol"] + " - Speed Fruit"
        self.board[self.map_x - 1][5] = "Increase your speed (500 points)"
        self.board[self.map_x - 1][7] = (
            fruits["move_blocking_fruit_symbol"] + " - Boring Fruit"
        )
        self.board[self.map_x - 1][8] = "Lose ability to change"
        self.board[self.map_x - 1][9] = "direction for 5 moves (750 points)"
        self.board[self.map_x - 1][11] = fruits["random_move_symbol"] + " - Drunk Fruit"
        self.board[self.map_x - 1][12] = "Randomly change directions"
        self.board[self.map_x - 1][13] = "for 3 moves (1500 points)"
        self.board[self.map_x - 1][15] = (
            fruits["multiply_fruit_symbol"] + " - Multiply Fruit"
        )
        self.board[self.map_x - 1][16] = "More fruits on board = more fun (2500 points)"
        self.board[self.map_x - 1][18] = fruits["death_fruit_symbol"] + " - Death Fruit"
        self.board[self.map_x - 1][19] = "You collect it, you die, simple and fun,"
        self.board[self.map_x - 1][20] = "you also get your final score multiplied by 2"

    def spawn_fruit(self, fruit_symbol):
        """
        Spawns given fruit symbol on 
        random unocuppied tile on map
        """
        x = random.randint(1, self.map_x - 2)
        y = random.randint(1, self.map_y - 1)
        while self.board[x][y] != blank_spot:
            x = random.randint(1, self.map_x - 2)
            y = random.randint(1, self.map_y - 1)
        self.board[x][y] = fruits[fruit_symbol]

    def spawn_snake(self, Snake):
        """
        Spawns the snake of given lenght on the map
        """
        x = int(self.map_x / 2)
        y = int(self.map_y / 2)
        for i in range(lenght + 1):
            self.board[x][y] = impassable_symbols["snake_symbol"]
            y += 1
            Snake.moves.append("w")
        Snake.moves[:] = Snake.moves[1:]
