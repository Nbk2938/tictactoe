import numpy as np
import random
import os
import sys
import keyboard
import pynput
from pynput.keyboard import Key, Controller
kb = Controller()



def winner(board): #if human winns return -1, if ai winns return +1, in tie return 0
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
            if board.index(0) is not None:
                return None
        except ValueError:
            return 0
            
game1 = [1,1,1,0,2,0,2,0,2]
game2 = [1,1,2,0,2,2,2,1,1]
game3 = [1,2,1,1,2,2,2,1,1]
game4 = [1,0,0,0,2,0,0,0,1]

move = [- np.inf, - np.inf,1, - 1, 1,-1,0,0,1]
moves = np.array(move)

bestScore = int(np.amax(moves))
get_indexes = lambda x, xs: [i for (y, i) in zip(xs, range(len(xs))) if x == y]
bestIndexes = get_indexes(bestScore, moves.tolist())
print(" ")
print(bestIndexes)
print(random.choice(bestIndexes))
print("do you like to restart? [y / n ?]")

while True:  
    try:                                      
        if keyboard.is_pressed('y'):          
            kb.press(Key.backspace)               
            kb.release(Key.backspace)
            os.execl(sys.executable, sys.executable, *sys.argv)
            break  
        elif keyboard.is_pressed('n'): 
            kb.press(Key.backspace)               
            kb.release(Key.backspace)
            sys.exit()
    except:
        break

