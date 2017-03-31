from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.urls import reverse

# def index(request):
# 	return HttpResponse(u"Welcome to django!")

def index(request):
	return render(request, 'home.html')

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

def add2(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

def old_add2_redirect(request, a, b):
	return HttpResponseRedirect(reverse('add2', args=(a, b)))

# 传递变量到访问的页面
def home(request):
	string = u'我是被传递的字符串。'
	List = ['html','css','javascript','python']
	Dict = {'en':'英语','cn':'中文'}

	return render(request, 'home.html', {'string':string, 'List':List, 'Dict':Dict})
	




