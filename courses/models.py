from django.db import models

class Course(models.Model):
    title = models.CharField(blank=False, max_length=255)
    logo_url = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=False)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    tutors = models.ManyToManyField('Tutor')
    devtype = models.ForeignKey('Devtype', on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Tutor(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    image_url = models.CharField(blank=False, max_length=255)
    summary = models.TextField(blank=False)
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return self.first_name + " " + self.last_name

class Devtype(models.Model):
    title = models.CharField(blank=False, max_length=50)
    def __str__(self):
        return self.title