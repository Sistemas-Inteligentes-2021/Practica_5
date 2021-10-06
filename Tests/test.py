from math import inf, sqrt
from typing import Counter

test = float("inf")


a=inf
b=-inf

# print(test)

# print(a)
# print(b)

# print('Aqui')

# for i in range(16):
#     print(i)
# initial_State=[' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']

# print(initial_State.count(' '))
# print(int(sqrt(16)))

# def interpretate(movement,actions):
#     #INTERPRETAR EL movimiento
#     size=int(sqrt(actions))
#     value=size*(int(movement[1])-1)+(ord(movement[0])-65)
#     return value

# print(interpretate("D3",25))

def count_columns(state,sym,num_sym,size):
    lines=0
    for n in range(size):
        sym_state=0
        blank_space=0
        i=0
        while i < size:
            if(state[(i*size)+n]==sym):
                sym_state=sym_state+1
            elif(state[(i*size)+n]==' '):
                blank_space=blank_space+1
            if(num_sym==sym_state and blank_space == size-num_sym):
                lines=lines+1
            i=i+1
    return lines
def count_rows(state,sym,num_sym,size):
    lines=0
    for n in range(size):
        sym_state=0
        blank_space=0
        i=0
        while i < size:
            if(state[i+(n*size)]==sym):
                sym_state=sym_state+1
            elif(state[i+(n*size)]==' '):
                blank_space=blank_space+1
            if(num_sym==sym_state and blank_space == size-num_sym):
                lines=lines+1
            i=i+1
    return lines

def count_diagonals(state,sym,num_sym,size):
    lines=0
    sym_state=0
    blank_space=0
    for n in range(size):
        if state[(size+1)*n]==sym:
            sym_state=sym_state+1
        elif state[(size+1)*n]==' ':
            blank_space=blank_space+1
        if(num_sym==sym_state and blank_space == size-num_sym):
            lines=lines+1
    sym_state=0
    blank_space=0
    for n in range(size):
        if state[(n+1)*(size-1)]==sym:
            sym_state=sym_state+1
        elif state[(n+1)*(size-1)]==' ':
            blank_space=blank_space+1
        if(num_sym==sym_state and blank_space == size-num_sym):
            lines=lines+1
    return lines

def count_lines(state,size,sym,num_sym):
    lines=count_rows(state,sym,num_sym,size)
    lines=lines+count_columns(state,sym,num_sym,size)
    lines=lines+count_diagonals(state,sym,num_sym,size)
    return lines

def eval(state,actions):
    size=int(sqrt(actions))
    x2=count_lines(state,size,'X',2)
    x1=count_lines(state,size,'X',1)
    o2=count_lines(state,size,'O',2)
    o1=count_lines(state,size,'O',1)
    return 3 * x2 + x1 - (3 * o2 + o1)

state=['O','X','O',' ','X',' ','X',' ','O']
# print(count_diagonals(state,'X',1,3))
print(eval(state,9))












#define Possible_Wins 8
# const int Three_in_a_Row[Possible_Wins][3] = {
#   { 0, 1, 2 },
#   { 3, 4, 5 },
#   { 6, 7, 8 },
#   { 0, 3, 6 },
#   { 1, 4, 7 },
#   { 2, 5, 8 },
#   { 0, 4, 8 },
#   { 2, 4, 6 }
# };
# const int Heuristic_Array[4][4] = {
#   {     0,   -10,  -100, -1000 },
#   {    10,     0,     0,     0 },
#   {   100,     0,     0,     0 },
#   {  1000,     0,     0,     0 }
# };

# int evaluatePosition(char board[9], char player) {
#   char opponent = (player == 'X') ? 'O' : 'X', piece;
#   int players, others, t = 0, i, j;
  
#   for (i = 0; i < 8; i++)  {
#     players = others = 0;
#     for (j = 0; j < 3; j++)  {
#       piece = board[Three_in_a_Row[i][j]];
#       if (piece == player)
#         players++;
#       else if (piece == opponent)
#         others++;
#     }
#     t += Heuristic_Array[players][others];
#   }
#   return t;
# }