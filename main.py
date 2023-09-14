from random import choice

from board import Board
from shape import Shape
from tetris_shapes import SHAPES


def exit_program():
    print("exit_game")

def get_random_shape():
    return choice(SHAPES)

def main():
    # game logic
    ROWS = 20
    COLS = 10
    is_game_over = False

    board = Board(w=COLS, h=ROWS)
    # shape = Shape(SHAPES[5])
    shape = Shape(get_random_shape())

    shape.coordinates = [[(10, 3), (10, 4), (10, 5)], [(11, 3), (11, 4), (11, 5)]]
    shape.normalized_coordinates = shape.normalize_coordinates(shape.coordinates)

    # keyboard logic
    # moves = {
    #     "right": (0, 1),
    #     "left": (0, -1),
    #     "bottom": (1, 0)
    # }
    
    count = 0
    while (not is_game_over):

        if count >= 4:
            break

        board.print_board(shape)
        shape.commit_rotated_shape()

        count += 1



if __name__ == "__main__":
    main()
