import Fruits
from Options import fruits, impassable_symbols, blank_spot, lenght
import unittest.mock
import Map
import Snake

mockparams = unittest.mock.MagicMock()
mockmap = unittest.mock.MagicMock()

def test_trigger_classic():
    mockparams.score = 0
    Fruits.trigger(fruits["classic_fruit_symbol"], mockmap, mockparams)
    assert mockparams.score == 250
    Fruits.trigger(fruits["classic_fruit_symbol"], mockmap, mockparams)
    Fruits.trigger(fruits["classic_fruit_symbol"], mockmap, mockparams)
    Fruits.trigger(fruits["classic_fruit_symbol"], mockmap, mockparams)
    assert mockparams.score == 1000


def test_trigger_speed():
    mockparams.score = 0
    mockparams.speed = 5
    Fruits.trigger(fruits["speed_fruit_symbol"], mockmap, mockparams)
    assert mockparams.speed == 4.9
    assert mockparams.score == 500
    mockparams.speed = 0.01
    Fruits.trigger(fruits["speed_fruit_symbol"], mockmap, mockparams)
    assert mockparams.speed == 0.01


def test_trigger_move_block():
    mockparams.score = 0
    mockparams.move_blocking_counter = 0
    mockparams.move_blocking_fruit_flag = False
    Fruits.trigger(fruits["move_blocking_fruit_symbol"], mockmap, mockparams)
    assert mockparams.score == 1000
    assert mockparams.move_blocking_counter == 4
    assert mockparams.move_blocking_fruit_flag == True


def test_trigger_random_move():
    mockparams.score = 0
    mockparams.random_move_counter = 0
    mockparams.random_move_flag = False
    Fruits.trigger(fruits["random_move_symbol"], mockmap, mockparams)
    assert mockparams.score == 1500
    assert mockparams.random_move_counter == 2
    assert mockparams.random_move_flag == True


def test_change_map_tiles():
    size_x = 20
    size_y = 20
    testmap = Map.Map_obj(size_x, size_y)
    assert testmap.board[size_x-3][size_y-1] == impassable_symbols["border_symbol"]
    assert testmap.board[size_x-2][5] == impassable_symbols["right_border"]
    assert testmap.board[0][0] == impassable_symbols["left_border"]


def test_spawn_snake():
    size_x = 20
    size_y = 20
    testmap = Map.Map_obj(size_x, size_y)
    mocksnake = unittest.mock.MagicMock()
    testmap.spawn_snake(mocksnake)
    assert testmap.board[int(size_x/2)][int(size_y/2)] == impassable_symbols["snake_symbol"]
    assert testmap.board[int(size_x/2)][int(size_y/2)+lenght] == impassable_symbols["snake_symbol"]
    mocksnake.moves.append.assert_called_with('w')

def test_snake_move():
    size_x = 20
    size_y = 20
    lenght = 4
    testmap = Map.Map_obj(size_x, size_y)
    mockparams = unittest.mock.MagicMock()
    testsnake = Snake.Snake(testmap, mockparams)
    mockparams = unittest.mock.MagicMock()
    testsnake.parameters_object.direction = "w"
    testsnake.move()
    assert testsnake.move_y == (size_y/2)-1
    assert testsnake.del_y == (size_y/2) + lenght - 1
    testsnake.parameters_object.direction = "a"
    testsnake.move()
    assert testsnake.move_y == (size_y/2) - 1
    assert testsnake.move_x == (size_x/2) - 1
    assert testsnake.del_y == (size_y/2) + lenght - 1
    assert testsnake.del_x == (size_x/2) - 1
    testsnake.move()
    testsnake.parameters_object.direction = "s"
    testsnake.move()
    assert testsnake.move_y == (size_y/2)
    assert testsnake.move_x == (size_x/2) - 2
    assert testsnake.del_y == (size_y/2) + lenght
    assert testsnake.del_x == (size_x/2) - 2
    testsnake.parameters_object.direction = "d"
    testsnake.move()
    assert testsnake.move_y == (size_y/2)
    assert testsnake.move_x == (size_x/2) - 1
    assert testsnake.del_y == (size_y/2) + lenght
    assert testsnake.del_x == (size_x/2) - 1

def test_move_decounter():
    mockparams = unittest.mock.MagicMock()
    testsnake = Snake.Snake(unittest.mock.MagicMock(), mockparams)
    
    testsnake.parameters_object.direction = "w"
    testsnake.parameters_object.move_blocking_counter = 5
    testsnake.parameters_object.random_move_counter = 3
    testsnake.move()
    assert testsnake.parameters_object.move_blocking_counter == 4
    assert testsnake.parameters_object.random_move_counter == 2