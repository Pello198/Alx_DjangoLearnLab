### CRUD Operations Summary

Below are the actual commands used and the actual outputs as they appear in Django shell.

---

#### 1) CREATE

```python
from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(b)
output 
1984 by George Orwell

RETRIEVE
from bookshelf.models import Book
print(Book.objects.all())
output
<QuerySet [<Book: 1984 by George Orwell>]>
UPDATE
from bookshelf.models import Book
b = Book.objects.get(id=1)
b.title = "Nineteen Eighty-Four"
b.save()
print(b)
output
Nineteen Eighty-Four by George Orwell
DELETE
from bookshelf.models import Book
b = Book.objects.get(id=1)
b.delete()
print(Book.objects.all())
output
<QuerySet []>
