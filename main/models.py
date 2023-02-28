from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, user_id, name, date_of_birth, school, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not user_id:
            raise ValueError('Users must have an user_id')

        user = self.model(
            user_id=user_id,
            name=name,
            date_of_birth=date_of_birth,
            school=school,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, name, password, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            user_id,
            name,
            '2005-07-01',
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    user_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=40, default='')
    date_of_birth = models.DateField()
    school = models.CharField(max_length=40, default='')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['name', 'school']

    def get_id(self):
        # The user is identified by their email address
        return self.user_id

    def __str__(self):
        # __unicode__ on Python 2
        return self.user_id

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


class UserInfo(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=40, default='')
    intro = models.CharField(max_length=511, default= '', blank=True)
    skills = models.CharField(max_length=511, default= '', blank=True)
    experience = models.CharField(max_length=511, default= '', blank=True)
    initiatives = models.CharField(max_length=511, default= '', blank=True)

    def __str__(self):
        return self.user_id


