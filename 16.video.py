numbers = [1, 2, 3, 4, 5, 6]

for i in numbers:
    print("Aquí i es igual a: ", i+1)


for i in range(10):
    print(i)

for i in range(3, 10):
    print(i)

fruits = ["apple", "Peach", "Grape", "Orange", "Tomato"]

for fruit in fruits:
    print("Value in fruit: ", fruit)
    if fruit == "Orange":
        print("Orange found")
    else:
        print("Orange not found")


x = 0;
while x < 10:
    print("Value in x: ", x)
    if x == 3:
        break

    x += 1

print("Fuera del programa")

