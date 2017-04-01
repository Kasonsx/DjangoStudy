from django.contrib import admin

# Register your models here.
from .models import Article, Person

class MyModelAdmin(admin.ModelAdmin):
	def get_queryset(self, request):#根据不同的人显示不同的内容列表
		qs = super(MyModelAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		else:
			return qs.filter(author=request.user)

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','pub_date','update_time')

	def save_model(self, request, obj, form, change):
		if change:#更改时
			obj_original = self.model.objects.get(pk=obj.pk)
		else:
			obj_original = None
		obj.user = request.user
		obj.save()

	def delete_model(self, request, obj):
		obj.delete()

class PersonAdmin(admin.ModelAdmin):
	list_display = ('full_name',)
	search_fields = ('name', )

	def get_search_results(self, request, queryset, search_item):
		queryset, use_distinct = super(PersonAdmin, self).get_search_results(request, queryset, search_term)
		try:
			search_term_as_int = int(search_item)
			queryset = self.model.objects.filter(age=search_term_as_int)
		except:
			pass
		return queryset,use_distinct

admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
