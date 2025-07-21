# Delete a Book Instance

**Command:**

```python
# Retrieve the book with title "Nineteen Eighty-Four"
book = Book.objects.get(title='Nineteen Eighty-Four')

# Delete the book instance
book.delete()

# Try retrieving all books to confirm deletion
books = Book.objects.all()
print(books)
```


# OUTPUT:
(1, {'bookshelf.Book': 1})  # Number of deleted objects and details

<QuerySet []>  # Empty QuerySet indicating the book was deleted
