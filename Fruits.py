from Options import fruits
from Other import game_over


def boring_fruit_effect(Map, parameters_object):
    """
    Sets the boring fruit flag to True 
    and sets the counter of moves till 
    the end to 5
    """
    parameters_object.boring_counter = 5
    parameters_object.boring_fruit_flag = True


def drunk_fruit_effect(Map, parameters_object):
    """
    Sets the drunk fruit flag to True 
    and sets the counter of moves till 
    the end to 3
    """
    parameters_object.drunk_counter = 3
    parameters_object.drunk_fruit_flag = True


def trigger(fruit_symbol, Map, parameters_object):
    """
    Function triggering the fruit effect, 
    based on the symbol of the fruit
    """
    if fruit_symbol == fruits["classic_fruit_symbol"]:
        parameters_object.score += 250
    elif fruit_symbol == fruits["speed_fruit_symbol"]:
        parameters_object.score += 500
        parameters_object.speed -= 0.1
        if parameters_object.speed < 0.01:
            parameters_object.speed = 0.01
    elif fruit_symbol == fruits["boring_fruit_symbol"]:
        parameters_object.score += 1000
        boring_fruit_effect(Map, parameters_object)
    elif fruit_symbol == fruits["drunk_fruit_symbol"]:
        parameters_object.score += 1500
        drunk_fruit_effect(Map, parameters_object)
    elif fruit_symbol == fruits["multiply_fruit_symbol"]:
        parameters_object.score += 1000
        [Map.spawn_fruit(x) for x in fruits.keys()]
    elif fruit_symbol == fruits["death_fruit_symbol"]:
        parameters_object.score *= 2
        game_over(parameters_object.score)
