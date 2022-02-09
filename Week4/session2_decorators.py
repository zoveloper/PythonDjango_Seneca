
print("\n****Simple Decorators****\n")

def my_decorator(some_function):
    def wrapper():
        print("Code before function.")
        some_function()
        print("Code after function.")
    return wrapper

def my_parameter():
    print("I’m the parameter!")

my_parameter = my_decorator(my_parameter)

my_parameter() 



@my_decorator # Just simple form of "my_param2 = my_decorator(my_param2)""
def my_param2():
    print("I am Parameter using decorator")

my_param2()


print("\n****Commonly used Decorators in Class****\n")

print("\n****@Property****\n")
from decorators_eg import my_property

decorators = my_property()

print(decorators.my_data)

decorators.my_data = 5

decorators.my_data = 150

try:
    print(decorators.my_data)
except:
    print("my_data got deleted")

del decorators.my_data

try:
    print(decorators.my_data)
except:
    print("my_data got deleted")


print("\n****Class methods and Static methods ****\n")
from car import Car

Car.wait_in_seconds(5)
Car.time_elapsed()

mazda_car = Car("Mazda", "CX5", "Red")
mazda_car.details()
mazda_car.feel_colour()
mazda_car.start_engine()
mazda_car.steering_system()

mazda_car.time_elapsed()
mazda_car.wait_in_seconds(2)
mazda_car.time_elapsed()





# Article to refer for more details https://realpython.com/primer-on-python-decorators/