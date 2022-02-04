
"If you are not sure of its initial value"
my_var = None


if my_var != None:
    print("Process the variable")
else:
    print("Abort or Re-Start the program based on req.")


try:
    var
except NameError:
    print("Var does not exist")

