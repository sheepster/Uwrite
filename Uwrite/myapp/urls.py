from django.urls import path
from myapp.views import index, indexItem, glavnaya, add_task, update_task, delete_task

app_name = "myapp"

urlpatterns = [
    #http://127.0.0.1:8000/Uwrite/
    path('',index, name='index'),
    path('<int:my_id>/',indexItem, name="detail"),
    path('add_task/',add_task, name="add_task"),
    path('main/',glavnaya, name="main"),
    path("update_task/<int:my_id>/",update_task, name="update_task"),
    path("delete_task/<int:my_id>/",delete_task, name="delete_task")
    

]