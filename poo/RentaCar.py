class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_rented = False

    def rent(self):
        if not self.is_rented:
            self.is_rented = True
            print(f"El coche {self.make} {self.model} {self.year} ha sido alquilado")
        else:
            print(f"El coche {self.make} {self.model} {self.year} no está disponible")
    
    def return_car(self):
        if self.is_rented:
            self.is_rented = False
            print(f"El coche {self.make} {self.model} {self.year} ha sido devuelto")
        else:
            print(f"El coche {self.make} {self.model} {self.year} no ha sido alquilado")

    def __str__(self):
        return f"Coche: {self.make} {self.model} {self.year}\nDisponible: {'Si' if not self.is_rented else 'No'}"


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.rented_cars = []
        
    def rent_car(self, car):
        if car.is_rented:
            print(f"El coche {car.make} {car.model} {car.year} no está disponible")
            return
        car.rent()
        self.rented_cars.append(car)
        print(f"El coche {car.make} {car.model} {car.year} ha sido alquilado a {self.name}")
    
    def return_car(self, car):
        if car in self.rented_cars:
            car.return_car()
            self.rented_cars.remove(car)

    def __str__(self):
        return f"Cliente: {self.name}\nID: {self.customer_id}\nCoches alquilados: {len(self.rented_cars)}"

class RentalSystem:
    def __init__(self):
        self.cars = []
        self.customers = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"El coche {car.make} {car.model} {car.year} ha sido agregado al sistema")

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado en el sistema")

    def show_available_cars(self):
        print("Coches disponibles:")
        for car in self.cars:
            if not car.is_rented:
                print(car)
            else:
                print(f"El coche {car.make} {car.model} {car.year} no está disponible")

    def show_rented_cars(self):
        print("Coches alquilados:")
        for customer in self.customers:
            if customer.rented_cars:
                print(customer)
            else:
                print(f"El cliente {customer.name} no tiene coches alquilados")

    def __str__(self):
        return f"Sistema de alquiler de coches: {len(self.cars)} coches y {len(self.customers)} clientes"
        

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Ford", "Mustang", 2021)
car3 = Car("Chevrolet", "Camaro", 2022)
car4 = Car("Audi", "A4", 2023)

customer1 = Customer("Cristian", 1)
customer2 = Customer("Antonio", 2)

rental_system = RentalSystem()

rental_system.add_car(car1)
rental_system.add_car(car2)
rental_system.add_car(car3)
rental_system.add_car(car4)

rental_system.register_customer(customer1)
rental_system.register_customer(customer2)
