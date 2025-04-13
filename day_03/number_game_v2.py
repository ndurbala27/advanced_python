# Durbala, Nate CPT
# A simple number guessing game
# Mar-27-2025

import random

# Constants for the game range. Using UPPERCASE for constants is a PEP 8 convention.
LOWER_BOUND, UPPER_BOUND = 1, 10

def guess_number():
    """Prompts the user for a guess and validates the input."""

    while True:
        try:
            num = int(input("Take a guess: "))
            if LOWER_BOUND <= num <= UPPER_BOUND:
                return num
            else:
                print(f"\nOutside of range [{LOWER_BOUND}, {UPPER_BOUND}]!")
        except ValueError:
            print("\nThat's not a valid number! Please enter an integer: ")


def check_match(guessed_num, rand_num):
    """Checks the user's guess against the random number and update the score."""

    # Initialize score outside the loop
    score = 100

    while True:
        try:
            guessed_num = int(guessed_num)
        except ValueError:
            guessed_num = input("\nThat's not a valid number! Please enter an integer.")
            # Skip to the next iteration if input is not a valid integer
            continue

        if guessed_num < rand_num:
            score -= 5
            print("\nToo low!")
            guessed_num = input(f"Guess again [{LOWER_BOUND}, {UPPER_BOUND}]: ")
        elif guessed_num > rand_num:
            score -= 5
            print("\nToo high!")
            guessed_num = input(f"Guess again [{LOWER_BOUND}, {UPPER_BOUND}]: ")
        else:
            return {'correct': True, 'score': score}



def play_again():
    """Asks the user if they want to play again and generates a new random number if so."""

    response = input("\nThat's it! Would you like to play again? (yes/no): ").lower()
    if response == 'yes':
        return random.randint(LOWER_BOUND, UPPER_BOUND)
    else:
        # No need for an 'elif' here, any non-"yes" is considered "no".
        # Returning 0 signals the end of the game.
        return 0

# Main game loop
print(f"Welcome!\nI'm thinking of a number between {LOWER_BOUND} and {UPPER_BOUND}!")

random_number = random.randint(LOWER_BOUND, UPPER_BOUND)
# Remove for the actual game
#print(random_number)

while random_number:
    results = check_match(guess_number(), random_number)
    if results['correct']:
        print(f"Your final score is {results['score']} points")
        random_number = play_again()

print("Thanks for playing!")