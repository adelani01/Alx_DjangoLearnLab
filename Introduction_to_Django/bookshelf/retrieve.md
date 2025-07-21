# Retrieve Book Instances

## Command

```python
from bookshelf.models import Book

# Retrieve all Book instances
books = Book.objects.all()

# Print each book's details
for book in books:
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Year: {book.publication_year}")
    print("-" * 30)
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

