from django.db import models

# Create your models here.
class Category(models.Model):
    service_name= models.CharField(max_length=200)
    stage = models.CharField(max_length = 50)
    price = models.FloatField()

    def __str__(self):
        return self.service_name

class Service(models.Model):
    service_available= models.CharField(max_length=200)
    details= models.TextField()
    images= models.ImageField(upload_to='media')

    def __str__(self):
        return self.service_available
#
class Ourdentist(models.Model):
    name= models.CharField(max_length=200)
    specialization= models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    facebook = models.URLField('facebook Address', blank=True)
    twitter = models.URLField('twitter Address', blank=True)
    images = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

class Testimony(models.Model):
    name= models.CharField(max_length=200)
    review= models.TextField()
    images = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name


class Appointment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name= models.CharField(max_length=20)
    your_phone = models.IntegerField()
    email= models.EmailField(max_length=50)
    address= models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    message= models.TextField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name