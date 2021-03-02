from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name= models.CharField(max_length=50)
	last_name= models.CharField( max_length=50)
	email = models.CharField(max_length=70)
	phone_number= models.CharField(max_length=20 , blank=True)
	create = models.DateTimeField(auto_now_add=True)
	modified= models.DateTimeField(auto_now= True)

	def __str__(self):
		return '{}'.format(self.first_name , self.id)


class datos_prestamo_manejado_por_staff(models.Model):
	
	first_name= models.CharField(max_length=50)
	last_name= models.CharField( max_length=50)
	cedula = models.IntegerField(unique=True)
	email = models.CharField(max_length=70)
	phone_number= models.CharField(max_length=20 , blank=True)
	create = models.DateTimeField(auto_now_add=True)
	modified= models.DateTimeField(auto_now= True)

	def __str__(self):
		return '{}'.format(self.first_name , self.id)






