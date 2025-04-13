from random import randint

print("Welcome!")
print("Guess a number from 1 to 100")

def get_guess():
    while True:
        try:
            valid_guess = int(input("Guess: "))
        except ValueError:
            print("Invalid")
        else:
            if 1 <= valid_guess <= 100:
                return valid_guess
            else:
                print("1-100")

def compare(g, r):
    if g < r:
        print("Too low")
        return True

    if g > r:
        print("Too high")
        return True

    if g == r:
        print("Winner")
        return False

def play_again():
    while True:
        again = input("Play again? [y or n]")
        match again:
            case 'y':
                return True
            case 'n':
                return False
            case _:
                print("y or n")

session = True
while session:
    game = True
    score = 0
    rando = randint(1, 100)
    while game:
        guess = get_guess()
        score += 1
        game = compare(guess, rando)
    print(f"Score {score}")
    session = play_again()
print("Goodbye")