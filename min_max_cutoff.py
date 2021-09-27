# Libraries
from math import inf

def cut_off(state,depth):
    print ('Cutoff')
 
def eval(state):
    print("Eval")

def Min_Max_Cut_Off(state,actions):
    v=-inf 
    s_act=None
    for action in actions:
        val=min_value(result(state,action),-inf,inf)
        if val > v :
            v=val
            s_act=action

    return s_act,v

def min_value(state,alfa,betha,depth):
    print('Min Value')


# Main Function
def main():
    print("hola mundo")


if __name__ == '__main__':
    main()