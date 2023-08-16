from django.shortcuts import render
from rest_framework import viewsets
from .models import Task


from django.http import JsonResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
@csrf_exempt
def task_create(request):
    title = request.POST['title']
    assigned_to = request.POST['assigned_to']
    due_date = request.POST['due_date']
    task = Task.objects.create(title=title, assigned_to=assigned_to, due_date=due_date)
    return JsonResponse({'message': 'Task created successfully', 'id': task.id})

def task_list(request):
    tasks = Task.objects.all()
    task_data = [{'id': t.id, 'title': t.title} for t in tasks]
    return JsonResponse({'tasks': task_data})

@csrf_exempt
def task_delete(request, task_id):
    if request.method == 'POST':
        Task.objects.filter(pk=task_id).delete()
        return JsonResponse({'message': 'Task deleted successfully'})
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def task_edit(request, task_id):
    if request.method == 'POST':
        title = request.POST.get('title', None)
        assigned_to = request.POST.get('assigned_to', None)
        due_date = request.POST.get('due_date', None)

        task = Task.objects.get(pk=task_id)

        if title is not None:
            task.title = title
        if assigned_to is not None:
            task.assigned_to = assigned_to
        if due_date is not None:
            task.due_date = due_date

        task.save()
        return JsonResponse({'message': 'Task edited successfully'})
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)