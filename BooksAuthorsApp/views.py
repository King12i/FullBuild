from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def books(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
        "books": Book.objects.all()
    }
    return render(request, "books.html", context)

def create_book(request):
    if 'user_id' not in request.session:
        return redirect('/')

    errors = Book.objects.book_val(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/dashboard/books')
    
    Book.objects.create(title=request.POST['title'], description=request.POST['description'], uploaded_by_id=request.session['user_id'])
    return redirect('/dashboard/books')


def one_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    # now i can use book_id as something
    context = {
        "this_book": Book.objects.get(id=book_id),
        "authors": Author.objects.all()
    }
    return render(request, "one_book.html", context)

def add_author_to_book(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_book = Book.objects.get(id=book_id)
    this_author = Author.objects.get(id=request.POST['author_id'])
    this_book.authors.add(this_author)
    # alternatively
    # this_author.books.add(this_book)

    return redirect(f"/dashboard/books/{book_id}")


def authors(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
        "authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def create_author(request):
    if 'user_id' not in request.session:
        return redirect('/')
    errors = Author.objects.author_val(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/dashboard/authors')
    
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'], uploaded_by_id=request.session['user_id'])
    return redirect('/dashboard/authors')

def one_author(request, author_id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "this_author": Author.objects.get(id=author_id),
        "books": Book.objects.all()
    }
    return render(request, "one_author.html", context)

def add_book_to_author(request, author_id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_author = Author.objects.get(id=author_id)
    this_book.authors.add(this_author)
    # alternatively
    # this_author.books.add(this_book)

    return redirect(f"/dashboard/authors/{author_id}")
    