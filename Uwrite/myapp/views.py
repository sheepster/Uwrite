from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product, Tasks
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
# from .models import  UserCourse

# def index(request):
#     items = Product.objects.all()
#     context = {
#         "items":items
#     }
#     return render(request, "myapp/index.html",context)


class TaskDetailView(DetailView):
    model = Tasks
    template_name = "myapp/task_detail.html"
    context_object_name = "task"

class TaskListView(ListView):
    model = Tasks
    template_name = "myapp/task_list.html"
    context_object_name = "tasks"


class ProductListView(ListView):
    model = Product
    template_name = "myapp/index.html"
    context_object_name = "items"


# def indexItem(request, my_id):
#     item = Product.objects.get(id=my_id)
#     context = {
#         "item":item
#     }
#     return render(request, "myapp/detail.html",context=context)

class ProductDetailView(DetailView):
    model = Product
    template_name = "myapp/detail.html"
    context_object_name = "item"



def glavnaya(request):
    return render(request, "myapp/index1.html")

@login_required
def add_course(request):
    if request.method == "POST":
        item.author = request.POST.get("author")
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES["upload"]
        item = Product(name=name, price=price, description=description, image=image)
        item.save()
    return render(request, "myapp/add_course.html")


@login_required
def update_course(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == "POST":
        item.author = request.POST.get("author")
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.description = request.POST.get("description")
        item.image = request.FILES.get("upload", item.image)
        item.save()
        return redirect("/Uwrite/")
    context = {"item":item}
    return render(request, "myapp/update_course.html", context)

@login_required
def delete_course(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == "POST":
        item.delete()
        return redirect("/Uwrite/")
    context = {"item":item}
    return render(request, "myapp/delete_course.html", context)

# def add_user_course(request):
#     if request.method == "POST":
#         user = request.user
#         course_id = request.POST.get("course_id")
#         course = Product.objects.get(id=course_id)
#         user_course = UserCourse(user=user, course=course)
#         user_course.save()
#         return redirect("myapp/profile.html")
#     items = Product.objects.all()
#     context = {
#         "items": items
#     }   
#     return render(request, "myapp/add_course.html", context=context)


