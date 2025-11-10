from django.db import models

# Create your models here.
class Post(models.Model):
  project_title= models.CharField(max_length=200)
  description= models.TextField()
  image= models.ImageField()
  skills= models.TextField()
  created_at= models.DateTimeField()
  
  def __str__(self):
    return self.project_title
  