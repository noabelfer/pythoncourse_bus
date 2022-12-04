import class_x0

if __name__ == '__main__':
    gamesize = 0
    while gamesize < 3 or gamesize >9:
        game_num = input('please enter the size of game (3-9) you would like to play:')
        if not game_num.isnumeric():
            print ('error, not numeric!')
            continue
        gamesize = int(game_num)

    game = class_x0.Board(gamesize)

    # display.grid
    game.greeting()
    while True:

        game.display1()
        game.next_move()
        game.changeplayer()
        result = game.victory()
        print(result)
        if result[0] != 'None':
            game.display1()
            break
    print(f" the winner is {game.name(result[1])}!!!: {result[0]} on {result[2]+1}")
    result = game.victory()




















