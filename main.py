from random import choice
from board import Board

from tetris_shapes import SHAPES
from shape import Shape

def get_random_shape():
    return choice(SHAPES)

def main():
    ROWS = 20
    COLS = 10

    board = Board(w=COLS, h=ROWS)
    shape = Shape(SHAPES[0])
    shape.coordinates = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)]]
    shape.normalized_coordinates = [(0, 0), (0, 1), (0, 2), (1, 2)]

    is_game_over = False
    moves = {
        "right": (0, 1),
        "left": (0, -1),
        "bottom": (1, 0)
    }

    y, x = moves["bottom"]

    while (not is_game_over):
        is_colliding_bottom = shape.check_if_next_move_is_colliding(y, x, board)
        is_colliding_right = shape.check_if_next_move_is_colliding(0, 1, board)

        board.print_board(shape)

        if not is_colliding_bottom and not is_colliding_right:
            shape.move_bottom()
            # shape.move_right()
        else:
            break



if __name__ == "__main__":
    main()
