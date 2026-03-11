class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehículo {self.brand} {self.model} ha sido vendido")
        else:
            print(f"El vehículo {self.brand} {self.model} no está disponible")

    def check_availability(self):
        return self.is_available

    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por las clases hijas")

    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por las clases hijas")

    def __str__(self):
        return f"Vehículo: {self.brand} {self.model}\nPrecio: {self.price}\nDisponible: {'Si' if self.is_available else 'No'}"


class Car(Vehicle):
    def __init__(self, brand, model, price, num_doors):
        super().__init__(brand, model, price)
        self.num_doors = num_doors

    def start_engine(self):
        if self.is_available:
            print(f"El motor del coche {self.brand} {self.model} ha sido encendido")
        else:
            print(f"El coche {self.brand} {self.model} no está disponible")

    def stop_engine(self):
        if self.is_available:
            print(f"El motor del coche {self.brand} {self.model} ha sido apagado")
        else:
            print(f"El coche {self.brand} {self.model} no está disponible")

    def __str__(self):
        return f"Coche: {self.brand} {self.model}\nPrecio: {self.price}\nDisponible: {'Si' if self.is_available else 'No'}\nNúmero de puertas: {self.num_doors}"


class Bike(Vehicle):
    def __init__(self, brand, model, price, num_gears):
        super().__init__(brand, model, price)
        self.num_gears = num_gears

    def start_engine(self):
        if self.is_available:
            print(f"El motor de la bicicleta {self.brand} {self.model} ha sido encendido")
        else:
            print(f"La bicicleta {self.brand} {self.model} no está disponible")

    def stop_engine(self):
        if self.is_available:
            print(f"El motor de la bicicleta {self.brand} {self.model} ha sido apagado")
        else:
            print(f"La bicicleta {self.brand} {self.model} no está disponible")

    def __str__(self):
        return f"Bicicleta: {self.brand} {self.model}\nPrecio: {self.price}\nDisponible: {'Si' if self.is_available else 'No'}\nNúmero de cambios: {self.num_gears}"

class Truck(Vehicle):
    def __init__(self, brand, model, price, num_wheels):
        super().__init__(brand, model, price)
        self.num_wheels = num_wheels

    def start_engine(self):
        if self.is_available:
            print(f"El motor del camión {self.brand} {self.model} ha sido encendido")
        else:
            print(f"El camión {self.brand} {self.model} no está disponible")

    def stop_engine(self):
        if self.is_available:
            print(f"El motor del camión {self.brand} {self.model} ha sido apagado")
        else:
            print(f"El camión {self.brand} {self.model} no está disponible")

    def __str__(self):
        return f"Camión: {self.brand} {self.model}\nPrecio: {self.price}\nDisponible: {'Si' if self.is_available else 'No'}\nNúmero de ruedas: {self.num_wheels}"


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle):
        if vehicle.is_available:
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
            print(f"El vehículo {vehicle.brand} {vehicle.model} ha sido comprado por {self.name}")
        else:
            print(f"El vehículo {vehicle.brand} {vehicle.model} no está disponible")

    def inquire_vehicle(self, vehicle):
        if vehicle.is_available:
            print(f"El vehículo {vehicle.brand} {vehicle.model} está disponible")
        else:
            print(f"El vehículo {vehicle.brand} {vehicle.model} no está disponible")

class Dealership:

    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicle(self, vehicle):
        self.inventory.append(vehicle)
        print(f"El vehículo {vehicle.brand} {vehicle.model} ha sido agregado a la dealership")

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado en la dealership")
    
    def show_available_vehicles(self):
        print("Vehículos disponibles:")
        for vehicle in self.inventory:
            if vehicle.is_available:
                print(vehicle)
            else:
                print(f"El vehículo {vehicle.brand} {vehicle.model} no está disponible")
    def show_sold_vehicles(self):
        print("Vehículos vendidos:")
        for customer in self.customers:
            if customer.purchased_vehicles:
                print(customer)
            else:
                print(f"El cliente {customer.name} no ha comprado ningún vehículo")
    
    def __str__(self):
        return f"Dealership: {len(self.inventory)} vehículos y {len(self.customers)} clientes"



car1 = Car("Toyota", "Corolla", 2020, 4)
bike1 = Bike("Honda", "CBR", 10000, 6)
truck1 = Truck("Ford", "F-150", 30000, 4)

customer1 = Customer("Cristian")
customer2 = Customer("Antonio")

dealership = Dealership()

dealership.add_vehicle(car1)
dealership.add_vehicle(bike1)
dealership.add_vehicle(truck1)

dealership.register_customer(customer1)
dealership.register_customer(customer2)