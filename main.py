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
    shape = Shape(get_random_shape())
    # keyboard logic
    moves = {
        "right": (0, 1),
        "left": (0, -1),
        "bottom": (1, 0)
    }
    y, x = moves["bottom"]

    while (not is_game_over):
        
        is_colliding = shape.check_if_next_move_is_colliding(y, x, board)
        board.print_board(shape)

        # test the bottom collisions
        if not is_colliding:
            shape.move_bottom()
        else:
            break




if __name__ == "__main__":
    main()
