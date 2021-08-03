from django.db import models

# Create your models here.

class TestModel(models.Model):
    test_column = models.CharField(max_length=100)