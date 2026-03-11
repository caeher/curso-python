class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no está disponible")

    def return_book(self):
        if not self.is_available:
            print(f"El libro {self.title} no ha sido prestado")
            return
        self.is_available = True
        print(f"El libro {self.title} ha sido devuelto")

    def __str__(self):
        return f"Libro: {self.title}\nAutor: {self.author}\nDisponible: {'Si' if self.is_available else 'No'}"


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title} no está disponible")  

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} no ha sido prestado")

    def __str__(self):
        return f"Usuario: {self.name}\nID: {self.user_id}\nLibros prestados: {len(self.borrowed_books)}"


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido agregado a la biblioteca")

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado en la biblioteca")

    def show_available_books(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.is_available:
                print(book)
            else:
                print(f"El libro {book.title} no está disponible")

    def show_borrowed_books(self):
        print("Libros prestados:")
        for user in self.users:
            if user.borrowed_books:
                print(user)
            else:
                print(f"El usuario {user.name} no tiene libros prestados")

    def __str__(self):
        return f"Biblioteca: {len(self.books)} libros y {len(self.users)} usuarios"

    
book1 = Book("El principito", "Antoine de Saint-Exupéry")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")
book4 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book5 = Book("Pride and Prejudice", "Jane Austen")

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

library.register_user(User("Cristian", 1))
library.register_user(User("Antonio", 2))

library.show_available_books()
library.show_borrowed_books()





