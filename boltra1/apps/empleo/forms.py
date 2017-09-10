from django import forms
from .models import Empresa

class DateInput(forms.DateInput):
    input_type = 'date'

class RegistroForm(forms.ModelForm):

	class Meta:
		model = Empresa

		fields = [
			'usuario',
			'contrasenia',
			'nombreEmpresa',
			'telefono',
			'email',
			'ubicacion',
			'rubro',
		]
		#labels = {
		#	'nombre':'Nombre',
		#	'fechaDeNacimiento':'Fecha de Nacimiento',
		#	'contrasenia': 'Contrasenia',
		#	'email':'E-mail',
		#}
		widgets = {
			'usuario': forms.TextInput(),
			'contrasenia': forms.PasswordInput(),
			'nombreEmpresa': forms.TextInput(),
			'telefono': forms.TextInput(),
			'email': forms.EmailInput(),
			'ubicacion': forms.Textarea(),
			'rubro': forms.TextInput(),
		}