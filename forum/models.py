from django.db import models
from courses.models import Course
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(blank=False, max_length=255)
    datetime = models.DateTimeField(blank=False)
    content = models.TextField(blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Answer(models.Model):
    datetime = models.DateTimeField(blank=False)
    content = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self):
        return self.content[0:50]
