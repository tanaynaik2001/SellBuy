from django.db import models
# Create your models here.

class addCrop(models.Model):
    addCropName = models.CharField(max_length=100)
    addCropPrice = models.IntegerField()
    addCropImg = models.ImageField(upload_to='pictures/')
    addCropDescription = models.CharField(max_length=500)
    addCropQuantity = models.IntegerField()
    addFarmerID = models.IntegerField()

    def __str__(self): 
        x = self.addCropName + " | Farmer ID: "+ str(self.addFarmerID)
        return x
        
class farmerData(models.Model):
    Name = models.CharField(max_length=30)
    Mobile_Number = models.IntegerField()
    Aadhar_no=models.IntegerField()

    def __str__(self):
        return self.Name
