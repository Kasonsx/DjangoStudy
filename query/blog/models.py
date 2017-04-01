from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Author(models.Model):
	name = models.CharField(max_length=50)
	qq = models.CharField(max_length=12)
	addr = models.TextField()
	email = models.EmailField()

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Article(models.Model):
	title = models.CharField(u'标题', max_length=50)
	#author = models.ForeignKey(Author)
	content = models.TextField(u'内容')
	#score = models.IntegerField()# 文章评分
	#tags = models.ManyToManyField('Tag')

	pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
	update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

	def __str__(self):
		return self.title

@python_2_unicode_compatible
class Person(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	def my_property(self):
		return self.first_name + ' ' + self.last_name
	my_property.short_description = "Full name of the person"

	full_name = property(my_property)


@python_2_unicode_compatible
class Tag(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

