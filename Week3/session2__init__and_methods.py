class Car:
    def __init__(self, name, model, colour):
        self.name = name
        self.model = model
        self.colour = colour

    def details(self):
        print(f"\n Make is {self.name}, Model is {self.model}, colour is {self.colour}")
    
    def feel_colour(self):
        """ https://stackabuse.com/how-to-print-colored-text-in-python/
        \x1b[- Escape code, always the same 
        1 - Text style, 0 for normal, 1 for Bold (Note, Class material has typo error saying 1 for normal)
        34 - Text colour, 34 is blue
        40m - Background colour, 40 is black"""
        if self.colour == "Blue":
            print("\x1b[0;34;40m " + self.name + " Car Ordered in Colour "+ self.colour + "!" + "\x1b[0m")
        elif self.colour == "Red":
            print("\x1b[1;31;40m " + self.name + " Car Ordered in Colour "+ self.colour + "!" + "\x1b[0m")


mazda_car = Car("Mazda", "CX_5", "Blue")
mazda_car.details()
mazda_car.feel_colour()

ferrari_car = Car("Ferrari", "GTO", "Red")
ferrari_car.details()
ferrari_car.feel_colour()
