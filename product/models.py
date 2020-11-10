from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	Nama		 = models.CharField(max_length=120)
	NoIdentitas	 = models.CharField(max_length=120)
	NIK			 = models.DecimalField(decimal_places=0, max_digits=1000000000)
	email		 = models.CharField(max_length=120)
	Password	 = models.CharField(max_length=20)
	Telepon		 = models.CharField(max_length=12)
	active		 = models.BooleanField(default=True)

	def get_absolute_url(self):
		return reverse("dynamic",kwargs={"my_id": self.id})