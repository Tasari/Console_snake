from Options import fruits
from Other import score_up, game_over

def boring_fruit_effect(Map):
    '''
    Sets the boring fruit flag to True 
    and sets the counter of moves till 
    the end to 5
    '''
    boring_counter = 5
    boring_fruit_flag = True
    return boring_fruit_flag, boring_counter



def drunk_fruit_effect(Map):
    '''
    Sets the drunk fruit flag to True 
    and sets the counter of moves till 
    the end to 3
    '''
    drunk_counter = 3
    drunk_fruit_flag = True
    return drunk_fruit_flag, drunk_counter


def trigger(
    fruit_symbol,
    Map,
    score,
    speed,
    drunk_fruit_flag,
    boring_fruit_flag,
    drunk_counter,
    boring_counter,
):
    '''
    Function triggering the fruit effect, 
    based on the symbol of the fruit
    '''
    if fruit_symbol == fruits["classic_fruit_symbol"]:
        score += 250
    elif fruit_symbol == fruits["speed_fruit_symbol"]:
        score += 500
        speed -= 0.1
        if speed < 0.01:
            speed = 0.01
    elif fruit_symbol == fruits["boring_fruit_symbol"]:
        score += 1000
        boring_fruit_flag, boring_counter = boring_fruit_effect(Map)
    elif fruit_symbol == fruits["drunk_fruit_symbol"]:
        score += 1500
        drunk_fruit_flag, drunk_counter = drunk_fruit_effect(Map)
    elif fruit_symbol == fruits["multiply_fruit_symbol"]:
        score += 1000
        [Map.spawn_fruit(x) for x in fruits.keys()]
    elif fruit_symbol == fruits["death_fruit_symbol"]:
        score *= 2
        game_over(score)
    return (
        score,
        speed,
        drunk_fruit_flag,
        boring_fruit_flag,
        drunk_counter,
        boring_counter,
    )
