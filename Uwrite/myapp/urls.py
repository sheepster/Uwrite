from django.urls import path
from myapp.views import glavnaya, add_task, update_task, delete_task, ProductListView, ProductDetailView

app_name = "myapp"

urlpatterns = [
    #http://127.0.0.1:8000/Uwrite/
    # path('',index, name='index'),
    path('',ProductListView.as_view(), name='index'),
    path('<int:pk>/',ProductDetailView.as_view(), name="detail"),
    path('add_task/',add_task, name="add_task"),
    path('main/',glavnaya, name="main"),
    path("update_task/<int:my_id>/",update_task, name="update_task"),
    path("delete_task/<int:my_id>/",delete_task, name="delete_task")
    

]