import Fruits
from Options import fruits
import unittest.mock

mockmap = unittest.mock.Mock()
mockparams = unittest.mock.Mock()


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