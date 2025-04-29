from django.shortcuts import render
from .models import Book
from django.db.models import Q
from .models import Student, Department
from django.db.models import Count
from django.db.models import Max
from django.shortcuts import render, redirect, get_object_or_404






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

def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookList.html', {'books': books})

def lab8_task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/bookList.html', {'books': books})

def lab8_task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) & ~Q(title__icontains='co') & ~Q(author__icontains='co')
    )
    return render(request, 'bookmodule/bookList.html', {'books': books})

def lab8_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': books})

from django.db.models import Count, Sum, Avg, Max, Min

def lab8_task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/statistics.html', {'stats': stats})

def lab8_task7(request):
    from .models import Student, Address
    results = Student.objects.values('address__city').annotate(count=Count('id')).order_by('-count')
    return render(request, 'bookmodule/students_by_city.html', {'results': results})



def lab9_task1(request):
    results = Student.objects.values('department__name').annotate(count=Count('id')).order_by('-count')
    return render(request, 'bookmodule/lab9_task1.html', {'results': results})




def lab9_task2(request):
    max_ages = Student.objects.values('department__name').annotate(max_age=Max('age'))

    result = []
    for item in max_ages:
        oldest = Student.objects.filter(
            department__name=item['department__name'], 
            age=item['max_age']
        ).first()
        result.append({'department': item['department__name'], 'student': oldest})

    return render(request, 'bookmodule/lab9_task2.html', {'result': result})


def lab9_task3(request):
    students = Student.objects.prefetch_related('courses').all()
    return render(request, 'bookmodule/lab9_task3.html', {'students': students})



def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10/list_books.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST.get("title"),
            author=request.POST.get("author"),
            price=request.POST.get("price"),
            edition=request.POST.get("edition")
        )
        return redirect('books.lab10.listbooks')
    return render(request, 'bookmodule/lab10/add_book.html')


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.price = request.POST.get("price")
        book.edition = request.POST.get("edition")
        book.save()
        return redirect('books.lab10.listbooks')
    return render(request, 'bookmodule/lab10/edit_book.html', {'book': book})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books.lab10.listbooks')








