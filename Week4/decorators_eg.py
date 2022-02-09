class my_property:
    
    def __init__(self):
        self._data = None

    @property
    def my_data(self):
        return self._data

    @my_data.setter
    def my_data(self, value):
        if value < 100:
            self._data = value
            print("Good data")
        else:
            print("Bad Data. Enter value less than 100")


    @my_data.deleter
    def my_data(self):
        print("Backed up the data before deleting")
        del self._data