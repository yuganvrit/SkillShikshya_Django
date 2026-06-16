"""
Rock Paper Scissors Tournament
--------------------------------
Best-of-5 game against the computer.
Scores are tracked in a dictionary: {"player": 0, "computer": 0, "draws": 0}
The game ends when either side reaches 3 wins, or after 5 rounds total,
whichever comes first.
"""

import random

CHOICES = ["rock", "paper", "scissors"]
WINS_NEEDED = 3
MAX_ROUNDS = 5


def determine_winner(p1, p2):
    """
    Compare two choices and return:
      "player"   if p1 beats p2
      "computer" if p2 beats p1
      "draw"     if they match
    """
    if p1 == p2:
        return "draw"

    # Each choice beats exactly one other choice
    beats = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    if beats[p1] == p2:
        return "player"
    else:
        return "computer"


def get_player_choice():
    """Ask the player for rock/paper/scissors, validating input."""
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in CHOICES:
            return choice
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")


def display_score(scores, round_num):
    """Print the current round number and running score."""
    print(f"\n--- Score after round {round_num} ---")
    print(f"Player: {scores['player']}  |  Computer: {scores['computer']}  |  Draws: {scores['draws']}")
    print("------------------------------------\n")


def play_round(scores, round_num):
    """Play a single round, update scores, and show the result."""
    player_choice = get_player_choice()
    computer_choice = random.choice(CHOICES)

    print(f"\nRound {round_num}: You chose {player_choice}, computer chose {computer_choice}.")

    result = determine_winner(player_choice, computer_choice)

    if result == "draw":
        print("It's a draw!")
        scores["draws"] += 1
    elif result == "player":
        print("You win this round!")
        scores["player"] += 1
    else:
        print("Computer wins this round!")
        scores["computer"] += 1

    display_score(scores, round_num)


def main():
    print("=== Rock Paper Scissors Tournament ===")
    print(f"First to {WINS_NEEDED} wins, or best score after {MAX_ROUNDS} rounds, takes the match!\n")

    scores = {"player": 0, "computer": 0, "draws": 0}
    round_num = 0

    while round_num < MAX_ROUNDS:
        round_num += 1
        play_round(scores, round_num)

        # Check if either side has already clinched the match
        if scores["player"] == WINS_NEEDED or scores["computer"] == WINS_NEEDED:
            break

    # Declare the overall winner
    print("=== Tournament Over ===")
    print(f"Final Score -> Player: {scores['player']}  |  Computer: {scores['computer']}  |  Draws: {scores['draws']}")

    if scores["player"] > scores["computer"]:
        print("🏆 You win the tournament!")
    elif scores["computer"] > scores["player"]:
        print("🏆 Computer wins the tournament!")
    else:
        print("🤝 The tournament ends in a tie!")


if __name__ == "__main__":
    main()
