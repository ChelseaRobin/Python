from random import randint

from player import *
from txtFile import *

#create a list of play options
moves = ["rock", "paper", "scissors"]

#assign a random play to the computer
computer = moves[randint(0,2)]

#set player to False
player = True

#adds a userID
userID = 0
#adds a count total of 3 games
count = 0
#stores the outcome of each round
rounds = []

file = open('save.text', 'a+')

print("\n------->Welcome to Rock, Paper, Scissors game<-------")

player, playerName = validatePlayerName(player)

while player:   
    
    print(f"\n------->Welcome {playerName}!<-------\n")

    for i in range(1,4):
        
        computer = moves[randint(0,2)]

        playerMove = validatePlayerMove(moves) #Validates the players moves
        
        count += i
        
        if computer == "paper" and playerMove == "rock":
            print("\nComputer wins!")
            winner = "C"
            print(computer, " beats ", playerMove)
        elif computer == "rock" and playerMove == "scissors":
            print("\nComputer wins!")
            winner = "C"
            print(playerMove, " beats ", computer)
        elif computer == "scissors" and playerMove == "paper":
            print("\nComputer wins!")
            winner = "C"
            print(computer, " beats ", playerMove)
        elif computer == playerMove or playerMove == computer:
            print("\nIt's a tie!")
            winner = "T"
            print(computer + " / " + playerMove )
            
        elif playerMove == "quit" or playerMove == "exit":
            break
            
        else:
            print("\nPlayer wins!")
            winner = "P"
            print(playerMove +" beats " +computer)
        
        rounds.append(f'{winner} |')
        
    current_date = getDate()
    addDate(file, current_date)
    addLines(file,playerName, rounds)
      
    if playerMove == "quit" or playerMove == "exit":
        break
        
    else: 
        playAgain = input("\nWould you like to play another round? yes/no:  ").casefold()

    if playAgain == "no": 
        print("\nThanks for playing! Bye-Bye!")
        break
        
    else: continue