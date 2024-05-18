from django.urls import path
from myapp.views import index, indexItem, glavnaya

app_name = "myapp"

urlpatterns = [
    #http://127.0.0.1:8000/Uwrite/
    path('',index),
    path('<int:my_id>/',indexItem, name="detail"),
    path('main/',glavnaya, name="main"),
]