from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def root(request):
    return redirect('/books')

def books(request):
    books = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'books.html', context)

def authors(request):
    authors = Author.objects.all()
    context = {
        'authors' : authors
    }
    return render(request, 'authors.html', context)

def create_book(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )
    return redirect('/books')

def create_author(request):
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name']
    )
    return redirect('/authors')

def view_book(request, book_id):
    correct_book = Book.objects.get(id=book_id)
    authors = correct_book.authors.all()
    non_authors = Author.objects.exclude(books__id=correct_book.id)
    context = {
        'book' : correct_book,
        'authors' : authors,
        'non_authors' : non_authors
    }
    return render(request, 'view_book.html', context)

def view_author(request, author_id):
    correct_author = Author.objects.get(id=author_id)
    books = correct_author.books.all()
    non_books = Book.objects.exclude(authors__id=correct_author.id)
    context = {
        'author' : correct_author,
        'books' : books,
        'non_books' : non_books
    }
    return render(request, 'view_author.html', context)

def add_book(request):
    correct_author = Author.objects.get(id = request.POST['author_id'])
    correct_book = Book.objects.get(id = request.POST['book_id'])
    correct_author.books.add(correct_book)
    return redirect(f'authors/{correct_author.id}')

def add_author(request):
    correct_book = Book.objects.get(id = request.POST['book_id'])
    correct_author = Author.objects.get(id = request.POST['author_id'])
    correct_book.authors.add(correct_author)
    return redirect(f'books/{correct_book.id}')