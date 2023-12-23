from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_t = models.IntegerField(default=1) 
    #user_type = 1 = unAuthurised user, 2 = admin, 3 = manager
    
    user_image = models.ImageField(upload_to='user_pic/', blank= True, null= True)



class cuostomer(models.Model):
    username = models.CharField(max_length=220, unique=True)
    first_name = models.CharField(max_length=220)
    mobile_number = models.CharField(max_length=220)
    password = models.CharField(max_length=220)


    @staticmethod
    def get_customer_by_username(xyz):
        try:
            return cuostomer.objects.get(username = xyz)
        except:
            return False
        
    
    def get_customer_by_password(password):
        try:
            return cuostomer.objects.get(username = password)
        except:
            return False



class category(models.Model):
    category_name        = models.CharField(max_length=200)
    category_image       = models.ImageField(upload_to='category/', blank=True, null=True)

class product(models.Model):
    product_name      = models.CharField(max_length=200)
    product_new_price = models.FloatField()
    product_old_price = models.FloatField()
    product_description = models.TextField()
    product_category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='cat')
    produ_image       = models.ImageField(upload_to='product/', blank=True, null=True)

class product_image(models.Model):
    product_image_all = models.ImageField(upload_to='product/', blank=True,null=True)
    product_table = models.ForeignKey(product, on_delete=models.CASCADE, related_name='product')
