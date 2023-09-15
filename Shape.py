from random import randint

board_w = 10

class Shape:
    def __init__(self, b) -> None:
        self.blocks = b
        # coordinates system
        self.ref = self.get_reference()
        self.coordinates = self.get_random_coordinates()
        self.normalized_coordinates = self.normalize_coordinates(self.coordinates)

    def get_rows_and_cols(self):
        return (len(self.blocks), len(self.blocks[0]))
    
    def get_random_coordinates(self):
        """
        Generate initial coordinates for the shape, always positioned at the
        top of the board.
    
        Returns:
            list of tuples: A list of (row, column) coordinates representing
            the initial position of the shape on the board.
        """
        rows, cols = self.get_rows_and_cols()

        last_permitted_coordinate = board_w - cols
        initial_cordinate = randint(0, last_permitted_coordinate)

        coordinates = []
        counter = 0

        for row in range(rows):
            new_cols = []
            for _ in range(cols):
                new_cols.append((row, initial_cordinate + counter))
                counter += 1

            counter = 0
            coordinates.append(new_cols)

        return coordinates
    
    def get_rotated_shape(self):
        # Obtenemos las dimensiones de la figura
        rows, cols = self.get_rows_and_cols()

        # Creamos una nueva matriz vacía para la figura rotada
        rotated_shape = [[0] * rows for _ in range(cols)]

        # Rotamos la figura
        for i in range(rows):
            for j in range(cols):
                rotated_shape[j][rows - 1 - i] = self.blocks[i][j]
    
        return rotated_shape

    def get_new_coordinates(self):
        _, initial_x = self.coordinates[0][0]
        rotated_shape = self.get_rotated_shape()
        
        # puede haber conflictos :c
        self.blocks = rotated_shape
        rows, cols = self.get_rows_and_cols()

        new_coordinates = []
        counter = 0
        for row in range(rows):
            coordinates_for_row = []
            for _ in range(cols):
                coordinates_for_row.append((row, initial_x + counter))
                counter += 1

            counter = 0
            new_coordinates.append(coordinates_for_row)
        return new_coordinates

    def get_rotated_shape_and_coordinates(self):
        return self.get_rotated_shape(), self.get_new_coordinates()
        
    def get_reference(self):
        """
        Extracts the coordinates of the occupied cells within the shape.

        This function iterates through the shape's blocks to determine the
        row and column indices where the current cell contains a value of 1.
        These indices indicate that the current cell is part of the shape and
        not an empty space (0).

        Returns:
            list of tuples: A list of (row, column) coordinates representing
            the occupied positions within the shape.
        """

        rows, cols = self.get_rows_and_cols()

        reference = []
        for j in range(rows):
            for i in range(cols):
                if self.blocks[j][i] == 1:
                    reference.append((j, i))
            
        return reference

    def normalize_coordinates(self, next_coordinates):
        """
        Obtain the actual (row, column) coordinates of the shape on the board.

        Returns:
            list of tuples: A list of (row, column) coordinates representing
            the true position of the shape on the game board.
        """
        coordinates = []
        for row, col in self.ref:
            y, x = next_coordinates[row][col]
            coordinates.append((y, x))

        return coordinates

    def get_true_coordinates(self, old_coordinates, new_coordinates):
        old_y, old_x = old_coordinates
        new_y, new_x = new_coordinates

        true_x = 0
        true_y = 0
        
        if new_x < 0:
            true_x = old_x - 1
        else:
            true_x = old_x + new_x

        if new_y < 0:
            true_y = old_y - 1
        else:
            true_y = old_y + new_y

        return (true_y, true_x)

    def get_next_coordinates(self, y, x):
        next_coordinates = []
        
        for row in self.coordinates:
            coordinates_for_row = []
            for old_coordinates in row:
                true_y, true_x = self.get_true_coordinates(old_coordinates, (y, x))
                coordinates_for_row.append((true_y, true_x))
            next_coordinates.append(coordinates_for_row)

        return next_coordinates

    def check_if_next_move_is_colliding(self, y, x, board):
        next_coordinates = self.get_next_coordinates(y=y, x=x)
        normalized_coordinates = self.normalize_coordinates(next_coordinates)

        for y, x in normalized_coordinates:
            if x > board.width - 1 or x < 0:
                return True
            elif y > board.height - 1:
                return True

        for y, x in normalized_coordinates:
            if board.grid[y][x] != 0:
                return True

        return False

    def commit_next_move(self, next_coordinates):
        self.coordinates = next_coordinates
        self.normalized_coordinates = self.normalize_coordinates(next_coordinates)

    def move_left(self):
        next_coordinates = self.get_next_coordinates(0, -1)
        self.commit_next_move(next_coordinates)

    def move_right(self):
        next_coordinates = self.get_next_coordinates(0, 1)
        self.commit_next_move(next_coordinates)

    def move_bottom(self, y=1, x=0):
        next_coordinates = self.get_next_coordinates(y, x)
        self.commit_next_move(next_coordinates)
    
    def rotate_move(self):
        rotated_shape, new_coordinates = self.get_rotated_shape_and_coordinates()
        self.blocks = rotated_shape
        self.ref = self.get_reference()
        self.commit_next_move(new_coordinates)


