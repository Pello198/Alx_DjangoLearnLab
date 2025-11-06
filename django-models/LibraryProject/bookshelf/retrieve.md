### Retrieve Operation

```python
from bookshelf.models import Book
Book.objects.get(id=1)

# Expected Output (example):
# <QuerySet [<Book: 1984 by George Orwell>]>
