from django.db import models




class Hero(models.Model):
    name = models.CharField(max_length=60)
    alies = models.CharField(max_length=60)

    def __str__(self):
        return self.name
    
class Peple(models.Model):
    name = models.CharField(max_length=90)
    age = models.IntegerField()
    def __str__(self):
        return self.name
