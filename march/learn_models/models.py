from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()

	def __str__(self):
		return self.name

# 新建一个对象四种：
# 1
Person.objects.create(name=name, age=age)
# 2
p = Person(name='Yourname',age=23)
p.save()
# 3
p = Person(name='Yourname')
p.age = 23
p.save()
# 4.防止重复，会返回一个tuple元组，第一个参数为Person对象
# 第二个为True or False,新建时为True，已存在时为False
Person.objects.get_or_create(name='Yourname',age=23)