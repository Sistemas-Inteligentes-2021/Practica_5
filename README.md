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

Nº | Player | Type | Space | Total Space | Time | Result 
:---: | :---: | :---: | :---: | :---: | :---: | :---:
 1 | Daniel | X | [3300, 2132, 1276, 626, 278, 113, 8] | 7 733 | 0.0.0802149772644043 | X Won! 
 2 | Daniel | O | [4016, 2674, 1666, 774, 381, 135, 17, 1] | 9 664 | 0.08178696036338806 |O Won! 
 3 | Adrian | X | [3300, 2132, 1184] | 6 616 | 0.1448960304260254 | X Won!
 4 | Adrian | O | [4016, 2674, 1666, 950, 472, 166, 38, 2] | 9 984 | 0.08500140905380249 | O Won!
 5 | Juslan | X | [3300, 2132, 1184] | 6 616 | 0.14067872365315756 | X Won!
 6 | Juslan | O | [4016, 2674, 1668, 950, 438] | 9 746 | 0.12540926933288574 | O Won!
 
- Difficult: 5 x 5

Nº | Player | Type | Space | Total Space | Time | Result 
:---: | :---: | :---: | :---: | :---: | :---: | :---:
 1 | Daniel | X | [13704, 10538, 11860, 28460, 4016, 2674, 2646, 1664, 832, 186, 32, 2] | 76 614 | 0.7020383675893148 | Tie! 
 2 | Daniel | O | [15500, 12052, 9156, 8824, 25788, 3300, 2132, 1602, 948, 532, 80] | 79 914 | 0.8150447715412487 |X Won! 
 3 | Adrian | X | [13704, 10538, 11860, 9154, 7399, 4043, 6890, 950, 764, 250, 44, 2] | 65 598 | 0.6062553723653158 | Tie!
 4 | Adrian | O | [15500, 12052, 9156, 6764, 4828, 5754, 4950, 1398, 684, 308, 72, 12, 0] | 61 478 | 0.5435923979832575 | Tie!
 5 | Juslan | X | [13704, 10538, 9563, 6852, 4016, 4234, 2646, 2077, 626, 246, 32, 2] | 54 536 | 0.5080046852429708 | Tie!
 6 | Juslan | O | [15500, 12052, 9156, 10808, 38080, 3300, 2132, 1276, 532, 301, 100, 10, 0] | 93 247 | 0.7698319508479192 | Tie!

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
:---: | :---: | :---: | :---: | :---: | :---: | :---:
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
 2 | Juslan | X | [56754, 1574, 60, 2]  | 58 390 |3.167483329772949 | Tie!
 3 | Adrian | O | [649300, 11024, 200, 12, 0] |  660 536 |  29.55744800567627  | Tie!

 ### Alpha Beta Pruning

- Difficult: 3 x 3 

Nº | Player | Type  | Spaces | Total Space | Time (Avg) | Result 
:---: | :---: | :---: | :---: | :---: | :---: | :---:
 1 | Daniel | X | [4081, 272, 48, 2] | 4 403 | 0.04032200574874878 | Tie!
 2 | Daniel | O | [30700, 2147, 147, 8]| 33 002| 0.24714940786361694 | X Won! 
 3 | Adrian | X | [6192, 362, 51, 2] |  6 607 | 0.05242621898651123 | Tie!
 4 | Adrian | O | [30700, 2704, 132, 10, 0] | 33 546 | 0.20253558158874513 | Tie! 
 5 | Juslan | X | [6130, 507, 36, 2] | 6 675 | 0.051823318004608154 | Tie!
 6 | Juslan | O | [30700, 2704, 132, 10, 0] | 33 546 | 0.19540271759033204 | Tie! 

- Difficult: 4 x 4, 
    ### Initial State

    Nº| A | B | C | D   
    ---|--- |--- | --- | ---
    1 | ' ' | ' ' | ' ' | ' ' 
    2 | ' ' | ' ' | ' ' | ' ' 
    3 | 'X' | 'O' | ' ' | ' ' 
    4 | 'O' | 'X' | 'O' | 'X' 
    

Nº | Player | Type | Spaces | Space | Time | Result 
:---: | :---: | :---: | :---: | :---: | :---: | :---:
1 | Daniel | O | [15017, 1480, 154, 10, 0] | 16 661 | 0.2658102035522461 | Tie! 
2 | Juslan | O | [14451, 1182, 128, 12, 0] | 15 773 | 0.2514761447906494 | Tie! 
3 | Adrian | O | [22371, 1307, 118] | 23 796 | 0.5870599746704102 |  X Won!  

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
 1 | Adrian | X | [15901, 477, 44, 2] | 16 424 | 0.6072256565093994 | Tie!
 2 | Juslan | X | [11295, 477, 42, 2]  | 11 816 |0.47043126821517944 | Tie!
 3 | Daniel | O | [42178, 1208, 169, 8] |  43 563 |   1.5239135026931763  | X Won! 
## 4. Conclusions
- How many states does the game tree have for 3x3, 4x4 and 5x5?

    As we can see in the experiments the game tree has the next number of states

    3x3:
        
        Min Max: 215 762.5 states
        Alpha Beta: 19 683.8 states
        Min Max CutOff: 5 602.5 states

    4x4:
    
        Min Max: 745 865.3 states  // For 10 possible moves
        Alpha Beta: 18 743.3 states  // For 10 possible moves
        Min Max CutOff: 8 393.2 states

    5x5:

        Min Max: 258 968.7 states  // For 9 possible moves
        Alpha Beta: 23 934.3 states  // For 9 possible moves
        Min Max CutOff: 71 897.8 states


- Which is the algorithm that (more) less delay and which is the algorithm that expand (more) less states?

    - In conclusion the algorithm that less delay and expand less states is the algorithm that we saw in classes 'Min Max CutOff' we can conclude that based on experiments.

    - In the other hand we have seen that the algorithm that more delay and expand more states is the algorithm "Min Max", in our experiments we can observe than is worst than Alpha Beta Pruning.

### Comments
- We put an initial state with 6 moves for the 4x4 experiments and 16 moves (Min Max & Alpha Beta) for the 5x5 board experiments, because the time we have been waiting for a result was more than 4 hours and we have not received a response from the machine after waiting that time.

- For the average of states in Min Max & Alpha Beta, we put the average just for 10 possible moves (4x4) and 9 possible moves (5x5).

## 5. Bibliography

➡️  Infinity: [Python Docs: Swarm][infinity]

➡️  Heuristic: [Mississippi University: Ole Miss][heuristic]

[infinity]: https://www.it-swarm-es.com/es/python/como-puedo-representar-un-numero-infinito-en-python/939929888/

[heuristic]: https://john.cs.olemiss.edu/~dwilkins/CSCI531/fall12/slides/AI_09_games.pdf