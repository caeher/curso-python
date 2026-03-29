import csv

# Leer un archivo csv
"""
with open('products.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
"""

with open('products.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Product: {row['name']}, Price: {row['price']}")


new_product = {
    'name': 'Smartphone',
    'price': 599.99,
    'quantity': 120,
    'category': 'Electronics'
}

with open('products.csv', 'a') as file:
    csv_writer = csv.DictWriter(file, fieldnames=['name', 'price', 'quantity', 'category'])
    csv_writer.writerow(new_product)


file_path = 'products.csv'
updated_file_path = 'products_updated.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    #Obtener lo snombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ['total_value']

    with open(updated_file_path, mode='w') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for row in csv_reader:
            row['total_value'] = float(row['price']) * float(row['quantity'])
            csv_writer.writerow(row)