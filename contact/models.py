from django.db import models

# Create your models here.
class Info(models.Model):
    
    email = models.EmailField(max_length=254)
    Phone_1 = models.CharField( max_length=20)
    Phone_2 = models.CharField( max_length=20)
    palce = models.CharField(max_length=50)
    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")

    def __str__(self):
        return self.email
