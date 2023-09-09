from random import randint
board_w = 10

class Shape:
    def __init__(self, b) -> None:
        self.blocks = b
        self.width = len(self.blocks[0])
        self.height = len(self.blocks)
        self.coordinates = self.get_random_coordinates()
        self.ref = self.get_reference()
    
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

    def get_coordinates(self):
        """
        Obtain the actual (row, column) coordinates of the shape on the board.

        Returns:
            list of tuples: A list of (row, column) coordinates representing
            the true position of the shape on the game board.
        """
        coordinates = []
        for row, col in self.ref:
            y, x = self.coordinates[row][col]
            coordinates.append((y, x))

        return coordinates
