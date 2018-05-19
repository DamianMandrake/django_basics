from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, phone, password, is_staff=False, is_admin=False, is_active=True):
        if not email or not phone or password:
            raise ValueError("insufficient information to create user")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.phone = phone
        user.set_password(password)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, phone, password):
        user = self.create_user(
            email=email,
            phone=phone,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, phone, password):
        user = self.create_user(
            email=email,
            phone=phone,
            password=password,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)

    phone = models.CharField(unique=True, max_length=10)

    verified = models.BooleanField(default=False)
    # registration token
    reg_token = models.TextField()

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    confirm_date = models.DateTimeField(auto_now_add=False)
    join_data = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # username, pwd are required by default
    REQUIRED_FIELDS = [


    ]

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_verified(self):
        return self.verified


# class UserInfo(models.Model):
#
#     # The user to whom this info belongs to
#     user_id = models.IntegerField()
#
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#
#     dob = models.DateField()
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     deleted = models.BooleanField(default=False)
#     deleted_at = models.DateTimeField(auto_now_add=False)
