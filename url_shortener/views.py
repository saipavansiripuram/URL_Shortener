from django.shortcuts import render

def task_view(request):
    dynamic_data = "Hello World"
    return render(request, 'task.html', {'dynamic_data': dynamic_data})
