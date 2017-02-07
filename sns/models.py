from django.db import models
from django.core.urlresolvers import reverse



class Album(models.Model):
    Place = models.CharField(max_length=50)
    Tab = models.CharField(max_length=50)
    #Image = models.FileField()

    def __str__(self):
        return self.Place + '--' + self.Tab

    
class Img(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    itype = models.CharField(max_length=10)


    
