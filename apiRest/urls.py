from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.authtoken import views

from apiRest.views import UserViewSet, TaskViewSet

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

todo_list = TaskViewSet.as_view({
    'get': 'tasksByUser',
    'post': 'createTask'
})

todo_detail = TaskViewSet.as_view({
    'get': 'tasksByUser_detail',
    'put': 'updateTask',
})

urlpatterns = format_suffix_patterns([
    url(r'^token-auth/', views.obtain_auth_token),
    url(r'^$', user_list, name='user_list'),
    url(r'^users/$', user_list, name='user_list'),
    url(r'^users/$', user_detail, name='user_detail'),
    url(r'^(?P<user_id>[0-9]+)/todo-list/$', todo_list, name='todo_list'),
    url(r'^(?P<user_id>[0-9]+)/todo-list/(?P<identifier>.+)/$', todo_detail, name='todo_detail')
])
