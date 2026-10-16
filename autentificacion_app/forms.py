from django import forms
# de la tabla user que viene por defecto en django
from django.contrib.auth.models import User
# viene por defecto en django para la creacion de formularios y es una clase
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
   email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm'}))

   class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']

   def __init__(self, *args, **kwargs):
       super(UserRegistrationForm, self).__init__(*args, **kwargs)
       for fieldname in ['username', 'password1', 'password2']:
           self.fields[fieldname].widget.attrs['class'] = 'form-control form-control-sm'