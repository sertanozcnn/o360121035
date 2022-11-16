from django.db import models


class housesale(models.Model):
    housesale_ID = models.IntegerField(primary_key = True)
    housesale_title = models.CharField(max_length=30) 
    housesale_description= models.CharField(max_length=250)
    housesale_image= models.ImageField(upload_to='house',null=True,blank=True)
    def __str__(self):
        return self.housesale_title


class Users(models.Model):
   User_ID = models.IntegerField(primary_key = True)
   User_Name = models.CharField(max_length=20)
   User_LastName = models.CharField(max_length=20)  
   User_Mail = models.EmailField(max_length = 254)
   User_Date= models.DateField()

   def __str__(self):
        return self.User_Mail


class Price(models.Model):
   Price_ID = models.IntegerField(primary_key = True)
   Price_Number = models.CharField(max_length=20)
   Price_Special = models.CharField(max_length=20)  
   Price_Money= models.CharField(max_length=50) 
   Price_Line1= models.CharField(max_length=50) 
   Price_Line2= models.CharField(max_length=50) 
   Price_Line3= models.CharField(max_length=50) 
   Price_Line4= models.CharField(max_length=50) 
   Price_Line5= models.CharField(max_length=50) 
   Price_Line6= models.CharField(max_length=50) 
   Price_URL = models.URLField(max_length = 200)

   def __str__(self):
        return self.Price_Special
    
    
class House_Category(models.Model):
   House_Category_ID = models.IntegerField(primary_key = True)
   HouseType = models.CharField(max_length=20)
   def __str__(self):
        return self.HouseType
    
    
