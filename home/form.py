from django import forms


class FeedbackForm(forms.Form):
	"""Форма зворотнього зв'язку"""
	name = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=30)
	message = forms.CharField(widget=forms.Textarea)

	def __str__(self) -> str:
		return f'{self.name} - {self.email} // {self.message}'

