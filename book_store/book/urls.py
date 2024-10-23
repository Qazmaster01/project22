from django.urls import path

from .views import *

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/all/', BookListAllView.as_view(), name='all-books-list'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/update/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    path('genres/', GenreCreateApiView.as_view(), name='genre-create'),
    path('genres/<int:pk>/', GenreUpdateApiView.as_view(), name='genre-update'),
    path('languages/', LanguageCreateApiView.as_view(), name='language-create'),
    path('languages/<int:pk>/', LanguageUpdateView.as_view(), name='language-update'),
]