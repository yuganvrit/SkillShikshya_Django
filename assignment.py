# # import random

# # def play_game():
# #     secret_number = random.randint(1, 100)
# #     counter = 0
# #     guess_list = []

# #     while counter < 7:
# #         user_input = int(input("Enter a number: "))

# #         if user_input > secret_number:
# #             guess_list.append(user_input)
# #             print("Too high")
# #             counter += 1

# #         elif user_input < secret_number:
# #             guess_list.append(user_input)
# #             print("Too low")
# #             counter += 1

# #         else:
# #             guess_list.append(user_input)
# #             print(f"You guessed the correct number: {user_input}")
# #             break

# #     return guess_list

# # print(play_game())


# ##2 

# def analyze_text(text):
    
#     # 1. Total word count (using split() only)
#     raw_words = text.split()
#     words = []
#     for word in raw_words:
#         if word != "":
#             words.append(word)
#     total_word_count = len(words)
    
#     # 2. Total character count (excluding spaces)
#     total_character_count = 0
#     for char in text:
#         if char != " " and char != "\t" and char != "\n":
#             total_character_count += 1
    
#     # 3. Most frequent word (dictionary counting)
#     word_counts = {}
#     for word in words:
#         # Clean punctuation manually (no strip())
#         clean_word = ""
#         for char in word.lower():
#             if char not in ".,!?;:'\"-()":
#                 clean_word += char
        
#         if clean_word != "":
#             if clean_word in word_counts:
#                 word_counts[clean_word] += 1
#             else:
#                 word_counts[clean_word] = 1
    
#     # Find the most frequent word
#     most_frequent_word = None
#     max_count = 0
#     for word, count in word_counts.items():
#         if count > max_count:
#             max_count = count
#             most_frequent_word = word
    
#     # 4. Number of sentences (split by ., !, ?)
#     number_of_sentences = 0
#     for char in text:
#         if char in ['.', '!', '?']:
#             number_of_sentences += 1
    
#     # Handle empty text edge case (no strip())
#     is_empty = True
#     for char in text:
#         if char != " " and char != "\t" and char != "\n":
#             is_empty = False
#             break
#     if is_empty:
#         number_of_sentences = 0
    
#     return {
#         'total_word_count': total_word_count,
#         'total_character_count': total_character_count,
#         'most_frequent_word': most_frequent_word,
#         'number_of_sentences': number_of_sentences
#     }


##Rock, Paper and Scissor
import random

# Function to determine the winner of a round
def determine_winner(player, computer):
    
    if player == computer:
        return "draw"

    if (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        return "player"

    return "computer"


# Score dictionary
scores = {
    "player": 0,
    "computer": 0,
    "draws": 0
}

choices = ["rock", "paper", "scissors"]

round_num = 1

while round_num <= 5 and scores["player"] < 3 and scores["computer"] < 3:

    print(f"\n--- Round {round_num} ---")

    player_choice = input("Enter rock, paper, or scissors: ").lower()

    if player_choice not in choices:
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(choices)

    print("Computer chose:", computer_choice)

    result = determine_winner(player_choice, computer_choice)

    # Update scores
    scores[result] += 1

    # Display round result
    if result == "draw":
        print("It's a draw!")
    elif result == "player":
        print("You win this round!")
    else:
        print("Computer wins this round!")

    # Running score
    print("\nCurrent Score:")
    print(f"Player   : {scores['player']}")
    print(f"Computer : {scores['computer']}")
    print(f"Draws    : {scores['draws']}")

    round_num += 1


# Final result
print("\n===== FINAL RESULT =====")

if scores["player"] > scores["computer"]:
    print(" You are the overall winner!")
elif scores["computer"] > scores["player"]:
    print("Computer is the overall winner!")
else:
    print("The game ended in a tie!")

print("\nFinal Scores:")
print(scores)