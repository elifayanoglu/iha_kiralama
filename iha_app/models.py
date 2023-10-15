from django.db import models

# Create your models here.

class  Iha(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=500)
    details = models.CharField(max_length=1000, blank=True, null=True)
    
    def __str__(self):
        return self.summary

class Kiralama(models.Model):
    kullanici_ismi = models.CharField(max_length=100, blank=True, null=True)
    tarih = models.DateField()
    iha_kiralanan = models.ForeignKey("Iha", on_delete=models.CASCADE, null=True) # İlişkiyi tanımla




