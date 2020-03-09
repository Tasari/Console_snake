from Fruits import trigger
from Options import fruits, impassable_symbols, blank_spot, lenght
from Other import game_over, val2key


class Snake:
    def __init__(self, Map, parameters_object):
        """
        Creates the table of past moves and 
        registers the snake on the middle of map
        """
        self.move_x = int(Map.map_x / 2)
        self.move_y = int(Map.map_y / 2)
        self.del_x = int(Map.map_x / 2)
        self.del_y = int(Map.map_y / 2) + lenght
        self.map = Map
        self.moves = []
        self.symbol = impassable_symbols["snake_symbol"]
        self.parameters_object = parameters_object

    def move(self):
        """
        moves the snake in given direction,
        remembers that move, ends the game if impassable
        symbol is approached, deletes the saved move 
        if its necessary, and lowers down the counter of blocked moves
        """
        if self.parameters_object.direction == "w":
            move = self.map.board[self.move_x][self.move_y - 1]
        elif self.parameters_object.direction == "a":
            move = self.map.board[self.move_x - 1][self.move_y]
        elif self.parameters_object.direction == "s":
            move = self.map.board[self.move_x][self.move_y + 1]
        elif self.parameters_object.direction == "d":
            move = self.map.board[self.move_x + 1][self.move_y]
        else:
            return
        self.moves.append(self.parameters_object.direction)
        if move in impassable_symbols.values():
            game_over(self.parameters_object.score)
        elif move in fruits.values():
            trigger(move, self.map, self.parameters_object)
            self.map.spawn_fruit(val2key(fruits, move))
        else:
            self.delete()
        if self.parameters_object.direction == "w":
            self.map.board[self.move_x][self.move_y - 1] = impassable_symbols[
                "snake_symbol"
            ]
            self.move_y -= 1
        elif self.parameters_object.direction == "a":
            self.map.board[self.move_x - 1][self.move_y] = impassable_symbols[
                "snake_symbol"
            ]
            self.move_x -= 1
        elif self.parameters_object.direction == "s":
            self.map.board[self.move_x][self.move_y + 1] = impassable_symbols[
                "snake_symbol"
            ]
            self.move_y += 1
        elif self.parameters_object.direction == "d":
            self.map.board[self.move_x + 1][self.move_y] = impassable_symbols[
                "snake_symbol"
            ]
            self.move_x += 1
        if self.parameters_object.random_move_counter == 0:
            self.parameters_object.random_move_flag = False
        else:
            self.parameters_object.random_move_counter -= 1
        if self.parameters_object.move_blocking_counter == 0:
            self.parameters_object.move_blocking_fruit_flag = False
        else:
            self.parameters_object.move_blocking_counter -= 1

    def delete(self):
        """
        Deletes the snake symbol from given tile
        """
        self.map.board[self.del_x][self.del_y] = blank_spot
        if self.moves[0] == "w":
            self.del_y -= 1
        elif self.moves[0] == "a":
            self.del_x -= 1
        elif self.moves[0] == "s":
            self.del_y += 1
        elif self.moves[0] == "d":
            self.del_x += 1
        self.moves = self.moves[1:]
