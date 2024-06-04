from django.db import models
from django.contrib.auth.models import User



class Tasks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField( default="Не задано описание")
    valid_value = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='2')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images')
    file = models.FileField(blank=True, upload_to='methods')
    tasks = models.ManyToManyField(Tasks)
   
    def __str__(self) -> str:
        return self.name
    



# class UserCourse(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     course = models.ForeignKey(Product, on_delete=models.CASCADE)
#     # Добавьте дополнительные поля по мере необходимости, например, дату записи или прогресс

#     class Meta:
#         unique_together = ('user', 'course')

#     def __str__(self) -> str:
#         return f"{self.user} - {self.course}"