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
l.add_book(Book("the adventure","aman singh"))
l.add_book(Book("war and peace","leo tolstoy"))
l.add_book(Book("utopia","sir thomas moor"))
l.add_book(Book("romio and juliet","William Shakespeare"))

l.display_books()

l.borrow("the adventure")

l.display_books()

l.return_book(Book("the adventure","aman singh"))

l.display_books()