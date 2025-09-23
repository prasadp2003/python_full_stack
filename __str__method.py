class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"

# Example usage
my_book = Book("1984", "George Orwell", 1949)
print(my_book)  # Output: '1984' by George Orwell (1949)