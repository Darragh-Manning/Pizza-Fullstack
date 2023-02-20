from django.db import models


# Create your models here.
Class Pizza(models.Model):
    size = models.ForeignKey()
    crust_choices = [
        'normal'
    ]
    crust = models.CharField(choices=crust_choice, default='Other', max_length=200)
    crus