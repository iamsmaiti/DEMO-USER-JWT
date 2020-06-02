from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager)

class UserManager(BaseUserManager):
	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError('email must be there')
		try:
			with transaction.atomic():
				user= self.model(email=email, **extra_fields)
				user.set_password(password)
				user.save(using=self._db)
		except:
			raise
	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_stuff', True)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password=password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_stuff', True)
		extra_fields.setdefault('is_superuser', True)
		return self._create_user(email, password=password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
	email= models.EmailField(max_length=30, unique=True)
	first_name= models.CharField(max_length=15, blank=True)
	last_name= models.CharField(max_length=15, blank=True)
	date_joined= models.DateTimeField(default=timezone.now)
	is_active= models.BooleanField(default=False)
	is_stuff= models.BooleanField(default=True)

	objects= UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name']

	def save(self, *args, **kwargs):
		super(User, self).save(*args, **kwargs)
		return self

