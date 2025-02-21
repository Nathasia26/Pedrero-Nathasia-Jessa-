class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear Published: {self.year_published}"

book1 = Book("The Scarlet Letter", "Nathaniel Hawthorne", 1850)
book2 = Book("War and Peace", "Leo Tolstoy", 1869)
book3 = Book("The Count of Monte Cristo", "Alexandre Dumas", 1844)

print(book1.describe())
print("\n" + "-"*30 + "\n")
print(book2.describe())
print("\n" + "-"*30 + "\n")
print(book3.describe())
