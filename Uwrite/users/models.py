from django.db import models
from django.contrib.auth.models import User
from myapp.models import Product, Tasks

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='_profile_images')
    contact_number = models.CharField(max_length=50,    default="79049550145")
    courses = models.ManyToManyField(Product, default=None)
    completed_tasks = models.ManyToManyField(Tasks,default=None)

    def __str__(self):
        return self.user.username



    
# Create your models here.
