from Options import speed


class Parameters:
    def __init__(self):
        self.speed = speed
        if speed < 0.01:
            self.speed = 0.01
        self.score = 0
        self.move_x = None
        self.del_x = None
        self.move_blocking_fruit_flag = False
        self.random_move_flag = False
        self.direction = None
        self.random_move_counter = 0
        self.move_blocking_counter = 0
        self.direction = None
