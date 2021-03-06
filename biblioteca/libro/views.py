from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views.generic import View , DetailView ,TemplateView , ListView , UpdateView ,CreateView , DeleteView
from libro.forms import Create_Book_form , Autor_Create_form , PrestamoForm , reservationForm
from usuario.forms import UserCreateForm 
from libro.models import Libro , Autor  , Prestamo  , reservation
from usuario.models import Profile , datos_prestamo_manejado_por_staff
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin


from django.conf import settings
from django.core.mail import send_mail

# Create your views here.


class inicio(TemplateView):
 
	template_name= "base.html"



 
class CreateBook(View):
	model= Libro
	form_class= Create_Book_form
	template_name='usuario_template/createLibro.html'

	success_url= reverse_lazy('libro:list_book')



	def get(self , request , *args , **kwargs):
		form=self.form_class

		return render(request , self.template_name , {'form':form})


	def post(self , request , *args , **kwargs):

		form = self.form_class(request.POST)

		if form.is_valid():
			#print(form.cleaned_data)
			form.save()

			return redirect(self.success_url)

			




def success(request):

	return render(request , 'usuario_template/success.html')				





def ListBook(request):
	queryset= request.GET.get("buscar")
	books = Libro.objects.filter(estado=True)
	if queryset:
		books = Libro.objects.filter(
			titulo__icontains = queryset)

	paginator = Paginator(books , 8)
	page= request.GET.get("page")
	books = paginator.get_page(page)	
		
	return render(request , 'usuario_template/ListBook.html' , {'books':books})








class updateBook(UpdateView):

	model = Libro
	form_class= Create_Book_form
	

	template_name='usuario_template/createLibro.html'
	success_url= reverse_lazy('libro:list_book')



class DeleteBook(DeleteView):

	model = Libro

	template_name='usuario_template/DeleteLibro.html'

	success_url= reverse_lazy('libro:list_book')

	def post(self, request , pk  , *args , **kwargs):

		date= self.model.objects.get(id=pk)

		date.estado= False
		date.save()

		return redirect(self.success_url)



class CreateAutor(CreateView):

	model= Autor

	form_class=Autor_Create_form
	template_name = 'autor_template/createAutor.html'

	success_url= reverse_lazy('libro:list_autor')



class ListAutor(ListView):


	model=Autor
	template_name= 'autor_template/ListAutor.html'




	def get_queryset(self):

		return  self.model.objects.filter(estado=True)



	def get_context_data(self , **kwargs):

		self.object_list= self.get_queryset()

		context= super().get_context_data(**kwargs)

		context['Autor']= self.object_list

		return context



class updateAutor(UpdateView):

	model = Autor
	form_class= Autor_Create_form
	

	template_name='autor_template/createAutor.html'
	success_url= reverse_lazy('libro:list_autor')



class DeleteAutor(DeleteView):

	model = Autor

	template_name='autor_template/DeleteAutor.html'

	success_url= reverse_lazy('libro:list_autor')

	def post(self, request , pk  , *args , **kwargs):

		date= self.model.objects.get(id=pk)

		date.estado= False
		date.save()

		return redirect(self.success_url)	




