from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment, Category


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'categories']
    list_filter = ('status', 'created_on', 'categories')
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)

