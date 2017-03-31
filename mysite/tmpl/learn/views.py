from django.shortcuts import render

# Create your views here.
def home(request):
	string = u"我正在学习django"
	return render(request, 'home.html', {'string':string})

def trsf_list(request):
	tflist = ['html', 'css', 'javascript', 'python']
	tfdict = {'site':u'中文', 'content':u'技术'}
	numlist = map(str, range(100))
	return render(request, 'list.html', {'tflist':tflist, 'tfdict':tfdict, 'numlist':numlist})