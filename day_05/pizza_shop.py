from pizza import Pizza

def make_pizza(pizza: Pizza):

    tops = pizza.get_toppings()
    size = pizza.get_size()
    sauce = pizza.get_sauce()
    style = pizza.get_style()
    print(f"Making a {size} pizza with the following:")

    if sauce:
        print(f"Sauce: {sauce}")
    else:
        print(f"Sauce: tomato")

    if style:
        print(f"Style: {style}")
    else:
        print("Style: thin crust")

    if tops:
        print("Toppings: ")
        for top in tops:
            print(f" - {top}")
    else:
        print("Making a plain old boring cheese pizza")