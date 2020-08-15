from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class Purchase(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase made for Course#{self.course_id} by user#{self.user_id} on {self.purchase_date}"