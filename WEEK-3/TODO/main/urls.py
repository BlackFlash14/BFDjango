from django.urls import path, re_path
from main import views

urlpatterns = [
    path('todo/', views.todo),
    re_path(r'^todo/(\d+)/completed/$', views.comp_todo),
]