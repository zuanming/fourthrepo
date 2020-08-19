from django.db import models
from courses.models import Course
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(blank=False, max_length=255)
    datetime = models.DateTimeField(blank=False)
    content = models.TextField(blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField(blank=False)
    datetime = models.DateTimeField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    def __str__(self):
        return self.text[0:50]