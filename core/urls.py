from django.urls import include, path
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .views import (
    UserViewSet,
    AuthorViewSet,
    AuthorsManager,
    BookViewSet,
    BooksManager,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

# взаимодействие с конкретным инстансом модели происходит через самописные Views,
# просмотр существующих инстансов и создание нового - через встроенный Viewsets
urlpatterns = [
    path('authors/<int:pk>/', AuthorsManager.as_view()),
    path('books/<int:pk>/', BooksManager.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
