from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel
from .forms import TaskForm

def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')
    else:
        task_form = TaskForm()
    return render(request, 'add_task.html', {'form': task_form})

def edit_task(request, id):
    task = get_object_or_404(TaskModel, pk=id)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')
    else:
        task_form = TaskForm(instance=task)
    return render(request, 'add_task.html', {'form': task_form})

def delete_task(request, id):
    task = get_object_or_404(TaskModel, pk=id)
    task.delete()
    return redirect('show_tasks')

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})
