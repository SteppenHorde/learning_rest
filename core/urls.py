from django.urls import include, path
from rest_framework import routers
from .views import (
    UserViewSet,
    AuthorViewSet,
    BookViewSet,
)


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
