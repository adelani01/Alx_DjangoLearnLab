# Update Book Title

## Command

```python
from bookshelf.models import Book

# Retrieve the book with title "1984"
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
updated_book = Book.objects.get(id=book.id)
print(updated_book.title) 
```

 # Expected output: 
 Nineteen Eighty-Four
