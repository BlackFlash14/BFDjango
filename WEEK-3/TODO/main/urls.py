from django.urls import path, re_path
from main import views

urlpatterns = [
    path('todos/', views.todo),
    path ('todos/completed', views.comp_todo, name='completed_todos'),
    re_path(r'^todos/(\d+)/completed/$', views.comp_todo),
]
