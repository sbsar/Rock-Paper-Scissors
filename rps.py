import random


def get_choice():
    options = ["rock", "paper", "scissors"]
    while True:
        player_choice = input("Enter a choice between rock | paper | scissors >>> ").lower()
        if player_choice in options:
            break
        else:
            print("Wrong choice")
    # options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print("You chose " + player + " Computer chose " + computer)
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "paper":
            return "Computer wins"
        else:
            return "Player wins"
    elif player == "scissors":
        if computer == "paper":
            return "Player wins"
        else:
            return "Computer wins"
    elif player == "paper":
        if computer == "rock":
            return "Player wins"
        else:
            return "Computer wins"


def game():
    while True:
        choices = get_choice()
        player = choices["player"]
        computer = choices["computer"]
        print(check_win(player, computer))
        game_on = input("Do you want to play again ? >>> ").lower()
        if game_on == 'q':
            break




game()
print("Thanks for playing")
