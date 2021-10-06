# def tests():
#     state=[' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']
#     actions=9
#     winner=None
#     while winner==None:
#         nextMove,v=min_max_cut_off(copy.deepcopy(state),actions)#Aqui capaz se deberia hacer un depcopy del estado
#         print("The machine did the next movement :", interpretate_Computer(nextMove,actions))
#         state=play_move(state,nextMove)
#         show_board(state,actions)
#         winner=is_a_winner(state,actions)
#         if winner==None:
#             nextMove,v=max_min_cut_off(copy.deepcopy(state),actions)#Aqui capaz se deberia hacer un depcopy del estado
#             print("The machine did the next movement :", interpretate_Computer(nextMove,actions))
#             state=play_move(state,nextMove)
#             show_board(state,actions)
#             winner=is_a_winner(state,actions)