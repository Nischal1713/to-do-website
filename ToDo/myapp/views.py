from django.shortcuts import render, redirect
from .models import task

def home(request):
    tasks=task.objects.filter(is_completed=False).order_by('-created_at')
    completed_tasks=task.objects.filter(is_completed=True).order_by('-created_at')
    context={
        'tasks': tasks,
        'completed_tasks': completed_tasks
    }
    return render(request, 'myapp/home.html', context)

def addtask(request):
    tasks=request.POST.get('task')
    task.objects.create(task=tasks)
    return redirect('home')

def mark_as_done(request, task_id):
    task_item = task.objects.get(id=task_id)
    task_item.is_completed = True
    task_item.save()
    return redirect('home')

def undo(request, task_id):
    task_item = task.objects.get(id=task_id)
    task_item.is_completed = False
    task_item.save()
    return redirect('home')

def delete(request, task_id):
    task_item = task.objects.get(id=task_id)
    task_item.delete()
    return redirect('home')

def edit(request, task_id):
    get_task = task.objects.get(id=task_id)
    if request.method == 'POST':
        new_task = request.POST.get('task')
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
    return render(request, 'myapp/edit.html', context)

