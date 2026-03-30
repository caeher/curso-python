x = 5 # Variable global

def modify_global():
    global x
    x = 10
    print(x)

print(x)
modify_global()
print(x)