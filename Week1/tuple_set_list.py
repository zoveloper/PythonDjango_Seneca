""" Please Note: Here, I am using methods (functions) [eg. mylist.append()] to add or remove items in DataTypes.
    Do not worry about that now, we will go in detail about that in Classes topic """

# List Mutable (existing item can be changed/removed, new item can be added)
# Can have duplicate data
# Ordered (refer data printed with the same order as defined)
my_list = ["List", 11,22,33,44, False, "List"] # Different Datatypes allowed
print(my_list)
# List members can be changed with assignment
my_list[0] = 111
print(my_list)
# New item added and need not be unique
my_list.append(22)
print(my_list)
# Existing item can be removed
my_list.pop(3) # with index number
print(my_list)
 
# Tuple Immutable (no change is allowed)
# Can have duplicate data
# Ordered (refer data printed with the same order as defined)
my_tuple = ("Tuple", True, 5,6,7,8, "Tuple")  # Different Datatypes allowed
print(my_tuple)
# Below line, you should see error when you run by removing "#" (comment)
# my_tuple[0] = 111

# Set Mutable (Can add/remove item, but cannot change the item)
# Cannot have duplicate data
# Unordered (reder the ouput from print - you shoulkd see data in random places)
my_set = {"Set", 11,22,33,"Set", "old"} # Different Datatypes allowed
print(my_set) # Cannot hold duplicate value - you should see only one "Set"
# Below line, you should see error when you run by removing "#" (comment)
# my_set[0] = 111 
my_set.add("new")
print(my_set)
my_set.remove("old") # with item directly, not with index like List
print(my_set)
