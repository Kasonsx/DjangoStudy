from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

# /add/?a=3&b=4
def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))
# /add/3/4/
def add2(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))

def index(request):
	return render(request, 'home.html')

# 收藏的旧地址自动跳转到新地址
def old_add2_redirect(request, a, b):
	return HttpResponseRedirect(
            reverse('add2', args=(a, b))
		)