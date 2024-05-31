from django.shortcuts import render, redirect,get_object_or_404
from .models import TodoList, Task_History
from datetime import datetime, time

def Todo_view(request):

    inc_task = TodoList.objects.filter(task_status=False)
    cmp_task = TodoList.objects.filter(task_status=True)
    total_task = TodoList.objects.all().count()

    d = { 'inc_task': inc_task, 'cmp_task': cmp_task , 'total_task' : total_task}
    return render(request, 'TodoApp/home.html', d)



def add_task(request):
    task = request.POST['add_task']
    TodoList.objects.create(task = task)
    return redirect('home')


def task_done(request, id):
    task=get_object_or_404(TodoList,id=id)
    task.task_status = True
    task.save()
    return redirect('home')

def del_task(request, id):
    task = get_object_or_404(TodoList,id=id)
    task.delete()
    print('***************************************************************')
    return redirect('home')

def update_task(request, id):
    record = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        updated_task=request.POST['update_task']
        record.task=updated_task
        record.save()
        return redirect('home')
    task = record.task
    d = {'task':task, 'record': record}
    return render(request, 'TodoApp/update.html',d)    


def undo_task(request, id):
    task=get_object_or_404(TodoList,id=id)
    task.task_status = False
    task.save()
    return redirect('home')


