from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from apiRest.models import User, Task
from apiRest.serializers import UserSerializer, TaskSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def tasksByUser(self, request, user_id):
        tasks = get_object_or_404(User, pk=user_id).task_set.all()
        serializer_class = TaskSerializer(tasks, many=True)
        return Response(serializer_class.data)

    def createTask(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        task = null
        if not(request.data['title']):
            task = Task(title=request.data['title'],
                    status=request.data['status'], user=user)    
        task = Task(title=request.data['title'],
                    status=request.data['status'], user=user)
        task.save()
        serializer_class = TaskSerializer(task)
        return Response(serializer_class.data)

    def tasksByUser_detail(self, request, user_id, pk):
        tasks = get_object_or_404(User, pk=user_id).task_set.all()
        task = get_object_or_404(tasks, pk=pk)

        serializer_class = TaskSerializer(task)
        return Response(serializer_class.data)

    def updateTask(self, request, user_id, pk):
        tasks = get_object_or_404(User, pk=user_id).task_set.all()
        task = get_object_or_404(tasks, pk=pk)
        task.status = request.data['status']
        task.save()
        serializer_class = TaskSerializer(task)
        return Response(serializer_class.data)
