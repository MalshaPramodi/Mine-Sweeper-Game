##Mine Sweeper Game

import random

class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.neighbor_mines = 0

class Board:
    def __init__(self, size, num_mines):
        self.size = size
        self.num_mines = num_mines
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]
        self.flags = num_mines

    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.num_mines:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if not self.grid[row][col].is_mine:
                self.grid[row][col].is_mine = True
                mines_placed += 1

    def calculate_neighbor_mines(self):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for i in range(self.size):
            for j in range(self.size):
                if not self.grid[i][j].is_mine:
                    for dx, dy in directions:
                        new_x, new_y = i + dx, j + dy
                        if 0 <= new_x < self.size and 0 <= new_y < self.size and self.grid[new_x][new_y].is_mine:
                            self.grid[i][j].neighbor_mines += 1

    def reveal(self, row, col):
        cell = self.grid[row][col]
        if cell.is_flagged:
            return
        if cell.is_mine:
            self.show_board()
            print("Game Over! You hit a mine.")
            return
        if not cell.is_revealed:
            cell.is_revealed = True
            if cell.neighbor_mines == 0:
                self.reveal_neighbors(row, col)

    def reveal_neighbors(self, row, col):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dx, dy in directions:
            new_x, new_y = row + dx, col + dy
            if 0 <= new_x < self.size and 0 <= new_y < self.size:
                self.reveal(new_x, new_y)

    def flag(self, row, col):
        cell = self.grid[row][col]
        if not cell.is_revealed:
            if not cell.is_flagged and self.flags > 0:
                cell.is_flagged = True
                self.flags -= 1
            elif cell.is_flagged:
                cell.is_flagged = False
                self.flags += 1

    def show_board(self):
        for i in range(self.size):
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

class Game:
    def start(self):
        print("Field Options:")
        print("1 - 10x10 with 12 mines")
        print("2 - 15x15 with 18 mines")
        print("3 - 20x20 with 24 mines")
        
        field_option = input("Enter the field option (1/2/3): ")
        
        if field_option == '1':
            size = 10
            num_mines = 12
        elif field_option == '2':
            size = 15
            num_mines = 18
        elif field_option == '3':
            size = 20
            num_mines = 24
        else:
            print("Invalid option. Exiting the game.")
            return
        
        board = Board(size, num_mines)
        board.place_mines()
        board.calculate_neighbor_mines()
        
        while True:
            board.show_board()
            user_input = input("Enter three letters <row letter><column letter><command>: ").upper()
            
            if len(user_input) != 3:
                print("Invalid input format. Try again.")
                continue
            
            row = ord(user_input[0]) - ord('A')
            col = ord(user_input[1]) - ord('A')
            command = user_input[2]
            
            if not ('A' <= user_input[0] <= chr(ord('A') + size - 1)) or not ('A' <= user_input[1] <= chr(ord('A') + size - 1)):
                print("Invalid row or column letter. Try again.")
                continue
            
            if command == 'R':
                board.reveal(row, col)
            elif command == 'F':
                board.flag(row, col)
            else:
                print("Invalid command. Try again.")

if __name__ == "__main__":
    game = Game()
    game.start()
