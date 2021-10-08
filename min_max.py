# Libraries
from math import inf, sqrt
from tabulate import tabulate
import copy
from time import time

# Vars
# max_depth=3
space = 0

# Play_Move: Transiction function
def play_move(state,action):
    player = 'O' if state.count(' ')%2==0 else 'X'
    if state[action]!=' ':
        return None
    state[action]=player
    return state

# Terminal_State: Player Won?
def terminal_state(state,actions):
    return is_a_winner(state,actions)
 
# min_max: 
def min_max(state,actions, space_counter):
    global space
    space = 0
    v=-inf 
    s_act=None
    for action in range(actions):
        nextAction=play_move(copy.deepcopy(state),action)
        if nextAction!=None:            
            val=min_value(nextAction,actions)            
            if val >= v :
                v=val
                s_act=action
    space_counter.append(space)
    print('Spaces to do this movement: ',space)
    return s_act,v

# max_min: 
def max_min(state,actions, space_counter):
    global space
    space = 0
    v=inf 
    s_act=None
    for action in range(actions):
        nextAction=play_move(copy.deepcopy(state),action)
        if nextAction!=None:
            val=max_value(nextAction,actions)
            if val <= v :
                v=val
                s_act=action
    space_counter.append(space)
    print('Spaces to do this movement: ',space)
    return s_act,v

# Min_Value: 
def min_value(state, actions):
    global space
    evalRes=terminal_state(state,actions)
    if evalRes!=None:
        return evalRes
    v=inf
    for action in range(actions):
        nextAction=play_move(copy.deepcopy(state),action)
        if nextAction!=None:
            space += 1
            v=min(v,max_value(nextAction,actions))
    return v

# Max_Value: 
def max_value(state, actions):
    global space
    evalRes=terminal_state(state,actions)
    if evalRes!=None:
        return evalRes
    v=-inf
    for action in range(actions):
        nextAction=play_move(copy.deepcopy(state),action)
        if nextAction!=None:
            space += 1
            v=max(v,min_value(nextAction,actions))
    return v

