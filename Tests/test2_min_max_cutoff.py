# Libraries
from math import inf, ldexp, sqrt
from tabulate import tabulate

max_depth=3

def play_move(state, movement, actions): #TRansiction function
    player = 'O' if state.count(' ') % 2 == 0 else 'X'
    if state[movement]!=' ':
        return invalid_movement(state,movement,actions)
    state[movement-1]=player
    return state

def invalid_movement(state, action, actions):
    print('Invalid Movement ' + str(action) +'! Choose again.')
    movement = int(input('Choose where to place (1 to ' + str(actions) +'): '))
    state = play_move(state, movement, actions)
    return state

def cut_off(state,depth):
    return depth==max_depth
 
def eval(state,actions):  #Funcion heurisitca
    
    print("Eval")

def Min_Max_Cut_Off(state,actions):
    v=-inf 
    s_act=None
    for action in range(actions):
        val=min_value(play_move(state,action, actions),-inf,inf,0,actions)
        if val > v :
            v=val
            s_act=action
    return s_act,v
    
def Max_Min_Cut_Off(state,actions):
    v=inf 
    s_act=None
    for action in range(actions):
        val=max_value(play_move(state,action, actions),-inf,inf,0,actions)
        if val < v :
            v=val
            s_act=action
    return s_act,v

def min_value(state,alfa,betha,depth, actions):
    if cut_off(state,depth):
        return eval(state,actions)
    v=inf
    for action in range(actions):
        v=min(v,max_value(play_move(state,action, actions)),alfa,betha,depth+1,actions)
        if (v<=alfa):
            return v
        betha=min(betha,v)
    return v


def max_value(state,alfa,betha,depth, actions):
    if cut_off(state,depth):
        return eval(state,actions)
    v=-inf
    for action in range(actions):
        v=max(v,min_value(play_move(state,action, actions)),alfa,betha,depth+1,actions)
        if (v>=betha):
            return v
        alfa=max(alfa,v)
    return v

# def show_board(state):
#     print(state)

# Split list to display
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
    #print('\n')

# def interpretate(movement,actions):#INTERPRETATE the movemente given by the human player
#     size=int(sqrt(actions))
#     value=size*(int(movement[1])-1)+(ord(movement[0])-65)
#     return value


def is_a_winner(state,actions): #Verify if it is a winner(X - 1  O - -1), draw ( 0 ) or none
    size=int(sqrt(actions))
    #rows
    x_counter=0
    o_counter=0
    for i in range(actions):
        #verify the jump of row
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
    #columns
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

    #diagonals
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
    #draw
    if state.count(' ')==0:
        return 0
    return None


def play_game(state,actions,type_player):
    winner=None
    if type_player=='X':
        print('AAAAAAAAAA')
        while winner==None:
            movement=int(input('Choose where to place (1 to ' + str(actions) +'): '))
            print(movement)
            print(type(movement))
            state=play_move(state, movement, actions)
            show_board(state, actions)

            
            nextMove,v=Min_Max_Cut_Off(state,actions)#Aqui capaz se deberia hacer un depcopy del estado
            print("The machine did the next movement :", nextMove)
            state=play_move(state,nextMove, actions)
            show_board(state)
            winner=is_a_winner(state,actions)
    else:
         while winner==None:
            nextMove,v=Max_Min_Cut_Off(state,actions)#Aqui capaz se deberia hacer un depcopy del estado
            print("The machine did the next movement :", nextMove)
            state=play_move(state,nextMove, actions)
            
            show_board(state)

            movement=input("Insert your movement coordinates\n")
            state=play_move(state,movement, actions)
           
            show_board(state)
            winner=is_a_winner(state,actions)
    return nextMove
    


def tests():
    state=[' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']
    actions=9
    while winner==None:
        nextMove,v=Max_Min_Cut_Off(state,actions)#Aqui capaz se deberia hacer un depcopy del estado
        print("The machine did the next movement :", nextMove)
        state=play_move(state,nextMove, actions)
        show_board(state)
        nextMove,v=Min_Max_Cut_Off(state,actions)#Aqui capaz se deberia hacer un depcopy del estado
        print("The machine did the next movement :", nextMove)
        state=play_move(state,nextMove, actions)
        show_board(state)
        winner=is_a_winner(state,actions)

def setup_controls():
    print('*** Welcome Pretty Human to Tic Tac Toe Game ***')
    player_choice = input("Pick the type of your chip (X - O): ")
    if player_choice == 'x':
        player_choice = 'X'
    else:
        if player_choice == 'o':
            player_choice = 'O'
        else:
            print('--- Try Again ---')
            player_choice = setup_controls()
    print('You are the player: ' + player_choice)
    return player_choice

def setup_difficult():
    print('\nChoose the difficuly')
    print('1 - Easy (3x3)')
    print('2 - InterMediate (4x4)')
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
    return initial_state, actions

# Main Function
def main():
    player_choice = setup_controls()
    # print(player_choice)
    initial_state, actions = setup_difficult()
    # print(initial_state)
    # print(actions)
    play_game(initial_state, actions, player_choice)

if __name__ == '__main__':
    main()