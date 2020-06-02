from django.db import models

# Create your models here.
class Item(models.Model):
	title = models.CharField(max_length=20)
	descripyion = models.TextField(max_length=200)
	category = models.CharField(max_length=10)
	price= models.IntegerField()
	seller= models.CharField(max_length=15)

	def __str__(self):
		return self.title


