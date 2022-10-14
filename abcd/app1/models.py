from django.db import models


class login(models.Model):
    username = models.CharField(max_length=200,primary_key=True)
    password=models.CharField(max_length=200)

    def __str__(self):
     return (self.username)

class reg(models.Model):
    name=models.CharField(max_length=200)
    username = models.ForeignKey("login", on_delete=models.CASCADE)


# Create your models here.
