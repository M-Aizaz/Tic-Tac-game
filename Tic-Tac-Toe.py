# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 15:33:25 2021

@author: Aizaz
"""



board =["_","_","_","_","_","_","_","_","_"]
going = True
a=0
curent_player = "x"

def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])

def play():
    display_board()
    
    while going:
          
          turn() 
          player()
          
          row()
          col()
          dia()
          tie()
          
    
    
    
def turn():
         global curent_player
         print(curent_player + "s turn.")
         postion=input("enter number 1-9:")
         valid = False
         while not valid:
         
                while postion not in ["1","2","3","4","5","6","7","8","9"]:
                      postion=input("enter agin number 1-9:")
                postion = int(postion) - 1
                if board[postion] == "_":
                    valid = True
                else:
                    print("you cant go there.Go again")
         
         board[postion]= curent_player                          
         display_board()
         return
""" 
        if board[postion] != "_":
             print("position occ")
             #curent_player == curent_player
         elif (curent_player == "x"):
               curent_player = "o"
         elif(curent_player == "o"):
               curent_player = "x
               """
         
      #  board[postion]= curent_player
         
         
         
   
        
         
def player():
    global curent_player
    
        
    if (curent_player == "x"):
         curent_player = "o"
    elif(curent_player == "o"):
         curent_player = "x"
    return 
#def winner():
    
 
def tie():
    global going
    if "_" not in board:
        going = False
        print("Game is Tie")


def row():
    global a,going
    row1 = board[0] == board[1] == board[2]  == "x" 
    row2 = board[3] == board[4] == board[5]  == "x"
    row3 = board[6] == board[7] == board[8]  == "x"
    row11 = board[0] == board[1] == board[2]  == "o" 
    row22 = board[3] == board[4] == board[5]  == "o"
    row33 = board[6] == board[7] == board[8]  == "o"
    if row1 or row2 or row3 :
        a==1
        print("X is win")
        going = False
    if  row11  or row22 or row33 :
        a==1
        print("O is win")
        going = False
        
def col():
    global a,going
    col1 = board[0] == board[3] == board[6] == "x"
    col2 = board[1] == board[4] == board[7] == "x"
    col3 = board[2] == board[5] == board[8] == "x" 
    col11 = board[0] == board[3] == board[6] == "o"
    col22 = board[1] == board[4] == board[7] == "o"
    col33 = board[2] == board[5] == board[8] == "o"      
    if col1 or col2 or col3 :
        a==1
        print(" X is win")
        going = False
    if col11 or col22 or col33:
        a==1
        print(" O is win")
        going = False
def dia():
    global a,going
    dia1 = board[0] == board[4] == board[8] == "x" 
    dia2 = board[2] == board[4] == board[6] == "x"
    dia11 = board[0] == board[4] == board[8] == "o" 
    dia22 = board[2] == board[4] == board[6] == "o"
    if dia1 or dia2 :
        a==1
        print("X is win")
        going = False
    if dia11 or dia22:
        a==1
        print("O is win")
        going = False
        
#def winer():

    
play()  
        
"""    
def wnner():
    global going
    if row():
        going = False
        print("jjj")
    """
"""

while True:
"""