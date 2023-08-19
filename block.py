class Block:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.type = t  # type of shape
        
        # the speed can be normal or fast
        self.speeds = (1, 2)

    def update_y(self, speed):
        self.y += self.speeds[speed]

    def update_x(self):
        # only by normal speed
        self.x += self.speeds(0)