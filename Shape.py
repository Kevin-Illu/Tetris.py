from constants import SHAPES, GRID_WIDTH, GRID_HEIGHT, TABLE_SIZE

class Shape():
    def __init__(self, shape, x):
        self.shape = shape
        self.x = x
        self.coordinates = None
    
    def get_coordinates(self, index):
        x = index % GRID_WIDTH
        y = index // GRID_WIDTH
        return x, y
    
    def get_shape_position(self):
        coordinates = []
        for row in self.shape:
            x, y = self.get_coordinates(row)
            coordinates.append((x, y))
            
        return coordinates
    
    def move(self, dx, dy):
        new_coordinates = []
        coordinates = self.get_shape_coordinates()
            
        for x, y in coordinates:
            new_x = x + dx
            new_y = y + dy
            
            new_coordinates.append((new_x, new_y))
        
        self.coordinates = new_coordinates


    def get_shape_coordinates(self):
        coordinates = None
        if self.coordinates is None:
            coordinates = self.get_shape_position()
        else:
            coordinates = self.coordinates
            
        return coordinates

    # def is_colliding(self):
    #     coordinates = self.get_shape_coordinates()
        
    #     for x, y in coordinates:
    #         if x < 0 or x >= TABLE_SIZE:
    #             return (True, False)
    #         elif y < 0 or y >= TABLE_SIZE:
    #             return (False, True)
    #         else:
    #             continue
        
    #     return (False, False)

    def is_colliding(self):
        for x, y in self.coordinates:
            if x < 0 or x >= TABLE_SIZE or y < 0 or y >= TABLE_SIZE:
                return True
        return False
