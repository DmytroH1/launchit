from django.db import models


class Category(models.Model):

	name = models.CharField(max_length=100, unique=True, null=False)

	def __str__(self) -> str:
		return str(self.name)


class Course(models.Model):

	name = models.CharField(max_length=100, unique=True, null=False)
	about = models.TextField(max_length=500, null=False)
	text = models.TextField(null=False, default="default text")
	photo = models.FileField(upload_to='courses/', null=False)
	price = models.IntegerField(null=False, default=10)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	url = models.SlugField(max_length=130, null=True)

	def __str__(self) -> str:
		return str(self.name)


class ApplicationForm(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	choice = models.CharField(max_length=50)
	call_time = models.CharField(max_length=120, blank=True, null=True)

	def __str__(self) -> str:
		return str(self.name)
