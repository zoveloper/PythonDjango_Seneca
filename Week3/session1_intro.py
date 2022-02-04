class CarProperties:
    name = "Honda"
    model = "CR_V"
    colour = "Black"

""" Car1 => Mazda; Car2 => Ferrari"""

print("\n Object MyCar1's Properties")
my_car1 = CarProperties()

print(my_car1.name)
print(my_car1.model)

my_car1.name = "Mazda"
my_car1.model = "CX_5"

print(my_car1.name)
print(my_car1.model)

print("\n Class Car Properties ")
print(CarProperties.name)
print(CarProperties.model)

print("\n Object MyCar2's Properties")
my_car2 = CarProperties()

print(my_car2.name)
print(my_car2.model)

my_car2.name = "Ferrari"
my_car2.model = "GTO"

print(my_car2.name)
print(my_car2.model)

print("\n Class Car Properties ")
print(CarProperties.name)
print(CarProperties.model)


class CarMethods:
    name = "Honda"
    model = "CR_V"
    colour = "Black"

    def details(self):
        # print("\n {} Method Running ".format(self))
        print("\n")
        print("Make is {}, Model is {}, colour is {}".format(self.name, self.model,self.colour))
        # print("We used to join variables using + like this " + self.name)

my_car1 = CarMethods()

my_car1.details()

my_car1.name = "Mazda"
my_car1.model = "CX_5"

my_car1.details()

#CarMethods.details()

my_car2 = CarMethods()

#CarMethods.details()

my_car2.name = "Ferrari"
my_car2.model = "GTO"

my_car2.details()

CarMethods.details(my_car1)
CarMethods.details(my_car2)
CarMethods.details(CarMethods)