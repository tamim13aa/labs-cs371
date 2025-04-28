from django.shortcuts import render
from .models import Book


def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, "bookmodule/list_books.html")

def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")


def links_page(request):
    return render(request, "bookmodule/html5/links.html")

def text_formatting_page(request):
    return render(request, "bookmodule/html5/text_formatting.html")

def listing_page(request):
    return render(request, "bookmodule/html5/listing.html")

def tables_page(request):
    return render(request, "bookmodule/html5/tables.html")

def search_page(request):
    return render(request, 'bookmodule/search.html')

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})


