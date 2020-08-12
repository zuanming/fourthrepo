from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(blank=False, max_length=255)
    def __str__(self):
        return self.title


class Tutor(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    
    def __str__(self):
        return self.first_name + " " + self.last_name

