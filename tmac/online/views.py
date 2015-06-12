#-*- coding: UTF-8 -*-   
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User,Group,Machine

class UserForm(forms.Form):
	username = forms.CharField(label='用户的名',max_length=100)
	password = forms.CharField(label='密码',widget=forms.PasswordInput())

def regist(req):
	if req.method == 'POST':
		uf = UserForm(req.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			User.objects.create(username=username,password=password,role=1)
			return HttpResponse('regist success!!')
	else:
		uf = UserForm()
	return render_to_response('regist.html',{'uf':uf}, context_instance=RequestContext(req))

def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                response = HttpResponseRedirect('/online/index/')
                response.set_cookie('username',username,3600)
                return response
            else:
                return HttpResponseRedirect('/online/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))


def loginVerify(req):
    if req.method == 'GET':
            username = req.GET['username']
            password = req.GET['password']
            print username,password 
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
				return HttpResponse('success')
            else:
				return HttpResponse('failed')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})

def logout(req):
    response = HttpResponse('logout !!')
    response.delete_cookie('username')
    return response
