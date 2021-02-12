from django.shortcuts import render , redirect 
from django.urls import reverse_lazy
from django.views.generic import View , DetailView ,TemplateView , ListView , UpdateView ,CreateView , DeleteView
from usuario.models import Profile
from libro.models import Prestamo
from usuario.forms import UserCreateForm  , UpdatePrestamo




# Create your views here.




class List_prestamo(View):
	model = Prestamo
	from_class= UserCreateForm
	template_name = 'user/list_prestamo.html'
	success_url = reverse_lazy('usuario:create_userANDist_user')


	def get_queryset(self):

		return self.model.objects.all()



	def get_contex_data(self , **kwargs):

		self.object_list= self.get_queryset()
		context = {}
		context['list_prestamo']= self.object_list
		
		return context

	def get(self , request , *args , **kwargs):
		
		

		return  render(request , 'user/list_prestamo.html' , self.get_contex_data())




class detalle_prestamo(DetailView):

	model=Prestamo
	second_model= Prestamo
	template_name='user/detalle_prestamo.html'
	pk_url_kwarg= 'pk'
	queryset= model.objects.all()



class update_estado_prestamo(UpdateView):

	

	model=Prestamo
	from_class=UpdatePrestamo
	fields=['libro_entregado']
	template_name='user/editar_estado_prestamo.html'
	success_url = reverse_lazy('usuario:List_prestamo')










"""
codigo de creacion y lista de usuario 

"""


class CreateUserANDListUser(View):
	model = Profile
	from_class= UserCreateForm
	template_name = 'user/create_user.html'
	success_url = reverse_lazy('usuario:create_userANDist_user')


	def get_queryset(self):

		return self.model.objects.all()



	def get_contex_data(self , **kwargs):

		self.object_list= self.get_queryset()
		context = {}
		context['list_user']= self.object_list
		context['form']= self.from_class
		return context

	def get(self , request , *args , **kwargs):
		
		form = self.from_class(request.GET)

		return  render(request , self.template_name , self.get_contex_data())


	def post(self , request , *args , **kwargs):

		form = self.from_class(request.POST)

		if form.is_valid():
			form.save()
			return redirect(self.success_url)






class deleteUser(DeleteView):

	model = Profile
	template_name = 'user/delete_user.html'
	success_url = reverse_lazy('usuario:CreateUserANDListUser')


class updateUser(UpdateView):
	
	model= Profile
	fields=['first_name' , 'last_name' , 'email' , 'phone_number' ]
	from_class= UserCreateForm
	template_name = 'user/create_user.html'
	success_url = reverse_lazy('usuario:CreateUserANDListUser')	

	



	def get_context_data(self ,  **kwargs ):
		self.object_list= self.get_queryset()

		
		context = super().get_context_data(**kwargs)
		context['list_user']= self.model.objects.all()
		
		return context


	def get_object( self , **kwargs):
		print("hola estoy aqui")
		return self.model.objects.get(id=self.kwargs['pk'])


	



	







	



	
