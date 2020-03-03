from Fruits import trigger
from Options import fruits, impassable_symbols, blank_spot, lenght
from Other import game_over, val2key


class Snake:
    def __init__(self, Map):
        self.move_x = int(Map.map_y / 2)
        self.move_y = int(Map.map_x / 2)
        self.del_x = int(Map.map_y / 2)
        self.del_y = int(Map.map_x / 2) + lenght
        self.map = Map
        self.moves = []
        self.symbol = blank_spot

    def move(
        self,
        direction,
        score,
        speed,
        drunk_fruit_flag,
        boring_fruit_flag,
        drunk_counter,
        boring_counter,
    ):
        if direction == "w":
            move = self.map.board[self.move_x][self.move_y - 1]
        elif direction == "a":
            move = self.map.board[self.move_x - 1][self.move_y]
        elif direction == "s":
            move = self.map.board[self.move_x][self.move_y + 1]
        elif direction == "d":
            move = self.map.board[self.move_x + 1][self.move_y]
        else:
            return (
                score,
                speed,
                drunk_fruit_flag,
                boring_fruit_flag,
                drunk_counter,
                boring_counter,
            )
        self.moves.append(direction)
        if move in impassable_symbols.values():
            game_over(score)
        elif move in fruits.values():
            (
                score,
                speed,
                drunk_fruit_flag,
                boring_fruit_flag,
                drunk_counter,
                boring_counter,
            ) = trigger(
                move,
                self.map,
                score,
                speed,
                drunk_fruit_flag,
                boring_fruit_flag,
                drunk_counter,
                boring_counter,
            )
            self.map.spawn_fruit(val2key(fruits, move))
        else:
            self.delete()
        if direction == "w":
            self.map.board[self.move_x][self.move_y - 1] = impassable_symbols[
                "snake_symbol"
            ]
            self.move_y -= 1
        elif direction == "a":
            self.map.board[self.move_x - 1][self.move_y] = impassable_symbols[
                "snake_symbol"
            ]
            self.move_x -= 1
        elif direction == "s":
            self.map.board[self.move_x][self.move_y + 1] = impassable_symbols[
                "snake_symbol"
            ]
            self.move_y += 1
        elif direction == "d":
            self.map.board[self.move_x + 1][self.move_y] = impassable_symbols[
                "snake_symbol"
            ]
            self.move_x += 1
        if drunk_counter == 0:
            drunk_fruit_flag = False
        else:
            drunk_counter -= 1
        if boring_counter == 0:
            boring_fruit_flag = False
        else:
            boring_counter -= 1
        return (
            score,
            speed,
            drunk_fruit_flag,
            boring_fruit_flag,
            drunk_counter,
            boring_counter,
        )

    def delete(self):
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
