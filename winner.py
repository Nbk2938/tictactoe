from tkinter import *
import tkinter
import numpy as np




def youLoose(canvas:Canvas):
    #new_canvas = Canvas(canvas, width=300, height=300, bg="white")
    looseLabel = Label(canvas, padx=0, pady=50, bg='white', fg='black', text=" you little shit.\n you thaught you colud win.\n there you go, you didn't.\n now go cry by your mama", font= ('Aerial', 18, "bold"))
    looseLabel.place(x = 14, y = 100)
    tkinter.Misc.lift(looseLabel)

def tie(canvas:Canvas):
    tieLabel = Label(canvas, padx=0, pady=50, bg='white', fg='black', text="no one won \n but i know that you'll\n NEVER win :)", font= ('Aerial', 18, "bold"))
    tieLabel.place(x = 70, y = 100)
    tkinter.Misc.lift(tieLabel)


def draw_win_line(vec,canvas:Canvas):
    if vec[0] == 1:
        canvas.create_line(35, 100, 465, 100, width= 2, fill='#8B0000')#rows
    elif vec[0] == 2:
        canvas.create_line(35, 250, 465, 250, width= 2, fill='#8B0000')
    elif vec[0] == 3:
        canvas.create_line(35, 400, 465, 400, width= 2, fill='#8B0000')

    elif vec[1] == 1:
        canvas.create_line(100, 35, 100, 465, width= 2, fill='#8B0000')#colums
    elif vec[1] == 2:
        canvas.create_line(250, 35, 250, 465, width= 2, fill='#8B0000')
    elif vec[1] == 3:
        canvas.create_line(400, 35, 400, 465, width= 2, fill='#8B0000')
    
    elif vec[2] == 1:
        canvas.create_line(35, 35, 465, 465, width= 2, fill='#8B0000')
    elif vec[2] == 2:
        canvas.create_line(465, 35, 35, 465, width= 2, fill='#8B0000')

def chek_for_win(matrix, winner, canvas:Canvas):
    state = np.append([],matrix).astype(int)

    for i in range(3): #control each row
        if matrix[i,0]!= 0 and matrix[i,0] == matrix[i,1] and matrix[i,0] == matrix[i,2]:
            if (winner == 1): 
                print("Cross wins")
            else: 
                print("Circle wins")
                youLoose(canvas)
            draw_win_line([i + 1,0,0], canvas)
            return [i,0,0]
    
    for i in range(3): #control each column
        if matrix[0,i]!= 0 and matrix[0,i] == matrix[1,i] and matrix[0,i] == matrix[2,i]:
            if (winner == 1): 
                print("Cross wins")
            else: 
                print("Circle wins")
                youLoose(canvas)
            draw_win_line([0,i + 1,0], canvas)
            return [0,i,0]
    
    if matrix[0,0] != 0 and matrix[0,0] == matrix[1,1] and matrix[0,0] == matrix[2,2]: # diagonal 1
        if (winner == 1): 
            print("Cross wins")
        else: 
            print("Circle wins")
            youLoose(canvas)
        draw_win_line([0,0,1], canvas)
        return [0,0,1]

    if matrix[0,2] != 0 and matrix[0,2] == matrix[1,1] and matrix[0,2] == matrix[2,0]: # diagonal 2
        if (winner == 1): 
            print("Cross wins")
        else: 
            print("Circle wins")
            youLoose(canvas)
        draw_win_line([0,0,2], canvas)
        return [0,0,2]
    
    else:
        try:
            if state.tolist().index(0) is not None:
                return None
        except ValueError:
            print("it's a tie")
            tie(canvas)
            return "tie"


