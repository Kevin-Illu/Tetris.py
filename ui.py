import os, sys, time
from constants import TABLE_SIZE

class UI:
    def __init__(self):
        self.table_size = TABLE_SIZE
        self.emtpy_cell = "."
        self.filled_cell = "#"
        self.tab = "\n" # tab in each row

    def sprint(self, str):
       for c in str + '\n':
         sys.stdout.write(c)
         sys.stdout.flush()
         time.sleep(6./90)

    def print_ui(self, board):
        board = self.get_board(board)
        self.clear_terminal()     
        sys.stdout.write(board)
        sys.stdout.flush()
        time.sleep(.5)
    
    def get_board(self, board):
        p_table = ""
        for row in board:
            p_row = ""
            for cell in row:
                p_cell = None
                
                if cell == 0:
                    p_cell = self.emtpy_cell
                else:
                    p_cell = self.filled_cell
                    
                p_row = p_cell + " " + p_row

            p_table = p_table + "\n" + p_row
            
        return p_table
    
    def clear_terminal(self):
        os.system("cls")
    
    def quit_game(self, sig, frame):
        self.clear_terminal()
        self.sprint('GAME OVER')
        sys.exit(0)
        