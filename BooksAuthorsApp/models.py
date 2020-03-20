from django.db import models
from LogRegApp.models import *

class BookManager(models.Manager):
    def book_val(self, postData):
        errors = {}

        books = Book.objects.filter(title=postData['title'])
        # Title should be minimum 2 characters 
        # and be unique in DB
        if len(postData['title']) < 2:
            errors['title'] = "Book title must be at least 2 characters long."
        if len(books) > 0:
            errors['title'] = "Cannot create duplicate book entry."

        # Description should be minimum 10 characters
        if len(postData['description']) < 10:
            errors['description'] = "Your description must be at least 10 characters long."
        
        return errors


class AuthorManager(models.Manager):
    def author_val(self, postData):
        errors = {}

        authors = Author.objects.filter(first_name=postData['first_name'], last_name=postData['last_name'])

        if len(postData['first_name']) < 2:
            errors['first_name'] = "Author's first name must be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Author's last name must be at least 2 characters."
        if len(authors) > 0:
            errors['author'] = "An author with that name already exists."

        if len(postData['notes']) < 10:
            errors['notes'] = "Notes must be longer than 10 characters."

        return errors
        


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_created", on_delete=models.CASCADE)
    # authors
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Author(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    notes = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="authors_created", on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()