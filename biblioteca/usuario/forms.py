from django import forms 
from usuario.models import Profile 

from libro.models import  Prestamo





class UserCreateForm(forms.ModelForm):

	class Meta:
		model=Profile

		fields=('first_name' , 'last_name' , 'email' , 'phone_number' )



		labels={
			'first_name':'nombre',
			'last_name': 'Apellido',
			'email': 'Email',
			'phone_number': 'Numero telefonico',
			
			


		}

		widgets={

		'first_name': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Ingrese Nombre' }),
		'last_name': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Ingrese Apellido' }),
		'email': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Ingrese correo electronico' }),
		'phone_number': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Ingrese numero telefonico' }),
		
		
		

		}





class UpdatePrestamo(forms.ModelForm):


	class Meta:
		model=Prestamo

		fields=('libro_entregado',)



		labels={
			'libro_entregado':'Libro entregado'
			
			


		}

		widgets={

			'libro_entregado': forms.Select(),
		
		
		

}