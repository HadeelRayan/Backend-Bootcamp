import random


def compare_moves(your_move, opponent_move):
    if your_move == opponent_move:
        return "It's a tie"
    elif (your_move == 1 and opponent_move == 2) or (your_move == 2 and opponent_move == 3) or \
            (your_move == 3 and opponent_move == 4) or (your_move == 4 and opponent_move == 5) or \
            (your_move == 5 and opponent_move == 6) or (your_move == 6 and opponent_move == 1):
        return "You win"
    else:
        return "You lose"


def main():
    print("Choose your move:")
    print("1. The Jab")
    print("2. The Cross")
    print("3. The Lead Hook")
    print("4. The Rear Hook")
    print("5. The Lead Uppercut")
    print("6. The Rear Uppercut")

    your_move = int(input("Enter the number of your move: "))
    opponent_move = random.randint(1, 4)
    result = compare_moves(your_move, opponent_move)
    print("Result:", result)

