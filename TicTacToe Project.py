#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random 
from IPython.display import clear_output
    
#Grid printing Format

#Individual Rows of board with assigned grid numbers:
row1 = {'1':' ','2':' ','3':' '}
row2 = {'4':' ','5':' ','6':' '}
row3 = {'7':' ','8':' ','9':' '}

#List containing all dictionaries (makes the board as a whole)

ticTacToeBoard = [row1,row2,row3]


#Initital assignments:

player1 = ''
player2 = ''
players = []

firstmove = ''

def printFunc(board):
    #The printing function takes all three rows of the dictionary
    clear_output()
    print("     "+'|'+"   "+'  |')
    print("  "+row1['1']+'  |  '+row1['2']+'  |  '+row1['3']+"  ")
    print("     "+'|'+"   "+'  |')


    print("-----------------")

    print("     "+'|'+"   "+'  |')
    print("  "+row2['4']+'  |  '+row2['5']+'  |  '+row2['6']+"  ")
    print("     "+'|'+"   "+'  |')
    
    print("-----------------")

    print("     "+'|'+"   "+'  |')
    print("  "+row3['7']+'  |  '+row3['8']+'  |  '+row3['9']+"  ")
    print("     "+'|'+"   "+'  |')

    print(" ")
    print(" ")

        
def playerAssignment():

    player1 = ""
    player2 = ""
    valid = False
    
    print("Welcome to Noah's Tic Tac Toe Game!")
    choice = input("Player 1: Would you like to be X or O? ")
    
    while valid == False:
        
        if choice == "X" or choice == "x":
            player1 = 'X'
            player2 = 'O'
            valid = True

        elif choice == "O" or choice == "o":
            player1 = 'O'
            player2 = 'X'
            
            valid = True
            
        else:
            print("Sorry I couldn't understand your input, Assure that you enter either X or O:")
            choice = input("Player 1: Would you like to be X or O? ")
    
    
    firstmove = firstMove()
    if firstmove == "Player 1":
        return player1, player2,firstmove
    
    
    else:        
        
        return player2, player1, firstmove


def firstMove():
    
    value = random.randint(1,2)  
    
    if value == 1:
        return "Player 1"
    else:
        return "Player 2"
    
def ready():
    
    acceptableValues = ['Y','N','y','n']
    ready = ""
    
    ready = input("Are you ready to start playing? (Y/N) ")
    
    while ready not in acceptableValues:
        print ("I could't understand your input, Assure you enter in Y or N")
        ready = input("Are you ready to start playing? (Y/N) ")
        
    while ready == "N" or ready == "n":
        
        ready = input("Are you ready now? (Y/N) ")
        
        while ready not in acceptableValues:
            print ("I could't understand your input, Assure you enter in Y or N")
            ready = input("Are you ready now? (Y/N) ")
                
    if ready == 'Y' or ready == 'y':
        return False
    
def readyAgain():
    acceptableValues = ['Y','N','y','n']
    
    ready = input("Do you wanna play again? (Y/N) ")
    
    while ready not in acceptableValues:
        print ("I could't understand your input, Assure you enter in Y or N")
        ready = input("Do you wanna play again? (Y/N) ")
        
    if ready == "N" or ready == "n":
        return False
    if ready == "Y" or ready == "y":
        return True
    
def gameLogic(players):
    
    playerID = ''
    move = ''
    done = False
    turn = 2
    currentPlayersLetter = ''
    
    startingPlayer = players[2]
    
    if startingPlayer == "Player 1":
        proceedingPlayer = "Player 2"
        SPL= players[0]
        PPL = players[1]
        
    elif startingPlayer == "Player 2":
        proceedingPlayer = "Player 1"
        SPL = players[1]
        PPL = players[0]

    for elements in range(0,9):
        
        if checkWin(SPL):
            print(startingPlayer+ ' Wins!')
            break
            
        elif checkWin(PPL):
            print(proceedingPlayer+ ' Wins!')
        
        if turn % 2 == 0:
            turn+=1
            print("\nIt's "+ startingPlayer +"'s turn:")
            move = playerInput()
            currentPlayersLetter = SPL
            
        elif turn % 2 != 0:
            turn+=1
            print("\nIt's "+ proceedingPlayer +"'s turn:")
            move = playerInput()
            currentPlayersLetter = PPL
            
        if move <=3:
            
            while row1[str(move)] == "X" or row1[str(move)] == "Y":
                print("There's already a letter there!")
                move = playerInput()

                    
            else:   
                row1[str(move)] = currentPlayersLetter
                printFunc(ticTacToeBoard)
                
        if move>=4 and move <=6:
            
            while row2[str(move)] == "X" or row2[str(move)] == "Y":
                print("There's already a letter there!")
                move = playerInput()

                
            else:
                row2[str(move)] = currentPlayersLetter
                printFunc(ticTacToeBoard)
            
        if move>=7 and move <=9:
            
            while row3[str(move)] == "X" or row3[str(move)] == "Y":
                print("There's already a letter there!")
                move = playerInput()

            else:   
                row3[str(move)] = currentPlayersLetter
                printFunc(ticTacToeBoard)
            
    else :
        print("Tie Game!")
        return

def playerInput():
    print("")
    print("Where you you like to move? (1-9)")
    move = input()
    
    #Input Validation
    while move.isdigit() == False or int(move) not in range(0,10):
        
        if move.isdigit() == False:
            print("Assure your input is a integer.)")
            print("Where you you like to move? (1-9)")
            move = input()
            
        elif int(move) not in range(0,10):
            print("Assure your input is a in range of 1-9.")
            print("Where you you like to move? (1-9)")
            move = input()
            
    return int(move)
    
def checkWin(marker):
    
    return ((row1['1']==row1['2']==row1['3']==marker) or 
            (row2['4']==row2['5']==row2['6']==marker) or 
           (row3['7']==row3['8']==row3['9']==marker) or
           (row1['1']==row2['4']==row3['7']==marker) or
            (row1['2']==row2['5']==row3['8']==marker) or
            (row1['3']==row2['6']==row3['9']==marker) or
            (row1['1']==row2['5']==row3['9']==marker) or
            (row1['3']==row2['5']==row3['7']==marker))
    
def ticTacToe():

    players = playerAssignment()
    
    firstmove = players[2]
    
    
    print('\n'+firstmove + " goes First! (Chosen Randomly)")
    
    ready()
    
    gameLogic(players)
    
    readyToPlay = readyAgain()
    if readyToPlay:
        ticTacToe()
        
    else:
        return
    
ticTacToe()


# 

# In[ ]:


8

