from django.db import models

class Trick(models.model):
    header = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    videoUrl = models.URLField()
