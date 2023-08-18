import signal
from random import randint

from ui import UI
from block import Block
from constants import TABLE_SIZE


def main():
    # representing the board
    board = [[0 for _ in range(0, TABLE_SIZE)] for _ in range(0, TABLE_SIZE)]
    running = True
    ui = UI(clock_tick=.2)

    # maneja la accion de salir del juego
    signal.signal(signal.SIGINT, ui.quit_game)

    # initial block
    initial_x_pos = randint(0, len(board[0]) - 1)
    block = Block(x=initial_x_pos, y=0, t=0)

    # posiciones en las que el bloque
    # colisiono con la ultima fila u otro bloque
    filled_cells = []

    while running:
        # TODO: Manejar las entradas del jugador (mover, rotar, acelerar)

        # Actualizar el tablero con las celdas ocupadas por bloques completos
        if len(filled_cells) != 0:
            for ended_x_pos, ended_y_pos in filled_cells:
                board[ended_y_pos][ended_x_pos] = 1

        # Crear el siguiente bloque si no hay uno en juego actualmente
        if block is None:
            initial_x_pos = randint(0, len(board[0]) - 1)
            block = Block(x=initial_x_pos, y=0, t=0)


        # Actualizar el tablero con la posición actual del bloque
        if block is not None:
            board[block.y][block.x] = 1
            ui.update(board)
            board[block.y][block.x] = 0

        
        # TODO: Lógica de colisión con otras celdas y finalización del juego
        # TODO: Actualizar la posición y estado del bloque en función de la lógica del juego
        # COLISION DE BLOQUES

        # verifica si la siguiente posicion del bloque se 
        # encuentra ocupada
        if block.y + 1 <= TABLE_SIZE - 1 and board[block.y + 1][block.x] == 1:
            filled_cells.append((block.x, block.y))
            block = None

        # verifica si el bloque actual ya llego a la ultima
        # fila del tablero
        elif block is not None and block.y >= TABLE_SIZE - 1:
            # update the cells occupied by the user
            filled_cells.append((block.x, block.y))
            block = None
        else:
            # si no es la ultima fila entonces
            # continua moviendoce c:
            block.update_y(0)


if __name__ == "__main__":
    main()
