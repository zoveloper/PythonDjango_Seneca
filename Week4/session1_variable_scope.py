print("*****global Keyword*****")

scope = "global"
print(f"At File level : {scope}") # will produce “global”

def global_scope():
    print(f"At function level : {scope}") # will produce “global”

global_scope()







class ScopeClass:
    def method_scope(self):
        print(f"At Class level : {scope}")

instance = ScopeClass()
instance.method_scope() # will produce “global”







def change_global_var():
    global scope
    scope = scope + " is used in local" # Error
    #scope = "new variable, not reusing global"
    print(scope) 

change_global_var()
global_scope()



print("*****nonlocal Keyword*****")

new_scope = "global"

def outer_function():
   """We did not specify global before using new_scope, so new variable created with local scope"""
   new_scope = "outer" 

   def inner_function():
        nonlocal new_scope 
        new_scope = "inner"
        print(new_scope)

   print(new_scope) # will produce “outer”
   inner_function() # will produce “inner”
   print(new_scope) # will produce “inner”

outer_function()

print(new_scope) # will produce “global”