# Libraries
from math import inf

max_depth=3


def miss_places(state):
    quantity=0
    for i in state:
        for j in i:
            quantity+= 1 if j==' ' else 0
    return quantity

def result(state,action): #TRansiction function
    player = 'O' if miss_places(state)%2==0 else 'X'

    return state


def cut_off(state,depth):
    return depth==max_depth
 

def count_rows(player,state):
    #for i in range(3):
    print("d")


def eval(state):  #Funcion heurisitca
    print("Eval")

def Min_Max_Cut_Off(state,actions):
    v=-inf 
    s_act=None
    for action in actions:
        val=min_value(result(state,action),-inf,inf,0,actions)
        if val > v :
            v=val
            s_act=action
    return s_act,v
    
def Max_Min_Cut_Off(state,actions):
    v=inf 
    s_act=None
    for action in actions:
        val=max_value(result(state,action),-inf,inf,0,actions)
        if val < v :
            v=val
            s_act=action
    return s_act,v

def min_value(state,alfa,betha,depth, actions):
    if cut_off(state,depth):
        return eval(state)
    v=inf
    for action in actions:
        v=min(v,max_value(result(state,action)),alfa,betha,depth+1,actions)
        if (v<=alfa):
            return v
        betha=min(betha,v)
    return v


def max_value(state,alfa,betha,depth, actions):
    if cut_off(state,depth):
        return eval(state)
    v=-inf
    for action in actions:
        v=max(v,min_value(result(state,action)),alfa,betha,depth+1,actions)
        if (v>=betha):
            return v
        alfa=max(alfa,v)
    return v

def show_board(state):
    print("Showing board")

def interpretate(movement):
    #INTERPRETAR EL movimiento
    return movement


def is_a_winner(state):
    return state


def play_game(state,actions,type_player):

    if type_player=='X':
        while is_a_winner(state)==0:
            movement=input("Ingrese Las coordenadas de su movimiento\n")
            state=result(state,interpretate(movement))
            show_board(state)
            nextMove,v=Min_Max_Cut_Off(state,actions)#Aqui capaz se deberia hacer un depcopy del estado
            print("The machine ")
            state=result(state,nextMove)
            show_board(state)
    
    return interpretate(nextMove)
    



# Main Function
def main():
    
    play=input("Welcome to Tic Tac Toe game made by DaniCam, please pick the type of your chip:\n1.-X\n2.-O")
    diff=input("Nice job now lets choose the difficuly of the game:\nPlease choose the difficulty\n1.-Easy(3x3)\n2.-InterMediate(4x4)\n3.-Hard(5x5)")
    if diff==1:
        initial_State=[[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        actions=9
    elif diff==2:
        initial_State=[[' ', ' ', ' ',' '], [' ', ' ', ' ',' '], [' ', ' ', ' ',' '], [' ', ' ', ' ',' ']]
        actions=16
    elif diff==3:
        initial_State=[[' ',' ', ' ',' ',' '], [' ', ' ', ' ',' ',' '], [' ', ' ', ' ',' ',' '], [' ', ' ', ' ',' ',' '], [' ', ' ', ' ',' ',' ']]
        actions=25
        
    play_game(initial_State,actions,play)

if __name__ == '__main__':
    main()







    '''
    
    if action == 1:
        if state[0][0]!=' ':
            return None
        state[0][0]=player
    elif action == 2:
        if state[0][1]!=' ':
            return None
        state[0][1]=player
    elif action == 3:
        if state[0][2]!=' ':
            return None
        state[0][2]=player
    elif action == 4:
        if state[1][0]!=' ':
            return None
        state[1][0]=player
    elif action == 5:
        if state[1][1]!=' ':
            return None
        state[1][1]=player
    elif action == 6:
        if state[1][2]!=' ':
            return None
        state[1][2]=player
    elif action == 7:
        if state[2][0]!=' ':
            return None
        state[2][0]=player
    elif action == 8:
        if state[2][1]!=' ':
            return None
        state[2][1]=player
    elif action == 9:
        if state[2][2]!=' ':
            return None
        state[2][2]=player
    return state
'''