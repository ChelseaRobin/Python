from random import randint

from player import *
from getDate import getDate
from database import *

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
player_info = []

print("\n------->Welcome to Rock, Paper, Scissors game<-------")

player, playerName = validatePlayerName(player)

while player:   
    
    print(f"\n------->Welcome {playerName}!<-------\n")
    player_info.append(f'{playerName}')
    

    for i in range(1,4):
        
        computer = moves[randint(0,2)]

        playerMove = validatePlayerMove(moves) #Validates the players moves
        
        count += i
        
        if computer == "paper" and playerMove == "rock":
            print("\nComputer wins!")
            winner = "defeat"
            print(computer, " beats ", playerMove)
        elif computer == "rock" and playerMove == "scissors":
            print("\nComputer wins!")
            winner = "defeat"
            print(playerMove, " beats ", computer)
        elif computer == "scissors" and playerMove == "paper":
            print("\nComputer wins!")
            winner = "defeat"
            print(computer, " beats ", playerMove)
        elif computer == playerMove or playerMove == computer:
            print("\nIt's a tie!")
            winner = "tie"
            print(computer + " / " + playerMove )
            
        elif playerMove == "quit" or playerMove == "exit":
            break
            
        else:
            print("\nPlayer wins!")
            winner = "winner"
            print(playerMove +" beats " +computer)
        
        player_info.append(f'{winner}')
        
    current_date = getDate()
    player_info.append(f'{current_date}')
    
    conn = create_connection(r"RPA_database.db")
    if conn is not None: #checks if database exists
        createDatabase(conn) #creates database
    
    if "tie" in player_info and "defeat" in player_info:
        addToHistory(conn,player_info)
    elif "tie" not in player_info and "defeat" not in player_info:
        rows = checkRows(conn)
        print(f'######## {rows}')
        if rows < 10:
            addPlayerToTT(conn,player_info)
      
    if playerMove == "quit" or playerMove == "exit":
        break
        
    else: 
        playAgain = input("\nWould you like to play another round? yes/no:  ").casefold()

    if playAgain == "no": 
        print("\nThanks for playing! Bye-Bye!")
        break
        
    else: continue