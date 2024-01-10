import random

class Cell:
    def __init__(self) :
        #initialize cell properties
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.neighbor_mines = 0


class Board:
    def __init__(self, size ,num_mines):
        #initialize the board with given size and number of mines
        self.size=size
        self.num_mines = num_mines
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]   
        self.flags = num_mines

    def place_mines(self):
        #randomly place mines on the board
        mines_placed=0
        while mines_placed <self.num_mines:
            row = random.randint(0, self.size -1)
            col = random.randint(0, self.size-1)
            if not self.grid[row][col].is_mine :
                self.grid[row][col].is_mine = True
                mines_placed +=1


    def calculate_neighbor_mines(self):
        #calculate the number of neighboring mines for each cell
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]    
        for i in range(self.size):
            for j in range(self.size):
                if not self.grid[i][j].is_mine:
                    for dx,dy in directions:
                        new_x, new_y = i+dx, j+dy
                        if 0<=new_x<self.size and  0<= new_y <self.size and self.grid[new_x][new_y].is_mine:
                            self.grid[i][j].neighbor_mines +=1


    def reveal(self,row,col):
        #reveal a cell and its neighbors
        cell = self.grid[row][col]
        if cell.is_flagged:
            return
        if cell.is_mine:
            self.show_board()
            print("Game Over!!! You hit a mine.")
            return
        if not cell.is_revealed:
            cell.is_revealed = True
            if cell.neighbor_mines == 0:
                self.reveal_neighbors(row,col)


    def revel_neighbors(self,row,col):
        #reveal neighboring cells recursively
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dx,dy in directions:
            new_x, new_y =row+dx ,col+dy
            if 0 <= new_x < self.size and 0 <= new_y < self.size:
                self.reveal(new_x,new_y)


    def flag(self,row,col):
        #Flag or unflag a cell
        cell = self.grid[row][col]
        if not cell.is_revealed:
            if not cell.is_flagged and self.flags >0:
                cell.is_flagged = True
                self.flags -=1
            elif cell.is_flagged:
                cell.is_flagged = False
                self.flags +=1
                 

    def show_board(self):
        #Print rows with row letters and cell content
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
    
      


           