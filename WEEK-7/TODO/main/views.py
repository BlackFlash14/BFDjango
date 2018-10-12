from django.shortcuts import render, redirect
from .models import Task
from datetime import datetime, timedelta
from .forms import TaskForm


# Create your views here.
def todo1(request):
    tasks = Task.objects.all();
    context = {
        'task': tasks
    }
    return render (request, "todo_list.html", context)


def todo(request):
    todo_list = Task.objects.all()
    context = {
        'todo_list': todo_list,
    }
    print(context)
    return render (request, 'todo_list.html', context)


def comp_todo(request, index):
    cur_day = datetime.today ()
    task = {
        'title': "Task {}".format (index),
        'created': cur_day.strftime ("%d/%m/%y"),
        'due_on': (cur_day + timedelta (days=3)).strftime ("%d/%m/%y"),
        'owner': "admin",
        'mark': 'Done'
    }
    context = {
        'task': task
    }
    return render (request, 'completed_todo.html', context)


def delete_task(request, id):
    try:
        task = Task.objects.get(pk=id)
        task.delete()
    except Exception as e:
        print (e)
    task = Task.objects.all()
    context = {
        'task': task
    }
    return render (request, 'todo_list.html', context)


def new_task(request):
    if request.method == 'POST':
        form = TaskForm (request.POST)
        if form.is_valid ():
            form.save ()
            return redirect ('todos')
    else:
        form = TaskForm ()
    context = {
        'form': form
    }
    return render (request, 'new.html', context)