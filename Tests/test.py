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

def interpretate(movement,actions):
    #INTERPRETAR EL movimiento
    size=int(sqrt(actions))
    value=size*(int(movement[1])-1)+(ord(movement[0])-65)
    return value

print(interpretate("D3",25))