
---

### **delete.md**

```md
### Delete Operation

```python
from bookshelf.models import Book

b = Book.objects.get(id=1)
b.delete()

# Expected Output:
# (1, {'bookshelf.Book': 1})

Book.objects.all()

# Expected Output:
# <QuerySet []>
