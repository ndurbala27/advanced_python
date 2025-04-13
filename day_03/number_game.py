# Durbala, Nate CPT
# a simple number guessing game
# Mar-27-2025

import random

# Set the range of numbers for game session. LOWER_BOUND must be >= 1
LOWER_BOUND, UPPER_BOUND = 1, 10

# 1. Greet the user with a message and instructions, and 3. provide the range to the user
print(f"Welcome!\nI'm thinking of a number between {LOWER_BOUND} and {UPPER_BOUND}!")

# 2. Generate a random number
random_number = random.randint(LOWER_BOUND, UPPER_BOUND)

def guess_number():
    """Prompt the user for a guess, try to convert input to an integer for validation,
    check if the input is within range, and then return that value"""

    while True:
        try:
            # 4. Prompt the user for a guess
            number = int(input("\nTake a guess: "))
            # 5. Validate user input. Don't accept anything other than integers
            # Don’t accept anything outside of the range.
            if LOWER_BOUND <= number <= UPPER_BOUND:
                return number
            else:
                print(f"\nOutside of range [{LOWER_BOUND}, {UPPER_BOUND}]!")
        except ValueError:
            print("\nThat's not a number [1, 2, 3 . . .]!")
            # Skip to the next iteration if input is not a valid integer
            continue


def check_match(guessed_num, rand_num):
    """take the user's guessed number as guessed_num and the random generated number as rand_num,
    check if they are equal, return 'correct' as a True boolean value"""

    # Initialize score outside the loop
    score = 100

    while True:
        try:
            # 6. Inform the user if the number is too high, too low or correct.
            if guessed_num < rand_num:
                score -= 5
                guessed_num = int(input(f"\nToo low!\nGuess again [{LOWER_BOUND}, {UPPER_BOUND}]: "))
            elif guessed_num > rand_num:
                score -= 5
                guessed_num = int(input(f"\nToo high!\nGuess again [{LOWER_BOUND}, {UPPER_BOUND}]: "))
            else:
                return {'correct': True, 'score': score}
        except ValueError:
            guessed_num = int(input("\nThat's not a valid number! Please enter an integer: "))
            # Skip to the next iteration if input is not a valid integer
            continue

def play_again():
    """The check_match function return a True match. Prompt the user if they want to play again.
    If the user wants to play again, return a new randomly generated number within the same range as initiated"""

    while True:
        # 8. Give the user the option to start a new game or quit.
        response = input("\nWould you like to play again? (yes/no): ").strip().lower()
        # 9. If the user opts to continue, generate a new random number.
        if response in ('yes', 'y'):
            new_rand_num = random.randint(LOWER_BOUND, UPPER_BOUND)
        elif response in ('no', 'n'):
            new_rand_num = 0
        else:
            print("Enter 'yes', 'y', 'no', or 'n'.")
            continue

        return new_rand_num




while random_number:
    results = check_match(guess_number(), random_number)
    if results['correct']:
        # 7. If the guess is correct, give the user a score.
        print(f"\nYou got it! Your final score is, {results['score']} points")
        # 8. Give the user the option to start a new game or quit.
        random_number = play_again()

# 10. If the user quits, display a 'goodbye' message.
print("\nThanks for playing! Goodbye!\n")