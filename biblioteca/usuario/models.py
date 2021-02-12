from django.db import models


# Create your models here.




class Profile(models.Model):

	first_name= models.CharField(max_length=50)
	last_name= models.CharField( max_length=50)
	email = models.CharField(max_length=70)
	phone_number= models.CharField(max_length=20 , blank=True)
	create = models.DateTimeField(auto_now_add=True)
	modified= models.DateTimeField(auto_now= True)

	def __str__(self):
		return '{}'.format(self.first_name , self.id)   