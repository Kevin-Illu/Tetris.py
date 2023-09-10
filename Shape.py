from random import randint
board_w = 10

class Shape:
    def __init__(self, b) -> None:
        self.blocks = b
        self.width = len(self.blocks[0])
        self.height = len(self.blocks)
        
        # coordinates system
        self.ref = self.get_reference()
        self.coordinates = self.get_random_coordinates()
        self.normalized_coordinates = self.normalize_coordinates(self.coordinates)
    
    def get_random_coordinates(self):
        """
        Generate initial coordinates for the shape, always positioned at the
        top of the board.
    
        Returns:
            list of tuples: A list of (row, column) coordinates representing
            the initial position of the shape on the board.
        """
        last_permitted_coordinate = board_w - self.width
        initial_cordinate = randint(0, last_permitted_coordinate)

        coordinates = []
        counter = 0

        for row in range(0, self.height):
            cols = []
            for _ in range(0, self.width):
                cols.append((row, initial_cordinate + counter))
                counter += 1

            counter = 0
            coordinates.append(cols)

        return coordinates

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
        reference = [(i, j) for i in range(self.height) for j in range(self.width) if self.blocks[i][j] == 1]
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
    

    # TODO: use the new coordinates
    def get_true_coordinates(self, old_coordinates, new_coordinates):
        old_y, old_x = old_coordinates
        new_y, new_x = new_coordinates

        true_x = 0
        true_y = 0

        if new_x < 0:
            true_x = old_x - 1
        else:
            true_x = old_x + new_x

        if new_y > 0:
            true_y = 1
        else:
            true_y = new_y

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

    def move_bottom(self):
        next_coordinates = self.get_next_coordinates(1, 0)
        self.commit_next_move(next_coordinates)

    def move_right(self):
        next_coordinates = self.get_next_coordinates(0, 1)
        self.commit_next_move(next_coordinates)


