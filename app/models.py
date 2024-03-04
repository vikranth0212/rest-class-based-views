from django.db import models

# Create your models here.
class Product_cart(models.Model):
    product_cart_id=models.IntegerField(primary_key=True)
    product_cart_name=models.CharField(max_length=100)

    def __str__(self):
        return self.product_cart_name

    


class product(models.Model):
    product_cart_id=models.ForeignKey(Product_cart,on_delete=models.CASCADE)
    pname=models.CharField(max_length=100)
    price=models.IntegerField()
    brand=models.CharField(max_length=100)
    price=models.IntegerField()
    pid=models.IntegerField()

    def __str__(self):
        return self.pname
  
