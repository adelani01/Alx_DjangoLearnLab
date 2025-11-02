# Retrieve Book Instances

## Command

```python
from bookshelf.models import Book

# Retrieve all Book instances
books = Book.objects.all()
print("All books:")
for book in books:
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Year: {book.publication_year}")
    print("-" * 30)

# Retrieve a single book with title '1984'
try:
    single_book = Book.objects.get(title="1984")
    print("Single book retrieved:")
    print(f"Title: {single_book.title}")
    print(f"Author: {single_book.author}")
    print(f"Year: {single_book.publication_year}")
except Book.DoesNotExist:
    print("Book with title '1984' not found.")
```


# OUTPUT:
Title: DARE
Author: emmanuel
Year: 2020
------------------------------
Title: datye
Author: maya
Year: 2222
------------------------------
Title: “1984”
Author: George Orwell
Year: 1949
------------------------------
Title: “1984”
Author: George Orwell
Year: 1949
------------------------------

