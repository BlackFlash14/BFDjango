from django.shortcuts import render
from datetime import datetime, timedelta


# Create your views here.
def todo(request):
    cur_day = datetime.today()
    todo_list = [{
        'title': "Task {}".format(i),
        'created': cur_day.strftime("%d/%m/%y"),
        'due_on': (cur_day + timedelta(days=3)).strftime("%d/%m/%y"),
        'owner': "admin",
        'mark': "Done"
    }
    ]
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'todo_list.html', context)

def comp_todo(request, index):
    cur_day = datetime.today()
    task = {
        'title': "Task {}".format(index),
        'created': cur_day.strftime("%d/%m/%y"),
        'due_on': (cur_day + timedelta(days=3)).strftime("%d/%m/%y"),
        'owner': "admin",
        'mark': "Undone"
    }
    context = {
        'task': task
    }
    return render(request, 'completed_todo.html', context)