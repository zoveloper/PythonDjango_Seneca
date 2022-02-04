import os
from car import Car

cwd = os.getcwd()
print(cwd)

dir_path = os.path.dirname(__file__)
print(dir_path)

os.chdir(dir_path)
cwd = os.getcwd()
print(cwd)

mazda_car = Car("Mazda", "CX_5", "Blue")
mazda_car.details()
mazda_car.feel_colour()
mazda_car.start_engine()
mazda_car.steering_system()

ferrari_car = Car("Ferrari", "GTO", "Red")
ferrari_car.details()
ferrari_car.feel_colour()
ferrari_car.start_engine()
ferrari_car.steering_system()

Toyoto_car = Car("Toyoto", "Camry", "White")
Toyoto_car.details()
Toyoto_car.feel_colour()
Toyoto_car.start_engine()
Toyoto_car.steering_system()
