# Durbala, Nate CPT
# Exercise 7
# Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments.
# Call the function with the required information and two other name-value pairs,
# such as a color or an optional feature.
# Return the dictionary.
# Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)

def make_car(mfr, model, **kwargs):
    """Build a dictionary containing everything we know about a car"""
    car_info = {'manufacturer': mfr, 'model': model}

    if kwargs:
        for kw,arg in kwargs.items():
            car_info[kw] = arg

    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
truck = make_car('ram', '2500', color='white', turbo=True, owner='durbala')
car2 = make_car('toyata', 'carolla', wheels=2)

print(car)
print(truck)
print(car2)