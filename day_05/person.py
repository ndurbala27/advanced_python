class Person():
    """A model of a person"""
    def __init__(self, f_name, l_name, age):
        """The attributes of a person"""
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.height = 0
        self.weight = 0

    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.age}"

    # def __str__(self):
    #     return (f"First name: {self.first_name}\n"
    #     f"Last name: {self.last_name}\n"
    #     f"Age: {self.age}\n"
    #             )