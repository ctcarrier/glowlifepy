from django.db import models
from datetime import datetime

class TrickCategory(models.Model):
    category_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.category_name

class Trick(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published', default=datetime.now, editable=False)
    trick_category = models.ForeignKey(TrickCategory)
    def __unicode__(self):
        return self.name

