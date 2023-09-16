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

    def check_lines(self):
        # rows to delete
        rows_to_delete = []

        # check every row and delete if is complete :)
        for index_row, row in enumerate(self.grid):
            if 0 not in row:
                rows_to_delete.append(index_row)
                self.grid.pop(self.grid.index(row))
                self.grid.insert(0, [0 for _ in range(self.width)])
                continue


        if len(rows_to_delete) > 1:
            self.remove_coordinates_of_shapes(rows_to_delete)
            self.update_tomb_coordinates()

    def remove_coordinates_of_shapes(self, rows):
        for row_index in rows:
            coordinates_to_delete = [(row_index, n) for n in range(self.width)] 
            for coordinate in coordinates_to_delete:
                y, x = coordinate

                result = self.get_index_to_delete((y, x))

                if result is not None:
                    shape_index, row_index = result
                    self.tomb[shape_index].pop(row_index)

    def update_tomb_coordinates(self):
        new_coordinates = []
        for shape in self.tomb:
            new_row = []
            for row in shape:
                y, x = row
                new_row.append((y + 1, x))
            new_coordinates.append(new_row)

        self.tomb = new_coordinates


    def get_index_to_delete(self, index_to_find):
        for shape_index, shape in enumerate(self.tomb):
            for row_index, row in enumerate(shape):
                if row == index_to_find:
                    return (shape_index, row_index)


