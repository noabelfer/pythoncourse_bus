class Board:
    size: int
    grid = []
    player:int = 1

#builds the table
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for row in range(self.size)] for col in range(self.size)]


    def display(self):
        for i in range(self.size):
            print (self.grid[i])

    def over(self) -> bool:
        pass

#returns a tuple of (player number, 'row', number of row of the victory)
    def victory(self) -> tuple:
        if self.victory_diagonal_right():
            return (self.player, 'diagonal right', 0)
        if self.victory_diagonal_lft():
            return (self.player, 'diagonal left', 0)
        for row in range(0,self.size):
            if self.victory_row(row):
                return (self.player, 'row', row)
        for col in range(0,self.size):
            if self.victory_col(col):
                return (self.player, 'col', col)
        return ('None', 0, 0)



    def victory_row(self,row) -> bool:
        #if the first item in a row if = 0, yes, no victory in this row.
        x = self.grid[row][0]
        if x == 0:
            return False
        #if the first item is not 0, checking if all the items after are equal to x:
        for i in range(1,self.size):
            if x != self.grid[row][i]:
                return False
        return True

    def victory_col(self, col) -> bool:
        y = self.grid[0][col]
        if y == 0:
            return False
        for i in range (1, self.size):
            if y != self.grid[i][col]:
                return False
        return True

    # victory \
    def victory_diagonal_lft(self):
        d = self.grid[0][0]
        if d == 0:
            return False
        for i in range(1,self.size):
            if d != self.grid[i][i]:
                return False
        return True

    #victory /
    def victory_diagonal_right(self):
        d = self.grid[0][self.size-1]
        if d == 0:
            return False
 #       for i in range(1,self.size-i-1):
        for i in range(1,self.size):
            print(d, i,self.size-i, self.grid[i][self.size-(i+1)])
            if d != self.grid[i][self.size-(i+1)]:
                return False
        return True









    def occupied(self, row:int, col:int) -> bool:
        if self.grid[row][col] == 0:
            return False
        return True

    def next_move(self):
        row = int(input ('row  '))
        col = int(input('col  '))
        while self.occupied(row,col):
            print('place is occupied, choose again:')
            row = int(input('row  '))
            col = int(input('col  '))
        self.grid[row][col] = self.player


    def changeplayer(self):
        self.player = 1 + (2-self.player)


    def showscore(self):
        pass



# game = Board(3)
# end_of_game = False
#
# while not end_of_game:
    # game.display()
    # game.next_move()
    # my_victory = game.victory()
    # print(my_victory)
    # # if my_victory[1] != "None":
    # #     end_of_game = True
    # game.changeplayer()

game = Board(3)

# display.grid
while True:
    game.display()
    game.next_move()
    result = game.victory()
    print(result)
    game.changeplayer()
    if result[2] != 0:
        break
print(f" the winner is player: {result[0]} on row {result[2]}")
#



















