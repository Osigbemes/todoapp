from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Task
from . forms import TaskForm

def index(request):

    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')

    return render(request, 'tasks/list.html', {'tasks':tasks, 'form':form})

def UpdateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task) # this pre-fills the form with the dat for you

    if request.method == "POST":
        form =TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('list')

    return render (request, 'tasks/update_task.html', {'form':form})

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method=="POST":
        item.delete()
        return redirect ('list')
    return render(request, 'tasks/delete.html', {'item':item})
