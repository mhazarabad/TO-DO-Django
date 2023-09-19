from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

app_name = "user_app"
urlpatterns = [
    path(route='token_manager/',view=csrf_exempt(views.Token_Manager),name='token_manager'),
    
    path(route='<str:user_username>/',view=csrf_exempt(views.User_Manager),name='user_manager'),
    
    path(route='',view=csrf_exempt(views.User_Manager)),
    
]
