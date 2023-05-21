from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# from froala_editor.fields import FroalaField

# Create your models here.

class BlogModel(models.Model):
    title = models.TextField(max_length=255)
    content = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='media/slider/%Y/%m', blank=True)
    created_date = models.DateTimeField(default = datetime.now, blank=True)
    user = User.username

# class RewardPoints(models.Model):
#     user = 
