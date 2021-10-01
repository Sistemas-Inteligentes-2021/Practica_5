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



print(0%2)









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