from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from .filters import BookFilter
from .models import Book, Author, Language, Genre
from .serializers import BookSerializer, AuthorSerializer, LanguageSerializer, GenreSerializer, BookListAllSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('author')
    serializer_class = BookSerializer
class BookListAllView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListAllSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('book_year', 'author')

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    partial = True

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'date': 'his delete'}, status=status.HTTP_200_OK)

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    partial = True

class LanguageCreateApiView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class LanguageUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    partial = True

class GenreCreateApiView(generics.ListCreateAPIView):
    queryset = Genre
    serializer_class = GenreSerializer

class GenreUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Genre
    serializer_class = GenreSerializer
    partial = True






