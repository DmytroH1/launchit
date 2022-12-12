from django.db import models
from django.urls import reverse


class News(models.Model):

	name = models.CharField(max_length=100, unique=True, null=False)
	topic = models.CharField(max_length=200, unique=True, null=False)
	text = models.TextField(null=False)
	photo = models.FileField(upload_to='news/', null=False)
	date = models.DateField()

	url = models.SlugField(max_length=130, null=True)

	def __str__(self) -> str:
		return str(self.name)

	def get_absolute_url(self):
		return reverse('post', kwargs={'slug': self.url})