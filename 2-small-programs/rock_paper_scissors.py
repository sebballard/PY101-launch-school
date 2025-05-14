import random

VALID_CHOICES = ["rock", "paper", "scissors", "spock", "lizard"]

WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'lizard':   ['paper',    'spock'],
    'spock':    ['rock',     'scissors'],
}


def prompt(message):
    print(f"==> {message}")

def check_substring_choice(choice_str):
    if len(choice_str) == 1 and (choice_str[0] == "s"):
        return False

    for valid_choice in VALID_CHOICES:
        if valid_choice.startswith(choice_str):
            return True

    return False


def give_full_choice(choice_str):
    for valid_choice in VALID_CHOICES:
        if valid_choice.startswith(choice_str):
            return valid_choice

    return None



def get_winner(user, computer):
    if computer in WINNING_COMBOS[user]:
        return "User"

    if user in WINNING_COMBOS[computer]:
        return "Computer"

    return None


def validate_best_of(input_str):
    input_str = input_str.strip()

    try:
        input_int = int(input_str)

    except ValueError:
        return False

    if input_int % 2 == 0 or input_int <= 0:
        return False

    return True

def get_num_best_of():
    prompt("Best of how many games do you want to play?")

    best_of_input = input()

    while not validate_best_of(best_of_input):
        prompt("Please enter an odd integer")
        best_of_input = input()

    return int(best_of_input)

def get_num_to_win(max_num_games):
    return (max_num_games // 2) + 1

def display_winner(winner_str):
    if not winner_str:
        prompt("It's a tie")
    else:
        prompt(f"{winner_str} wins!")

def update_scores(scores, winner_str):
    if winner_str == "User":
        scores["user"] += 1
    elif winner_str == "Computer":
        scores["comp"] += 1

def display_overall_winner(winner_str):
    if num_games_to_win == 1:
        prompt(f"{winner_str} is the winner!")
    else:
        prompt(f"{winner_str} is the match winner with" +
               f" {num_games_to_win} wins!")

num_best_of = get_num_best_of()
num_games_to_win = get_num_to_win(num_best_of)

scores_dict = {"user": 0, "comp": 0}

while ((scores_dict["user"] < num_games_to_win) and
       (scores_dict["comp"] < num_games_to_win)):

    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while not check_substring_choice(choice):
        prompt("That's not a valid choice")
        choice = input()

    choice = give_full_choice(choice)
    computer_choice = random.choice(VALID_CHOICES)

    prompt(f"You chose {choice}, computer chose {computer_choice}")
    winner = get_winner(choice, computer_choice)
    display_winner(winner)

    if winner:
        update_scores(scores_dict, winner)

    prompt(f"User: {scores_dict["user"]}")
    prompt(f"Computer: {scores_dict["comp"]}")

display_overall_winner(winner)