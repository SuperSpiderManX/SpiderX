from django.shortcuts import render_to_response
from django.template import loader, Context, Template
from django.http import HttpResponse
from blog.models import Employee
from django import forms

class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
	self.item = {'1':'test1','2':'test2','3':'test3'}
	#self.item = [1,2,3]

    def say(self):
        return  "I'm " + self.name

def index(req):
    users = {'name':'tom','age':23,'sex':'male'}
    user = Person('tom',23,'male')
    book_list =  ['python','java','php','c++','web']
    return render_to_response('index.html',{'title':'my page','user':user,'book_list':book_list,'users':users})

def index1(req):
    t = loader.get_template('index.html')     
    c = Context({'uname':'alen'})
    html = t.render(c)
    return HttpResponse(html)
    #return HttpResponse(t.render(c))

def index2(req):
    t = Template('<h1>hello {{uname}}</h1>')
    c = Context({'uname':'tmac'})
    return HttpResponse(t.render(c))

def index3(req):
	emps = Employee.objects.all()
	return render_to_response('index3.html',{'emps':emps})

class UserForm(forms.Form):
	username = forms.CharField()
	headimg = forms.FileField()
	
def register(req):
	if req.method == 'POST':
		form = UserForm(req.POST, req.FILES)
		if form.is_valid():
			print form.cleaned_data['username']
			print form.cleaned_data['headimg'].name
			print form.cleaned_data['headimg'].size
			fileupload = file('/upload/' +  form.cleaned_data['headimg'].name,'wb')
			source = form.cleaned_data['headimg'].read()
			fileupload.write(source)
			fileupload.close()
			return HttpResponse('ok')
	else:
		form = UserForm()
	return render_to_response('register.html',{'form':form})
