from django.db import models

# Create your models here.
class GoldHistory(models.Model):
    years = models.CharField(max_length=50)
    returns = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.years


class MutualFundData(models.Model):
    MutualFundHouseTop10 = models.CharField(max_length=100)
    Column2= models.CharField(max_length=100)
    Column3= models.CharField(max_length=100)
    Column4= models.CharField(max_length=100)
    Column5= models.CharField(max_length=100)
    Column6= models.CharField(max_length=100)
    


    def __str__(self) -> str:
        return self.MutualFundHouseTop10



class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=150)

    


    