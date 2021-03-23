from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('books', views.books),
    path('authors', views.authors),
    path('create_book', views.create_book),
    path('create_author', views.create_author),
    path('books/<int:book_id>', views.view_book),
    path('authors/<int:author_id>', views.view_author),
    path('add_book', views.add_book),
    path('add_author', views.add_author),
]