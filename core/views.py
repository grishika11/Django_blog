from django.shortcuts import render,redirect
from .models import Core
from django.views.generic import ListView, DetailView, UpdateView, CreateView,DeleteView, View, TemplateView
from django.urls import reverse_lazy
from .forms import PostForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
class IndexView(ListView):
	model = Core
	template_name = 'index.html'
	context_object_name = 'index'

class SingleView(DetailView):
	model = Core
	template_name = 'single.html'
	context_object_name = 'post'

@method_decorator(staff_member_required,name='dispatch')
class PostView(ListView):
	model = Core
	template_name = 'post.html'
	context_object_name = 'post_list'

class AddView(CreateView):
	model = Core
	template_name = 'add.html'
	fields = '__all__'
	success_url = reverse_lazy('core:post')

class EditView(UpdateView):
	model = Core
	template_name = 'edit.html'
	fields = '__all__'
	pk_url_kwarg = 'pk'
	success_url = reverse_lazy('core:post')


class Delete(DeleteView):
	model = Core
	pk_url_kwarg = 'pk'
	success_url = reverse_lazy('core:post')
	template_name = 'delete.html'

class LoginView(TemplateView):

	def post(self,request):
		if request.method=='POST':
			username = request.POST['username']
			password = request.POST['password']

			user = authenticate(username = username,password=password)
			if user.is_staff:
				login(request,user)
				return HttpResponseRedirect('/post')
		else:
			template_name = 'admin_login.html'		



   