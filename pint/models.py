from django.db import models

# Create your models here.
class MyUser(models.Model):
    email = models.EmailField(max_length=255, primary_key=True)
    nickname = models.CharField(max_length=255)
    password = models.CharField(max_length=128)

class Photo(models.Model):
    photo = models.ImageField(max_length=128)
    description = models.TextField(max_length=255)
    likes = models.TextField(MyUser)

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

