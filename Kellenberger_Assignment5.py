# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 19:56:36 2023

@author: Thomas Pingel
"""

import numpy as np
import time


#%%

def check_state(board):
    # returns 'x_wins', 'o_wins', 'cat_game', or 'no_winner'
    if np.any(np.sum(board=='x',axis=0)==3) or \
        np.any(np.sum(board=='x',axis=1)==3) or \
            np.trace(board=='x')==3 or np.trace(np.rot90(board)=='x')==3:
           return 'x_wins'
    if np.any(np.sum(board=='o',axis=0)==3) or \
        np.any(np.sum(board=='o',axis=1)==3) or \
            np.trace(board=='o')==3 or np.trace(np.rot90(board)=='o')==3:
           return 'o_wins'
    if np.sum(board==' ')==0:
        return 'cat_game'
    else:
        return 'no_winner'
    

def make_random_move(board,player):
    tic = time.time()

    r,c = np.nonzero(board==' ')
    choice = np.random.choice(range(len(c)))
    board[r[choice],c[choice]] = player

    toc = time.time()
    
    return board,toc-tic    

# *** THIS IS THE FUNCTION TO WORK ON ***
def make_move(board,player):
    
    tic = time.time()
    
    #if middle spot has not been claimed, claim middle spot
    if board[1,1] == ' ':
        board[1,1] = player
        toc = time.time()
        return board, toc-tic
    
    #if middle spot is claimed & if corners not claimed, claim corner
    if board[1,1] == player:
        if board[0,0] == ' ':
            board[0,0] = player
            toc = time.time()
            return board, toc-tic
        elif board[0,2] == ' ':
            board[0,2] = player
            toc = time.time()
            return board, toc-tic
        elif board[2,0] == ' ':
            board[2,0] = player
            toc = time.time()
            return board, toc-tic
        elif board[2,2] == ' ':
            board[2,2] = player
            toc = time.time()
            return board, toc-tic
    
    
    #if 2 claimed spaces in row/column, play on remaining square in that row/column
    if np.any(np.sum(board==player,axis=1)==2):
        row = np.where((np.sum(board==player,axis=1)==2))
        r = row[0]
        r = r[0]
        col = np.where(board[r,] == ' ')
        if(col[0] == 0 or col[0] == 1 or col[0] == 2):
            c = col[0]
            c = c[0]
            board[r,c] = player
            toc = time.time()
            return board, toc-tic
        else:
            return make_random_move(board, player)
    elif np.any(np.sum(board==player,axis=0)==2):
        col = np.where((np.sum(board==player,axis=0)==2))
        c = col[0]
        c = c[0]
        row = np.where(board[:,c] == ' ')
        if(row[0] == 0 or row[0] == 1 or row[0] == 2):
            r = row[0]
            r = r[0]
            board[r,c] = player
            toc = time.time()
            return board, toc-tic
        else:
            return make_random_move(board, player)
        
    #if 2 claimed spaces in diagonal, play on remaining square in diagonal
    elif np.any((np.sum(np.diagonal(board)==player) == 2)):
        diag = np.where(np.diagonal(board) == ' ')
        if(diag[0] == 0 or diag[0] == 1 or diag[0] == 2):
            spot = diag[0]
            board[spot,spot] = player
            toc = time.time()
            return board, toc-tic
        else:
            make_random_move(board, player)
    elif np.any((np.sum(np.fliplr(board).diagonal()==player) == 2)):
        diag = np.where(np.fliplr(board).diagonal() == ' ')
        if(diag[0] == 0 or diag[0] == 1 or diag[0] == 2):
            spot = diag[0]
            board[spot,spot] = player
            toc = time.time()
            return board, toc-tic
        else:
            return make_random_move(board, player)
    
    else:
        return make_random_move(board, player)
    
#%%

board = np.full((3,3),' ')
state = 'no_winner'

while state=='no_winner':
    num_ohs = np.sum(board=='o')
    num_exes = np.sum(board=='x')
    if num_ohs==num_exes:
        make_random_move(board,'o')
    else:
        make_move(board,'x')
    print(board,'\n')
    state = check_state(board)

print(state)

#%%

#percentage won test

board = np.full((3,3),' ')
state = 'no_winner'
i = 0

x_wins = 0
o_wins = 0
cat_game = 0

while i <= 10000:
    while state=='no_winner':
        num_ohs = np.sum(board=='o')
        num_exes = np.sum(board=='x')
        if num_ohs==num_exes:
            make_random_move(board,'o')
        else:
            make_move(board,'x')
        state = check_state(board)
    if state == 'x_wins':
        x_wins += 1
        i += 1
        board = np.full((3,3),' ')
        state = 'no_winner'
    elif state == 'o_wins':
        o_wins += 1
        i += 1
        board = np.full((3,3),' ')
        state = 'no_winner'
    elif state == 'cat_game':
        cat_game += 1
        i += 1
        board = np.full((3,3),' ')
        state = 'no_winner'
    
print('X Wins: ' + str(x_wins/10000))
print('O Wins: ' + str(o_wins/10000))
print('Tie Games: ' + str(cat_game/10000))



