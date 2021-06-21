from django.db import models


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, blank=False, null=False)
    product_tag = models.CharField(max_length=70, blank=False, null=False)
    product_description = models.CharField(max_length=200, blank=True)
    product_image = models.ImageField(blank=True, upload_to='product_images/')
    product_price = models.IntegerField(blank=False, null=False)
    is_vegan = models.BooleanField(blank=False, null=False, default="YES")

    def __str__(self):
        detail = self.product_name
        return detail
