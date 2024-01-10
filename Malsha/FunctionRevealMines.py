import random

class Board:
    def __init__(self, size, num_mines):
        self.size = size
        self.num_mines = num_mines
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]
        self.flags = num_mines

# Code to reveal the mine locations
    def reveal(self, row, col):
        cell = self.grid[row][col]
        if cell.is_flagged:
            return
        if cell.is_mine:
            self.show_board(reveal_all = True)
            print("Game Over! You hit a mine.")
            self.reveal_all_mines()
            return
        if not cell.is_revealed:
            cell.is_revealed = True
            if cell.neighbor_mines == 0:
                self.reveal_neighbors(row, col)
     
    #Function to reveal all mine locations when the user hit a mine           
    def reveal_all_mines(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j].is_mine:
                    self.grid[i][j].is_revealed = True

    def reveal_neighbors(self, row, col):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dx, dy in directions:
            new_x, new_y = row + dx, col + dy
            if 0 <= new_x < self.size and 0 <= new_y < self.size:
                if not self.grid[new_x][new_y].is_revealed:
                    if self.grid[new_x][new_y].neighbor_mines == 0:
                        self.reveal(new_x, new_y)
                    else:
                        self.grid[new_x][new_y].is_revealed = True



    def show_board(self, reveal_all = False):
        # Print rows with row letters and cell content
        for i in range(self.size):
            print(chr(ord('A') + i), end=" |")
            for j in range(self.size):
                cell = self.grid[i][j]
                if cell.is_flagged:
                    print('F', end=' ')
                elif not cell.is_revealed:
                    print('c', end=' ')
                elif cell.is_mine:
                    print('*', end=' ')
                else:
                    print(cell.neighbor_mines, end=' ')
            print()
        
        # Print column letters at the bottom
        print("   ", end="")
        for i in range(self.size):
            print(chr(ord('A') + i), end=" ")
        print()

