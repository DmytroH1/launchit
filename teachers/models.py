from django.db import models


class Teachers(models.Model):

	name = models.CharField(max_length=100, unique=True, null=False)
	about = models.TextField(null=False)
	photo = models.FileField(upload_to='teachers/', null=False)
	email = models.CharField(max_length=100, unique=True, null=False)
	age = models.CharField(max_length=50, null=False)
	salary = models.IntegerField(null=False)

	def __str__(self) -> str:
		return str(self.name)
