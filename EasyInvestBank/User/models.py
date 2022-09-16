import random

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from .constants import COUNTRY_CHOICES, CURRENCY_CHOICES


class AccountManager(BaseUserManager):
    def create_user(
        self, email, date_of_birth, 
        full_name, address, country, 
        password=None
    ):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            full_name=full_name,
            address=address,
            country=country,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email,
        date_of_birth,
        full_name,
        address,
        country,
        password=None
    ):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            full_name=full_name,
            address=address,
            country=country,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    def create_random_iban():
        not_unique = True
        while not_unique:
            unique_number = random.randint(100000000000, 999999999999)
            if not Account.objects.filter(IBAN=unique_number):
                not_unique = False
        return str(unique_number)

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    full_name = models.CharField(
        verbose_name='Full Name',
        max_length=100,
    )
    address = models.CharField(max_length=100)
    country = models.CharField(
        verbose_name='Country', 
        max_length=50, 
        choices=COUNTRY_CHOICES, 
        default='LT'
    )
    IBAN = models.CharField(
        max_length=16, 
        default=create_random_iban
    )
    balance = models.DecimalField(
        max_digits=20, 
        decimal_places=2, 
        default=0
    )
    currency = models.CharField(
        max_length=5, 
        default='EUR', 
        choices=CURRENCY_CHOICES
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'full_name', 'address', 'country']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin