# Libraries
from math import inf, sqrt
from tabulate import tabulate
import copy
from time import time

# Vars
max_depth=5             # 3 x 3
# max_depth=3           # 4 x 4
# max_depth=3           # 5 x 5
space = 0

# Play_Move: Transiction function
def play_move(state, action): 
    player = 'O' if state.count(' ')%2==0 else 'X'
    if state[action]!=' ':
        return None
    state[action]=player
    return state

# Terminal_State: Player Won?
def terminal_state(state,actions):
    return is_a_winner(state,actions)

# Cut_Off: Limit MAX DEPTH
def cut_off(depth):
    return depth == max_depth

# Count_Columns: Count Lines
def count_columns(state,sym,num_sym,size):
    lines=0
    for n in range(size):
        sym_state=0
        blank_space=0
        i=0
        while i < size:
            if(state[(i*size)+n]==sym):
                sym_state=sym_state+1
            elif(state[(i*size)+n]==''):
                blank_space=blank_space+1
            if(num_sym==sym_state and blank_space == size-num_sym):
                lines=lines+1
            i=i+1
    return lines

# Count_Rows: Count Lines
def count_rows(state,sym,num_sym,size):
    lines=0
    for n in range(size):
        sym_state=0
        blank_space=0
        i=0
        while i < size:
            if(state[i+(n*size)]==sym):
                sym_state=sym_state+1
            elif(state[i+(n*size)]==''):
                blank_space=blank_space+1
            if(num_sym==sym_state and blank_space == size-num_sym):
                lines=lines+1
            i=i+1
    return lines

# Count_Diagonals: Count Lines
def count_diagonals(state,sym,num_sym,size):
    lines=0
    sym_state=0
    blank_space=0
    for n in range(size):
        if state[(size+1)*n]==sym:
            sym_state=sym_state+1
        elif state[(size+1)*n]=='':
            blank_space=blank_space+1
        if(num_sym==sym_state and blank_space == size-num_sym):
            lines=lines+1
    sym_state=0
    blank_space=0
    for n in range(size):
        if state[(n+1)*(size-1)]==sym:
            sym_state=sym_state+1
        elif state[(n+1)*(size-1)]=='':
            blank_space=blank_space+1
        if(num_sym==sym_state and blank_space == size-num_sym):
            lines=lines+1
    return lines

# Count_Lines: Total Lines
def count_lines(state,size,sym,num_sym):
    lines=count_rows(state,sym,num_sym,size)
    lines=lines+count_columns(state,sym,num_sym,size)
    lines=lines+count_diagonals(state,sym,num_sym,size)
    return lines

# Eval: Heuristic Function
def eval(state,actions):
    size=int(sqrt(actions))
    if size==3:
        return 3*count_lines(state,size,'X',2)+count_lines(state,size,'X',1)-(3*count_lines(state,size,'O',2)+count_lines(state,size,'O',1))
    elif size ==4:
        return 4*count_lines(state,size,'X',3)+count_lines(state,size,'X',2)+count_lines(state,size,'X',1)-(4*count_lines(state,size,'O',3)+count_lines(state,size,'O',2)+count_lines(state,size,'O',1))
    else:
        return 5*count_lines(state,size,'X',4)+count_lines(state,size,'X',3)+count_lines(state,size,'X',2)+count_lines(state,size,'X',1)-(5*count_lines(state,size,'O',4)+count_lines(state,size,'O',3)+count_lines(state,size,'O',2)+count_lines(state,size,'O',1))
    
# Min_Max_Cut_Off: 
def min_max_cut_off(state,actions,space_counter):
    global space
    space = 0
    v=-inf 
    s_act=None
    for action in range(actions):
        nextAction=play_move(copy.deepcopy(state),action)
        if nextAction!=None:            
            val=min_value(nextAction,actions,-inf,inf,0)
            if val >= v :
                v=val
                s_act=action
    space_counter.append(space)
    print('Spaces to do this movement: ',space)
    return s_act,v

# Max_Min_Cut_Off: 
def max_min_cut_off(state,actions,space_counter):
    global space
    space = 0
    v=inf 
    s_act=None
    for action in range(actions):
        nextAction=play_move(copy.deepcopy(state),action)
        if nextAction!=None:
            val=max_value(nextAction,actions,-inf,inf,0)
            if val <= v :
                v=val
                s_act=action
    space_counter.append(space)
    print('Spaces to do this movement: ',space)
    return s_act,v

# Min_Value: 
def min_value(state, actions,alfa,beta,depth):
    global space
    evalRes=terminal_state(state,actions)
    if evalRes!=None or cut_off(depth):
        if evalRes==None:
            return eval(state,actions)
        return evalRes
    v=inf
    for action in range(actions):
        nextAction=play_move(copy.deepcopy(state),action)
        if nextAction!=None:
            space += 1
            v=min(v,max_value(nextAction,actions,alfa,beta,depth+1))
            if v<=alfa:
                return v
            beta=min(beta,v)
    return v

# Max_Value: 
def max_value(state, actions,alfa,beta,depth):
    global space
    evalRes=terminal_state(state,actions)
    if evalRes!=None or cut_off(depth):
        if evalRes==None:
            return eval(state,actions)
        return evalRes
    v=-inf
    for action in range(actions):
        nextAction=play_move(copy.deepcopy(state),action)
        if nextAction!=None:
            space+=1
            v=max(v,min_value(nextAction,actions,alfa,beta,depth+1))
            if v>=beta:
                return v
            alfa=max(alfa,v)
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
def interpretate_computer(movement,actions):
    size=int(sqrt(actions))
    mod = movement % size
    letter=chr(65+mod)
    num=str(int(movement/size)+1)
    return letter+num

# Verify_Rows: Verify the jump of row
def verify_rows(state,actions,size):
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
    winner=verify_rows(state,actions,size)
    if winner!=None:
        return winner
    winner=veriy_columns(state,actions,size)
    if winner!=None:
        return winner
    winner=verify_diagonals(state,actions,size)
    if winner!=None:
        return winner
    if state.count(' ')==0:     # Draw
        return 0
    return None

# Play_Game:  
def play_game(state,actions,type_player):
    space_counter = []
    actions_time = []
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
                nextMove,v=max_min_cut_off(copy.deepcopy(state),actions,space_counter)
                print("The Machine did the Movement: ", interpretate_computer(nextMove,actions))
                state=play_move(state,nextMove)
                show_board(state,actions)
                winner=is_a_winner(state,actions)
                end_time = time() - start_time                      # End Timer                
                actions_time.append(end_time)
    else:
         while winner==None:
            start_time = time()                                     # Start Timer
            nextMove,v=min_max_cut_off(copy.deepcopy(state),actions,space_counter)           
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

    avg_time = sum(actions_time) / len(actions_time)                # Avarage Timer
    print('Time Avarage: ', avg_time)
    print(actions_time)

    print('Space Counter: ', end='')                                # Space Timer
    print(space_counter)
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
        actions=16
    elif difficult=='3':
        initial_state=[' ',' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ']
        actions=25   
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

# :------------:
if __name__ == '__main__':
    main()