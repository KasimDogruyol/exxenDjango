from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Movie(models.Model):
    isim =models.CharField(max_length =100,verbose_name = 'Film İsmi')
    resim = models.FileField(upload_to ='filmler/',verbose_name = 'Film Resmi')
    
    def __str__(self):
        return self.isim #bana ismini göster demek