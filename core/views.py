from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from django.http import Http404

from .serializers import (
    UserSerializer,
    AuthorSerializer,
    BookSerializer,
)
from .models import (
    Author,
    Book,
)


# ViewSets представляют собой очень удобную основу api, а в самописных Views
# переопределяем некоторые методы
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('-birth_year')
    serializer_class = AuthorSerializer


class AuthorsManager(APIView):
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get_books(self, author):
        books = author.book_set.all()
        # сначала сериализуем книги, затем вытаскиваем данные:
        serialized_books = list(map(BookSerializer, books))
        serialized_books = list(map(
                                    lambda book: book.data,
                                    serialized_books,
                                    )
                                )
        return serialized_books

    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serialized_books = self.get_books(author)
        # переводим в словарь, т.к. serializer неизменяемый:
        serialized_author = dict(AuthorSerializer(author).data)
        serialized_author['books'] = serialized_books
        return Response(serialized_author)

    def delete(self, request, pk, format=None):
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-pub_year')
    serializer_class = BookSerializer


class BooksManager(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        print('here')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
