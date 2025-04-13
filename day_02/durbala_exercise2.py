# Durbala, Nate CPT
# Exercise 2
# Modify the make_shirt() function
# so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message,
# and a shirt of any size with a different message.

def make_shirt(size='large', msg='I love Python'):
    """Display the default size and the default message printed on the shirt."""
    print(f'\n My {size} shirt says: "{msg.upper()}."')

make_shirt()
make_shirt('medium')
make_shirt(msg="whales of mass destruction (wmd). atomic orcas: u.s. navy's newest weapon has a killer instinct", size='x-large')