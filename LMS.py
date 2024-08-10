

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    

class library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added {book}")

    def display_books(self):
        if not self.books:
            print("No Books are available")
        else:
            print("\n\nThe Books in Library")
            for book in self.books:
                print(book)

    def borrow(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"\n----------\nyou borrowed {book}\n----------")
                return
            print("this book is not available")

    def return_book(self,book):
        self.books.append(book)
        print(f"\n++++++++++\nbook returned and added {book}\n++++++++++")

l = library()      

def user_input():
    while True:
        a = int(input("--------------------\nWelcome to the Library-:\nChoose the adjecent number of the task you want to preform.\n(1)-Display books\n(2)-borrow books\n(3)-Return book\n--->>>"))


        if a == 1 :
            l.display_books()
        elif a == 2:
            b = input("Enter the name of book you want -->").lower()
            l.borrow(b)

        elif a == 3:
            c = input("Name of the Book-->").lower()
            d = input("Name of the Author-->").lower()
            l.return_book(Book(c,d))

        else:
            print("write a valid integer")



l.add_book(Book("the adventure","aman singh"))
l.add_book(Book("war and peace","leo tolstoy"))
l.add_book(Book("utopia","sir thomas moor"))
l.add_book(Book("romio and juliet","William Shakespear"))
           
user_input()