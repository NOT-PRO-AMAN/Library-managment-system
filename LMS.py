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
            print("The Books in Library")
            for book in self.books:
                print(book)


       




l = library()
l.add_book(Book("the adventur","aman singh"))
l.add_book(Book("war and peace","leo tolstoy"))
l.add_book(Book("utopia","sir thomas moor"))
l.add_book(Book("romio and juliet","William Shakespeare"))



l.display_books()



