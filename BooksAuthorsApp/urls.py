from django.urls import path
from . import views

urlpatterns = [
    # path and method for book dashboard
    path('/books', views.books),

    # path and view for creating a new book
    path('/books/create', views.create_book),

    # path and method for one book
    path('/books/<int:book_id>', views.one_book),

    # path and method for adding an author to one book
    path('/books/<int:book_id>/add_author', views.add_author_to_book),

    # path and method for author dashboard
    path('/authors', views.authors),

    # path and method for creating a new author
    path('/authors/create', views.create_author),

    # path and method for one author
    path('/authors/<int:author_id>', views.one_author),

    # path and method for adding a book to one author
    path('/authors/<int:author_id>/add_book', views.add_book_to_author)

]