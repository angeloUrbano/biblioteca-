from django import forms

from libro.models import Libro , Autor , Prestamo


class Create_Book_form(forms.ModelForm):


	

	#titulo = forms.CharField(max_length=200)
	#book_picture = forms.ImageField(required=False)
	#cantidad_existente= forms.IntegerField()


	class Meta:
		model=Libro

		fields=('titulo' ,  'cantidad_existente' , 'autor_id')



		labels={
			'titulo':'Titulo',
			
			'cantidad_existente': 'Cantidad de libros',
			'autor_id':'Autor'
			


		}

		widgets={

		'titulo': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Ingrese titulo' }),
		
		'cantidad_existente': forms.NumberInput(attrs={'class':'form-control' , 'placeholder':'Ingrese la cantidad de lirbos'}),
		

		}




class Autor_Create_form(forms.ModelForm):



	class Meta:
		model=Autor

		fields=('nombre' , 'apellido' , 'descripcion')



		labels={
			'nombre':'Nombre del autor',
			'apellido': 'apellido del autor',
			
			'descripcion':' pequeña descripcion',


		}

		widgets={

		'nombre': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Ingrese el nombre del autor' ,'id':'nombre'}),
		'apellido': forms.TextInput(attrs={'class':'form-control' , 'placeholder':'Ingrese el apellido del autor','id':'apellido'}),
		
		'descripcion': forms.Textarea(attrs={'class':'form-control' , 'placeholder':'Ingrese una pequeña descripcion','id':'descripcion'}),

		}	




class PrestamoForm(forms.ModelForm):



	class Meta:
		model=Prestamo

		fields=('libro_id' , 'user_id' )

