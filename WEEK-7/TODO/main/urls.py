from django.urls import path, re_path
from main import views
from django.conf.urls import url

urlpatterns = [
    path('todos/', views.todo, name='todos'),
    url(r'^todos/(?P<id>\d+)/delete/$', views.delete_task, name='delete'),
    path('todos/new/', views.new_task, name='new_task'),
    path('todos/completed', views.comp_todo, name='completed_todos'),
    re_path(r'^todos/(\d+)/completed/$', views.comp_todo),
]
