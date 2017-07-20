from django.db import models

# Create your models here.
class Treasure(models.Model):
	name = models.CharField(max_length=100)
	value = models.DecimalField(max_digits=10,
								decimal_places=2)
	material = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	image = models.ImageField(upload_to = 'treasure_images',
		default = 'media/default.png')

	def __str__(self):
		return self.name