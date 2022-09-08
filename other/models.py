from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    statement = models.TextField()

    def _str_(self):
        return self