### Update Operation

```python
from bookshelf.models import Book

b = Book.objects.get(id=1)
b.title = "Nineteen Eighty-Four"
b.save()
b

# Expected Output:
# <Book: Nineteen Eighty-Four by George Orwell>
