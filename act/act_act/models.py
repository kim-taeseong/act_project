from django.db import models

# Create your models here.

class Works(models.Model):

    date = models.DateField(auto_now_add=True)
    work = models.CharField(max_length=10)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']