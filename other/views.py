from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

def list_tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render (request,'index.html',context)

def create_task(request):
    if request.method == 'GET':
        task_form = TaskForm()
        context = {
            'form':task_form
        }
    else:
        task_form = TaskForm(request.POST)
        context = {
            'form':task_form
        }
        if task_form.is_valid():
            task_form.save()
            return redirect('index')
    return render (request,'create_task.html',context)

def edit_task(request,id):
    task = Task.objects.get(id = id)
    if request.method == 'GET':
        task_form = TaskForm(instance = task)
        context = {
            'form': task_form
        }
    else:
        task_form = TaskForm(request.POST, instance = task)
        context = {
            'form':task_form
        }
        if task_form.is_valid():
            task_form.save()
            return redirect('index')
    return render (request,'create_task.html',context)
def add_dcl(request):
    return render(request,'painterdcl.html')

