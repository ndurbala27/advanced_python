# 1. create a list of at least four names.
names = ['nate', 'amy', 'ethan', 'elliott']

# copy the list to a new list
new_list = names[:]

# remove two names from the original list and add two names to the new list
names.remove('nate')
names.remove('amy')
new_list.append('ricky')
new_list.append('bobby')

# write for loops that will rint every name in the lists
for name in names:
    print(name)

for new in new_list:
    print(new)


# 2. create a block of code that prompts the user for a first name, last name, and middle initial.
first = input('First name: ')
last = input('Last name: ')
middle = input('Middle initial: ')

# store the information in a dictionary
names = {
    'First name' : first,
    'Last name' : last,
    'Middle initial' : middle
}

# print the dictionary to the screen
print(f"\n{names}\n")

# print the keys and values to the screen.
# use formatting to present the information in an organized manner.
for k, v in names.items():
    print(f"{k:>15} : {v.title()}")


# 3. create a list of answers in the style of a "Magic 8 Ball"
ball_answers = ["Yes", "No", "Maybe", "Don't count on it!"]

# prompt the user for a question
question = input("Ask the 'Magic 8 Ball' a question: ")

# display a random answer from the list
import random
print(random.choice(ball_answers))


# 4. Create a block of code that prompts the user for thier first name and 
# then prompts again for the their last name
first = input("First name: ")
last = input("Last name: ")

# write the full name to the file named 'output.txt'
filename = "output.txt"
with open(filename, 'w') as f:
    f.write(f"{first.title()} {last.title()}")
