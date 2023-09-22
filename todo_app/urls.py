from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = "todo_app"
urlpatterns = [
    path(route='<str:todo_id>/',view=csrf_exempt(views.Todo_Manager),name='todo_manager'),
    path(route='',view=csrf_exempt(views.Todo_Manager)),
]
