from random import choice
from Board import Board

from tetris_shapes import SHAPES
from Shape import Shape

def get_random_shape():
    return choice(SHAPES)

def main():
    ROWS = 20
    COLS = 10

    board = Board(w=COLS, h=ROWS)
    shape = Shape(SHAPES[0])
    shape.normalized_coordinates = shape.normalize_coordinates([[(18, 7), (18, 8), (18, 9)], [(19, 7), (19, 8), (19, 9)], [(20, 7), (20, 8), (20, 9)]])

    is_game_over = False

    while (not is_game_over):
        board.print_board(shape)
        break


if __name__ == "__main__":
    main()
