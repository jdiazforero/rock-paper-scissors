from random import randint

options = ["Rock", "Paper", "Scissors"]
computer = options[randint(0,2)]
player = False

while player == False:
    player = raw_input("Choose\n"+"Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lost "+ computer+  " covers " + player)

        else:
            print("You win! "+ player+" smashes "+ computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lost "+ computer+ " cuts "+ player)
        else:
            print("You win! "+ player+" covers "+ computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lost "+computer+" smashes "+ player)
        else:
            print("You win! "+ player+ " cuts "+ computer)
    else:
        print("huh?")
    player = False
    computer = options[randint(0,2)]