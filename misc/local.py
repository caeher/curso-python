def local_function():
    x = 10 # Variable local
    print(x)

x = 20 # Variable global
print(x)
local_function()
print(x)