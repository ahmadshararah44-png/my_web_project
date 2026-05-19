from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        priority = request.POST.get('priority', 'medium')
        due_date = request.POST.get('due_date') or None
        if title:
            Task.objects.create(title=title, priority=priority, due_date=due_date)
        return redirect('task_list')

    # Display tasks, ordered by latest
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')