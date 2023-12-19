from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Phone number must be set')

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(phone_number, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone_validator = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Yaroqsiz telefon raqam!"
    )
    phone_number = models.CharField(
        max_length=25,
        validators=[phone_validator],
        null=True,
        blank=True,
        unique=True
    )
    username = models.CharField(max_length=155, unique=False, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, null=True, blank=True)
    activation_key_expires = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'

    def save(self, *args, **kwargs):
        # Aktivatsiya muddatini offset-naive qilamiz
        if self.activation_key_expires:
            self.activation_key_expires = timezone.make_naive(self.activation_key_expires)

        super().save(*args, **kwargs)


class UserProfile(models.Model):
    class Gender(models.TextChoices):
        MALE = 'MALE'
        FEMALE = 'FEMALE'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=Gender.choices)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Item(models.Model):
    class Type(models.TextChoices):
        LOST = 'LOST',
        FOUND = 'FOUND'

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_validator = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Yaroqsiz telefon raqam!"
    )
    contact_info = models.CharField(
        max_length=25,
        validators=[phone_validator],
        null=True,
        blank=True,
        unique=True
    )
    type = models.CharField(
        max_length=100, choices=Type.choices, default=Type.FOUND
    )
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    more = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Items'


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    related_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='related_item')
