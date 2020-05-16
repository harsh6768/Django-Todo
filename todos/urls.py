from django.conf.urls import url

from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('add',views.addTodo),
    path('deleteTodo/<int:todo_id>',views.deleteTodo),
    path('editTodo/<int:todo_id>',views.editTodo),
]