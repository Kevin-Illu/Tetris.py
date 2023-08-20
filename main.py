import signal
from random import randint

from ui import UI
from Shape import Shape
from constants import TABLE_SIZE, SHAPES, TICKS


def get_random_shape():
    random_index = randint(0, len(SHAPES) - 1)
    random_shape = SHAPES[3][0]
    index = randint(0, TABLE_SIZE - 1)
    shape = Shape(random_shape, index)
    shape.move(0, 0)
    return shape


def main():
    # representing the board
    board = [[0 for _ in range(TABLE_SIZE)] for _ in range(TABLE_SIZE)]
    running = True
    ui = UI(clock_tick=TICKS)

    # maneja la accion de salir del juego
    signal.signal(signal.SIGINT, ui.quit_game)

    shape = get_random_shape()
    
    tomb_of_shapes = []

    translate_x = 1
    translate_y = 0

    while running:
        
        x_is_colliding, y_is_colliding = shape.is_colliding()
        
        for x_pos, y_pos in shape.coordinates:
            
            if x_is_colliding:
                translate_x = 0
                translate_y = 1
                new_x_pos = x_pos + -1
            else:
                new_x_pos = x_pos
                
            if y_is_colliding:
                translate_x = x_pos * -1
                translate_y = 0
                new_y_pos = y_pos + -1
            else:
                new_y_pos = y_pos
            
            board[new_y_pos][new_x_pos] = 1
            
        ui.update(board)
        
        for x_pos, y_pos in shape.coordinates:
            if x_is_colliding:
                new_x_pos = x_pos + -1
            else:
                new_x_pos = x_pos
                
            if y_is_colliding:
                new_y_pos = y_pos + -1
            else:
                new_y_pos = y_pos

            
            board[new_y_pos][new_x_pos] = 0
        
        shape.move(translate_x, translate_y)
            

       

if __name__ == "__main__":
    main()
