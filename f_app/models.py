from django.db import models

# Create your models here.
class questions(models.Model):
    question=models.CharField(max_length=300)
    answer=models.CharField(max_length=500)
    date=models.DateTimeField()
