# Libraries
from math import inf, sqrt
from tabulate import tabulate
import copy

max_depth=3

def result(state,action): #TRansiction function
    player = 'O' if state.count(' ')%2==0 else 'X'
    if state[action]!=' ':
        return None
    state[action]=player
    return state

def terminal_state(state,actions):
    return is_a_winner(state,actions)
 

def Min_Max(state,actions):
    v=-inf 
    s_act=None
    #print(state)
    for action in range(actions):
        nextAction=result(copy.deepcopy(state),action)
        if nextAction!=None:            
            val=min_value(nextAction,actions)            
            if val >= v :
                v=val
                s_act=action
    return s_act,v
    
def Max_Min(state,actions):
    v=inf 
    s_act=None
    for action in range(actions):
        nextAction=result(copy.deepcopy(state),action)
        if nextAction!=None:
            val=max_value(nextAction,actions)
            if val <= v :
                v=val
                s_act=action
    return s_act,v

def min_value(state, actions):
    evalRes=terminal_state(state,actions)
    if evalRes!=None:
        return evalRes
    v=inf
    for action in range(actions):
        nextAction=result(copy.deepcopy(state),action)
        if nextAction!=None:
            v=min(v,max_value(nextAction,actions))
    return v


def max_value(state, actions):
    evalRes=terminal_state(state,actions)
    if evalRes!=None:
        return evalRes
    v=-inf
    for action in range(actions):
        nextAction=result(copy.deepcopy(state),action)
        if nextAction!=None:
            v=max(v,min_value(nextAction,actions))
    return v
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

def interpretate(movement,actions):#INTERPRETATE the movemente given by the human player
    size=int(sqrt(actions))
    value=size*(int(movement[1])-1)+(ord(movement[0])-65)
    return value


def veriy_rows(state,actions,size):
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
    return None


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

def is_a_winner(state,actions): #Verify if it is a winner(X - 1  O - -1), draw ( 0 ) or none
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
    #draw
    if state.count(' ')==0:
        return 0
    return None


def play_game(state,actions,type_player):
    winner=None
    if type_player=='1':
        while winner==None:
            show_board(state,actions)
            movement=input("Insert your movement coordinates\n")
            state=result(state,interpretate(movement,actions))
            while state==None:
                print("Invalid Movement, please try again with other movement\n")
                movement=input("Insert your movement coordinates\n")
                state=result(state,interpretate(movement,actions))
            show_board(state,actions)
            winner=is_a_winner(state,actions)
            if winner==None:
                nextMove,v=Max_Min(copy.deepcopy(state),actions)#Aqui capaz se deberia hacer un depcopy del estado
                print("The machine did the next movement :", nextMove)
                state=result(state,nextMove)
                show_board(state,actions)
                winner=is_a_winner(state,actions)
    else:
         while winner==None:
            nextMove,v=Min_Max(copy.deepcopy(state),actions)#Aqui capaz se deberia hacer un depcopy del estado            
            print("The machine did the next movement :", nextMove)
            state=result(state,nextMove)
            show_board(state,actions)
            winner=is_a_winner(state,actions)
            if winner==None:
                movement=input("Insert your movement coordinates\n")
                state=result(state,interpretate(movement,actions))
                while state==None:
                    print("Invalid Movement, please try again with other movement\n")
                    movement=input("Insert your movement coordinates\n")
                    state=result(state,interpretate(movement,actions))
                show_board(state,actions)
                winner=is_a_winner(state,actions)
    return winner
    


def tests():
    state=[' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']
    actions=9
    winner=None
    while winner==None:
        nextMove,v=Min_Max(copy.deepcopy(state),actions)#Aqui capaz se deberia hacer un depcopy del estado
        print("The machine did the next movement :", nextMove)
        state=result(state,nextMove)
        show_board(state,actions)
        winner=is_a_winner(state,actions)
        if winner==None:
            nextMove,v=Max_Min(copy.deepcopy(state),actions)#Aqui capaz se deberia hacer un depcopy del estado
            print("The machine did the next movement :", nextMove)
            state=result(state,nextMove)
            show_board(state,actions)
            winner=is_a_winner(state,actions)

# Main Function
def main():
    # initial_State=[]
    # actions=0
    # play=input("Welcome to Tic Tac Toe game made by DaniCam, please pick the type of your chip:\n1.-X\n2.-O\n")
    # diff=input("Nice job now lets choose the difficuly of the game:\nPlease choose the difficulty\n1.-Easy(3x3)\n2.-InterMediate(4x4)\n3.-Hard(5x5)\n")
    # if diff=='1':
    #     initial_State=[' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']
    #     actions=9
    # elif diff=='2':
    #     initial_State=[' ', ' ', ' ',' ', ' ', ' ', ' ',' ', ' ', ' ', ' ',' ', ' ', ' ', ' ',' ']
    #     actions=16
    # elif diff=='3':
    #     initial_State=[' ',' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ']
    #     actions=25        
    # winner=play_game(initial_State,actions,play)
    # if winner==1:
    #     print("Gano las X")
    # elif winner==-1:
    #     print("Gano las O")
    # else:
    #     print("Empate")
    tests()

if __name__ == '__main__':
    main()