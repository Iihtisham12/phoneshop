from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    

class Expense(models.Model):
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    category = models.ForeignKey(Menu, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name
   
    