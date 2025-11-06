### Update Operation

```python
from bookshelf.models import Book

book = Book.objects.get(id=1)   # retrieve the book first
book.title = "Nineteen Eighty-Four"   # update the title
book.save()

print(book.title)

# Expected Output:
# Nineteen Eighty-Four
