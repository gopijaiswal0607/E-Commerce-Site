from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField # use of auto matic increatment 
    product_name = models.CharField(max_length=50)
    category= models.CharField(max_length=50 , default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images" , default="")
    # No need to make migrations becasuse we are not changing the models

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msgid = models.AutoField(primary_key=True) # use of auto matic increatment 
    name = models.CharField(max_length=50)
    email= models.CharField(max_length=50 , default="")
    phone = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=500)
    # No need to make migrations becasuse we are not changing the models

    def __str__(self):
        return self.name

