import random

option = ['rock', 'paper', 'scissor', 'Rock', 'Paper', 'Scissor']
computer = option[random.randint(0, 2)]


# Function for player to play using options
def plays():
    playerWin = 0
    computerWin = 0
    ties = 0
    player = True

    while player == True:
        player = input("\nEnter your choice (Rock - Paper - Scissor): ")
        if player == computer:
            print("Computer's Choice: ", computer)
            print("Tie!")
            ties += 1
        elif player == 'Rock' or player == 'rock':
            if computer == 'Paper' or computer == 'paper':
                print("Computer's Choice: ",computer)
                print("Computer wins!")  # R+P=P
                computerWin += 1
            else:
                print("Computer's Choice: ", computer)
                print(playerName, "Wins!")  # P+R=P
                playerWin += 1

        elif player == 'Paper' or player == 'paper':
            if computer == 'Scissor' or computer == 'scissor':
                print("Computer's Choice: ", computer)
                print("Computer wins!")  # P+S=S
                computerWin += 1
            else:
                print("Computer's Choice: ", computer)
                print(playerName, "Wins!")  # S+P=S
                playerWin += 1

        elif player == 'Scissor' or player == 'scissor':
            if computer == 'Rock' or computer == 'rock':
                print("Computer's Choice: ", computer)
                print("Computer wins!")  # S+R=R
                computerWin += 1
            else:
                print("Computer's Choice: ", computer)
                print(playerName, "Wins!")  # R+S=R
                playerWin += 1

        else:
            print("Oops! Please enter a valid input")
        player = True
        print("\n******************Score********************")
        print(playerName, "\t\t", "Ties", "\t\t", "Computer")
        print(playerWin, "\t\t\t", ties, "\t\t\t", computerWin)
        print("******************************************")

        ans=input("\nDo you want to continue (y/n)? ")
        if ans =='n' or ans =='N':
            break

print("                         ROCK - PAPER - SCISSOR")
print("                         ======================")
print('''Rules:
          * Rock + Paper = Paper
          * Paper + Scissor = Scissor
          * Scissor + Rock = Rock''')
playerName = input("\nPlease enter your Name: ")
plays()