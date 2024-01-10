from distutils.command.upload import upload
from email.policy import default
from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    Name = models.CharField(max_length=20)

    def __str__(self):
        return self.Name

class Product(models.Model):
    Name = models.CharField(max_length=200)
    Author_Name = models.CharField(max_length=200)
    desc = models.TextField(max_length=200000)
    Price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to= 'pics', default=1)
    populer = models.BooleanField(default=False)
    tranding = models.BooleanField(default=False)  
    top = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "books"

    def __str__(self):
        return self.Name


class Contact(models.Model):
    name = models.CharField(max_length=111)
    email = models.CharField(max_length=111)
    phone = models.IntegerField()
    subject = models.CharField(max_length=111)
    message = models.TextField(max_length=11111)

    class Meta:
        verbose_name_plural = "contact"

    def __str__(self):
        return self.name



class Orders(models.Model):
    name = models.CharField(max_length=111)
    email = models.CharField(max_length=111)
    City = models.CharField(max_length=111)
    Address = models.CharField(max_length=111)
    Zip_code = models.CharField(max_length=111)
    State = models.CharField(max_length=111)
    phone = models.IntegerField()
    Book = models.CharField(max_length=111)
    price = models.IntegerField()

    class Meta:
        verbose_name_plural = "orders"
    
    def __str__(self):
        return self.name

class Upcoming(models.Model):
    Name = models.CharField(max_length=200)
    Author_Name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(upload_to= 'pics', default=1)
    class Meta:
        verbose_name_plural = "upcoming"
    def __str__(self):
        return self.Name

class Slider(models.Model):
    img = models.ImageField(upload_to= 'pics',help_text = "use png image")
    t1 = models.CharField(max_length=200)
    t2 = models.CharField(max_length=200)
    t3 = models.CharField(max_length=200)
    t4 = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "slider"
    def __str__(self):
        return self.Name

class Testimonials(models.Model):
    name = models.CharField(max_length=111)
    work = models.CharField(max_length=111)
    desc = models.TextField(max_length=2000)

class Working(models.Model):
    name = models.CharField(max_length=111)
    post = models.CharField(max_length=111)
    img = models.ImageField(upload_to= 'pics',help_text = "use png image")





        