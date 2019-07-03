from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import (
    UserSerializer,
    AuthorSerializer,
    BookSerializer,
)
from .models import (
    Author,
    Book,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('last_name')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
