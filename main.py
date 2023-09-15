from random import choice
import keyboard

from board import Board
from shape import Shape
from tetris_shapes import SHAPES

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

    is_colliding = False

    while (not is_game_over):

        board.mark_deaths()
        board.print_board(shape)

        y, x = moves["bottom"]
        is_colliding = shape.check_if_next_move_is_colliding(y, x, board)

        if not is_colliding:
            shape.move_bottom()
        else:
            board.tomb.append(shape.normalized_coordinates)
            del shape
            shape = Shape(get_random_shape())
            

        try:
            event = keyboard.read_event()

            if event.name == 'q':
                break  # Sale del bucle si la tecla "q" está presionada
            
            elif event.name == 'j':
                y, x = moves["bottom"]
                is_bottom_colliding = shape.check_if_next_move_is_colliding(0, 0, board)

                if not is_bottom_colliding:
                    shape.move_bottom(0, 0)
                else:
                    continue

            elif event.name == 'h':
                y, x = moves["left"]
                is_left_colliding = shape.check_if_next_move_is_colliding(y, x, board)

                if not is_left_colliding:
                    shape.move_left()
                else:
                    continue

            elif event.name == 'l':
                y, x = moves["right"]
                is_colliding = shape.check_if_next_move_is_colliding(y, x, board)

                if not is_colliding:
                    shape.move_right()
                else:
                    continue

            elif event.name == 'k':
                y, x = moves["left"]
                is_left_colliding = shape.check_if_next_move_is_colliding(y, x, board)

                if is_left_colliding:
                    continue

                y, x = moves["right"]
                is_right_colliding = shape.check_if_next_move_is_colliding(y, x, board)

                if is_right_colliding:
                    continue

                shape.rotate_move()         
        except:
            break




if __name__ == "__main__":
    main()
