from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("todos/", views.todo, name="ToDo Lists")
]