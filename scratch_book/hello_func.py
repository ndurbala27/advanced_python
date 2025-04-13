# def hello_world():
	# """
	# print 'hello world'
	# """
	
	# print("Hello, World")

# hello_world()


# def greet_user(first='world', last=''): 
	# """	First name is default to 'world',
		# and last name as optional string
		# and Display a personalized greeting."""
	# if last:
		# print(f"Hello, {first.title()} {last.title()}!")
	# else:
		# print(f"Hello, {first.title()}!")
	

# greet_user('nate', 'durbala')
# greet_user('jesse', 'james')
# greet_user('bob')
# greet_user()
# greet_user(last='wick', first='john')
# greet_user(last='people')

def add_numbers(x : int, y : int) -> int: 
	"""Takes x as int and y as int, and return the sum as int."""
	#if (type(x) == int) and (type(y) == int):
	if isinstance(x, int) and isinstance(y, int):
		return x + y
	print("Error")
	
	
added = add_numbers(4, 5)
if added: 
	print(added)
