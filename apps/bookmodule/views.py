from django.shortcuts import render

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, "bookmodule/list_books.html")

def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")

def aboutus(request):
    return render(request, "bookmodule/aboutus.html")

# New views for Lab 5
def links_page(request):
    return render(request, "bookmodule/html5/links.html")

def text_formatting_page(request):
    return render(request, "bookmodule/html5/text_formatting.html")

def listing_page(request):
    return render(request, "bookmodule/html5/listing.html")

def tables_page(request):
    return render(request, "bookmodule/html5/tables.html")
