from django.db import models

# Create your models here.
class Color(models.Model):
    name = models.CharField(max_length=32)

    def __repr__(self):
        return f'Color({self.name})'

class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField() 
    description = models.TextField(max_length=200, default="Базовое описание")
    colors = models.ManyToManyField(to=Color)
    
    def __str__(self):
        return f'Item(name={self.name}, brand={self.brand}, count={self.count})'
    
    def __repr__(self):
        return f'Item{self.name}, {self.brand}, {self.count}'