class Prestamo(DetailView):
	model = Libro
	second_model = datos_prestamo_manejado_por_staff
	third_model = Prestamo
	form_class= UserCreateForm
	second_form_class= PrestamoForm
	template_name= 'usuario_template/prestamo.html'
	pk_url_kwarg= 'pk'
	queryset= model.objects.all()


	def  get_context_data(self , **kwargs):

		amount_count= self.model.objects.get(id = self.kwargs['pk'] )

		info_prestamo=self.third_model.objects.filter(libro_id=self.kwargs['pk'] , libro_prestado=True , libro_entregado=False)
		
		count= 0
		for dato in info_prestamo:

			print(dato)
			count+=1
		
		context= super().get_context_data(**kwargs)


		
		self.object = self.get_object()
		
		

		if count< amount_count.cantidad_existente:
			context['form']= self.form_class

		if count>= amount_count.cantidad_existente:
			
			no_hay_libro = "¡No hay libro disponible para hacer prestamo!"	
			context['no_hay']= no_hay_libro

		return context


	def get(self , request , *args , **kwargs):
		self.object = self.get_object()
		return render(request , self.template_name , self.get_context_data())



	def get_object( self , **kwargs):
		
		
		return self.model.objects.get(id=self.kwargs['pk'])	



	def post(self , request ,  *args , **kwargs):
		
		form = self.form_class(request.POST)

		if form.is_valid():
			
			form.save()

			
			#print(info_prestamo)
			#if self.kwargs['pk']
			#profile = self.third_model()

			
		
			var_person = self.second_model.objects.all().order_by('-create')[0]
			tipo = datos_prestamo_manejado_por_staff.objects.get(pk = var_person.id)
			"""
			in var tipo saving the object because i can't save an int for the relation fk
			and thisis the shape salvando.libro_id.add(self.kwargs['pk'])  of save un 
			manytomany
			"""
			salvando=  self.third_model.objects.create(user_id=tipo)
			salvando.libro_id.add(self.kwargs['pk'])
			salvando.save()
			
			return redirect('usuario:List_prestamo')	
			#data={ 'libro_id':profile.libro_id.set(self.kwargs['pk']), 'user_id':profile.user_id}
			#salvando=  self.third_model.objects.create(profile)

		else:
			#import pdb;pdb.set_trace()
			

			amount_count= self.model.objects.get(id = self.kwargs['pk'] )

			return render(request , 'usuario_template/prestamo.html' ,  {'form':form , 'object': amount_count} )	
		


class Create_request_Book(CreateView):
	model = reservation
	second_model = Profile
	form_class = reservationForm
	template_name='usuario_template/reservation.html'
	success_url=reverse_lazy('libro:list_book')


	def  get_context_data(self , **kwargs):

		context = super().get_context_data(**kwargs)

		context['form']= self.form


		return context




	def get(self , request , *args , **kwargs):
	
		form= reservationForm()
		print(form)
		print("estoy en la funcion get")

		return render(request , 'usuario_template/reservation.html' ,{'form':form})


	def post(self , request , *args , **kwargs):

		form = reservationForm(request.POST)

		save_reservation = self.model()
		
		#import pdb;pdb.set_trace()

		if form.is_valid():
			
			person = self.second_model.objects.get(id = request.user.profile.pk)

			data= form.cleaned_data

			save_reservation.user_id= person
			save_reservation.titulo_libro= data['titulo_libro']
			save_reservation.autor_libro= data['autor_libro']
			save_reservation.cantidad_solicitada= data['cantidad_solicitada']
			save_reservation.descripcion= data['descripcion']

			save_reservation.save()

			return redirect('libro:lista__usuario_activa')
		else:
			#import pdb;pdb.set_trace()
			

			print(form.errors)
			print("estoy en la funcion get")	

			return render(request , 'usuario_template/reservation.html' ,  {'form':form} )


			 

			


class show_success_reservation (TemplateView):

	template_name = 'usuario_template/success_reservation.html'



class list_reservation_active(ListView):

	model = reservation
	template_name = 'usuario_template/list_reservation_active.html'
	queryset = model.objects.filter(estado = True )


class reservation_usuario_active(ListView):

	model = reservation
	template_name = 'usuario_template/list_reservation_para_usuario_active.html'
	#queryset = model.objects.filter(estado = True )



	def get_context_data(self , **kwargs):

		context = super().get_context_data(**kwargs)
		
		context['date'] = self.model.objects.filter(user_id= self.request.user.profile, estado = True )

		return context


class list_reservation_no_active(ListView):

	model = reservation
	template_name = 'usuario_template/list_reservation_no_activa.html'
	queryset = model.objects.filter(estado = False )	



class sent_email_to_user(DetailView):


	model = reservation
	template_name= 'usuario_template/Email.html'
	pk_url_kwarg= 'pk'
	queryset= model.objects.all()

	

	def post(self , request , *args , **kwargs):

		var = self.model.objects.get(id = self.kwargs['pk'])






		subjects= request.POST["asunto"]

		message= request.POST["mensaje"] 
		email_from=settings.EMAIL_HOST_USER

		RECIPIENT_LIST=[var.user_id.email]

		send_mail(subjects , message , email_from , RECIPIENT_LIST)

		var.estado = False

		var.save()
		return redirect('libro:lista_activa')

		
	


			




		
			

			

	






	
