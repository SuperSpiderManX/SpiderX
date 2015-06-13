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


class ServerInfo:
    def __init__(self):
        self.ip = ""
        self.port = ""
        self.serverName = ""
        self.groupName = ""
        self.comment = ""
        self.serverId = 0

def assetList(req):
    viewPage = "1"
    serverInfoList = []
    username = req.COOKIES.get('username','')
    usergroup = User.objects.get(username='xjt').group_set.all()
    allmachine = Group.objects.get(groupname='admin').machine_set.all()
    
    for i in allmachine:
        appendObj = ServerInfo()
        appendObj.serverName = i.name
        appendObj.ip = i.ip
        appendObj.port = i.port
        appendObj.user = i.loginuser
        appendObj.password = i.loginpassword
        appendObj.comment = ""
        
        serverInfoList.append(appendObj)
        print serverInfoList
        
    pageViewIndex = viewPage
    
    return render_to_response('assetList.html',{'serverInfoList':serverInfoList,"pageViewIndex":pageViewIndex})



def logout(req):
    response = HttpResponse('logout !!')
    response.delete_cookie('username')
    return response
