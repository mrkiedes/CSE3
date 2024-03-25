class Dog:
    # Attributes
    fur = True
    legs = 4
    fur_color = "brown"

    # Constructor - Setup every variable
    def __init__(self, fur, num_of_legs, fur_color):
        self.fur = fur
        self.legs = num_of_legs
        self.fur_color = fur_color

    def __str__(self):
        return ("fur: " + str(self.fur) + " legs: " + str(self.legs) +
                " fur color: " + self.fur_color)




