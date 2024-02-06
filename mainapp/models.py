from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Picture(models.Model):
    picture = models.ImageField(upload_to='project_pictures')

class Project(models.Model):
    project_title = models.TextField(blank=True)
    project_description = RichTextField(blank=True)
    project_pictures = models.ManyToManyField(Picture, blank=True)
    live_link = models.TextField(blank=True)

class ClientReview(models.Model):
    client_name = models.TextField(blank=True)
    client_picture = models.TextField(blank=True)
    client_from = models.TextField(blank=True)
    client_country = models.TextField(blank=True)
    number_of_stars = models.FloatField(default=0.0)
    feedback = models.TextField(blank=True)