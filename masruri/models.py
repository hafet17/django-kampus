from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):

    gender_choice = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    roll_no = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    full_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    gender = models.CharField(choices=gender_choice, max_length=100)

    def __str__(self):
        return self.full_name


class Custumer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    category = models.CharField(
        max_length=200, blank=True, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    custumer = models.ForeignKey(
        Custumer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.product.name
