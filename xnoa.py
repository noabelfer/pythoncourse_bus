
class Board:
    size: int
    grid = []
    player:int = 1
    player1 = 'name'
    player2 = 'name2'
    name_dict = {}



#builds the table
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for row in range(self.size)] for col in range(self.size)]
        print(self.name_dict)




    def greeting(self) ->list:
        print("welcome to tic-tac-toe!!!")
        player1:str = input("hello player, please enter your name:  ")
        player2:str = input("hello player, please enter your name:  ")
        self.player1 = player1
        self.player2 = player2
        self.name_dict[1] = self.player1
        self.name_dict[2] = self.player2
        print(self.name_dict)

    def name(self, playernum) -> str:
        return self.name_dict[playernum]


    def display(self):
        dict = {0: ' ', 1: 'X', 2: 'O'}
        for row in range(self.size):
            #goes over all the lines, every line goes over all columns
            newgrid = self.grid[row].copy()
            for col in range(self.size):
                ch = self.grid[row][col]
                newgrid[col] = dict[ch]
            print (newgrid)

    def over(self) -> bool:
        pass

#returns a tuple of (player number, 'row', number of row of the victory)
    def victory(self) -> tuple:
        res =  self.victory_diagonal_right()
        if res[0] == True:
            return ('diagonal right', res[1], 0)
        res =  self.victory_diagonal_lft()
        if res[0] == True:
            return ('diagonal left',res[1], 0)
        for row in range(0,self.size):
            res = self.victory_row(row)
            if res[0] == True:
                return ('row',res[1],row)
        for col in range(0,self.size):
            res = self.victory_col(col)
            if res[0] == True:
                return ('col', res[1], col)
        if self.no_moves():
            return ('teko',0,0)
        return ('None', 0, 0)


    def victory_row(self,row) -> tuple:
        #if the first item in a row if = 0, yes, no victory in this row.
        x = self.grid[row][0]
        if x == 0:
            return (False, x)
        #if the first item is not 0, checking if all the items after are equal to x:
        for i in range(1,self.size):
            if x != self.grid[row][i]:
                return (False, x)
        return (True, x)

    def victory_col(self, col) -> tuple:
        y = self.grid[0][col]
        if y == 0:
            return (False, y)
        for i in range (1, self.size):
            if y != self.grid[i][col]:
                return (False, y)
        return (True, y)

    # victory \
    def victory_diagonal_lft(self):
        d = self.grid[0][0]
        if d == 0:
            return (False, d)
        for i in range(1,self.size):
            if d != self.grid[i][i]:
                return (False, d)
        return (True, d)

    #victory /
    def victory_diagonal_right(self) -> tuple:
        d = self.grid[0][self.size-1]
        if d == 0:
            return (False, d)
        for i in range(1,self.size):
            print(d, i,self.size-i, self.grid[i][self.size-(i+1)])
            if d != self.grid[i][self.size-(i+1)]:
                return (False, d)
        return (True, d)


    def occupied(self, row:int, col:int) -> bool:
        if self.grid[row][col] == 0:
            return False
        return True

    def next_move(self):
        pn = self.name_dict[self.player]
        print(f" {pn} please enter numbers between 1 and {self.size}:")

        while True:
            row_col = input ('row,col  ')
            row_col_spl = row_col.split(',')
            if len(row_col_spl) != 2:
                print('please enter again1: ')
                continue
            if not row_col_spl[0]. isnumeric() or not row_col_spl[1]. isnumeric():
                print('please enter again2: ')
                continue
            row = int(row_col_spl[0])-1
            col = int(row_col_spl[1])-1

            #check if the array is in the range of numbers
            if row < 0 or row >= self.size or col< 0 or col >= self.size:
                print('please enter again: ')
                continue

            if self.occupied(row,col):
                print('place is occupied, choose again:')
                continue
                # row = int(input('row  '))
                # col = int(input('col  '))
            self.grid[row][col] = self.player
            break


    def changeplayer(self):
        self.player = 1 + (2-self.player)


    def no_moves(self) -> bool:
        for row in range(0,self.size):
            for col in range(0, self.size):
                if self.grid[row] [col] == 0:
                    return False
        return True

    # def end_game(self) -> bool:
    #     end = self. victory()
    #     if end[0] != None:
    #         print('the game is over!')
    #         return True
    #     nomove = self.no_moves()
    #     if nomove == True:
    #         print('no more moves!')
    #         return True
    #     return False




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
game.greeting()
while True:

    game.display()
    game.next_move()
    game.changeplayer()
    result = game.victory()
    print(result)
    if result[0] != 'None':
        break
print(f" the winner is {game.name(result[1])}: {result[0]} on {result[2]+1}")
result = game.victory()




















