from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200 , blank=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.Category_name)
    #     super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.category_name)

    class Meta:
           verbose_name_plural = _("Category")
 

class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = _("QuantityVariant")

class ColourVariant(models.Model):
    colour_name = models.CharField(max_length=100)
    colour_code = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = _("ColourVariant")



class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100) 


    class Meta:
        verbose_name_plural = _("SizeVariant")

class product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  
    product_name = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='ststic/products') 
    price = models.CharField(max_length=20)
    description = models.TextField()
    stock = models.IntegerField(default=100)



    def __str__(self):
        return str(self.product_name)
    
    class Meta:
        verbose_name_plural = _("product")

