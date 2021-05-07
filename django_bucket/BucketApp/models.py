from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Category(models.Model):
    topic=models.CharField(max_length=200)

    def __str__(self):
        return self.topic 

class Item(models.Model):
    title = models.CharField(max_length=200, default='Name of the item')
    categories = models.ManyToManyField(Category, blank=True,related_name='relatedItems',db_column='relatedItems',symmetrical=False)
    def __str__(self):
        return self.title