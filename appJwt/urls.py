
from django.urls import path, include

from . import views
from .views import RegisterApi, BlacklistRefreshView

urlpatterns = [
      path('api/register', RegisterApi.as_view()),
      path('api/logout',  BlacklistRefreshView.as_view(), name='logout'),
      path('api/books',  views.BookApi.as_view()),
      path('hello/', views.Greeting.as_view()),
]