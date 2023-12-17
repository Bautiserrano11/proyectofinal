# blogapp/models.py
from django.db import models
from accounts.models import CustomUser

class Category (models.Model):
    name = models.CharField(max_length=150)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)



