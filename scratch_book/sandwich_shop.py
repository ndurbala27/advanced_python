menu = ['ham', 'pastrami', 'blt', 'tuna']
orders = []
done = []
pastrami = True

print(f"{'MENU':#^24}")
for item in menu:
	print(f" - {item.title()}")

while len(orders) < 7:
	order = input("Whaddaya want? ")
	if order == 'pastrami' and pastrami:
		orders.append(order)
		pastrami = False
	elif order == 'pastrami':
		print("We are out of pastrami")
	elif order in menu:
		orders.append(order)
		print("Next!")
	else:
		print("We don't have that")

while orders:
	sammy = orders.pop(0)
	print(f"Making a {sammy} sandwich.")
	done.append(sammy)
