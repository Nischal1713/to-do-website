from django.shortcuts import render, redirect
from .models import task

def home(request):
    tasks=task.objects.filter(is_completed=False).order_by('-created_at')
    context={
        'tasks': tasks
    }
    return render(request, 'myapp/home.html', context)

def addtask(request):
    tasks=request.POST.get('task')
    task.objects.create(task=tasks)
    return redirect('home')