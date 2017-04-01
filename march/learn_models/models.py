from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()

	def __str__(self):
		return self.name

# 新建一个对象四种：
# 1
# Person.objects.create(name=name, age=age)
# # 2
# p = Person(name='Yourname',age=23)
# p.save()
# # 3
# p = Person(name='Yourname')
# p.age = 23
# p.save()
# # 4.防止重复，会返回一个tuple元组，第一个参数为Person对象
# # 第二个为True or False,新建时为True，已存在时为False
# Person.objects.get_or_create(name='Yourname',age=23)

# # 获取对象有以下方法：
# # 1。获取所有
# Person.objects.all()
# # 2.切片操作，获取前10个，但不支持负索引
# Person.objects.all()[:10]
# # 3.获取一个名字为name
# Perosn.objects.get(name="abc")
# # 4.获取所有名字严格为"abc"，相当于Person.objects.filter(name__exact="abc")
# Person.objects.filter(name="abc")
# # 5.名字为abc但不区分大小写，能匹配ABC,Abc,aBC
# Person.objects.filter(name__iexact="abc")
# # 6.名字包含abc
# Person.objects.filter(name__contains="abc")
# # 7.名字包含abc,但不分大小写
# Person.objects.filter(name__icontains="abc")
# # 8.通过正则表达式查询
# Person.objects.filter(name__regex="^abc")
# Person.objects.filter(name__iregex="^abc")#不分大小写
