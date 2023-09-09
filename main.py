from random import randint, choice
from shapes import SHAPES

def main():
    rows = 20
    cols = 10
    board = [[0 for _ in range(0, cols)] for _ in range(0, rows)]
    shape = get_random_shape()

    shape_w = len(shape[0])
    shape_h = len(shape)

    shape_coordinates = get_random_coordinates(cols, shape_w, shape_h)
    ref = get_coordinate_reference(shape)

    # merge coordinates and references :D
    for row, col in ref:
        y, x = shape_coordinates[row][col]
        board[y][x] = 1

    for row in board:
        print(row)

def get_random_shape():
    return choice(SHAPES)

def get_coordinate_reference(shape):
    reference = []

    for i, row in enumerate(shape):
        for e, col in enumerate(row):
            if col == 1:
                reference.append((i, e))

    return reference

def get_random_coordinates(board_w, shape_w, shape_h):
    last_permited_cordinate = board_w - shape_w
    initial_cordinate = randint(0, last_permited_cordinate)

    coordinates = []
    counter = 0

    for row in range(0, shape_h):
        cols = []
        for _ in range(0, shape_w):
            cols.append((row, initial_cordinate + counter))
            counter += 1

        counter = 0
        coordinates.append(cols)

    return coordinates

if __name__ == "__main__":
    main()
