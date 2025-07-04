from django.shortcuts import render,HttpResponse
from .models import toDoItems

# Create your views here.
def home(request):
  return render(request,"home.html")

def todo(request):
  items = toDoItems.objects.all()
  return render(request, "todo.html", {"todos":items})
