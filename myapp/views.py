from django.shortcuts import render, redirect
from .models import toDoItems
def todo(request):
  if request.method == 'POST':
    todoTitle = request.POST.get('task')
    if todoTitle:
      toDoItems.objects.create(title=todoTitle)
      return redirect('todo')
    

  tasks = toDoItems.objects.all()
  return render(request,"todo.html",{"tasks":tasks})

def delete_task(request, task_id):
    try:
        toDoItems.objects.get(id=task_id).delete()
    except toDoItems.DoesNotExist:
        pass  # Handle the case where task doesn't exist
    return redirect('todo')

def mark_done(request, task_id):
    task = toDoItems.objects.get(id=task_id)
    task.completed = True
    task.save()  # Mark task as done
    return redirect('todo')

