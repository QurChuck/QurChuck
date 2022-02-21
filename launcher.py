#init
pick = False
choice = 0
c1 = 0
c2 = 0
c3 = 0

def choose_another():
    another = False
    pick = input('Do You want pick another game? (Y/N): ')

    while not another:
        if pick.lower() == 'y':
            another = True
        elif pick.lower() == 'n':
            break
        else:
            print("Wrong Input! Try again!")
    
    return another


while not pick:
    choice = input('Pick an Application: \n1 - TicTacToe\n2 - War\n3 - BlackJack\n')

    match choice:
        case "1":
            from games.tictactoe import game as tictactoe
            pick = True

            if c1 == 0:
                c1 +=1
            else:
                tictactoe()

        case "2":
            from games.war import game as war
            pick = True

            if c2 == 0:
                c2 +=1
            else:
                war()

        case "3":
            from games.blackjack import game as blackjack
            pick = True

            if c3 == 0:
                c3 +=1
            else:
                blackjack()

        case _:
            exit = input("Wrong input, do You want to exit? (Y/N): ")
            if exit.lower() == 'y':
                break
            else:
                pass

    pick = not choose_another()
