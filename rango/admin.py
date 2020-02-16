
# Register your models here.
from django.contrib import admin 
from rango.models import Category, Page, UserProfile

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ['category']}),
        ('Page information', {'fields':['title','url']})
    ]
    
    list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}



admin.site.register(Category, CategoryAdmin) 
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
