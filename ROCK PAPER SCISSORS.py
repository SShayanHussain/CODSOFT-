import random
def help():
    print("----RULES----")
    print('''1. IF CHOICES ARE SAME THEN GAME IS TIED AND BOTH GOT A SCORE OF 5.
2. ONLY CHOOSE FROM ROCK,PAPER AND SCISSORS.
3. IF PLAYER WINS HE WILL GET A SCORE OF 10 AND COMPUTER GET A MINUS OF SCORE 2 AND VICE VERSA.
4. THANKS FOR READING. PLAY GAME''')



def rps():
    options = ('rock','paper','scissors')
    player = input("CHOOSE (rock,paper,scissors): ")
    comp=random.choice(options)
    print("YOUR CHOICE: ", player)
    print("COMPUTER'S CHOICE: ", comp)

    if player == comp:
        print("GAME TIED")

    elif player == 'rock' and comp == 'paper':
        print("COMPUTER WINS")

    elif player == 'rock' and comp == 'scissors':
        print("YOU WIN")

    elif player == 'paper' and comp == 'rock':
        print("YOU WIN")

    elif player == 'paper' and comp == 'scissors':
        print("COMPUTER WINS")

    elif player == 'scissors' and comp == 'rock':
        print("COMPUTER WINS")

    elif player == 'scissors' and comp == 'paper':
        print("YOU WIN")


    user=input("DO YOU WANT TO PLAY AGAIN? (y/n): ")
    if user == 'y' or user == 'Y':
        rps()
    else:
        print("THANKS FOR PLAYING. EXITING.....")

def main():
    print("1. PLAY")
    print("2. HELP")
    print("3. EXIT")
    choice = int(input("ENTER CHOICE: "))

    if choice == 1:
        rps()
    elif choice == 2:
        help()
    else:
        print("THANKS FOR PLAYING. EXITING.....")

if __name__=="__main__":
    main()
