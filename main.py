import signal

from ui import UI
from block import Block
from constants import TABLE_SIZE


def main():
    # representing the matrix of the tetrix
    board = [[0 for _ in range(0, TABLE_SIZE)] for _ in range(0, TABLE_SIZE)]
    running = True

    ui = UI()
    signal.signal(signal.SIGINT, ui.quit_game)
    block = Block(0, 0, 0)

    while running:
        
        
        # user input
        

        if block.y <= TABLE_SIZE:
            # update the position of the block
            board[block.y - 1][block.x - 1] = 1
        else:
            block.y = 0

        # through to each column and row and create
        # the ascii art to print to screen
        ui.print_ui(board)

        if block.x <= TABLE_SIZE:
            board[block.y - 1][block.x - 1] = 0
        else:
            block.x = 0
        block.y += 1

if __name__ == "__main__":
    main()
