from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    CASHIER = 1
    MANAGER = 2
    ADMIN = 3
    ROLE_CHOICES = (
        (CASHIER, 'Cashier'),
        (MANAGER, 'Manager'),
        (ADMIN, 'Admin'),
    )
    MALE = 1
    FEMALE = 2
    NULL = 3
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NULL, 'null'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photo/', default='photo/foto.jpg')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, default=1)
    phone_number = models.CharField(max_length=30, blank=True, null=True, default=None)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, blank=True, default=NULL)

    def __str__(self):
        return self.user.username
