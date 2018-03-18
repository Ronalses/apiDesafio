from rest_framework import viewsets, status, permissions, routers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from apiRest.models import User, Task
from apiRest.serializers import UserSerializer, TaskSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def tasksByUser(self, request, user_id):
        tasks = get_object_or_404(User, pk=user_id).task_set.all()
        serializer_class = TaskSerializer(tasks, many=True)
        return Response(serializer_class.data)

    def createTask(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        if not (request.data['title']):
            task = Task(status=request.data['status'], user=user)
        else:
            task = Task(title=request.data['title'],
                    status=request.data['status'], user=user)
        task.save()
        serializer_class = TaskSerializer(task)
        return Response(serializer_class.data)

    def tasksByUser_detail(self, request, user_id, identifier):
        tasks = get_object_or_404(User, pk=user_id).task_set.all()
        task = get_object_or_404(tasks, identifier=identifier)

        serializer_class = TaskSerializer(task)
        return Response(serializer_class.data)

    def updateTask(self, request, user_id, identifier):
        tasks = get_object_or_404(User, pk=user_id).task_set.all()
        task = get_object_or_404(tasks, identifier=identifier)
        task.status = request.data['status']
        task.save()
        serializer_class = TaskSerializer(task)
        return Response(serializer_class.data)
