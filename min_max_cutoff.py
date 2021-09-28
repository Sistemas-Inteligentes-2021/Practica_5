# Libraries
from math import inf

max_depth=3
initial_State=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def count_rows(player,state):
    #for i in range(3):
    print("d")

def cut_off(state,depth):
    return depth==max_depth
 
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


# Main Function
def main():
    print("hola mundo")


if __name__ == '__main__':
    main()