from random import randint

#create a list of play options
moves = ["rock", "paper", "scissors"]

#assign a random play to the computer
computer = moves[randint(0,2)]

#set player to False
player = True
#adds a count total of 3 games
count = 0

print("\n------->Welcome to Rock, Paper, Scissors game<-------")
playerName = input("\nPlease enter your name: ")

if len(playerName) == 0 :
    print("\nYour Name should contain at least one letter ")
    playerName = input("\nPlease enter your name: ")
    player == False

else : 
    player == True

while player:   
    
    print("Welcome "+playerName+"!\n")

    for i in range(1,4):
        
        computer = moves[randint(0,2)]

        playerMove = input("\nMake your move: ").casefold()
        
        #add function to validate playerMove
        
        count =+ i
        
        #add to function
        
        if computer == "paper" and playerMove == "rock":
            print("\nComputer wins!")
            print(computer, " beats ", playerMove)
        elif computer == "rock" and playerMove == "scissors":
           print("\nComputer wins!")
           print(playerMove, " beats ", computer)
        elif computer == "scissors" and playerMove == "paper":
            print("\nComputer wins!")
            print(computer, " beats ", playerMove)
        elif computer == playerMove or playerMove == computer:
            print("\nIt's a tie!")
            print(computer + " / " + playerMove )
            
        elif playerMove == "quit" or playerMove == "exit":
            break
            
        else:
            print("\nPlayer wins!")
            print(playerMove +" beats " +computer)
            
            #add to function
            
    if playerMove == "quit" or playerMove == "exit":
        break
        
    else: playAgain = input("\nWould you like to play another round? yes/no:  ").casefold()

    #add this to function
    if playAgain == "no": 
        print("\nThanks for playing! Bye-Bye!")
        break
        
    else: continue