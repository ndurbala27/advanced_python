def say_hello(name):
    """Takes name as a string and prints to screen"""
    print(f"Hello {name.title()}!")

while True:
    n = input("What is your name? ")
    say_hello(n)