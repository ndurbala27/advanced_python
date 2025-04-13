class Pizza:
    """a model of a pizza"""
    def __init__(self, size, *toppings):
        """the attributes of a pizza"""
        self.size = size
        self.toppings = list(toppings)
        self.shape = ""
        self.sauce = ""
        self.style = ""
        self.crust = ""
        self.slices = 0

    def __repr__(self):
        return f"{self.size} {self.toppings}"

    def __str__(self):
        dsc = f"Size: {self.size}"
        if self.toppings == " ":
            dsc += "\nToppings:"
            for topping in self.toppings:
                dsc += f"\n - {topping}"
        if self.style:
            dsc += f"\nStyle: {self.style}"
        if self.sauce:
            dsc += f"\nSauce: {self.sauce}"
        return dsc

    def get_size(self):
        return self.size

    def get_toppings(self):
        return self.toppings

    def get_sauce(self):
        return self.sauce

    def set_sauce(self, sauce):
        self.sauce = sauce

    def get_style(self):
        return self.style

    def set_style(self, style):
        self.style = style

    def add_topping(self, top):
        self.toppings.append(top)


if __name__ == '__main__':
    my_pizza = Pizza('large', 'ham', 'pineapple')
    print(my_pizza)