steering = {"Mazda": "GVC Steering", "Ferrari": "EPS Steering", "Honda": "EPA Rack&Pinion Steering"}
engine = {"Mazda": "SKYACTIV Engine", "Ferrari": "F136 Engine", "Honda": "VTEC Turbo Engine"}


class Car:
    def __init__(self, name="Honda", model="CR_V", colour="Black"):
        """Here we initialize the Car Properties"""
        self.name = name
        self.model = model
        self.colour = colour

    def details(self):
        """This function gives us the details of car object being used"""
        print(f"\nMake is {self.name}, Model is {self.model}, colour is {self.colour}")
    
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
        else:
            print("Colour not supported yet")
    
    def steering_system(self):
        """Steering system of the respective Car make is loaded"""
        try:
            print(f"Loading {steering[self.name]} system")
        except:
            print("Maker not supported in Steering section yet")

    def start_engine(self):
        """Starting the engine of the respective Car maker"""
        try:
            print(f"Start {engine[self.name]}")
        except:
            print("Maker not supported in Engine section yet")
