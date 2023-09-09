from random import choice

from tetris_shapes import SHAPES
from Shape import Shape


def get_random_shape():
    return choice(SHAPES)

def main():
    ROWS = 20
    COLS = 10
    board = [[0 for _ in range(0, COLS)] for _ in range(0, ROWS)]
    shape = Shape(SHAPES[1])

    for row, col in shape.get_coordinates():
        board[row][col] = 1

    for row in board:
        print(row)

if __name__ == "__main__":
    main()
