from django.contrib.auth.models import User
from django.db import models

STATUS = ((0, 'В наличии'), (1, 'У пользователя'))

class Category(models.Model):
    title = models.CharField(max_length=100)

class Book(models.Model):
    categories = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='books')

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    books = models.ForeignKey(Book, related_name='orders', on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

