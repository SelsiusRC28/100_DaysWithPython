#Library

class Book:
    def __init__(self, title, autor):
        self.title = title
        self.autor = autor
        self.is_borrowed = False
        
    def display_info(self):
        print(f"\n ------ {self.title}----------")
        print(f"Autor: {self.autor}")
        print(f"Status: {"Available" if not self.is_borrowed else "No Available"}")
        
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, title, autor):
        new_book = Book(title, autor)
        self.books.append(new_book)
        print("Book has created succesfully")
        
    def show_books(self):
        if not self.books:
            print("There are no books")
        else:
            for book in self.books:
                book.display_info()
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                print("Disfruta tu lectura")
                return
        print("Book not found")
    
    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                print("Thanks for return book")
                return
        print("Book not found")

#Main
library = Library()

while True:
    print("\n ------ Lybrary XD --------")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    
    choise = int(input("Select the option: ").strip())
    
    if choise == 1:
        title = input("Title of book: ").strip()
        autor = input("Autor of book: ").strip()
        library.add_book(title, autor)
    elif choise == 2:
        library.show_books()
    elif choise == 3: 
        title = input("Title of book: ").strip()
        library.borrow_book(title)
    elif choise == 4: 
        title = input("Title of book: ").strip()
        library.return_book(title)
    elif choise == 5:
        break
    else:
        print("Invalit option")
        