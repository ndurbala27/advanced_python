# Durbala, Nate CPT
# Exercise 1
# Write a function called make_shirt() that accepts a size and
# the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and
# the message printed on it.
# Call the function once using positional arguments to make a shirt
# Call the function a second time using keyword arguments.

def make_shirt(size, msg):
    """Display the size of the shirt and the message printed on the shirt"""
    print(f'\n My {size} shirt says: "{msg.upper()}."')

make_shirt('large', 'give me coffee or give me death')
make_shirt(msg='liability waivers excite me', size='x-large')
