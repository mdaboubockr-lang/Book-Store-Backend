from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from store_APIS.views import BookDetailView, BookListCreateView, UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/books/', BookListCreateView.as_view(), name='book_list_create'),
    path('api/books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('api/register/', UserCreateView.as_view(), name='user_register'),
]

