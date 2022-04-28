from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
