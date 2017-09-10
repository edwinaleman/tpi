# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def pagInicial(request):
	facultad=Facultad.objects.all()
	return render(request, 'inicio.html', {'facultad': facultad})

def registro(request):
	if request.method=='POST':
		form = RegistroForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('empleo:pag_reg')
	else:
		form=RegistroForm()
	return render(request, 'usuario/registro.html', {'form': form})

def inicioSesion(request):
	empresa=Empresa.objects.all()
	return render(request, 'usuario/inicioSesion.html', {'empresa': empresa})

#def validate(request):
 #   username = request.POST.get('username', False)
  #  users = user.objects.get(username=username)
   # if users.password == request.POST['password']:
    #        request.session['member_id'] = users.id
     #       return HttpResponseRedirect('/profile/view/' + users.username)
      #      # return render(request, 'user/view_profile.html', {'user': users})
    #else:
     #   return HttpResponseRedirect('/login/')