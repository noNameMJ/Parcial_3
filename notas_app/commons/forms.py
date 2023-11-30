from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	full_name = forms.CharField(required=True)

	class Meta:
		model = User
		fields = ("username", "full_name", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		full_name = self.cleaned_data['full_name']
		first_name, *last_name_parts = full_name.split()
		user.first_name = first_name
		user.last_name = ' '.join(last_name_parts)
		if commit:
			user.save()
		return user