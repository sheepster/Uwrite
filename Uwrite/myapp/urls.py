from django.urls import path
from myapp.views import glavnaya, add_course, update_course, delete_course, ProductListView, ProductDetailView, task_detail, enroll_course

app_name = "myapp"

urlpatterns = [
    #http://127.0.0.1:8000/Uwrite/
    # path('',index, name='index'),
    path('courses',ProductListView.as_view(), name='index'),
    path('courses/<int:pk>/',ProductDetailView.as_view(), name="detail"),
    path('task/<int:task_id>/', task_detail, name='task_detail'),
    path('enroll/<int:course_id>/', enroll_course, name='enroll_course'),
    path('add_course/',add_course, name="add_course"),
    path('',glavnaya, name="main"),
    path("update_course/<int:my_id>/",update_course, name="update_course"),
    path("delete_course/<int:my_id>/",delete_course, name="delete_course")
    

]