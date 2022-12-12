from django.db import models


class Subscribe(models.Model):
	"Підписка на новини"
	email = models.EmailField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email