# Split_List: 
def split_list(my_list, wanted_parts):
    length = len(my_list)
    return [ my_list[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

# Display Array in Grid
def show_board(my_list, size):
    n_parts = int(sqrt(size))
    item = split_list(my_list, n_parts)
    table = tabulate(item, tablefmt="fancy_grid")
    print(table)
    print('\n:------------------:\n')

# Interpretate: Movement A1 -> 1
def interpretate(movement,actions):
    size=int(sqrt(actions))
    value=size*(int(movement[1])-1)+(ord(movement[0])-65)
    return value

# Interpretate_Computer: Movement 1 -> A1
def interpretate_Computer(movement,actions):
    size=int(sqrt(actions))
    mod = movement % size
    letter=chr(65+mod)
    num=str(int(movement/size)+1)
    return letter+num

# Verify_Rows: Verify the jump of row
def veriy_rows(state,actions,size):
    x_counter=0
    o_counter=0
    for i in range(actions):
        if i % size ==0:
            x_counter=0
            o_counter=0
        if state[i]=='X':
            x_counter+=1
        elif state[i]=='O':
            o_counter+=1
        if x_counter==size:
            return 1
        if o_counter==size:
            return -1
    return None

# Verify_Columns: 
def veriy_columns(state,actions,size):
    for i in range(size):
        x_counter=0
        o_counter=0
        for j in range(size):                        
            if state[i+j*size]=='X':
                x_counter+=1
            elif state[i+j*size]=='O':
                o_counter+=1
        if x_counter==size:
            return 1
        if o_counter==size:
            return -1
    return None

# Verify_Diagonals: 
def verify_diagonals(state,actions,size):
    x_counter=0
    o_counter=0
    for i in range(size):
        if state[(size+1)*i]=='X':
            x_counter+=1
        elif state[(size+1)*i]=='O':
            o_counter+=1
    if x_counter==size:
        return 1
    if o_counter==size:
        return -1
    x_counter=0
    o_counter=0
    for i in range(size):
        if state[(size-1)*(i+1)]=='X':
            x_counter+=1
        elif state[(size-1)*(i+1)]=='O':
            o_counter+=1
    if x_counter==size:
        return 1
    if o_counter==size:
        return -1
    return None

# Is_A_Winner: Verify if it is a winner(X - 1  O - -1), draw ( 0 ) or none
def is_a_winner(state,actions):
    size=int(sqrt(actions))
    winner=veriy_rows(state,actions,size)
    if winner!=None:
        return winner
    winner=veriy_columns(state,actions,size)
    if winner!=None:
        return winner
    winner=verify_diagonals(state,actions,size)
    if winner!=None:
        return winner
    if state.count(' ')==0:
        return 0
    return None

# Interpretate_Computer: Movement 1 -> A1
def interpretate_computer(movement,actions):
    size=int(sqrt(actions))
    mod = movement % size
    letter=chr(65+mod)
    num=str(int(movement/size)+1)
    return letter+num

# Play_Game:  
def play_game(state,actions,type_player):
    actions_time = []
    space_counter = []
    winner=None

    if type_player=='X':
        while winner==None:
            movement=input('Choose where to place (coordinates): ')
            new_state=play_move(state,interpretate(movement,actions))

            while new_state==None:
                print('Invalid Movement! Choose again.')
                movement = input('Choose where to place (coordinates): ')
                new_state=play_move(state,interpretate(movement,actions))

            state = new_state
            show_board(state,actions)
            winner=is_a_winner(state,actions)

            if winner==None:
                start_time = time()                                 # Start Timer
                nextMove,v=max_min(copy.deepcopy(state),actions,space_counter)
                print("The Machine did the Movement: ", interpretate_computer(nextMove,actions))
                state=play_move(state,nextMove)
                show_board(state,actions)
                winner=is_a_winner(state,actions)
                end_time = time() - start_time                      # End Timer                
                actions_time.append(end_time)
    else:
         while winner==None:
            start_time = time()                                     # Start Timer
            nextMove,v=min_max(copy.deepcopy(state),actions,space_counter)           
            print("The Machine did the Movement: ", interpretate_computer(nextMove,actions))
            state=play_move(state,nextMove)
            show_board(state,actions)
            winner=is_a_winner(state,actions)
            end_time = time() - start_time                          # End Timer                     
            actions_time.append(end_time)
            
            if winner==None:
                movement=input('Choose where to place (coordinates): ')
                new_state=play_move(state,interpretate(movement,actions))
               
                while new_state==None:
                    print('Invalid Movement! Choose again.')
                    movement = input('Choose where to place (coordinates): ')
                    new_state=play_move(state,interpretate(movement,actions))

                state = new_state
                show_board(state,actions)
                winner=is_a_winner(state,actions)

    avg_time = sum(actions_time) / len(actions_time)
    print('Time Avarage: ', avg_time)
    print(actions_time)

    print('Space Counter: ', end='')
    print(space_counter)
    # print('---- ',sum(space_counter))
    return winner

# Setup_Controls: Select Player X or Player O 
def setup_controls():
    # print('*** Game Made By: Adrian Mendoza - Daniel Camacho - Jhuslan Vargas ***\n')
    print('\n*** Welcome Pretty Human to Tic Tac Toe Game ***')
    player_choice = input("Pick the type of your chip (X - O): ")
    player = ""
    if player_choice == 'x' or player_choice == 'X' :
        player = "X"
    else:
        if player_choice == 'o' or player_choice == 'O':
            player = "O"
        else:
            print('--- Try Again ---')
            player = setup_controls()
    print('You are the player: ' + player)
    return player

# Setup_Difficult: Easy, Medium or Hard
def setup_difficult():
    print('\nChoose the difficuly')
    print('1 - Easy (3x3)')
    print('2 - Medium (4x4)')
    print('3 - Hard (5x5)')
    difficult = input("Please choose the difficult: ")
    initial_state = []
    if difficult=='1':
        initial_state=[' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']
        actions=9
    elif difficult=='2':
        initial_state=[' ', ' ', ' ',' ', ' ', ' ', ' ',' ', ' ', ' ', ' ',' ', ' ', ' ', ' ',' ']
        # initial_state=[' ', ' ', ' ',' ', ' ', ' ', ' ',' ', 'X', 'O', ' ',' ', 'O', 'X', 'O','X']
        actions=16
    elif difficult=='3':
        initial_state=[' ',' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ']
        # initial_state=[' ',' ', ' ',' ',' ', ' ', ' ', 'X',' ',' ', 'O', 'X', 'X','O','X', 'O', 'X', 'O','O','X', 'O', 'X', 'O','X','X']
        actions=25   
    # show_board(initial_state,actions)
    print('\n:------------------:\n')
    return initial_state, actions

# Display_Winner: Player X, Player O or Tie
def display_winner(winner):
    print('\n:--------  ', end='')
    if winner==1:
        print("xxx PLAYER X WON xxx", end='')
    elif winner==-1:
        print("ooo PLAYER O WON ooo", end='')
    else:
        print("xox TIE xox", end='')
    print('  --------:\n')

# Main Function
def main():
    player_choice = setup_controls()
    initial_state, actions = setup_difficult()
    winner=play_game(initial_state, actions, player_choice)
    display_winner(winner)
    print('*** Game Made By: Adrian Mendoza - Daniel Camacho - Jhuslan Vargas ***\n')

if __name__ == '__main__':
    main()