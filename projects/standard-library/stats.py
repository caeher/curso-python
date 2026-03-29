import statistics
import csv 

# Leer el archivo de ventas mensuales
monthly_sales = {}
with open('monthly_sales.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)

# Hallar la media
mean_sales = statistics.mean(sales)
print(f"Media de las ventas: {mean_sales}")

# Halla la moda
mode_sales = statistics.mode(sales)
print(f"Moda de las ventas: {mode_sales}")

# Hallas la desviacion estandar
std_sales = statistics.stdev(sales)
print(f"Desviacion estandar de las ventas: {std_sales}")

# Hallas la varianza
var_sales = statistics.variance(sales)
print(f"Varianza de las ventas: {var_sales}")

# Hallas el rango
range_sales = statistics.stdev(sales)
print(f"Rango de las ventas: {range_sales}")
