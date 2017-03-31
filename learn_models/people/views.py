from django.shortcuts import render
from people.models import Person
# Create your views here.
def index(request):
	return render(request, 'addperson.html')

def add_person(request):
	name = request.GET['name']
	age = request.GET['age']
	p = Person(name=name, age=age)
	p.save()

