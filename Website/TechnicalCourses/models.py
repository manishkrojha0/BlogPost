from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class AllCourses(models.Model):
    coursename = models.CharField(max_length=200)
    insname = models.CharField(max_length=200)
    startedfrom = models.DateTimeField('Started from')

    def __str__(self):
        return self.coursename

    def was_published_recently(self):
        return self.startedfrom >= timezone.now() - datetime.timedelta(days=1)


class details(models.Model):
    course = models.ForeignKey(AllCourses, on_delete=models.CASCADE)
    ct = models.CharField(max_length=500)  # course type
    yourChoice = models.BooleanField(default=False)

    def __str__(self):
        return str(self.ct)
