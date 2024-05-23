from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView


# def index(request):
#     items = Product.objects.all()
#     context = {
#         "items":items
#     }
#     return render(request, "myapp/index.html",context)


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
def add_task(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES["upload"]
        item = Product(name=name, price=price, description=description, image=image)
        item.save()
    return render(request, "myapp/add_task.html")

def update_task(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.description = request.POST.get("description")
        item.image = request.FILES.get("upload", item.image)
        item.save()
        return redirect("/Uwrite/")
    context = {"item":item}
    return render(request, "myapp/update_task.html", context)

def delete_task(request, my_id):
    item = Product.objects.get(id=my_id)
    if request.method == "POST":
        item.delete()
        return redirect("/Uwrite/")
    context = {"item":item}
    return render(request, "myapp/delete_task.html", context)