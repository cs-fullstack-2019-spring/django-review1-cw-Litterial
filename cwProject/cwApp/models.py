from django.db import models

# Create your models here.

#Cocktail models
class Cocktail(models.Model):
     name= models.CharField(max_length=100)
     alcoholPercentage= models.DecimalField(max_digits=3,decimal_places=2)
     servingGlass=models.CharField(max_length=100)

     def __str__(self):
         return self.name


class Page(models.Model):
    name= models.CharField(max_length=100)

    def __str__(self):
        return self.name
