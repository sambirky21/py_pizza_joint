# Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.

# Add a method for interacting with a pizza's toppings, called add_topping.

# Add a method for outputting a description of the pizza (sample output below).

# Make two different instances of a pizza. If you have properly defined the class, you should be able to do something like the following code with your Pizza type.

class Pizza:

    def __init__(self):
        self.size = 0
        self.style = ""
        self.crust = ""
        self.toppings = []
        self.no_topping= False

    def add_topping(self, toppings):
        # self.no_topping = True
        self.toppings.append(toppings)
        # print(f'Your pizza has f"{self.toppings}" on it.')

    def print_order(self, size, style, crust, toppings):
        topping_str = ', '.join(self.toppings)
        print(f'Your {self.size} {self.style} with {topping_str} and a {self.crust} crust is ordered.')

meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "Deep dish"
meat_lovers.crust = "thin"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order(16, "neopolitan", "thin", "pepperoni")