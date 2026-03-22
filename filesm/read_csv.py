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
