from django.db import models

class Productos(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()


    def __str__(self):
        return self.name
    
