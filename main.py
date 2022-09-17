
from tkinter import *
import numpy as np
import time
from winner import chek_for_win
from ai import Ai_choice
import pyautogui
import sys
import os
import keyboard
import pynput
from pynput.keyboard import Key, Controller
import threading
kb = Controller()

sys.setrecursionlimit(2000)


level = np.matrix([[0,0,0],[0,0,0],[0,0,0]])

alternate = ["1","0","1","0","1","0","1","0","1","0"]
count = iter(alternate)

root = Tk ()
root.title('tic-tac-toe')
root.geometry("500x500")
#root.resizable(False, False)

my_canvas=Canvas(root, width=500, height=500, bg="white")
my_canvas.pack()

print(" ")
print("New game of tic tac toe")
print("try beating me")
print("make your beginning choice")

def reStart():
    
    print("press 'y' to restart")

    while True:  
        try:                                     
            if keyboard.is_pressed('y'):          
                kb.press(Key.backspace)               
                kb.release(Key.backspace)
                os.execl(sys.executable, sys.executable, *sys.argv)
                break  
            """elif keyboard.is_pressed('n'): 
                kb.press(Key.backspace)               
                kb.release(Key.backspace)
                #thread.join()
                sys.exit()
                break"""
        except:
            break

       
thread = threading.Thread(target = reStart)

def update(button_num, define):
    row = int(button_num / 3)
    col = button_num % 3
    level[row,col] = define
    #print(level)

def drawGameStatus(a,b, widget, num):
    sign = 0
    if next(count) == "1":
        my_canvas.create_line(a + 25, b + 125, a + 125, b + 25, width= 2) #cross
        my_canvas.create_line(a + 25, b + 25, a + 125, b + 125, width= 2)
        widget.destroy()
        sign = 1
        update(num,sign)
        win = chek_for_win(level, sign, my_canvas) 
        if win is None:
            Ai_choice(level, num)
        else: 
            thread.start()
    else:
        my_canvas.create_oval(a + 25, b + 125, a + 125, b + 25, width= 2) #circle
        widget.destroy()
        sign = 2
        update(num,sign)
        win2 = chek_for_win(level, sign, my_canvas)
        if win2 is not None:
            thread.start()
        
    

    #mouse_pos = pyautogui.position()
    #print(mouse_pos)
    #time.sleep(500)
    #Ai_choice(level, num)
    


button0 = Button(my_canvas, padx=69, pady=55, bg='white', fg='white', command =lambda: drawGameStatus(25,25, button0,0))# first row
button1 = Button(my_canvas, padx=69, pady=55, bg='white', fg='white', command =lambda: drawGameStatus(175,25, button1,1))
button2 = Button(my_canvas, padx=69, pady=55, bg='white', fg='white', command =lambda: drawGameStatus(325,25, button2,2))

button3 = Button(my_canvas, padx=69, pady=55, bg='white', fg='white', command =lambda: drawGameStatus(25,175, button3,3))# second row
button4 = Button(my_canvas, padx=69, pady=55, bg='white', fg='white', command =lambda: drawGameStatus(175,175, button4,4))
button5 = Button(my_canvas, padx=69, pady=55, bg='white', fg='white', command =lambda: drawGameStatus(325,175, button5,5))

button6 = Button(my_canvas, padx=69, pady=55, bg='white', fg='white', command =lambda: drawGameStatus(25,325, button6,6))# third row
button7 = Button(my_canvas, padx=69, pady=55, bg='white', fg='white', command =lambda: drawGameStatus(175,325, button7,7))
button8 = Button(my_canvas, padx=69, pady=55, bg='white', fg='white', command =lambda: drawGameStatus(325,325, button8,8))

button0.place(x = 25, y = 24)
button1.place(x = 175, y = 24)
button2.place(x = 325, y = 24)
button3.place(x = 25, y = 175)
button4.place(x = 175, y = 175)
button5.place(x = 325, y = 175)
button6.place(x = 25, y = 325)
button7.place(x = 175, y = 325)
button8.place(x = 325, y = 325)

my_canvas.create_line(175, 25, 175, 475, fill="black") #lines
my_canvas.create_line(325, 25, 325, 475, fill="black")
my_canvas.create_line(25, 175, 475, 175, fill="black")
my_canvas.create_line(25, 325, 475, 325, fill="black")

root.mainloop()