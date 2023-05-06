# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 19:56:36 2023

@author: Thomas Pingel
"""

import numpy as np

#%%

def check_state(board):
    # Using numpy to check the state of the game and returns 'x_wins', 
    # 'o_wins', 'cat_game', or 'no_winner' as appropriate.
    # Suggested numpy functions: np.any, np.all, np.sum, np.trace, np.diagonal, np.rot90
    # Remember many of these functions take "axis=" parameters to calculate by row or column!
    
    state = 'no_winner'
    
    #check if o is winner (vertical, horizontal, diagonal * 2)
    o_col = np.any(np.sum(board=='o',axis=0) == 3)
    o_row = np.any(np.sum(board=='o', axis=1) == 3)
    o_diag1 = np.any(np.sum(np.diagonal(board) == 'o') == 3)
    o_diag2 = np.any(np.sum(np.fliplr(board).diagonal() == 'o') == 3)
    
    #check if x is winner (vertical, horizontal, diagonal * 2)
    x_col = np.any(np.sum(board=='x',axis=0) == 3)
    x_row = np.any(np.sum(board=='x', axis=1) == 3)
    x_diag1 = np.any(np.sum(np.diagonal(board) == 'x') == 3)
    x_diag2 = np.any(np.sum(np.fliplr(board).diagonal() == 'x') == 3)
    
    #if no winner yet, check if game is tied
    
    #else, return no winner
    if o_col or o_row or o_diag1 or o_diag2:
        state = 'o_wins'
    elif x_col or x_row or x_diag1 or x_diag2:
        state = 'x_wins'
    elif np.sum(board != ' ') == 9:
        state = 'cat_game'
    else:
        state = 'no_winner'
        
    return state
    
def create_board():
    # Use numpy to write a function that creates a 3x3 board, each filled with a space " "
    # Suggested numpy functions: np.full
    
    board = np.full((3,3), ' ', dtype = str)
    
    return board

def play_x(board):
    # Use numpy to write a function that places an "x" down randomly in any unfilled space
    # Suggested numpy functions: np.random.choice, np.nonzero, .ravel(), np.unravel_index  
    
    try_again = True
    
    while try_again:
        try_this = np.random.choice(9, 1, replace=False)
        r,c = np.unravel_index(try_this, (3,3))
        if board[r,c] != ' ':
            try_again = True
        else:
            board[r,c] = 'x'
            try_again = False
    
    return board

def play_o(board):
    # Use numpy to write a function that places an "o" down randomly in any unfilled space
    
    try_again = True
    
    while try_again:
        try_this = np.random.choice(9, 1, replace=False)
        r,c = np.unravel_index(try_this, (3,3))
        if board[r,c] != ' ':
            try_again = True
        else:
            board[r,c] = 'o'
            try_again = False
    
    return board


#%%

#play once

board = create_board()
state = 'no_winner'

while state=='no_winner':
    num_ohs = np.sum(board=='o')
    num_exes = np.sum(board=='x')
    if num_ohs==num_exes:
        print('playing o')
        play_o(board)
    else:
        print('playing x')
        play_x(board)
    print(board)
    state = check_state(board)
print(state)
