import random

# Generar un numero aleatorio 

random_number = random.randint(1, 100)
print(random_number)

data = random.sample(range(1, 100), 10)
sum_data = sum(data)

relative_data = [x / sum_data for x in data]
print(relative_data)

# Elegir colores aleatorios
colors = ["red", "green", "blue", "yellow", "purple", "orange", "brown", "black", "white", "gray"]
random_color = random.choice(colors)

# Barajar una lista de cartas
cards = ["As", "Reina", "Rey", "Jota", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
random.shuffle(cards)
print(cards)