from django.db import models

# Create your models here.

class addCrop(models.Model):
    addCropName = models.CharField(max_length=100)
    addCropPrice = models.IntegerField()
    addCropImg = models.ImageField(upload_to='pictures/')
    addCropDescription = models.CharField(max_length=500)

    def __str__(self): 
        return self.addCropName