from os.path import split

from pizza import Pizza
from pizza_shop import make_pizza

# my_pizza = Pizza('lage', 'ham', 'pineapple', 'bacon', 'bbq sauce')
# your_pizza = Pizza('x-large', 'spam', 'eggs', 'bacon bits')
# your_pizza.set_sauce('gravy')
# your_pizza.set_style('breakfast')
# print(f"Your pizza is:\n{your_pizza}")
# print(f"Your current order:\n{my_pizza}")
# my_pizza.set_style('chicago')
# my_pizza.set_sauce('marinara')
# print(f"Updated order: {my_pizza}")
# print(f"\nOrdering Pizza")
# make_pizza(my_pizza)


print("Order a pizza")
size = input("What size? ")
top = input("Toppings (enter for none): ")
your_pizza = Pizza(size, top)

if top:
    while True:
        ans = input("Another topping? (or q for quit): ")
        if ans != 'q':
            your_pizza.add_topping(ans)
        else:
            break

sauce = input("Sauce: ")
style = input("Style: ")

print(your_pizza)
