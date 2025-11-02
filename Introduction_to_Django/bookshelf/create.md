# Create a Book Instance (with Full Details)

This demonstrates how to create a `Book` instance from the Django shell and print its full details.

---

##  Django Shell Commands

```python
# Import the model
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Print full book details
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")

```


OUTPUT:
Title: 1984
Author: George Orwell
Publication Year: 1949

