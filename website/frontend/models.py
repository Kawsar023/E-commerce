from django.db import models
from adminpanel.models import cuostomer,product

class wishlist(models.Model):
    prd = models.ForeignKey(product,on_delete=models.SET_NULL,blank=True,null=True)
    cust = models.ForeignKey(cuostomer,on_delete=models.SET_NULL,blank=True,null=True)
    wish_date = models.DateField(auto_now=True)

class check_out(models.Model):
    custom_user = models.ForeignKey(cuostomer,on_delete=models.SET_NULL,blank=True,null=True)
    prod = models.ForeignKey(product,on_delete=models.SET_NULL,blank=True,null=True)
    checkout_date = models.DateField(auto_now=True)
    prodct_qtt = models.IntegerField(default=1)