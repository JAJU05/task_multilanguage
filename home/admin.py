from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableModelForm
from home.models import Blog, Category


class BlogAdmin(TranslatableAdmin):
    list_display = ('name', 'description')



class CategoryAdmin(TranslatableAdmin):
    base_form = TranslatableModelForm
    base_model = Category
    base_fields = ('name',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

