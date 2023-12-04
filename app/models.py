from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class User(models.Model):
    username = models.CharField(max_length=100)
    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Users'


class Item(models.Model):
    class Type(models.TextChoices):
        LOST = 'LOST',
        FOUND = 'FOUND'

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=255)
    type = models.CharField(
        max_length=100, choices=Type.choices, default=Type.FOUND
    )
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Items'
