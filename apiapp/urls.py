from django.urls import path
from .views import booksAPI, helloAPI, oneBookAPI

urlpatterns = [
  path("hello/",helloAPI),
  path("books/",booksAPI),
  path("book/<int:bid>",oneBookAPI)
  ]