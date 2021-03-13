from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class File(models.Model):
    file_name = models.FileField(max_length = 200)
    author = models.ForeignKey(User, on_delete = True)
    objects = models.Manager()

def __str__(self):
    return self.file_name