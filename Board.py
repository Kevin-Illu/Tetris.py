import os
import sys
import time

class Board:
    def __init__(self, w, h) -> None:
        self.width = w
        self.height = h
        self.grid = [[0 for _ in range(0, self.width)] for _ in range(0, self.height)]
        self.tomb = []

    # UI
    def mark_deaths(self):
        if len(self.tomb) < 1:
            return

        for coordinate in self.tomb:
            for row, col in coordinate:
                self.grid[row][col] = 1

    def print_board(self, shape):
        for row, col in shape.normalized_coordinates:
            self.grid[row][col] = 1

        str_board = ""
        for rows in self.grid:
            for col in rows:
                if (col == 1):
                    str_board += " # "
                else:
                    str_board += " . "
            str_board += "\n"

        os.system("cls")
        sys.stdout.write(str_board)
        sys.stdout.flush()
        time.sleep(.1)
        
        # clean the grid
        for row, col in shape.normalized_coordinates:
            self.grid[row][col] = 0





