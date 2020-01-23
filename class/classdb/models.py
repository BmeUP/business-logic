from django.db import models


class Stuff(models.Model):
    name = models.CharField(max_length=200)

    def all():
        return Stuff.objects.all()
    
    def first_by_id(id):
        return Stuff.objects.filter(id=id).first()


class AnotherOne(models.Model):
    surename = models.CharField(max_length=200)

# Create your models here.
