from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Task
from .serializer import TaskSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def api_overview(request):
    capital = {
        'Bangladesh':'Dhaka',
        'India':'Dilli',
        'Pakisthan':'Islamabad'
    }
    return JsonResponse(capital,safe=True)

@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def task_list(request):
    task = Task.objects.all()
    serializer_list = TaskSerializer(task,many=True)
    return Response(serializer_list.data)

@api_view(['GET'])
def task_details(request,pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_update(request,pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def task_delete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Yes Delete Done')


