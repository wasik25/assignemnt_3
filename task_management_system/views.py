from django.shortcuts import render
from tasks.models import TaskModel

def home(request):
    data = TaskModel.objects.all()
    # print(data)
    # for i in data:
    #     print(i.title)
    #     for j in i.category.all():
    #         print(j)
    #     print()
    return render(request, 'home.html', {'data' : data})