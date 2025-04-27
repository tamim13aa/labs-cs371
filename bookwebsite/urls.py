
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  

urlpatterns = [
    path('', lambda request: redirect('books.index')),  
    path('admin/', admin.site.urls),
    path('books/', include('apps.bookmodule.urls')),
]

