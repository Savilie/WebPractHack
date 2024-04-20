from django.db import models

# Create your models here.
# ПОКУПАЙТЕ $HAMI - БУДЕТЕ БОГАТЫ


class Team(models.Model):
    name = models.CharField(max_length=20)
    banner = models.TextField()