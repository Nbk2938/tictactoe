
from secrets import choice
import pyautogui
import numpy as np
import math
import random

def assign_value(value):

    x = np.arange(0,9).reshape(3,3)
    y,x = np.where(x == value)
    return (x,y)

def move_mouse(start, target):
    pos_start = assign_value(start)
    pos_target = assign_value(target)
    move = tuple(map(lambda x, y: x - y, pos_target, pos_start))
    return tuple(150 * x  for x in move)

def winner(board:np.ndarray): #if human winns return -1, if ai winns return +1, in tie return 0
    players = [1,2]
    for p in players:
        if (board[0] == p and board[1] == p and board[2] == p) or (board[3] == p and board[4] == p and board[5] == p) or (board[6] == p and board[7] == p and board[8] == p):
            if p == 1:
                return -1
            else:
                return 1
        elif (board[0] == p and board[3] == p and board[6] == p) or (board[1] == p and board[4] == p and board[7] == p) or (board[2] == p and board[5] == p and board[8] == p):
            if p == 1:
                return -1
            else:
                return 1
        elif (board[0] == p and board[4] == p and board[8] == p) or (board[2] == p and board[4] == p and board[6] == p):
            if p == 1:
                return -1
            else:
                return 1
    else:
        try:
            if board.tolist().index(0) is not None: # are there still free spacecs left?
                return None
        except ValueError:
            return 0

def minimax(board, depth, isMaximising): #(boardstate, deapth, next move is human or ai. False if human)
    result = winner(board)               # check for terminal state (if there is alredy a winner) and return the score
    if result is not None:
        return result
    
    if isMaximising: # turn of ai
        bestScore = - math.inf
        for i, cell in enumerate(board):
            if cell == 0:
                board[i] = 2
                score = minimax(board, depth + 1, False)
                board[i] = 0
                bestScore = max(score, bestScore)
        return bestScore

    else: # turn of human
        bestScore = math.inf
        for i, cell in enumerate(board):
            if cell == 0:
                board[i] = 1
                score = minimax(board, depth + 1, True)
                board[i] = 0
                bestScore = min(score, bestScore)
        return bestScore



def Ai_choice(matrix, butt_num):
    
    bestScore = - math.inf
    boardState = np.append([],matrix).astype(int) # game array (0=empty, 1=human, 2=ai)
    moves = - np.ones(9) * np.inf
    for i, cell in enumerate(boardState):         # cicle trough each cell
        if cell == 0:                             # determin if it's empty
            boardState[i] = 2                     # apply move
            score = minimax(boardState, 0, False) # return score of the hipotetical play in that cell
            moves[i] = score
            boardState[i] = 0                     # undo move
            if score > bestScore:                 # return the best score possible and the cell on wich to play
                bestScore = score
                bestMove = i
    bestScores = int(np.amax(moves))              # get highest score 
    get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y] 
    bestIndexes = get_indexes(bestScore, moves.tolist()) # get index of best scores
    choice = random.choice(bestIndexes)  #chose a random index
    pyautogui.move(move_mouse(butt_num, choice))
    pyautogui.click()
    #move mouse to specific location and click the button
