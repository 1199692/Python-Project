# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
global moves
def startgame():
    a=(input('welcome! Do you want to play Game now '))
    if a.lower()=='yes' or'yup':
        b=(input('which team you do you want to choose x or o '))
        if b.lower()=='x':
            Iboard()
            Cxboard()
        elif b.lower()=='o':
            Iboard()
            Coboard()
        else:
            print('please select out of x and o only')
            pass
    elif a.lower()=='no':
        print('Thanks for playing!Come back again')
    else:
        print('please provide your correct input(yes/No)')
        startgame()
def Iboard():
    moves = [' ', ' ',' ',' ', ' ',' ',' ', ' ',' ']
    board = "|{}|{}|{}|\n|{}|{}|{}|\n|{}|{}|{}|\n"
    print(board.format(*moves))

def Cxboard():
    moves = [' ', ' ',' ',' ', ' ',' ',' ', ' ',' ']
    board = "|{}|{}|{}|\n|{}|{}|{}|\n|{}|{}|{}|\n"
    j=int(input('Team x-where do you want to put'))
    moves[j-1]='x'
    print(board.format(*moves))
    for i in range(0,10):
        if (moves[i]== moves[i+1]== moves[i+2]) or (moves[i] == moves[i+2] == moves[i+4]):
            print('you won!')
            c=input('do you want to play again')
            if c.lower()=='yes':  
                startgame()
            elif c.lower()=='no':
                print('Thanks for playing!Come back again')
            else:
                print('please provide your correct input(yes/No)')
                startgame()
        else:
            Coboard()       
    
def Coboard():
    k=int(input('Team y-where do you want to put'))
   Cxboard.moves[k- 1]='o'
    print(board.format(*(moves)))
    for i in range(0,10):
        if (x.moves[i]== x.moves[i+1]== x.moves[i+2]) or (x.moves[i] == x.moves[i+2] == x.moves[i+4]):
            print('you won!')
            d=input('do you want to play again')
            if d.lower()=='yes':
                startgame()
            elif d.lower()=='no':
                print('Thanks for playing!Come back again')
            else:
                print('please provide your correct input(yes/No)')
                startgame()
        else:
            Cxboard()

startgame()