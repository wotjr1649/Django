from django.urls import path
from .views import booksAPI, helloAPI

urlpatterns = [
  path("hello/",helloAPI),
  path("books/",booksAPI),
  ]