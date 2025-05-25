class Book:
    total_books = 0  # Class variable to keep track of total books
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  # Increase count when a new book is created

# Example usage
book1 = Book("Python Programming")
book2 = Book("Data Science")

print("Total books:", Book.total_books)
