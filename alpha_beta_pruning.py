# Libraries
from math import inf, ldexp, sqrt

max_depth=3

def result(state,action): #TRansiction function
    player = 'O' if state.count(' ')%2==0 else 'X'
    if state[action]!=' ':
        return None
    state[action]=player
    return state

def cut_off(state,depth):
    return depth==max_depth
 


def eval(state,actions):  #Funcion heurisitca

    print("Eval")

def Min_Max_Cut_Off(state,actions):
    v=-inf 
    s_act=None
    for action in range(actions):
        val=min_value(result(state,action),-inf,inf,0,actions)
        if val > v :
            v=val
            s_act=action
    return s_act,v
    
def Max_Min_Cut_Off(state,actions):
    v=inf 
    s_act=None
    for action in range(actions):
        val=max_value(result(state,action),-inf,inf,0,actions)
        if val < v :
            v=val
            s_act=action
    return s_act,v

def min_value(state,alfa,betha,depth, actions):
    if cut_off(state,depth):
        return eval(state,actions)
    v=inf
    for action in range(actions):
        v=min(v,max_value(result(state,action)),alfa,betha,depth+1,actions)
        if (v<=alfa):
            return v
        betha=min(betha,v)
    return v


def max_value(state,alfa,betha,depth, actions):
    if cut_off(state,depth):
        return eval(state,actions)
    v=-inf
    for action in range(actions):
        v=max(v,min_value(result(state,action)),alfa,betha,depth+1,actions)
        if (v>=betha):
            return v
        alfa=max(alfa,v)
    return v

def show_board(state):
    print(state)

def interpretate(movement,actions):#INTERPRETATE the movemente given by the human player
    size=int(sqrt(actions))
    value=size*(int(movement[1])-1)+(ord(movement[0])-65)
    return value


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
        while winner==None:
            movement=input("Insert your movement coordinates\n")
            state=result(state,interpretate(movement,actions))
            while state!=None:
                print("Invalid Movement, please try again with other movement\n")
                state=result(state,interpretate(movement,actions))
            show_board(state)
            nextMove,v=Min_Max_Cut_Off(state,actions)#Aqui capaz se deberia hacer un depcopy del estado
            print("The machine did the next movement :", nextMove)
            state=result(state,nextMove)
            show_board(state)
            winner=is_a_winner(state,actions)
    else:
         while winner==None:
            nextMove,v=Max_Min_Cut_Off(state,actions)#Aqui capaz se deberia hacer un depcopy del estado
            print("The machine did the next movement :", nextMove)
            state=result(state,nextMove)
            show_board(state)
            movement=input("Insert your movement coordinates\n")
            state=result(state,interpretate(movement))
            while state!=None:
                print("Invalid Movement, please try again with other movement\n")
                state=result(state,interpretate(movement,actions))
            show_board(state)
            winner=is_a_winner(state,actions)
    return interpretate(nextMove)
    


def tests():
    state=[' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']
    actions=9
    while winner==None:
        nextMove,v=Max_Min_Cut_Off(state,actions)#Aqui capaz se deberia hacer un depcopy del estado
        print("The machine did the next movement :", nextMove)
        state=result(state,nextMove)
        show_board(state)
        nextMove,v=Min_Max_Cut_Off(state,actions)#Aqui capaz se deberia hacer un depcopy del estado
        print("The machine did the next movement :", nextMove)
        state=result(state,nextMove)
        show_board(state)
        winner=is_a_winner(state,actions)

# Main Function
def main():
    
    play=input("Welcome to Tic Tac Toe game made by DaniCam, please pick the type of your chip:\n1.-X\n2.-O")
    diff=input("Nice job now lets choose the difficuly of the game:\nPlease choose the difficulty\n1.-Easy(3x3)\n2.-InterMediate(4x4)\n3.-Hard(5x5)")
    if diff==1:
        initial_State=[' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']
        actions=9
    elif diff==2:
        initial_State=[' ', ' ', ' ',' ', ' ', ' ', ' ',' ', ' ', ' ', ' ',' ', ' ', ' ', ' ',' ']
        actions=16
    elif diff==3:
        initial_State=[' ',' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ', ' ', ' ', ' ',' ',' ']
        actions=25        
    play_game(initial_State,actions,play)

if __name__ == '__main__':
    main()