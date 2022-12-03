import class_x0
if '__name__' = '__main__'
game = class_x0.Board(3)

# display.grid
game.greeting()
while True:

    game.display1()
    game.next_move()
    game.changeplayer()
    result = game.victory()
    print(result)
    if result[0] != 'None':
        break
print(f" the winner is {game.name(result[1])}: {result[0]} on {result[2]+1}")
result = game.victory()