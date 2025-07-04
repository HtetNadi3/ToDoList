from django.urls import path
from . import views

urlpatterns = [
  # path("", views.home, name="home"),
  path("", views.todo, name="todo"),
   path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete task
    path('done/<int:task_id>/', views.mark_done, name='done'),  # Mark task done
]