# Practica_5
## Members

- Daniel Camacho
- Adrian Mendoza
- Juslan Vargas

## 1. Describing the Problem

The main problem that we want to solve in this practice is the famouse game 'Tic Tac Toe', we want to implement the game for  diferents sizes boards (3x3, 4x4, 5x5) with an intelligent algorithm.
## 2. Describing the Solution

To solve the problem we developed the 'Tic Tac Toe' algorithm with adversarial search, we used 'Min Max', 'Alpha Beta Pruning' & our own algorithm that we call 'Min Max CutOff'.

The solution consist that a player play the game with diferents options, like he can choose if he wants to start the game ('X' Option) or be the second one ('O' Option) and the difficulty of the game (3x3, 4x4, 5x5)

## 3. Experiments & Results

We test all the algorithms but we focused in 'Min Max CutOff' Algorithm with a dificulty 3x3.

Firstly we played against the code that we made (Min Max CutOff, Min Max & Alpha Beta Pruning). Then we made that our classmates play our game. Finally we made that our algorithm deal against others algorithms in video games sites and we get the next results
### Min Max Cut Off

- Difficult: 3 x 3, Depth: 5

Nº | Player | Type | Space | Total Space | Time | Result 
:---: | :---: | :---: | :---: | :---: | :---: | :---:
 1 | Daniel | X | [2969, 493, 48, 2] | 3 512 | 0.014499783515930176 | Tie! 
 2 | Daniel | O | [5256, 2171, 132, 10, 0] | 7 569 | 0.026001548767089842 | Tie! 
 3 | Adrian | X | [2337, 453, 32, 2] | 2 824 | 0.012748658657073975 | Tie!
 4 | Adrian | O | [5256, 2171, 132, 7] | 7 566 | 0.03250157833099365 | X Won!
 5 | Juslan | X | [4857, 541, 39, 2] | 5 439 | 0.023073136806488037  | Tie!
 6 | Juslan | O | [5256, 1293, 153, 3] | 6 705| 0.02880072593688965 | X Won!

- Difficult: 4 x 4

Nº | Player | Type | Space | Time | Result 
:---: | :---: | :---: | :---: | :---: | :---:
 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |
 
- Difficult: 5 x 5

Nº | Player | Type | Space | Time | Result 
:---: | :---: | :---: | :---: | :---: | :---:
 | | | | | |
 | | | | | |
 | | | | | |
 | | | | | |

### Min Max

- Difficult: 3 x 3 

Nº | Player | Type | Space | Total Space | Time (Avg) | Result 
:---: | :---: | :---: | :---: | :---:  | :---: | :---:
 1 | Daniel | X | [59696, 928, 42, 2] | 60 668 | 0.26824891567230225 | Tie! 
 2 | Daniel | O | [549936, 7972, 252, 4] | 558 164 | 2.4795034527778625 | X Won! 
 3 | Adrian | X | [59696, 928, 42, 2] | 60 668| 0.26400017738342285 | Tie!
 4 | Adrian | O | [549936, 7324, 192, 10, 0] | 557 462 | 1.9845251560211181 | Tie!
 5 | Juslan | X | [55496, 1048, 48, 2] | 56 594 |0.2562618851661682 | Tie!
 6 | Juslan | O | [549936, 7324, 192, 10, 0]| 557 462 | 1.9858028888702393 | Tie! 

- Difficult: 4 x 4, 
    ### Initial State

    Nº| A | B | C | D   
    ---|--- |--- | --- | ---
    1 | ' ' | ' ' | ' ' | ' ' 
    2 | ' ' | ' ' | ' ' | ' ' 
    3 | 'X' | 'O' | ' ' | ' ' 
    4 | 'O' | 'X' | 'O' | 'X' 
    

Nº | Player | Type | Spaces | Space | Time | Result 
:---: | :---: | :---: | :---: | :---: | :---:
1 | Adrian | O | [796488, 10232, 284, 10, 0] | 807 014 | 16.635729169845582 | Tie! 
2 | Juslan | O | [620872, 6158] | 627 030 | 27.92502772808075  | O Won! |
3 | Daniel | O | [796488, 6842, 212, 10, 0] | 803 552 | 14.743660354614258 | Tie! 

- Difficult: 5 x 5
    ### Initial State

    Nº| A | B | C | D | E
    ---|--- |--- | --- | --- | ---
    1 | ' ' | ' ' | ' ' | ' ' | ' ' 
    2 | ' ' | ' ' | 'X' | ' ' | ' ' 
    3 | 'O' | 'X' | 'X' | 'O' | 'X' 
    4 | 'O' | 'X' | 'O' | 'O' | 'X' 
    5 | 'O' | 'X' | 'O' | 'X' | 'X' 

Nº | Player | Type  | Spaces | Total Space | Time (Avg) | Result 
:---: | :---: | :---: | :---: | :---: | :---: | :---:
 1 | Daniel | X | [56754, 1180, 44, 2] | 57 980 | 3.1415116786956787 | Tie!
 2 | Juslan | X | [56754, 1574, 60, 2]  | 58390 |3.167483329772949 | Tie!
 3 | Adrian | O | [649300, 11024, 200, 12, 0] |  660536 |  029.55744800567627  | Tie!

 ### Alpha Beta Pruning

- Difficult: 3 x 3 

Nº | Player | Type  | Spaces | Total Space | Time (Avg) | Result 
:---: | :---: | :---: | :---: | :---: | :---: | :---:
 1 | Daniel | X | [59696, 928, 42, 2] | 60 668 | 0.265067458152771 | Tie!
 2 | Daniel | O | [549936, 7972, 252, 7] | 558 167 | 2.521013557910919 | X Won! 
 3 | Adrian | X | [59696, 928, 42, 2] |  60 668 |  0.2658373713493347 | Tie!
 4 | Adrian | O | [549936, 7972, 252, 7] | 558 167 |  2.46313613653183 | X Won! 
 5 | Juslan | X | [59696, 928, 42, 2] |  60 668 | 0.26260846853256226 | Tie!
 6 | Juslan | O | [549936, 7324, 192, 10, 0] | 557 462 |  1.9810106754302979 | Tie! 

## 4. Conclusions
- How many states does the game tree have for 3x3, 4x4 and 5x5?

    As we can see in the experiments the game tree has the next number of states

    3x3:
        
        Min Max: 215 762.5 states
        Alpha Beta: 309 300 states
        Min Max CutOff: 5 602.5 states

    4x4:

    5x5:


- Which is the algorithm that (more) less delay and which is the algorithm that expand (more) less states?

    In conclusion the algorithm that less delay and expand less states is the algorithm that we saw in classes 'Min Max CutOff' we can conclude that based on experiments.

### Comments



## 5. Bibliography

➡️  Infinity: [Python Docs: Swarm][infinity]

[infinity]: https://www.it-swarm-es.com/es/python/como-puedo-representar-un-numero-infinito-en-python/939929888/