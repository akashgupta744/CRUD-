from django.db import models

# Create your models here.

class Product(models.Model):
    pro_id = models.IntegerField(primary_key = True)
    pro_name = models.CharField(max_length = 100)
    pro_price = models.DecimalField(max_digits=10, decimal_places=2)
    pro_desc = models.CharField(max_length = 100)
    pro_img = models.ImageField(upload_to = 'Product Img')
    
    def __str__(self):
        return self.pro_name
    