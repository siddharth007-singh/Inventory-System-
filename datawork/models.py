from typing import Text
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import CharField, TextField
from django.utils import timezone
# from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_desc = models.TextField(null=True)
    cat_doc = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.cat_name



class Brand(models.Model):
    brand_name = models.CharField(max_length=200)
    brand_cxategory = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    brand_desc = models.TextField(null=True)
    brand_doc = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.brand_name


class Thickness(models.Model):
    thickness_name = models.CharField(max_length=200)
    thick_brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.thickness_name
    

class Size(models.Model):
    size_name = models.CharField(max_length=200)
    size_thick = models.ForeignKey(Thickness, on_delete=models.CASCADE, null=True)
    size_doc = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.size_name



class Product(models.Model):
    STOCK = (("0","show"),("1","hide"))
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to="product/", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_size = models.ForeignKey(Size, on_delete=models.CASCADE)
    product_thickness = models.ForeignKey(Thickness, on_delete=models.CASCADE)
    doc = models.DateTimeField(default=timezone.now)
    price = models.IntegerField(default=0)
    stock = models.CharField(max_length=100, choices=STOCK, default="0", null=True)

    def __str__(self):
        return self.name



class Profile(models.Model):
    # users = models.ForeignKey(User, on_delete=models.CASCADE)
    dp = models.ImageField(upload_to="product/")
    address = models.TextField()
    mobile = models.CharField(max_length=200)


    def __str__(self):
        return self.user.username


class Customer(models.Model):
    name = CharField(max_length=200)
    contact = models.CharField(max_length=200)
    address = models.TextField()


    def __str__(self):
        return self.name


class OrderProduct(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    qty = models.IntegerField(default=1)

    def __str__(self):
        return self.item.name

    def total_price(self):
        return self.qty * self.item.price

    def total_discount_price(self):
        return self.qty * self.item.discount_price

    def final_price(self):
        if self.item.discount_price:
            return self.total_discount_price()
        else:
            return self.total_price()

    def total_saving(self):
        return self.total_price() - self.total_discount_price()

    def total_stock(self):
        return self.item.quantity - self.qty


# class OrderPro(models.Model):
#     item = models.ForeignKey(Category, on_delete=DO_NOTHING)
#     ordered = models.BooleanField(default=False)
#     qty = models.IntegerField(default=1)

#     def __str__(self):
#         return self.cat.cat_name


class Order(models.Model):
    STATUS = (("Credit","Credit"),("Paid","Paid"))
    c_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderProduct)
    pay_method = models.CharField(max_length=100, choices=STATUS, null=True)
    discount_price = models.CharField(max_length=150, null=True, blank=True)
    start_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.c_id.name

    def get_total_amount(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.final_price()
        return total

    def get_actual_total_amount(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.total_price()
        return total

    def grand_total(self):
        if self.discount_price:
            return self.get_actual_total_amount() - float(self.discount_price)
        else:
            return self.get_actual_total_amount()



# class Ordering(models.Model):
#     STATUS = (("Credit","Credit"),("Paid","Paid"))
#     c_id = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
#     ordered = models.BooleanField(default=False)
#     items = models.ManyToManyField(OrderPro)
#     pay_method = models.CharField(max_length=100, choices=STATUS, null=True)
#     discount_price = models.CharField(max_length=150, null=True, blank=True)
#     start_date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.discount_price