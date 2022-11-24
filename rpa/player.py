def validatePlayerName(player):
    playerName = input("\nPlease enter your name: ")

    while len(playerName) == 0 :
        print("\nYour Name should contain at least one letter ")
        playerName = input("\nPlease enter your name: ")

    player == True
    return player, playerName
    

def validatePlayerMove(moves):
    playerMove = input("\nMake your move: ").casefold()
    
    while len(playerMove) > 0:
        if playerMove not in moves:
            print("\nInvalid move. Please enter rock, paper, scissors")
            playerMove = input("\nMake your move: ").casefold()
        else: 
            return playerMove
        