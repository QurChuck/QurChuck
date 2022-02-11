def visu(matrix):
    print(matrix[2])
    print(matrix[1])
    print(matrix[0])
def user_choice():
    
    choice = 'Error'
    acceptable_values = range(1,10)
    confirm = False
    
    while not confirm:
        choice = input('Enter a number of field (1-9): ')
        
        if choice.isdigit():
            choice = int(choice)
            
            if choice in acceptable_values:
                confirm = True
            else:
                print('Value out of range')
        else:
            print('Wrong input')
            
    return choice
def find_place(index):
    column = (index-1)%3
    row = 3
    
    if index in range(1,4):
        row = 0
    elif index in range(4,7):
        row = 1
    elif index in range(7,10):
        row = 2
    else:
        print(f'Error debug: Row={row}, Column={column}')
        
    mapa = [row, column]
        
    return mapa
def check_place(mapa, matrix):
    #column = mapa[1]
    #row = mapa[0]
        
    return matrix[mapa[0]][mapa[1]] == ' '
def replace(mapa, matrix, value):
    
    matrix[mapa[0]][mapa[1]] = value
    
    return None   
def swap_value(value):
    if value == 'X':
        value = 'O'
    else:
        value = 'X'
        
    return value
def complete(matrix):
    full = True
    end = False
    lenght = len(matrix)
    i = 0
    
    row1 = matrix[0]
    row2 = matrix[1]
    row3 = matrix[2]
    column1 = []
    column2 = []
    column3 = []
    
    #check if there is an empty spot on board
    while i < lenght:
        if ' ' in matrix[i]:
            full = False
        else:
            #print(f'{i}')
            pass
        i += 1
    
    #check Row for winner
    if set(row1) == {'X'} or set(row1) == {'O'}:
        end = True
        print(f'{set(row1)} won the game!')
    elif set(row2) == {'X'} or set(row2) == {'O'}:
        end = True
        print(f'{set(row2)} won the game!')
    elif set(row3) == {'X'} or set(row3) == {'O'}:
        end = True
        print(f'{set(row3)} won the game!')
    else:
        pass
        
    #check Columns for winner
    for x,y,z in matrix:
        column1.append(x)
        column2.append(y)
        column3.append(z)
        
    if set(column1) == {'X'} or set(column1) == {'O'}:
        end = True
        print(f'{set(column1)} won the game!')
    elif set(column2) == {'X'} or set(column2) == {'O'}:
        end = True
        print(f'{set(column2)} won the game!')
    elif set(column3) == {'X'} or set(column3) == {'O'}:
        end = True
        print(f'{set(column3)} won the game!')
    else:
        pass
    
    #Check diagonal
    if set([matrix[0][0],matrix[1][1],matrix[2][2]]) == {'X'} or set([matrix[0][0],matrix[1][1],matrix[2][2]]) == {'O'}:
        end = True
        print(f'{set([matrix[0][0],matrix[1][1],matrix[2][2]])} won the game!')
    elif set([matrix[0][2],matrix[1][1],matrix[2][0]]) == {'X'} or set([matrix[0][2],matrix[1][1],matrix[2][0]]) == {'O'}:
        end = True
        print(f'{set([matrix[0][2],matrix[1][1],matrix[2][0]])} won the game!')
    

    return full or end
def replay():
    exit = input('Replay a game? (Y or N): ')
    return not exit.lower() == 'y'
def game():
    #init
    matrix = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
    value = 'X'
    compl = False
    
    visu(matrix)
    while not compl:        
        empty = False        
        while not empty and not compl:        
            index = user_choice()
            mapa = find_place(index)
            empty = check_place(mapa, matrix)
            if empty:
                replace(mapa, matrix, value)
                value = swap_value(value)
                visu(matrix)
                compl = complete(matrix)
            else:
                print('You must choose an empty place')
            
            if compl:
                compl = replay()
                matrix = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
                value = 'X'
                if not compl:
                    visu(matrix)
            else:
                pass

game()