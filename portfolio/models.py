from django.db import models




class Exp_Model (models.Model):
    Job_name = models.CharField( max_length=200)
    Job_place = models.CharField( max_length=150)
    Job_Date_From =models.CharField(max_length=50)
    Job_Date_To =models.CharField(max_length=50)
    class Meta:
        verbose_name = ("Exp_Model")
        verbose_name_plural = ("Exp_Models")

    def __str__(self):
        return self.Job_name

class Info_Model (models.Model):
    name = models.CharField(max_length=50)
    cv_link = models.CharField(max_length=254)
    created_at =models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = ("Info_Model")
        verbose_name_plural = ("Info_Models")

    def __str__(self):
        return self.name



class Portfolio_Model(models.Model):
    project_name = models.CharField(max_length=100)
    project_Img = models.ImageField(upload_to='images/')
    project_desc = models.CharField(max_length=100)
    class Meta:
        verbose_name = ("Portfolio_Model")
        verbose_name_plural = ("Portfolio_Models")

    def __str__(self):
        return self.project_name
