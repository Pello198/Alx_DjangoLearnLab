created Django project
Deep Dive into Django Models and Views

This project extends the Introduction_to_Django project by focusing on advanced Django ORM and model relationships.
It includes creating new models that use ForeignKey, ManyToMany, and OneToOne relationships inside a new Django app called relationship_app within the django-models project.

Models Implemented

Author → simple model with a name

Book → has a ForeignKey relationship to Author

Library → has a ManyToMany relationship with Book

Librarian → has a OneToOne relationship with Library

Query Samples

All required query examples are implemented inside:

relationship_app/query_samples.py

Location

Repository: Alx_DjangoLearnLab
Directory: django-models