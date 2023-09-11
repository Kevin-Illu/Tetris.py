from random import choice

from board import Board
from shape import Shape
from keyboard_handler import KeyboardHandler
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
    shape = Shape(SHAPES[0])
    shape.coordinates = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)]]
    shape.normalized_coordinates = [(0, 0), (0, 1), (0, 2), (1, 2)]
    # keyboard logic
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

        if is_colliding_bottom or is_colliding_right:
            is_game_over = True
            print("game mover")



if __name__ == "__main__":
    main()
